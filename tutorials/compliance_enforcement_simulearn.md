https://skillbuilder.aws/learn/1X2YUV851Q/aws-simulearn-compliance-enforcement

> Jane Roe
Hi! Thank you for meeting me on such short notice. Let me get straight to the point. Our hospital's new CFO wants to know our AWS monthly costs for production compared to nonproduction environments. On top of that, our hospital wants an audit of all Amazon EC2 instances to make sure that they all have the correct IAM role attached.
You
Wow! Sounds like you have a busy week ahead. I'm happy to help. These two tasks might sound different, but we can use the same solution for both, only configured a little differently.
Jane Roe
That would be great. What do you propose?
You
AWS Config, AWS Systems Manager, and AWS Lambda are three services that can help us out here.
Jane Roe
I know that Lambda is a serverless, event-driven compute service that we can use to run code for virtually any type of application or backend service without provisioning or managing servers. I have not heard about AWS Config or AWS Systems Manager.
You
AWS Config is a service that you can use to assess, audit, and evaluate the configurations of your AWS resources. AWS Config provides you with the ability to define rules for provisioning and configuring AWS resources.
You
You can use AWS Systems Manager to view and control your infrastructure on AWS. Automation, a capability of AWS Systems Manager, streamlines common maintenance, deployment, and remediation tasks for many AWS services.
Jane Roe
So, how will using all three services help me meet our CFO's two requests?
You
I propose that we enable two AWS Config managed rules. One will determine if the right tags are applied to resources. The other will ensure that EC2 instances have the correct IAM instance profile assigned to them.
You
Then, we will set up a remediation action on the AWS Config rules by using Automation documents within Systems Manager. The documents will invoke two separate Lambda functions that will apply the tags and instance profiles if they are missing.
Jane Roe
Ok, I am with you. And then, using the tags applied to our production resources, I should be able to use AWS Cost Explorer to view a breakdown of our costs by using the Environment=Prod tag?
You
That's exactly right!


### Solution Request
Use AWS Config, AWS Systems Manager, and AWS Lambda to ensure compliance of Amazon EC2 tagging policies and ensure instances have detailed monitoring enabled.


#### Step 1

<img width="717" height="492" alt="image" src="https://github.com/user-attachments/assets/9bf8335c-73b1-4831-815e-d5bacd293da8" />

This solution uses AWS Config to track configuration changes of AWS resources. AWS Systems Manager is used to remediate incorrect configurations.


#### Step 2

<img width="703" height="497" alt="image" src="https://github.com/user-attachments/assets/29f427c3-73b1-44d9-8dcc-5c07e586e1d0" />

AWS Config provides customizable, predefined rules that continually evaluate and flag the compliance status of AWS resources. The first rule in this solution checks for required tags.


#### Step 3

<img width="695" height="505" alt="image" src="https://github.com/user-attachments/assets/8ca3b447-051e-450f-ae9d-a52bba27a856" />

AWS Systems Manager can be used to automate common and repetitive IT tasks, providing predefined playbooks to manage AWS resources across multiple accounts and Regions.


#### Step 4

<img width="681" height="490" alt="image" src="https://github.com/user-attachments/assets/54f0e49e-110d-4544-99be-d350f5a3d081" />

An AWS Config rule can be linked to a Systems Manager automation playbook to quickly remediate noncompliant resources.

#### Step 5

<img width="693" height="492" alt="image" src="https://github.com/user-attachments/assets/ca96e0d7-b5b7-4c39-b898-5b01eb17ec6d" />

To manage and remediate AWS resources, such as to add missing required tags, AWS Lambda can be used to create custom automation playbooks that extend functionality.


#### Step 6

<img width="696" height="494" alt="image" src="https://github.com/user-attachments/assets/f2e3f10e-1739-4ef2-9761-0dec22a032dc" />

A typical use case for an AWS Config rule is to tag resources for financial reporting and resource management.


#### Step 7

<img width="705" height="491" alt="image" src="https://github.com/user-attachments/assets/2cfc3968-8683-42ff-88af-ee1672beeb07" />


