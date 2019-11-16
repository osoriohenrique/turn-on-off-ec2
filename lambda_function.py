import boto3
from datetime import datetime
hour_now = datetime.now().strftime("%H:%M")

ec2 = boto3.client('ec2')

def start_instances():
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
                        ec2.start_instances(
                            InstanceIds=[
                                instanceid
                            ],
                            DryRun=False
                        )

def stop_instances():
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag-key',
                'Values': ['TURNOFF']
            }
        ]
    )

    instanceid = ''
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            instanceid = instance['InstanceId']
            for tag in instance['Tags']:
                if tag['Key'] == 'TURNOFF':
                    if tag['Value'] == hour_now:
                        ec2.stop_instances(
                            InstanceIds=[
                                instanceid
                            ],
                            Hibernate=False,
                            DryRun=False,
                            Force=False
                        )

def lambda_handler(event, context):
    start_instances()
    stop_instances()