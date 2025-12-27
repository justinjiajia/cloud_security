


## Simulated business scenario
 
A startup company requires rapid deployment of its IT resources for application development. 
The company's compliance officer has a big challenge, tracking and managing any changes to AWS resource configurations.




> Paulo Santos
Hello! Thanks for stopping by. I have a compliance problem that I hope you can help with.
You
Hi! I will if I can. What is the problem?
Paulo Santos
I am the compliance officer for a new startup company. Because we’re a startup, we need to be agile and move fast. But changes can be made to the IT environment that are not tracked and are often in violation of our agreed standards.
Paulo Santos
Is there anything we can do to help automate the compliance of IT resources?
You
Yes there is! I would start by using infrastructure as code with AWS CloudFormation. That change alone will help standardize your creation and change process.
Paulo Santos
Infrastructure as code? I know what IT infrastructure is, but I don’t understand how it can be accomplished with code?
You
With infrastructure as code, you create a template that describes all the AWS resources that you want to include in your infrastructure, such as Amazon EC2 instances and AWS Lambda functions.
You
CloudFormation can then provision and configure those resources for you. You can treat your new template like any other code by saving it in a repository and performing a code review on it before deployment.
Paulo Santos
Awesome! But how can that help with compliance?
You
You can ensure that standards are followed during the code review process. But even as you manage your resources through CloudFormation, users can change those resources outside of CloudFormation.
You
What’s great is that CloudFormation has drift detection. That’s the ability to detect if resources no longer match the template used to deploy them.
Paulo Santos
That is fantastic. So, by using CloudFormation and drift detection, I can tell when something has been changed in our environment. Now if we could just automatically reverse the changes.
You
You can! In AWS Lambda, you can create a function that monitors for drift and remediates any drift that is detected.
Paulo Santos
That sounds really cool, and it would make my work much easier.


### Solution Request
Use an AWS Lambda function, invoked by an Amazon EventBridge schedule, to detect and remediate changes to an environment that was built by using AWS CloudFormation.


####  Step 1

In this solution, a template stored in an Amazon Simple Storage Service (Amazon S3)  bucket is used by AWS CloudFormation to deploy and manage a stack. 
A stack is a collection of AWS resources that you can manage as a single unit. Any changes manually made to that stack are detected and remediated by an AWS Lambda function.


<img width="642" height="470" alt="image" src="https://github.com/user-attachments/assets/7cb4c134-44ba-4486-88e2-bd413eeac0a3" />

### Step 2

 
A template is used to describe resources within a stack. That template can be uploaded from local storage or obtained from an S3 bucket.

<img width="647" height="477" alt="image" src="https://github.com/user-attachments/assets/86ad9508-50a2-4523-aed4-c68f56099467" />



### Step 3


<img width="651" height="478" alt="image" src="https://github.com/user-attachments/assets/0a73d74d-a611-4e12-96b1-d4cabbe38b81" />

Any changes to a stack after deployment should be managed by CloudFormation. Changes to resources can be made directly, but these direct changes can create issues when updating or deleting an existing stack through CloudFormation.



### Step 4

<img width="645" height="468" alt="image" src="https://github.com/user-attachments/assets/1751cdb4-c38a-45e5-9377-fd374ad66d66" />

While drift can be manually detected, this solution uses a Lambda function to automatically obtain the stack’s drift status from CloudFormation.



### Step 5

<img width="659" height="482" alt="image" src="https://github.com/user-attachments/assets/45937953-307a-441e-9a75-f7b5b5a83706" />

An Amazon EventBridge rule is set up to invoke the Lambda function on a schedule.


### Step 6

<img width="650" height="477" alt="image" src="https://github.com/user-attachments/assets/e5ce4d7d-b771-4ede-8e4e-dbb214713923" />

When invoked, the Lambda function queries for the drift status. The Lambda function then automatically reverses any changes, as required, to bring the stack back to a non-drifted state.


