# Outages

> :warning: Please note that this extension is experimental and currently under active development.

This LocalStack extension lets you simulate outages for specified AWS regions or services.

## Prerequisites

- LocalStack Pro
- Docker
- Python

## Installation

Before installing the extension, make sure you're logged into LocalStack. If not, log in using the following command:
```bash
localstack login
```

You can then install this extension using the following command:

```bash
localstack extensions install outages
```

## Configuration

The extension can be configured using the following API call:

To add configurations for specific AWS services or regions, you can update the 'services' or 'regions' fields in your request with the appropriate values.
```bash
curl --location --request PUT 'http://outages.localhost.localstack.cloud:4566/outages' \
  --header 'Content-Type: application/json' \
  --data '{
    "services": ["kms"],
    "regions": ["us-east-1"]
  }'
```

If you want to remove the current configuration, you can pass an empty array for both the "services" and "regions" parameters. This would effectively clear the current settings. Here's the updated API call:
```bash
curl --location --request PUT 'http://outages.localhost.localstack.cloud:4566/outages' \
  --header 'Content-Type: application/json' \
  --data '{
    "services": [],
    "regions": []
  }'
```

To retrieve the current configuration, use the following API call:

```bash
curl --location --request GET 'http://outages.localhost.localstack.cloud:4566/outages'
```

## License

(c) 2023 LocalStack GmbH
