
## Simulated business scenario

The city’s IT department is organizing a cloud-based hackathon session for its employees. They want to prevent any unauthorized resource creation, especially Amazon EC2 instances, to mitigate potential cost issues and resource misuse. The department is looking for an efficient, cost-effective solution that safeguards against resource misuse while promoting effective resource management.

https://skillbuilder.aws/learn/EPXBP3KKZV/aws-simulearn-intelligent-ec2-monitoring

>Mateo Jackson
Thank you for answering our call. We can really use your help with a potential security issue.
You
I'm glad to help any way I can. What security issue do you have?
Mateo Jackson
Our city’s IT department is organizing a cloud-based hackathon session for its employees. They want to prevent any unauthorized resource creation during the event, especially unauthorized Amazon EC2 instances.
You
Unauthorized EC2 instances can certainly become a security, and cost, issue if they are not monitored.
Mateo Jackson
We'd like an efficient and cost-effective monitoring solution that safeguards against resource misuse while promoting effective resource management during our hackathons.
You
Let me clarify your requirements. Do you have servers set up to run this solution, or would you need something that does not require setup and maintenance?
Mateo Jackson
We'd prefer to not have to set up or maintain our own servers for this.
You
Is your IT team familiar with the Python programming language?
Mateo Jackson
Some people on the team have several years experience with Python, but others are somewhat new to it.
You
Okay, I believe I have enough information now to propose a solution. I suggest using an AWS Lambda script written in Python to automatically check your account for unauthorized EC2 instances. You can write the script to check for both instance type and number of running instances.
You
The results can be evaluated immediately and can shut down any extra instances.
Mateo Jackson
Is this script complicated? I'm concerned that our junior IT members might not be able to help write or maintain it.
You
That's actually not a problem if you use Amazon Q Developer, a general purpose, machine learning-powered code generator that provides code recommendations in real time.
You
Amazon Q works from within the Lambda code editor, after you grant permission to generate "suggestions" and activate the service in the editor.
Mateo Jackson
This sounds great! How difficult is the process to activate suggestions in the code editor?
You
It's actually a couple clicks in the code editor to activate and deactivate the option.
You
As you write code, Amazon Q automatically generates suggestions based on your existing code and comments. If you accept the suggestion, Amazon Q automatically advances your cursor to the next comment and makes another suggestion.
Mateo Jackson
I'm excited to see what this solution can do.


## Solution Request
To prevent any unauthorized resource creation, especially EC2 instances, use Amazon Q Developer to create an AWS Lambda function that monitors compute resources.


### Step 1

<img width="696" height="507" alt="image" src="https://github.com/user-attachments/assets/cba6180b-18ca-4567-9843-1ab5f3ea3690" />

This solution uses an AWS Lambda function, created in part with Amazon Q Developer, to monitor and help prevent unauthorized use of a fleet of Amazon Elastic Compute Cloud (Amazon EC2) instances.
Amazon Q Developer is a general purpose, machine learning-powered code generator that provides code recommendations to developers in real time. 

### Step 2
<img width="685" height="495" alt="image" src="https://github.com/user-attachments/assets/a33c7791-bfc5-4131-9c05-f33517b750e2" />

 
First, an AWS Identity and Access Management (IAM) role is added to the Lambda function with permissions that allows Amazon Q Developer to give code suggestions in the Lambda code editor.


### Step 3

<img width="681" height="499" alt="image" src="https://github.com/user-attachments/assets/1447b4e3-d0e9-42f2-a659-c4336440df3a" />

Developers use Amazon Q Developer suggestions in the Lambda code editor to help create a basic Lambda function. 


### Step 4

<img width="688" height="495" alt="image" src="https://github.com/user-attachments/assets/3d3af914-bd95-49fc-b1b7-d12b26471000" />

As the developers write code in Lambda, Amazon Q Developer automatically generates suggestions based on existing code and comments. The personalized recommendations can vary in size and scope, ranging from a single line comment to fully formed functions.


### Step 5