## Lab

Concept
In this practice lab, you will:
- Provision AWS resources by using an AWS CloudFormation template.
- Review the concept of drift detection in CloudFormation.
- Simulate drift by adding a rule to a security group.
- Review how to detect and remediate drift by using an AWS Lambda function.
- Create an Amazon EventBridge schedule to run the Lambda function.

<img width="647" height="468" alt="image" src="https://github.com/user-attachments/assets/e7bb351c-2fea-477a-af87-58a0d640ec5a" />



Practice Lab Goals
Provision AWS resources by using an AWS CloudFormation template.
Review the concept of drift detection in CloudFormation.
Simulate drift by adding a rule to a security group.
Review how to detect and remediate drift by using an AWS Lambda function.
Create an Amazon EventBridge schedule to run the Lambda function.


 
### Step 1


1. Review the practice lab objectives in the Concept section.
2. Click Start Lab or Open AWS Console to begin.
3. Follow the lab instructions carefully, and use the arrows below to navigate between steps.

AWS services not used in this lab are disabled in the lab environment. In addition, the capabilities of the services used in this lab are limited to what the lab requires.


### Step 2

1. In the top navigation bar search box, type: `s3`

2. In the search results, under Services, click S3.

### Step 3

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/415d2fae-7733-4487-b85a-84a6af956dc4" />


Concept
Amazon Simple Storage Service (Amazon S3) provides a simple web service interface that you can use to store and retrieve any amount of data, at any time, from anywhere.
 
1. On the General purpose buckets tab, click the S3 bucket name that starts with resource-bucket-.


### Step 4

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/8cc02050-7651-42f3-b957-21bddeeeaad8" />

Concept
Amazon S3 is a simple key-based object store. When you store data, you assign a unique object key that can later be used to retrieve the data. Keys can be any string, and they can be constructed to mimic hierarchical attributes.
 
1. On the Objects tab, click sample-cloudformation.yaml.
 
Backup:  https://github.com/justinjiajia/cloud_security/blob/main/tutorials/resources/sample-cloudformation.yaml

### Step 5

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/bf4c508a-83e6-4edd-9b92-28f36155c3c4" />

Concept
Amazon S3 supports both virtual-hosted–style and path-style URLs to access a bucket. Because buckets can be accessed by using path-style and virtual-hosted–style URLs, we recommend that you create buckets with DNS-compliant bucket names. 
 
1. On the Properties tab, in the Object overview section, under Object URL, click the copy icon to copy the provided URL, and then paste it in the text editor of your choice on your device.

- You use the URL in a later step.

https://resource-bucket-4f8f0e60.s3.us-east-1.amazonaws.com/sample-cloudformation.yaml

### Step 6


Concept
Using AWS CloudFormation, you can create and provision AWS infrastructure deployments predictably and repeatedly.
 
1. In the top navigation bar search box, type: cloudformation

2. In the search results, under Services, click CloudFormation.


### Step 7

Concept
A stack is a collection of AWS resources that you can manage as a single unit. You can create, update, or delete a collection of resources by creating, updating, or deleting stacks.
 
1. In the Stacks section, click Create stack to expand the dropdown list.
2. Choose With new resources (standard).

### Step 8



Concept
To provision and configure your stack resources, you should understand CloudFormation templates, which are formatted text files in JSON or YAML. These templates describe the resources that you want to provision in your CloudFormation stacks. 
 
1. In the Create stack step, for Prepare template, review to confirm that Choose an existing Template is selected.
2. In the Specify template section, for Template source, review to confirm that Amazon S3 URL is selected.
3. For Amazon S3 URL, paste the object URL that you copied in an earlier step.
4. Scroll down to the bottom of the page, and then click Next (not shown).

### Step 9

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/8123b65f-7588-4440-bd67-343f60479360" />


Concept
Use the optional Parameters section to customize your templates. In this section, you can input custom values to your template each time you create or update a stack.
 
