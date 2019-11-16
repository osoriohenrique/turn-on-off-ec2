import boto3
from datetime import datetime

hour_now = datetime.now().strftime("%H:%M")

ec2 = boto3.client('ec2')

response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'tag-key',
            'Values': ['TURNON']
        }
    ]
)

instanceid = ''
for reservation in (response["Reservations"]):
    for instance in reservation["Instances"]:
        instanceid = instance['InstanceId']
        for tag in instance['Tags']:
            if tag['Key'] == 'TURNON':
                if tag['Value'] == hour_now:
                    print(instanceid)
