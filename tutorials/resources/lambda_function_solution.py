# base lab lambda code
import json, os
import boto3
from datetime import datetime
import urllib3
import random
import logging

http = urllib3.PoolManager()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(event)

    # get number of max instances from environment variable.
    max_instances = int(os.environ['MAX_INSTANCES'])

    
    try:
        #Setup boto3 client to interact with AWS ec2 service named ec2_client
        ec2_client = boto3.client('ec2')

        
        #Setup a specific boto3 call to retrieve ec2 instance details
        response_get_ec2_hosts = ec2_client.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ["*"]}])

        
        # Create an empty list of ec2 instances
        ec2_hosts = []


        # DIY - use CodeWhisperer to create a code snippet from the following comment #####
        # Create a second empty list with name t3micro_list for instances of type t3.micro
        t3micro_list = []

        
        #Use boto3 to query AWS and gather ec2 instance info
        for item in response_get_ec2_hosts['Reservations']:
            for int_ids in item['Instances']:
                if (int_ids['State']['Name'] != 'terminated') and (int_ids['State']['Name'] != 'shutting-down'):
                    
                    # append instanceID to list of ec2 instances created above
                    ec2_hosts.append(int_ids['InstanceId'])
                    
                    # DIY - use CodeWhisperer to create a code snippet from the following comment ####
                    # append InstanceID to list of instance with type t3.micro created above
                    if int_ids['InstanceType'] == 't3.micro':
                        t3micro_list.append(int_ids['InstanceId'])


                else:
                    pass
        
        logger.info(ec2_hosts)
        
        # Get the length of the list of ec2 instances and save into variable num.
        num = len(ec2_hosts)

        
        # Delete random instances while num is more than max_instance
        while num > max_instances:
            logger.info('time to delete')
            
            # Generate a random integer between zero and num-1.
            # This will be the index of the instance to delete.
            random_int = random.randint(0, num-1)

            logger.info(random_int)


            #DIY - uncomment the if clause lines to see check for t3 micro instance and assign it to ec2_hosts ###
            
            if t3micro_list:
                ec2_hosts = t3micro_list
                random_int = 0

            # Terminate an EC2 instance using the instance ID
            response_ec2_delete = ec2_client.terminate_instances(InstanceIds=[ec2_hosts[random_int]])
                                
            logger.info(response_ec2_delete)
            
            #subtract 1 from num.
            num = num - 1                       

        return "All instances more than max number deleted"

    except Exception as exp:
        logger.exception(exp)