A second AWS Config rule evaluates the configuration of Amazon Elastic Compute Cloud (Amazon EC2) instances, and it ensures that the correct instance profile, in AWS Identity and Access Management (IAM), is attached.

#### Step 8

<img width="694" height="483" alt="image" src="https://github.com/user-attachments/assets/8a3d4f16-7f83-4e41-8918-859885f945fc" />

If the EC2 instance is not compliant, a second automation playbook runs to attach the correct instance profile.


## Lab

Concept
In this practice lab, you will:
- Create AWS Systems Manager Automation documents.
- Deploy AWS Config and enable rules to detect noncompliant resources. 
- Create AWS Config rule actions that remediate noncompliant resources.

  <img width="726" height="499" alt="image" src="https://github.com/user-attachments/assets/f316754c-8eae-4df8-8c05-cdcb71824417" />

Practice Lab Goals
Create AWS Systems Manager Automation documents.
Deploy AWS Config and enable rules to detect noncompliant resources.
Create AWS Config rule actions that remediate noncompliant resources.


### Step 1

Concept
In this practice lab, you will:
- Create AWS Systems Manager Automation documents.
- Deploy AWS Config and enable rules to detect noncompliant resources. 
- Create AWS Config rule actions that remediate noncompliant resources.

1. Review the practice lab objectives in the Concept section.
2. Click Start Lab or Open AWS Console to begin.
3. Follow the lab instructions carefully, and use the arrows to navigate between steps.

AWS services not used in this lab are disabled in the lab environment. In addition, the capabilities of the services used in this lab are limited to what the lab requires. 

### Step 2

Concept
All the files required for this lab are provided to you.
 
1. On this page, click the Lab Files tab. 
2. Click the download icons to save the two lab files to your device. 

- You use these files in later steps. 

3. Click the Steps tab to return to the Practice Lab steps. 

The backup for the two files:

https://github.com/justinjiajia/cloud_security/blob/main/tutorials/resources/automation-diy.yaml
https://github.com/justinjiajia/cloud_security/blob/main/tutorials/resources/automation.yaml

### Step 3

1. In the top navigation bar search box, type:

ec2

2. In the search results, under Services, click EC2.

### Step 4
1. On the EC2 Dashboard, in the Resources section, click Instances (running).

### Step 5

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/1ea41f15-3b61-4531-b9cc-932e843bd3d5" />

 Concept
You can assign metadata to your AWS resources in the form of tags. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources. You can create tags to categorize resources by purpose, owner, environment, or other criteria.
 
1. In the Instances section, choose the check box to select HR-AppServer.
2. Below that section, select (highlight) and copy the instance ID, and then paste it to the text editor of your choice on your device. 

- You use this instance ID in a later step.

i-061f9593f2fb58fc6

3. Click the Tags tab.
4. Review the various tags assigned to this instance.



### Step 6

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/185e4efb-cba8-4af1-afc8-3db3849149b8" />

1. Navigate to the AWS Lambda console.

- Remember, on the top navigation bar, you can use the Services search box (or click Services) to navigate to a different service console.

2. In the Functions section, click labFunction.
- The Environment tag is missing and is added in a later step.

### Step 7
 Concept
You can use the code editor on the AWS Lambda console to write, test, and view the execution results of your Lambda function code.
 
1. Scroll down to the Code tab (not shown).
2. To expand the lambda_function.py window, on the Code source toolbar, click the expand icon.

- The Python code accepts an EC2 instance-id as input and uses the tag_resources boto3 API to apply the Environment:Prod tag key-value pair to the instance.

```python
"""
This lambda function reviews tags in all the instance and 
Updates the required tags
"""

import json
import sys
import os
import os
import boto3
import base64
from botocore.exceptions import ClientError
import logging

# It is a good practice to use proper logging.
# Here we are using the logging module of python.
# https://docs.python.org/3/library/logging.html

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(event)
    
    client = boto3.client('sts')
    response_account = client.get_caller_identity()['Account']
    
    instance = event['instanceId']
    resourse_ARN = f"arn:aws:ec2:us-east-1:{response_account}:instance/{instance}"
    logger.info(resourse_ARN)
    
    
    tag_client = boto3.client('resourcegroupstaggingapi')
    try:
        response_tag = tag_client.tag_resources(
                 ResourceARNList=[
                     resourse_ARN,
                 ],
                 Tags={
                    'Environment':'Prod'
                 }
                     )
        print(response_tag)
    except Exception as exp:
        logger.exception(exp)
        
    return {
        "compliance_type": "COMPLIANT",
        "annotation": "This resource is compliant with the rule."
    }
```
3. Review the lambda_function.py code.


