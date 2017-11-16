import os
import boto3

client = boto3.client(
    "sns",
    aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
    aws_secret_access_key=os.environ["AWS_SECRET_KEY"],
    region_name="us-east-1"
)

client.publish(
    PhoneNumber=os.environ['MY_PHONE_NUMBER'],
    Message="Sending you a message with AWS"
)