1. In the Specify stack details step, for Stack name, type: `app-stack`

2. For VpcId, on the dropdown list, choose the VPC name that contains infrastructure-as-code.

- By providing this parameter, you can tell the template to build the resources in a specific VPC.

3. Click Next.


### Step 10
1. In the Configure stack options step, at the bottom of the page, click Next.

### Step 11
1. In the Review and create step, review the stack details.
2. Scroll down to the bottom of the page, and then click Submit (not shown).

### Step 12


1. In the left Stacks window, review the app-stack status.

- The creation of your stack should be in progress.

2. If needed, click the window's refresh icon until the status changes to CREATE_COMPLETE.

### Step 13

1. In the Events tab, review to confirm that the app-stack creation is completed.

- You can click the section's refresh icon as needed.


### Step 14
Concept
Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the AWS Cloud. Using Amazon EC2 removes the need to invest in hardware up front, so you can develop and deploy applications faster.
 
1. In the top navigation bar search box, type: `ec2`

2. In the search results, under Services, click EC2.


### Step 15

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/2fda8796-97e5-40a7-8ded-4f4030ec8563" />

Concept
A security group acts as a virtual firewall, controlling the traffic that is allowed to reach and leave the resources that it is associated with. For example, after you associate a security group with an Amazon EC2 instance, the security group controls the inbound and outbound traffic for the instance.
Step
15
1. Navigate to the Amazon EC2 console.
2. In the left navigation pane, click Instances.
3. In the Instances section, choose the checkbox to select the available app-server instance.
4. Below that section, click the Security tab.
5. Under Security groups, click the available security group.


### Step 16

Concept
You can add or remove rules for a security group, also referred to as authorizing or revoking inbound or outbound access. A rule applies either to inbound traffic (ingress) or outbound traffic (egress). You can grant access to a specific CIDR range, or to another security group in your VPC or a peer VPC. Note that a peer VPC requires a VPC peering connection.
 
1. On the Inbound rules tab, click Edit inbound rules.

### Step 17
1. Below Inbound rule 2, click Add rule.


### Step 18
Concept
When you choose a source type of Anywhere-IPv4, you effectively choose the CIDR range 0.0.0.0/0.
 
1. In the new rule, for Type, choose `HTTPS`.
2. For Source type, choose Anywhere-IPv4.
3. Click Save rules.

### Step 19


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/3e353659-cc08-4013-9387-5ebc525be0af" />

Concept
Even as you manage your resources through CloudFormation, users can change those resources outside of CloudFormation. Users can edit resources directly by using the underlying service that created the resource. Changes made outside of CloudFormation can complicate stack update or deletion operations.
 
1. Navigate to the AWS CloudFormation console.

- Remember you can use the Services search box (or click Services) on the top navigation bar to navigate to a different service console.

2. On the Stacks page, choose the radio button to select app-stack.
3. Click Stack actions to expand the dropdown list.
4. Choose Detect drift.

### Step 20

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/a175e09a-636f-4822-8918-7bdb54068399" />

Concept
Using drift detection, you can detect whether a stack's actual configuration differs (or has drifted) from its expected configuration. Use CloudFormation to detect drift on an entire stack or on individual resources within the stack.
 
1. Review to confirm that app-stack is selected.
2. On the Stack actions dropdown list, choose View drift results.


### Step 21

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/ff95cac5-5853-450b-91b3-a5e3fbeb347c" />

Concept
In the Resource drift status section, CloudFormation lists each stack resource, its drift status, and the last time drift detection was initiated on the resource.
 
1. At the top of the page, click Detect stack drift.
2. In the Stack drift status section, review to confirm that the Drift status is DRIFTED.

- You can click the Drifts refresh icon as needed.

3. In the Resource drift status section, under Drift status, review to confirm that the WebServerSecurityGroup shows MODIFIED.
4. Choose WebServerSecurityGroup.
5. Click View drift details.