<img width="682" height="499" alt="image" src="https://github.com/user-attachments/assets/2c1fa8e5-4c4e-43e0-b774-44af27c2df4f" />

During code development, developers often write comments to clarify the coding process for other developers. Amazon Q Developer can use these comments to suggest code snippets to extend and add functionality to the code. The completed Lambda function can then be deployed to monitor the fleet of EC2 instances.  


### Step 6

<img width="683" height="501" alt="image" src="https://github.com/user-attachments/assets/3c9a7b42-0e6d-483f-9198-9a2246707071" />
If the fleet of EC2 instances exceeds the number of instances allowed, for example, the Lambda script can be coded to remove extra instances until the number of instances meets the set parameters.

### Step 7

<img width="687" height="501" alt="image" src="https://github.com/user-attachments/assets/1c84059d-db4b-48fc-80e6-33a7a939cb2e" />

Developers can also use Amazon Q Developer suggestions to create code that monitors and enforces instance type. In the Lambda script, EC2 instances that do not meet type requirements might be set to terminate.  


## Lab

Concept
In this practice lab, you will:
- Attach an IAM policy to an existing IAM role so that Amazon Q Developer can make suggestions for AWS Lambda functions.
- Create a Lambda function and enable Amazon Q suggestions in the Lambda code editor.
- Add comments to generate suggestions and create an Amazon EC2 monitoring function.
- Deploy and test the Lambda function.

<img width="691" height="499" alt="image" src="https://github.com/user-attachments/assets/fcd56d23-c5cb-4d6b-9cce-2deda9bed157" />

  
Practice Lab Goals
Attach an IAM policy to an existing IAM role so that Amazon Q Developer can make suggestions for AWS Lambda functions.
Create a Lambda function and enable Amazon Q suggestions in the Lambda code editor.
Add comments to generate suggestions and create an Amazon EC2 monitoring function.

### Step 1

 
1. Review the practice lab objectives in the Concept section.
2. Click Start Lab or Open AWS Console to begin.
3. Follow the lab instructions carefully, and use the arrows to navigate between steps.

AWS services not used in this lab are disabled in the lab environment. In addition, the capabilities of the services used in this lab are limited to what the lab requires.

### Step 2


Concept
Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance.
 
1. In the top navigation bar search box, type: s3

2. In the search results, under Services, click S3.


### Step 3

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/55ef2ca6-a511-4f20-87aa-c50bbe665ccb" />



1. On the General purpose buckets tab, click the bucket name that starts with input-bucket-.
2. Go to the next step.


### Step 4

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/462a45c4-5fc8-47fa-a37f-1e1367ba7b13" />

1. On the Objects tab, review the lambda_function_solution.py file.

- This file can be used as a code reference in later steps if needed.

2. Choose the checkbox to select the lambda_function.zip file.

 backup:  https://github.com/justinjiajia/cloud_security/blob/main/tutorials/resources/lambda_function.zip
   
4. Click Copy S3 URI, and then paste it in the text editor of your choice on your device.

The content of the lambda_function_solution.py file

```python
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
```


### Step 5


1. In the top navigation bar search box, type: IAM

2. In the search results, under Services, click IAM.


### Step 6

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/61a55e84-1a22-4fca-b7dc-87fbc09abfad" />

Concept
AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can access. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.
 
1. In the left navigation pane, click Roles.
2. In the Roles section search box, type: LambdaLabRole

3. Under Role name, click the role that starts with LambdaLabRole.


