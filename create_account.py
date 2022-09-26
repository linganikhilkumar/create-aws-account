import re
import boto3
import json
import marshmallow.validate


def create_account(payload):
    try:
        client = boto3.client('organizations')

        response = client.create_account(
            Email=payload.get("email"),
            AccountName=payload.get("account_name")
        )
        return response['CreateAccountStatus']
    except Exception as err:
        print(err)

def lambda_handler(event, context):
    input = json.loads(event.get("data"))
   
    create_account(input)










