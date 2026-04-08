import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    ec2.reboot_instances(InstanceIds=['YOUR_INSTANCE_ID'])
    return "Reboot triggered"