### Step 8


1. To minimize the window, click the expand icon again.
2. To view the list of Lambda functions, in the top breadcrumbs menu, click Functions.


### Step 9
1. Review to see that another lambda function, `labFunction-DIY`, is displayed.
 
- You must use this function in the later DIY section of this solution.


```python
"""
This lambda function reviews instance profiles and replaces them with default
"""

import json
import sys
import os
import boto3
import base64
from botocore.exceptions import ClientError
import logging

# It is a good practice to use proper logging.
# Here we are using the logging module of python.
# https://docs.python.org/3/library/logging.html

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ec2 = boto3.resource('ec2')
def lambda_handler(event, context):
    logger.info(event)
    instance = ec2.Instance(event['instanceId'])
    try:
        response = instance.monitor(
            DryRun=False
        )
        logger.info(response)
        return {
            "compliance_type": "COMPLIANT",
            "annotation": "This resource is compliant with the rule."
        }
    except Exception as exp:
        logger.exception(exp)
```

### Step 10

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/c0e5b23b-f68b-48b6-a2dc-3a85462329b4" />

Concept
Using AWS Systems Manager, you can centralize operational data from multiple AWS services and automate tasks across your AWS resources.
 
1. Navigate to the AWS Systems Manager console.

- You can type "ssm" in the top navigation bar search box.
- You can safely ignore the permissions error alert.

2. In the left navigation pane, scroll down to Change Management Tools.
3. Click Documents.

### Step 11

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/3729fe34-205d-4fd2-895c-e77eb71b17f1" />

Concept
To help you get started quickly, Systems Manager provides predefined runbooks. These runbooks are maintained by AWS, AWS Support, and AWS Config.
 
1. On the Owned by Amazon tab, click Create document to expand the dropdown list.
2. Choose Automation.

### Step 12

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/113deede-1e8a-45be-95ff-bc01a9e70c58" />

Concept
You can create your own automation runbooks. Runbooks use YAML or JSON, and they include steps and parameters that you specify.
 
- If you see a Getting started pop-up box, click X to close it.

1. Click the edit icon next to the runbook title to edit the runbook name.
2. In the text box, type: `Lab-TagProdInstances`

3. Click Code.

### Step 13

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/81d64c9c-0fb8-444d-9192-b49bd82f3f35" />

1. Select (highlight) the existing code, and then delete it.

### Step 14

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/8a6965c8-46bf-4fc4-946e-54270c1db5fd" />

Concept
The automation defined in a runbook includes one or more steps. Each step is associated with a particular action and is defined in the mainSteps section of the document.
 
1. On your device, copy the contents of the automation.yaml file that you downloaded at the beginning of the lab, and then paste it in the Document editor.
2. On the top navigation bar, click the username to expand the menu.
3. Click the copy icon to copy the Account ID.
4. In the Document editor, on line 28 of the code, to replace <account-id>, paste the account ID that you just copied.


### Step 15
 
Concept
The action types, aws:executeAwsApi and aws:invokeLambdaFunction, are two of the many different action types supported by Systems Manager automation documents.
 
1. On line 28, review the FunctionName to confirm that you did not overwrite the colons before and after the account-id.
2. Click Create runbook.

### Step 16

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/a949a679-c668-4cf1-b1ae-32bb4aad96c2" />

Concept
We recommend using the aws:executeScript action to embed inline Python or PowerShell scripts directly in your runbooks, allowing scripts to run for up to 10 minutes (600 seconds) with configurable timeouts.
 
1. In the pop-up box, click Create runbook.

### Step 17

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/f4283d55-fdf9-4f1a-adee-5443d042c05e" />


 Concept
