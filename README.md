# turn(on|off)ec2

Lambda to start and stop ec2's from AWS in the time desired

### Prerequisites

The lambda needs to have the policy below attached to be enabled to start and stop instances.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:StopInstances"
            ],
            "Resource": "arn:aws:ec2:*:*:instance/*"
        },
        {
            "Effect": "Allow",
            "Action": "ec2:DescribeInstances",
            "Resource": "*"
        }
    ]
}
```

### USAGE

Clone the repository

```
$ git clone https://github.com/osoriohenrique/turn-on-off-ec2.git
$ cd turn-on-off-ec2
```

Zip all the files:

```
zip lambda.zip *
```

Go to your AWS console and create a new lambda function using python 3.7, and insert in it the policy above. Create a trigger that will fit the times you want to stop and start the ec2.


In the ec2 create two new tags with keys TURNON and TURNOFF, their values will be the time where the ec2 will be started and stoped respectively. Example of value: **22:15**


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