### Step 22

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/556a71ba-3ccf-41d6-8f38-1456fa0cb437" />

Concept
For resources with a MODIFIED status, CloudFormation displays resource drift details.
Step
22
1. In the Differences section, choose the checkbox to select the available security group.

### Step 23

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/21d30e5b-8ba4-4cad-86ca-9634abc24ce3" />

1. In the Details section, under Actual, review the highlighted section to compare what is different from the Expected stack.

- By selecting the security group in the previous step, the change for that selection is highlighted in the Details section.


### Step 24

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/8b5afa24-e7f2-45f0-a952-0be03b2254ca" />


Concept
You can use the AWS Lambda compute service to run code without provisioning or managing servers. Lambda runs your code on a high-availability compute infrastructure. Lambda performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, code monitoring, and logging.
 
1. Navigate to the AWS Lambda console.
2. In the Functions section, click labFuction-compliance.

```python
"""
This Lambda function returns IAM and Security Group resources 
to compliance if drift is detected in CloudFormation stack.
"""
import os
import json
import logging
import time
import boto3

# It is a good practice to use proper logging.
# Here we are using the logging module of python.
# https://docs.python.org/3/library/logging.html

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Define CloudFormation stack information
STACK_NAME = "Enter_your_stack_name"
ROLE_NAME = os.environ['role_name']

# Importing IAM and CloudFormation boto3 client.
# For additional info: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

cloudformation_client = boto3.client('cloudformation')
iam_client = boto3.client('iam')


def repair_security_groups(resource_id,expected_value, actual_value):
    """Repair SG updates"""
    allowed_IpPermissions = [
        {
            "IpProtocol": "tcp",
            "FromPort": 22,
            "ToPort": 22,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
        },
        {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
        }
    ]
    
    if expected_value != actual_value:
        ec2 = boto3.client('ec2')
        # Update SG rules
        print(expected_value)
        print(actual_value)
        response_SG = ec2.describe_security_groups(
                GroupIds=[resource_id]
            )
        current_IpPermissions = response_SG["SecurityGroups"][0].get('IpPermissions')
        logger.info(response_SG["SecurityGroups"][0].get('IpPermissions'))
        ec2.revoke_security_group_ingress(GroupId=resource_id,IpPermissions=current_IpPermissions)
        ec2.authorize_security_group_ingress(GroupId=resource_id, IpPermissions=allowed_IpPermissions)
        logger.info(f"Configuration restored for the security group with id {resource_id}")
    else:
        logger.info(f"No updates for the security group with id {resource_id}")
        

def repair_instance_profile(resource_id,expected_value, actual_value):
    """Repair instance profiles attached to EC2"""
    if expected_value != actual_value:
        
        ec2 = boto3.client('ec2')
        iam = boto3.client('iam')
        
        response_list_profiles = iam.list_instance_profiles(PathPrefix='/')
        # Iterate to get the approved instance profile ARN
        for profile in response_list_profiles['InstanceProfiles']:
            if expected_value in profile['InstanceProfileName']:
                approved_profile_arn = profile['Arn']
                logger.info(approved_profile_arn)
        
        
        #Get Association ID of the profile
        response_ec2_profile = ec2.describe_iam_instance_profile_associations(
                                        Filters=[
                                                    {
                                                        'Name': 'instance-id',
                                                        'Values': [resource_id]
                                                    }
                                                ]
                                        )
        # If the association is empty, update with approved profile
        # Else dissociate the unapproved profile and attach approved
        # instance profile.
        if not response_ec2_profile['IamInstanceProfileAssociations']:
            print("Empty")
            
            #Associate approved instance profile
            response_profile_associate = ec2.associate_iam_instance_profile(
                                            IamInstanceProfile={
                                                'Arn': approved_profile_arn,
                                                'Name': expected_value
                                            },
                                            InstanceId=resource_id
                                        )
            logger.info(response_profile_associate)
            logger.info(f"Instance Profile restored for the instance {resource_id}")
        else:
            associations = response_ec2_profile['IamInstanceProfileAssociations']
            association_id = associations[0]['AssociationId']
            logger.info(f"Association_ID:{association_id}")
        
            #Disassociate instance profile
            response_profile_disassociate = ec2.disassociate_iam_instance_profile(
                            AssociationId=association_id
                        )
            logger.info(response_profile_disassociate)
            
            #Associate approved Instance profile
            response_profile_associate = ec2.associate_iam_instance_profile(
                                            IamInstanceProfile={
                                                'Arn': approved_profile_arn,
                                                'Name': actual_value
                                            },
                                            InstanceId=resource_id
                                        )
            logger.info(response_profile_associate)
            logger.info(f"Instance Profile restored for the instance {resource_id}")
    else:
        logger.info(f"No instance profile update needed for the instance {resource_id}")


def lambda_handler(event, context):
    """Handle Lambda invocations from CloudWatch"""

    logger.info(event)
    # Initiate a stack drift detection

    initiate_stack_drift_detection = cloudformation_client.detect_stack_drift(
                StackName=STACK_NAME
    )
    stack_drift_detection_id = initiate_stack_drift_detection["StackDriftDetectionId"]
    logger.info("Initiating drift detection.  Stack Drift Detection Id: %s",
                stack_drift_detection_id)

    # Wait for the stack drift detection to complete
    drift_detection_status = ""
    while drift_detection_status not in ["DETECTION_COMPLETE",  "DETECTION_FAILED"]:
        check_stack_drift_detection_status = cloudformation_client.describe_stack_drift_detection_status(
            StackDriftDetectionId=stack_drift_detection_id
        )
        drift_detection_status = check_stack_drift_detection_status["DetectionStatus"]
        # Add artificial delay to avoid throttling by CloudFormation APIs
        time.sleep(1)
    logger.info("Drift detection complete. Stack Drift Status: %s", drift_detection_status)

    if drift_detection_status == "DETECTION_FAILED":
            logger.info("The stack drift detection did not complete successfully for at \
                         least one resource. Results will be available for resources that \
                         successfully completed drift detection")

    # Check if the stack has drifted
    if check_stack_drift_detection_status["StackDriftStatus"] == "DRIFTED":
        # Retrieve resources that have drifted
        stack_resource_drift = cloudformation_client.describe_stack_resource_drifts(
            StackName=STACK_NAME
        )
        
        logger.info("Drifted stack resources: %s", str(stack_resource_drift))

        # Iterate over drifted resources and return to compliance
        for drifted_stack_resource in stack_resource_drift["StackResourceDrifts"]:
            """
            Get resource type, resource id, expected resource configurations 
            and detected drift configurations
            """
            resource_type = drifted_stack_resource["ResourceType"]
            resource_id = drifted_stack_resource["PhysicalResourceId"]
            expected_properties = json.loads(drifted_stack_resource["ExpectedProperties"])
            actual_properties = json.loads(drifted_stack_resource["ActualProperties"])
            
            #### Roll back the security group to standard allowed rules ####
            try:
                if resource_type =="AWS::EC2::SecurityGroup":
                    repair_security_groups(resource_id, expected_properties.get("SecurityGroupIngress", []),
                                        actual_properties.get("SecurityGroupIngress", []))
            except Exception as e:
                print(e)
            
            #### Roll back the attached instance profile of the EC2 instance to allowed instance profile ####
            # try:
            #     if resource_type == "AWS::EC2::Instance":
            #         repair_instance_profile(resource_id,expected_properties.get("IamInstanceProfile", []),
            #                                 actual_properties.get("IamInstanceProfile", []))
            # except Exception as e:
            #     print(e)
    else:
        logger.info("No drift detected")
```