You can run Systems Manager automations across multiple AWS Regions and AWS accounts, or AWS organizational units (OUs) from an Automation management account.
 
1. In the success alert, review the message.
2. Click the Owned by me tab.
3. Click the Lab-TagProdInstances document.

### Step 18

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/7fc8afd3-15f6-4f11-b94e-0a927448f022" />

1. Scroll down to the bottom of the page.
2. In the left visual step viewer, click the updatetags step.
3. In the right Step details section, click the Inputs tab.
4. Review the attributes associated with the updatetags step.

- The updatetags step takes a payload of instanceId and invokes the Lambda function, labFunction.

5. Scroll up to the top of the page.



### Step 19

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/b4d16cf7-51a4-4d09-8e57-3a3d060c1e45" />

 Concept
You can define input parameter types for instances in Amazon Elastic Compute Cloud (Amazon EC2), buckets in Amazon Simple Storage Service (Amazon S3), and roles in AWS Identity and Access Management (IAM).
 
1. Click the Content tab.

- This tab displays the YAML code that the automation document will execute.

```yaml
description: |-
  *Use this SSM automation document to remediate ec2 instance that have not been properly tagged.*  

  ---
  # How does it work?
  This SSM automation doc will invoke the lambda function labFunction that will add tags to instances.
  The lambda function will tag any non-compliant EC2 resources with the Environment:Prod key value pair
  ## Pre-requisites
  1. Make sure to replace <account-id> with the actual account id of your provisioned lab account.


  You can create a [link to another webpage](https://aws.amazon.com/).
schemaVersion: '0.3'
parameters:
  InstanceId:
    type: String
    description: ID of the instance to be tagged
mainSteps:
  - name: updatetags
    action: aws:invokeLambdaFunction
    isEnd: true
    inputs:
      InvocationType: Event
      Payload: |
        {
          "instanceId": "{{ InstanceId }}"
        }
      FunctionName: arn:aws:lambda:us-east-1:078337410918:function:labFunction
```

### Step 20

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/7506c0e8-da77-4f6f-a02b-c4cbfbefb554" />

Concept
When you change the contents of a document, Systems Manager automatically increments the version of the document. The default version of a document can be updated to a newer version or reverted to an older version.
 
1. Click the Versions tab.
2. Review to confirm that only one version of this document is displayed, and it's the default version.


### Step 21

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9cc7a4bd-99a1-4a37-8172-fdbfd6ec31c0" />

1. Click the Details tab.
2. Review the Parameters section.
3. Scroll down to Permissions.

### Step 22

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/d5eff2e2-90f1-458c-bb4e-0d3145544980" />


Concept
To privately share a document, you modify the document permissions and allow specific individuals to access it according to their AWS account ID.
 
1. Review the Permissions section.

- The document is set to Private by default.

2. Review the Tags section.

- No tags are applied.

### Step 23

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/c21ac66c-cd42-4fe5-a0d0-fa5b451626ff" />

Concept
Using AWS Config, you can continuously audit and assess the overall compliance of your AWS resource configurations with your organization’s policies and guidelines.
 
1. Navigate to the AWS Config console.

- You can type "config" in the top navigation bar search box.

2. On the AWS Config console home page, click Get started.

### Step 24

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/3b58b488-024b-4d87-a153-c4a8f67a0926" />

 Concept
AWS Config uses the configuration recorder to detect changes in your resource configurations and capture these changes as configuration items. You must create a configuration recorder before AWS Config can track your resource configurations.
 
1. In the Settings step, scroll down to Data governance.
2. For IAM role for AWS Config, choose the radio button to select Choose a role from your account.
3. For Existing roles, choose lab-config-role-xxxxxxx.
4. In the Delivery channel section, for Amazon S3 bucket, choose the radio button to select Choose a bucket from your account.
5. For S3 Bucket name, choose the bucket name that starts with config-bucket-.
6. Next to that bucket name, type: `Config`

- This prefix identifies the folder where AWS Config will store data.

7. Scroll down to the bottom of the page and click Next (not shown).


### Step 25

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/c0d5fb72-ccbf-4d4f-9e7f-0faad4318068" />