Policy 1: LambdaLabPolicy

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": "us-east-1"
                }
            },
            "Action": [
                "codewhisperer:GenerateRecommendations",
                "ec2:Delete*",
                "ec2:Describe*",
                "ec2:Disable*",
                "ec2:Get*",
                "ec2:Revoke*",
                "ec2:Stop*",
                "ec2:Terminate*",
                "lambda:InvokeFunction",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "s3:Get*",
                "s3:List*",
                "tag:*"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
```

Policy 2: LambdaLabRoleDefaultPolicy08C69D99

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "*",
            "Resource": [
                "arn:aws:lambda:us-east-1:078337410918:function:gbl_lab_monitoring",
                "arn:aws:iam::078337410918:role/LabStack-52553f06-5082-48-GblLabMonitoringgbllabmon-qEqccVCT783Z",
                "arn:aws:events:us-east-1:078337410918:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-yEBXMrjpY0UQ",
                "arn:aws:events:us-east-1:078337410918:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-6ME2cC19Ve2z",
                "arn:aws:events:us-east-1:078337410918:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-ohgNTY2ZHvk2",
                "arn:aws:events:us-east-1:078337410918:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-lFtbJpT7rmsy",
                "arn:aws:events:us-east-1:078337410918:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-KWf8r0f4DHx3",
                "arn:aws:events:us-east-1:078337410918:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-i7LL6xc4GSxr"
            ],
            "Effect": "Deny"
        },
        {
            "Action": "lambda:PutProvisionedConcurrencyConfig",
            "Resource": "*",
            "Effect": "Deny"
        }
    ]
}
```

trust policy

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

### Step 7

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/f39aa1a9-68cc-445b-83a0-c81c408a3e45" />

Concept
For Amazon Q Developer to provide recommendations in the AWS Lambda console, the correct IAM permissions must be enabled for either the IAM user or role. Specifically, you must add the codewhisperer:GenerateRecommendations permission.
Step
7
1. Scroll down to the Permissions tab.
2. Under Policy name, click the + to expand the LambdaLabPolicy.
3. In the LambdaLabPolicy, review the codewhisperer:GenerateRecommendations permission.

- You might see references to CodeWhisperer on the console, which is a legacy name from the Amazon CodeWhisperer service that merged with Amazon Q Developer.

### Step 8

Concept
Amazon Elastic Compute Cloud (Amazon EC2) provides on-demand, scalable computing capacity in the AWS Cloud. Using Amazon EC2 reduces hardware costs so you can develop and deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage.
 
1. Navigate to the Amazon EC2 console.

- Remember, on the top navigation bar, you can use the Services search box (or click Services) to navigate to a different service console.

2. In the left navigation pane, click Instances.
3. In the Instances section, click Launch instances.

### Step 9

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9d0638be-3ef2-4ce0-bb2c-af70fd710468" />

1. In the Name and tags section, type:

my-webserver


### Step 10

1. In the Application and OS Images (Amazon Machine Image) section, under Quick Start, choose the Amazon Linux AMI.
2. For Amazon Machine Image (AMI), on the dropdown list, choose Amazon Linux 2023 kernel-6.1 AMI.
3. Scroll down to Instance type.


### Step 11

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/75bc5477-b3c8-42cc-b4d0-70f278e228a4" />

1. For Instance type, choose t3.micro.

- Note that you must choose a different instance type on this dropdown list in the later DIY section of this solution.

2. For Key pair name, choose Proceed without a key pair.


### Step 12

1. Review the Network settings section.
2. For Firewall (security groups), choose Create security group.
3. Choose Allow SSH traffic from and Anywhere.
4. Scroll down to the Summary section.

### Step 13

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/f4bb66d7-d564-476b-8521-cf5c289159ea" />

1. For Number of instances, type: `3`

2. Review the selected instance settings.
3. Click Launch instance.

### Step 14

1. In the success alert, review the message.

   
### Step 15

1. In the left navigation pane, click Instances.
2. In the Instances section, review to confirm that three webserver instances are now running.

- You can click the section's refresh icon as needed until all three are in a Running state.

### Step 16

Concept
AWS Lambda is a serverless, event-driven compute service that helps you run code for virtually any type of application or backend service without provisioning or managing servers. Lambda runs your code on high availability compute infrastructure and performs all the administration of your compute resources.
 
1. Navigate to the AWS Lambda console.
2. On the Functions page, click Create function.


### Step 17

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/1107cea6-248d-4d47-af87-6a22d8418274" />


Concept
A Lambda function is a resource that you can invoke to run your code in Lambda. A function has code to process the events that you pass into the function or that other AWS services send to the function.
 
1. For Create function, choose Author from scratch.
2. For Function name, type: `monitor-EC2-instances`

3. For Runtime, choose the latest supported Python version.

- The Python version in the lab might differ from the screenshot.

### Step 18

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/5d8104f8-5580-4bf6-8278-6aeb07e87f4f" />

1. Under Permissions, click to expand Change default execution role.
2. For execution role, choose Use an existing role.
3. For Existing role, choose the role that starts with LambdaLabRole.
4. Click Create function.

### Step 19


1. In the success alert, review the message.
2. Scroll down and click the Code tab.

### Step 20


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/eed8a4d5-04a3-4030-ad1e-13c87481a543" />

1. Click Upload from to expand the dropdown list. 
2. Choose Amazon S3 location.



### Step 21

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/48fa0860-4841-41e2-a56f-c5d75e4c5d6d" />

1. In the pop-up box, for Amazon S3 link URL, paste the S3 URI for the input-bucket .zip file that you copied in an earlier step.

- The label says Amazon S3 link URL, but either the URL or the URI will work here.

2. Click Save.

### Step 22

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/75e74207-7c59-4f45-b240-566983789861" />

1. In the success alert, review the message.
2. In the left Explorer window, review to confirm that lambda_function.py is the file that opened.


### Step 23

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/b2e87476-dde1-43e5-ac30-7abd38c81c52" />

1. Click the Configuration tab.
2. Click General configuration.
3. Click Edit.


### Step 24

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/2998759c-9a51-4ff5-8fab-dcc5ac4a40a3" />

1. For Timeout, next to sec, type: `30`

2. Click Save.


### Step 25

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/cd729a9e-48ff-4bda-ba2c-af91a04c214b" />

Concept
You can use environment variables to adjust your function's behavior without updating code. An environment variable is a pair of strings that is stored in a function's version-specific configuration. The Lambda runtime makes environment variables available to your code and sets additional environment variables that contain information about the function and invocation request.
 
1. Click Environment variables.
2. Click Edit.

### Step 26

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/8e9a8fac-3ef8-4f70-874a-2c7732cacae5" />


1. Click Add environment variable.
2. For Key, type: `MAX_INSTANCES`

3. For Value, type: `2`

4. Click Save.



### Step 27
1. In the Environment variables section, review to confirm that a new environment variable was added.

- The new variable key should be MAX_INSTANCES, and the value should be 2.

2. To return to the code source editor, click the Code tab.


### Step 28

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/23cfc73e-db42-4b72-a71c-b4e40455a0d5" />

Concept
Prompt generation can take some practice to get consistent results. In general, the more specific you can make your prompt, the better results you will get back from Amazon Q.
 
1. In the code editor, click to place the cursor at the end of line 16.

- Line 16 is a comment line that details what the next code snippet needs to do. Amazon Q uses this comment and other data as a prompt to determine a suggestion.

2. To engage Amazon Q and generate a code snippet suggestion, on your keyboard, press Alt+C (Windows) or Opt+C (Mac) (not shown).
3. To accept the code snippet, press Tab on your keyboard (not shown).

- If you are not sure that you have accepted the correct code suggestion, compare your Amazon Q prompt output with the same section in the lab-lambda-solution.py file located in the S3 bucket reviewed in an earlier step.
- You can practice rewording your prompt until your generated code matches the code in the full code script.

### Step 29

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/ee1af7e3-11c3-4250-b367-7ed4e1f03953" />

Concept
In addition to using a keyboard shortcut, Amazon Q Developer supports the ability to provide real-time code recommendations as you write your code.
Step
29
1. On line 17, review to confirm that the selected code snippit was inserted into the code.

- If the code snippet is not aligned as shown in the screenshot example, adjust until the indent matches.

2. At the bottom of the Code tab, click Amazon Q.
3. Choose Resume Auto-Suggestions.


### Step 30

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/d9abed86-27d6-4cad-a26d-2c2f21d318d5" />

Concept
Prompts often return more than one code snippet option. Choose the option that best fits your function's requirements, or try adding more details to your prompt to help narrow the choices.
Step
30
1. Click to place the cursor at the end of line 21, and then press Enter to add a new line.

- Amazon Q automatically suggests a code snippet.
- If the suggestion does not appear, you can still press Alt+C or Opt+C to generate a suggestion.

2. Press Tab to accept the code snippet (not shown).


### Step 31


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/adbd2fb0-f1d2-4c22-9491-b60c9d33c3f9" />

1. One line 29, type: `# Create an empty list of ec2 instances`

2. Press Enter, and then engage Amazon Q for a suggestion (not shown).
3. Press Tab to accept the suggestion (not shown).

- Note that the comment on line 34 is needed in the upcoming DIY section.

### Step 32

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/06fa4027-7b81-42cb-9a74-b6f1266c6646" />

Concept
It's possible to generate more complicated code from your prompt in a single step. However, generating code snippets in stages, modifying the prompt further after each successful iteration, might prove more useful at times.
 
1. On line 42, type: `# append InstanceID to list of ec2 instances created above`

2. Press Enter, and then engage Amazon Q for a suggestion (not shown).
3. Press Tab to accept the suggestion (not shown).




### Step 33

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/af0f722d-9490-42e8-bfdf-0aef77284ffa" />

1. Click to place the cursor at the end of line 54, press Enter, and then engage Amazon Q for a suggestion.
2. Press Tab to accept the suggestion.
- Note that the comment on line 46 is needed in the upcoming DIY section.


### Step 34

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/1272b92b-1014-420f-b26d-e53bf75ec682" />

1. Click to place the cursor at the end of line 80, press Enter, and then engage Amazon Q for a suggestion.

- Note that Amazon Q will suggest either num -= 1 or num = num -1. Either choice is acceptable.

2. Press tab to accept the suggestion.

- Note that lines 71–73 are needed in the upcoming DIY section.



### Step 35

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/4a4e6be5-6db3-4a81-a144-7b0bc659641e" />

1. In the Explorer window, click Deploy.

- Deploying Lambda changes is necessary to make sure any code updates take effect.

2. Click Test.
3. Choose Create new test event.


### Step 36


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/ffb1e935-0275-4521-845b-fc06122f98c7" />

1. In the pop-up box, for Event name, type a name that you like, such as TestLambdaFunction.
2. Click Save.

### Step 37

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/c8908a63-100b-4936-970b-175d349b5a30" />


### Step 38

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/54968f1b-0807-4bcc-a5f7-0ab0d10e811a" />

1. Navigate to the Amazon EC2 console.
2. In the left navigation pane, click Instances.
3. In the Instances section, review to see that one of the instances is shutting down or is terminated.

- Because the Lambda function chooses an instance at random, yours might be different from what is displayed in the screenshot example.

1. Click Invoke.
2. In the Execution results window, on the OUTPUT tab, under Response, review to see the "All instances more than max number deleted" response.



## DIY Goals
Update the Lambda function to delete any EC2 instance that has a t3.micro instance type.
Create a new EC2 instance with the instance type, t3.micro.
Run the Lambda function again to remove any unauthorized instances.  

<img width="687" height="497" alt="image" src="https://github.com/user-attachments/assets/ec26939f-8fd3-416a-a30d-ae5f581b18ce" />

```python
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
    max_instances = int(os.environ.get('MAX_INSTANCES'))
    
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
                    
                    # append InstanceID to list of ec2 instances created above
                    ec2_hosts.append(int_ids['InstanceId'])

                    # DIY - use CodeWhisperer to create a code snippet from the following comment ####
                    # append InstanceID to list of instance with type t3.micro created above


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
```
Solution Validation Method
Our servers will confirm that the Lambda code is checking for instance type. 

Hints:
1. Several lines in the Lambda code contain DIY instructions.
2. Use Amazon Q Developer to add functionality, which removes t3.micro instances.
3. Test the Lambda function to remove the t3.micro instance.
