import boto3

# @todo: implement connection pooling

def conn(aws_profile_name):
    boto3.setup_default_session(profile_name = aws_profile_name)
    ec2 = boto3.client('ec2')