### Step 25

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/488d11d4-ac50-4ac6-92d0-8bf50aca1ebf" />

Concept
A function is a resource that you can invoke to run your code in Lambda. A function has code to process the events that you pass into the function or that other AWS services send to the function.
 
1. Scroll down to the Code tab.
2. In the lambda_function code editor, on line 19, for STACK_NAME, to replace Enter_your_stack_name, type:

app-stack

- Make sure to keep the quotation marks.



### Step 26


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/41daedcd-677a-4b97-9d40-825a7c2d62b2" />

1. In the Explorer window, review to see that the changes have not deployed.

- In Lambda, you must deploy to save your changes.

2. Click Deploy.


### Step 27

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9776e4eb-54d2-447c-b74f-8dd42b1fbc63" />

Concept
To monitor the resources in the CloudFormation stack, you create a Lambda function that is invoked on a schedule by an Amazon EventBridge rule. This Lambda function checks if any resource in the stack has drifted. If so, the function returns the resource to compliance.
 
1. In the success alert, review the message.
2. In the lambda_function code editor, review the code.

- This code detects drift in a CloudFormation stack and repairs certain settings automatically.


### Step 28


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/641dcce2-0584-4e39-aae7-36b4d8556702" />

1. Review the code on lines 185–191.

- This portion of code is specifically used to return an instance profile to an accepted value if changed. You must use this code in the upcoming DIY section of this solution.

