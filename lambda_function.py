import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    ec2.reboot_instances(InstanceIds=['i-073b55a8ce9122ec3'])
    return "Reboot triggered"