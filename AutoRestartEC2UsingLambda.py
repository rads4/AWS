import json
import boto3  #library through which we can talk with server
import time

def lambda_handler(event, context):

    ec2 = boto3.client('ec2')
    instance_id = ['i-09f5694c9672cafbc']
    res = ec2.stop_instances(InstanceIds=instance_id)
    
    time.sleep(30)  #waiting for 3 minutes

    res = ec2.start_instances(InstanceIds=instance_id)  #restarting
    return res
