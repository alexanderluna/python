# Send Text [(View Source)](send_text.py)

[<= GO BACK](../README.md)

__Task: Send an SMS to your phone__

Planning the program outline:

```
import libraries

setup a connection to SMS service
setup message

send message
```

import the required libraries

```
import boto3
```

setup a connection to SMS service (AWS SNS)

```
client = boto3.client(
    "sns",
    aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
    aws_secret_access_key=os.environ["AWS_SECRET_KEY"],
    region_name="us-east-1"
)
```

setup message and send message

```
client.publish(
    PhoneNumber=os.environ['MY_PHONE_NUMBER'],
    Message="Sending you a message with AWS"
)
```
