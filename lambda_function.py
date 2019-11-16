import boto3
import sys

ec2 = boto3.client('ec2')

response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'tag-key',
            'Values': ['TURNON']
        }
    ]
)
for reservation in (response["Reservations"]):
    for instance in reservation["Instances"]:
        for tag in instance['Tags']:
            if tag['Key'] == 'TURNON':
            print(tag['Value'])
