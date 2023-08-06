# work with EC2 instances

from pprint import pprint
import boto3
from botocore.config import Config

my_config = Config(
    region_name = 'ca-central-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

ec2 = boto3.client('ec2', config=my_config)

response = ec2.describe_instances()
pprint(response)