Concept
While AWS Config continuously tracks the configuration changes that occur among your resources, it checks whether these changes violate any of the conditions in your rules. If a resource violates a rule, AWS Config flags the resource and the rule as noncompliant.
 
1. In the Rules step, review the various AWS managed rules that are delivered with AWS Config.

- A full list of managed rules can be found in the AWS Config Developer Guide.

2. Scroll down to the bottom of the page.
3. Click Next.

### Step 26

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9d65f604-0c3f-43e8-aef2-71f9ebeb5742" />

Concept
AWS Config tracks changes in the configuration of your AWS resources, and it regularly sends updated configuration details to an Amazon S3 bucket that you specify. For each resource type that AWS Config records, it sends a configuration history file every six hours.
 
1. In the Review step, review the AWS Config setup details.
2. Click Confirm.

### Step 27

Concept
The AWS Config dashboard helps you quickly identify the top resources in your AWS account, what rules or resources are noncompliant, what traffic is driving your AWS Config usage, and key metrics for failures that have occurred in your workflows.
 
You can safely ignore Update the IAM Policy used by AWS Config banner

1. On the AWS Config Dashboard, review the various components.
2. In the left navigation pane, click Rules.


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/7a93f35c-eeb7-4ec0-8d6b-b19c7b3ab74e" />


### Step 28


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/b340ee79-55ad-44ce-b311-fd47df5da5ab" />

Concept
The Rules Development Kit (RDK) is designed to support a compliance-as-code workflow that is intuitive and productive. It abstracts away much of the undifferentiated heavy lifting associated with deploying AWS Config rules backed by custom Lambda functions, and it provides a streamlined develop-deploy-monitor iterative process.
 
1. In the Rules section, review to confirm that no active rules have been deployed.
2. Click Add rule.


### Step 29

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/acf9f5b9-66f1-46fd-8bad-c75c19281ef0" />

1. In the Specify rule type step, for Select rule type, choose Add AWS managed rule.
2. In the AWS Managed Rules search box, type:

Name = required-tags

3. Choose the radio button to select required-tags.
4. Click Apply.


### Step 30

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/6c2bc863-5c46-4e48-bcad-2aeaf6b14903" />

1. Choose the radio button to select required-tags.
2. Click Next.

### Step 31

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/0a945405-4b27-43c3-bd0e-00ca7756242c" />

1. In the Configure rule step, for Name, review to see that the field is prepopulated. 

- You can change the name to anything you like. 

2. Scroll down to Evaluation mode.

### Step 32

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/59a659ed-f77e-4f2d-bbba-4aebf85ee1f7" />

Concept
Specify a scope to constrain which resources invoke an evaluation for a rule. The scope can include one or more resource types, a combination of a tag key and value, or a combination of one resource type and one resource ID. 
 
1. For Scope of changes, choose Resources.
2. For Resource category, choose AWS resources.

### Step 33



<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/4b569622-e14b-478d-9c44-0bef68d50e40" />
1. In the Resource type search box, type: `EC2 I`

- This narrows the list of choices.

2. Choose AWS EC2 Instance.
3. Scroll down to Parameters.

### Step 34

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/a7fb04ae-a922-4c37-be1d-e45f7e8d6014" />


Concept
Each tag has two parts:
- A tag key (for example, CostCenter or Project)
- A tag value (for example, 111122223333 or Production)

Tag keys and tag values are both case sensitive.
 
1. In the Parameters section, for tag1Key, under Value, delete the default value of CostCenter, and then type:

Environment

2. For tag1Value, under Value, type:

Prod

3. Scroll down to the bottom of the page, and then click Next (not shown).


### Step 35

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/6a4b7fae-4728-411b-b6c5-4aa56529b387" />
Concept
The required-tags managed rule checks that your resources have the tags that you specify. For example, you can check whether your Amazon EC2 instances have the CostCenter tag. When you separate multiple values with commas, you can check multiple tags at a time.
 
1. In the Review and create step, review the Details and Evaluation mode sections for accuracy.
2. Scroll down to Parameters.


