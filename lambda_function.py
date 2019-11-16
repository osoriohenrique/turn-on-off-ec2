import boto3
from datetime import datetime

ec2 = boto3.client('ec2')

def start_instances():
    hour_now = datetime.now().strftime("%H:%M")
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
                        print(f'Starting instance {instanceid}')
                        ec2.start_instances(
                            InstanceIds=[
                                instanceid
                            ],
                            DryRun=False
                        )

def stop_instances():
    hour_now = datetime.now().strftime("%H:%M")
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
                        print(f'Stopping instance {instanceid}')
                        ec2.stop_instances(
                            InstanceIds=[
                                instanceid
                            ],
                            Hibernate=False,
                            DryRun=False,
                            Force=False
                        )

def lambda_handler(event, context):
    print(hour_now)
    start_instances()
    stop_instances()
