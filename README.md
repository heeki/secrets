# Basic AWS Secrets Manager Usage
Sample repository for using AWS Secrets Manager with boto3.

## Deployment
To deploy, configure the following configuration files:

etc/execute_env.sh
```bash
PROFILE=[aws-cli-profile]
STACK=[stack-name]
TEMPLATE=iac/kms.yaml
```

etc/execute_env.json
```json
[
    {
        "ParameterKey": "user",
        "ParameterValue": "your-user-name"
    },
    {
        "ParameterKey": "role",
        "ParameterValue": "your-role"
    }
]
```

To create: `make cfn`
To update: `make cfn.update`

## Execution
To execute, configure the following configuration file:

etc/secrets.json
```json
[
    {
        "your-secret-1": "abcdefghijklmnopqrstuvwxyz"
    },
    {
        "your-secret-2": "abcdefghijklmnopqrstuvwxyz"
    }
]
```

Install dependencies: `pip install -r requirements.txt`
Get the KMS key id: `make cfn.outputs`
Execute the command provided: `export KMS_KEY_ID=uuid-uuid-uuid-uuid-uuid`
Create a secret: `python src/secrets.py -c [name]`
Get a secret: `python src/secrets.py -g [name]`
