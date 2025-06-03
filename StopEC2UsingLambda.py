import json
import boto3  #library through which we can talk with server
import time

def lambda_handler(event, context):

    ec2 = boto3.client('ec2')
    instance_id = ['i-09f5694c9672cafbc']
    res = ec2.stop_instances(InstanceIds=instance_id)
    return res
