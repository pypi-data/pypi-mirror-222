import boto3
import pytest
import requests
from botocore.exceptions import ClientError

from outages.exceptions import ServiceUnavailableException

LOCALSTACK_ENDPOINT = "http://localhost:4566"
EXTENSIONS_ENDPOINT = f"{LOCALSTACK_ENDPOINT}/_localstack/extensions"
OUTAGES_ENDPOINT = "http://outages.localhost.localstack.cloud:4566/outages"


class TestOutages:
    SERVICE_UNAVAILABLE_EXCEPTION = "Service not accessible (LocalStack Outages Extension)"
    REGION_UNAVAILABLE_EXCEPTION = "Region not accessible (LocalStack Outages Extension)"

    @pytest.fixture()
    def create_config(self):
        def _put_config(**kwargs):
            response = requests.put(OUTAGES_ENDPOINT, json=kwargs["RequestedConfig"])
            assert response.status_code == kwargs["ExpectedStatusCode"]
            assert (
                response.json() == kwargs["RequestedConfig"]
                if not kwargs.get("ExpectedConfig")
                else kwargs["ExpectedConfig"]
            )

        yield _put_config

        config = {"services": [], "regions": []}
        response = requests.put(OUTAGES_ENDPOINT, json=config)
        assert response.status_code == 200

    def _get_config(self, config, expected_status_code):
        response = requests.get(OUTAGES_ENDPOINT)
        assert response.json() == config
        assert response.status_code == expected_status_code

    def test_load_outages_extension(self):
        # check if outage is loaded using /_localstack/extensions

        response = requests.get(EXTENSIONS_ENDPOINT)
        parsed_response = response.json()

        assert parsed_response
        outages_items = [item for item in parsed_response if item.get("name") == "outages"]
        assert len(outages_items) == 1
        assert outages_items[0]["is_initialized"]
        assert outages_items[0]["is_loaded"]

    @pytest.mark.parametrize(
        "services,regions,error_message",
        [
            (["kms"], ["us-east-1"], SERVICE_UNAVAILABLE_EXCEPTION),
            (["kms"], [], SERVICE_UNAVAILABLE_EXCEPTION),
            ([], ["us-east-1"], REGION_UNAVAILABLE_EXCEPTION),
        ],
    )
    def test_outage_simulation_atmost_one_service_region(
        self, services, regions, create_config, error_message
    ):
        config = {"services": services, "regions": regions}
        create_config(RequestedConfig=config, ExpectedStatusCode=200)

        # create boto3 client for kms
        kms_client = boto3.client("kms", endpoint_url=LOCALSTACK_ENDPOINT, region_name="us-east-1")
        s3_client = boto3.client("s3", endpoint_url=LOCALSTACK_ENDPOINT, region_name="eu-west-1")

        with pytest.raises(ClientError) as e:
            kms_client.create_key()

        assert e.value.response["Error"]["Code"] == ServiceUnavailableException.code
        assert (
            e.value.response["ResponseMetadata"]["HTTPStatusCode"]
            == ServiceUnavailableException.status_code
        )
        assert e.value.response["Error"]["Message"] == error_message

        with pytest.raises(ClientError) as e:
            kms_client.list_keys()

        assert e.value.response["Error"]["Code"] == ServiceUnavailableException.code
        assert (
            e.value.response["ResponseMetadata"]["HTTPStatusCode"]
            == ServiceUnavailableException.status_code
        )
        assert e.value.response["Error"]["Message"] == error_message

        response = s3_client.list_buckets()
        assert response["ResponseMetadata"]["HTTPStatusCode"] == 200

    @pytest.mark.parametrize(
        "services,regions,error_message",
        [
            (["kms", "s3"], [], SERVICE_UNAVAILABLE_EXCEPTION),
            (["kms", "s3"], ["us-east-1", "us-east-2"], SERVICE_UNAVAILABLE_EXCEPTION),
            ([], ["us-east-1", "us-east-2"], REGION_UNAVAILABLE_EXCEPTION),
        ],
    )
    def test_outage_simulation_multiple_service_region(
        self, services, regions, create_config, error_message
    ):
        config = {"services": services, "regions": regions}
        create_config(RequestedConfig=config, ExpectedStatusCode=200)

        # create boto3 client for kms
        kms_client = boto3.client("kms", endpoint_url=LOCALSTACK_ENDPOINT, region_name="us-east-1")
        s3_client = boto3.client("s3", endpoint_url=LOCALSTACK_ENDPOINT, region_name="us-east-2")
        lambda_client = boto3.client(
            "lambda", endpoint_url=LOCALSTACK_ENDPOINT, region_name="eu-west-1"
        )

        with pytest.raises(ClientError) as e:
            kms_client.list_keys()

        assert e.value.response["Error"]["Code"] == ServiceUnavailableException.code
        assert (
            e.value.response["ResponseMetadata"]["HTTPStatusCode"]
            == ServiceUnavailableException.status_code
        )
        assert e.value.response["Error"]["Message"] == error_message

        with pytest.raises(ClientError) as e:
            s3_client.list_buckets()

        assert e.value.response["Error"]["Code"] == ServiceUnavailableException.code
        assert (
            e.value.response["ResponseMetadata"]["HTTPStatusCode"]
            == ServiceUnavailableException.status_code
        )
        assert e.value.response["Error"]["Message"] == error_message

        response = lambda_client.list_functions()
        assert response["ResponseMetadata"]["HTTPStatusCode"] == 200

    @pytest.mark.parametrize(
        "services,regions",
        [
            ([], []),
            (["s3"], []),
            (["s3"], ["us-east-1"]),
            (["s3", "kms"], ["us-east-1", "us-east-2"]),
        ],
    )
    def test_outages_valid_fetch_update_config(self, services, regions, create_config):
        config = {"services": services, "regions": regions}
        create_config(RequestedConfig=config, ExpectedStatusCode=200)
        self._get_config(config, 200)

    @pytest.mark.parametrize(
        "config",
        [
            (
                {
                    "services": [],
                    "regions": ["us-east-1"],
                    "invalid-key": "invalid-value",
                }
            ),
            ({"invalid-key": "invalid-value"}),
            ({"invalid-key": ""}),
        ],
    )
    def test_outages_invalid_fetch_update_config(self, config, create_config):
        error_message = {
            "error": "Error in validation: Additional"
            " properties are not allowed ('invalid-key' was unexpected)"
        }
        create_config(RequestedConfig=config, ExpectedStatusCode=400, ExpectedConfig=error_message)
        self._get_config({"services": [], "regions": []}, 200)
