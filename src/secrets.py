import argparse
import boto3
import botocore.errorfactory
import os
import json
import sys
import uuid

class Secrets:
    def __init__(self, keyid=None):
        self.client = boto3.client('secretsmanager')
        self.keyid = keyid

    def save(self, k, v):
        token = str(uuid.uuid4())
        try:
            response = self.client.create_secret(
                Name=k,
                ClientRequestToken=token,
                KmsKeyId=self.keyid,
                SecretString=v
            )
        except self.client.exceptions.ResourceExistsException as e:
            print(f"{e}")
            sys.exit(1)
        return response

    def get(self, k):
        response = self.client.get_secret_value(
            SecretId=k
        )
        output = {
            "ARN": response["ARN"],
            "Name": response["Name"],
            "VersionId": response["VersionId"],
            "SecretString": response["SecretString"],
            "VersionStages": response["VersionStages"],
            "CreatedDate": response["CreatedDate"].isoformat()
        }
        return output

    def print_exceptions(self):
        for ex_code in self.client.exceptions._code_to_exception:
            print(ex_code)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-c')
    ap.add_argument('-g')
    ap.add_argument('-p', action='store_true')
    args = ap.parse_args()

    keyid = os.environ["KMS_KEY_ID"]
    agent = Secrets(keyid)

    if args.c is not None:
        with open("etc/secrets.json", "r") as jfile:
            secrets = json.load(jfile)
            for secret in secrets:
                for k in secret:
                    if k == args.c:
                        print(json.dumps(secret))
                        agent.save(k, secret[k])
    elif args.g is not None:
        resp = agent.get(args.get)
        print(json.dumps(resp))
    elif args.p is not None:
        agent.print_exceptions()
    
if __name__ == "__main__":
    main()