### Step 36

 <img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/881c5aaa-91d7-420a-bb2f-067b4b5a061c" />

Concept
You can default up to six tag key-value pairs.
 
 
1. Review to confirm that the tag key-value pairs were correctly entered.
2. Click Save.

### Step 37

 <img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/7a28f758-d64e-4444-a3a7-53bc31969830" />

1. In the success alert, review the message.

- The required-tags rule was added.

2. In the Rules section, under Remediation action, review to confirm that the remediation action is currently Not set.
3. Click the required-tags rule.

- You create a remediation action in the next few steps.


### Step 38


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/039a5316-ce99-443f-8715-e0cb8ab6f3fe" />

1. Click Actions to expand the dropdown list.
2. Choose Manage remediation.
 

### Step 39
<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/a770736d-fe34-4019-9756-30e8f6a2692c" />

1. For Select remediation method, choose Manual remediation.
2. For Choose remediation action, type:

Lab-

3. Choose the Lab-TagProdInstances remediation action that you created in an earlier step.
4. Scroll down to Resource ID parameter.


### Step 40

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/be3d63a4-180f-440f-87f5-2e9b78994944" />

1. For Resource ID parameter, choose instanceId.
2. Click Save changes.

### Step 41

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/1c11806e-614f-4054-8f2b-e37138980a39" />

1. In the success alert, review the message.

- The required-tags rule was updated.

2. Scroll down to Resource in scope.


### Step 42

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/d4f78597-d7e7-4a54-ad31-c0e0071c8dce" />

1. In the Resources in scope section, choose the radio button to select the instance ID for the HR-AppServer.

- You copied the HR-AppServer instance ID in an earlier step.

2. Click Remediate.
3. On the Resources in scope dropdown list, choose All.
4. Under Status, review to confirm that the status changed to Action executed successfully.
5. After a few minutes, click the section's refresh icon.
6. Under Compliance, review to confirm that the instance's compliance status changed to Compliant.

- The Compliance status might take about 5 minutes to change.
- Alternatively, you can scroll to the top of the page, click Actions, and then choose Re-evaulate.


### Step 43

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9680fd11-bd6f-4a2c-9b80-3004a26db0df" />

1. Navigate to the Amazon EC2 console.
2. In the left navigation pane, click Instances.
3. In the Instances section, choose the check box to select HR-AppServer.
4. Below the section, click the Tags tab.
5. Review to confirm that the Environment:Prod tag was applied.

### Step 44

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9e01f05e-6ab5-4d54-870e-5aeb6302b647" />

1. In the Instances section, clear the check box to deselect HR-AppServer.
2. Choose the check box to select HR-WebServer.
3. Below the section, click the Details tab.
4. Scroll down to Instance details.

### Step 45

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/16004231-5896-4194-97ad-63869a912b77" />

1. Under Monitoring, review to confirm that monitoring is disabled for HR-WebServer.

- You must remediate this issue in the upcoming DIY section by configuring the ec2-instance-detailed-monitoring-enabled AWS Config rule.

### Step 46

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/02ef5d88-b50f-4422-8f55-5d1482017599" />

1. Click the Tags tab.
2. Review to confirm that the HR-WebServer instance does NOT have the Environment:Prod tag applied. 

- You must remediate this issue in the upcoming DIY section.


# DIY

<img width="713" height="493" alt="image" src="https://github.com/user-attachments/assets/7deddbce-d059-4c99-bca3-e15a33e2ca01" />


DIY Goals
Create a new Automation document within Systems Manager.
Deploy a new AWS Config rule, `ec2-instance-detailed-monitoring-enabled`.
Apply any remediation required to make the HR-WebServer instance fully compliant.

<img width="1142" height="495" alt="image" src="https://github.com/user-attachments/assets/01d6cbdc-eedb-4526-b183-9875ee4e50f3" />

### Solution Validation Method
The testing server will query the instance-id of the HR-WebServer EC2 instance to confirm that the right tags and detailed monitoring have been enabled.


Hint: 
- In addition to applying remediation based on the new config rule, remember to also apply remediation for the required-tags config rule to the HR-WebServer EC2 instance.
