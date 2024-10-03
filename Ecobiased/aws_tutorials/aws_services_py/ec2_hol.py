"""
This script manages Amazon EC2 instances using the using boto3 python SDK
"""
# import statements
import boto3

# create EC2 resource and instance name
ec2 = boto3.resource('ec2')
instance_name = 'dct-ec2-hol'

# store instance ID
instance_id = None

# check if instance which you are trying to create already exists
# and only work with an instance that hasn't been terminated.
instances = ec2.instances.all()
instance_exists = False

for instance in instances:
    for tag in instance.tags:
        if tag['Key'] == 'Name' and tag['Value'] == instance_name:
            instance_exists = True
            instance_id = instance.id
            print(f"An instance with name {instance_name} and with id {instance.id} Already Exists.")
            break
    if instance_exists:
        break

if not instance_exists:
    # Launch a new EC2 instance if it hasn't already been created.
    new_instance = ec2.create_instances(
        ImageId='ami-0ebfd941bbafe70c6', # Replace with valid AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='us-east-1', # Replace with your key-pair
        SubnetId='subnet-0db6f71a5c25af139',
        TagSpecifications= [
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    },
                ]
            },
        ]
    )
    instance_id = new_instance[0].id
    print(f"{instance_name} Instance with id as {instance_id} has been created.")

# stop instance
ec2.Instance(instance_id).stop()
print(f"Instance {instance_name}-{instance_id} stopped.")

# start instance
ec2.Instance(instance_id).start()
print(f"Instance {instance_name}-{instance_id} started.")

# terminate instance
ec2.Instance(instance_id).terminate()
print(f"Instance {instance_name}-{instance_id} has been terminated.")