### Step 29

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/a86578ec-c72f-4ab7-b351-a2de969f0d62" />

Concept
Amazon CloudWatch monitors your AWS resources, and the applications that you run on AWS, in real time. You can use CloudWatch to collect and track metrics, which are variables that you can measure for your resources and applications.
 
1. Navigate to the Amazon EventBridge console.
2. In the left navigation pane, under Buses, click Rules.
3. In the Rules section, click Create rule.



### Step 30

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/e2cea665-653f-4920-9ddc-7ce20dd969d2" />


<img width="1401" height="652" alt="image" src="https://github.com/user-attachments/assets/64a85b55-b7f5-4110-a289-f0919fb957ad" />


1. In the Define rule detail step, for Name, type:

compliance-lambda-rule

2. For Description, type:

Invokes the compliance Lambda function

3. For Rule type, choose Schedule.


### Step 31

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/68b63cfd-6ee7-417d-b3dc-d3851e0d9511" />

<img width="1384" height="468" alt="image" src="https://github.com/user-attachments/assets/87df39b6-124e-4beb-bc68-9c24f3e1160e" />

1. Review the new EventBridge scheduling capability, called EventBridge Scheduler.

- EventBridge Scheduler is not used in this practice lab.

2. Click Continue to create rule.

### Step 32

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/2ccd53ce-5c12-4e49-814a-6da4418dd3d8" />
<img width="1094" height="610" alt="image" src="https://github.com/user-attachments/assets/6b1a7751-8417-44d6-a57a-cf8597f746d3" />

Concept
A rule can run in response to an event or at certain time intervals. For example, to periodically run a Lambda function, you can create a rule to run on a schedule by using cron or rate expressions. 
 
1. In the Define schedule step, for Schedule pattern, choose "A schedule that runs at a regular rate..."
2. Under Rate expression, for Value, type: `2`

3. For Unit, choose `Minutes`.
4. Click Next.

### Step 33

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/d29cddd8-822f-4939-9f04-51c8ded4f5b2" />

<img width="1387" height="564" alt="image" src="https://github.com/user-attachments/assets/d775b1db-fce9-4ae7-937b-397e0ab50cc2" />
<img width="1095" height="420" alt="image" src="https://github.com/user-attachments/assets/1416ab52-1e1a-4570-839c-5180e0810e60" />


1. In the Select target(s) step, for Target types, choose AWS service.
2. For Select a target, choose Lambda function.
3. For Function, choose labFunction-compliance.
4. Clear the checkbox to deselect Use execution rule.
5. Click Next.


### Step 34

 
