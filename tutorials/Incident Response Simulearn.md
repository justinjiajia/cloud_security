### Simulated business scenario

A fast food security analyst wants to automate Amazon EC2 instance isolation in order to respond to security events in a timely manner.

### Overview

In this AWS SimuLearn assignment, you review a real-world scenario, helping a fictional customer design a solution on AWS.

After the design is completed, you build the proposed solution through structured, step-by-step guidance in a lab within a live AWS Management Console environment.

You gain hands-on experience working with AWS services, developing job-ready competencies using the same tools technology professionals use to construct AWS solutions.

### How it works

AWS SimuLearn is powered by generative AI to help develop your soft skills, such as communication and problem-solving, in life-like conversations with AI-generated customers. An AI quiz agent evaluates your conversation responses, and an AI helper agent, Dr. Newton, is available when you get stuck.

After each solution-building conversation, you build and validate the solution in a live AWS Console environment, gaining practical skills with real-world application for career advancement.



https://skillbuilder.aws/learn/S3RE7GSSBH/aws-simulearn-incident-response/

AWS SimuLearn: Incident Response


> Mary Major: Hi! Thank you for meeting me during my lunch break. I intern for the infrastructure security office at one of the city's best rated restaurant chains. We recently had a security incident, and I need some ideas on how to better prepare for any future intrusions.

> You: I just received my AWS Certified Security - Specialty certification. I would be happy to help. Tell me more about the incident.

> Mary Major: One of our application servers was hacked into. Reviewing some of the logs, it looks like the hacker was able to guess one of the administrator passwords. The hacker then took advantage of the attached IAM instance role to download some files from Amazon S3.

> You: Wow! That is a very common technique for hacking into computer systems. How did you eventually realize that there was an intrusion?

> Mary Major: I was reviewing one of the application logs and noticed too many HTTP 401 - Unauthorized response status messages. I alerted my supervisor who told me to isolate the EC2 instance immediately, but I was not sure exactly what that meant.

> You: Your supervisor probably meant to make sure the EC2 instance can no longer accept connections through any port, and to remove any access to other systems or services.

> Mary Major: Is it possible to automatically isolate a resource if an intrusion is suspected?

>You: Yes. It requires integrating a few AWS services. First, we need to install the Amazon CloudWatch agent on your EC2 servers so we can ingest your application log files.
> You: Then we could create a metric filter from the log file data to look for specific keywords that might be suspicious.
Mary Major
Got it! Then I could create an Amazon CloudWatch alarm to email me whenever the metric reaches a high number?

> You: Yes, but we can further automate it. We can invoke an Amazon CloudWatch alarm anytime the threshold is breached. The alarm can automatically publish a message to an Amazon Simple Notification Service topic. We call it Amazon SNS for short.

You
We'll create an AWS Lambda function that isolates the EC2 instance by removing the IAM instance profile, and any security groups attached to it. The SNS topic can be used as the trigger to run the isolating AWS Lambda function.

> Mary Major: Wow! This is better than I thought. If we can get this to work, I'll really impress my boss. I might even get a permanent position here and continue getting discounts at our restaurants.


#### Solution Request: Use the Amazon CloudWatch agent to monitor application events and isolate affected Amazon EC2 resources.


<img width="832" height="427" alt="image" src="https://github.com/user-attachments/assets/7a16249d-4e1e-4b68-a283-4a8271ff5c6e" />

- Step 1
  This solution automates the notification and response to a security incident detected on an Amazon Elastic Compute Cloud (Amazon EC2) instance. 
  The suspect EC2 instance will be isolated.

<img width="829" height="431" alt="image" src="https://github.com/user-attachments/assets/750b77e8-6669-45ec-8648-e6d2a1c433c7" />

- Step 2
  When an intrusion is detected on an EC2 instance, a possible action is to remove the AWS Identity and Access Management (IAM) instance profile and security group to restrict resource access.
  This action prevents a malicious actor from gaining access to other resources through the EC2 instance.

<img width="826" height="401" alt="image" src="https://github.com/user-attachments/assets/e2cfe81b-6a98-433a-a02b-14487ecdb9eb" />

- Step 3
  An Amazon Simple Notification Service (Amazon SNS) topic is created to notify stakeholders and other downstream systems of a security event.

<img width="833" height="436" alt="image" src="https://github.com/user-attachments/assets/cb96f731-1c1a-4f92-9242-f35b793ec6cc" />

- Step 4
  The Run Command, a capability of AWS Systems Manager, can be used to install the Amazon CloudWatch agent on an entire fleet of EC2 instances at scale.

<img width="833" height="407" alt="image" src="https://github.com/user-attachments/assets/ee6c7426-a2b2-4909-a6ca-5a034bb06248" />

- Step 5
  The AWS Command Line Interface (AWS CLI) is used to configure the CloudWatch agent to send critical operating system and application logs to Amazon CloudWatch Logs.

<img width="800" src="https://github.com/user-attachments/assets/1e518878-2766-4748-8bc8-90c21e2be507" />


- Step 6

  CloudWatch Logs is used to create metric filters that can query logs for specific keywords, such as invalid password, that might indicate an intrusion attempt.

<img width="839" height="405" alt="image" src="https://github.com/user-attachments/assets/3fc0a7a2-72da-40f1-b511-90ab321a4333" />


- Step 7

  CloudWatch alarms can be created from custom metric filters. For example, an alarm might notify an Amazon SNS topic when a threshold is breached.

<img width="836" height="403" alt="image" src="https://github.com/user-attachments/assets/812d89a6-d8ea-434c-89e0-f0bd79f893e5" />


- Step 8
  The AWS Lambda function can be invoked by configuring the Amazon SNS topic as a trigger.
  The Lambda function can then take steps to isolate an EC2 instance by removing IAM instance profiles and attaching security groups that have no access to other resources.

<img width="835" height="412" alt="image" src="https://github.com/user-attachments/assets/afb26fc4-e946-4a1e-9ed2-da56dfe1227a" />

- Step 9
  Amazon SNS topics support multiple subscriber protocols, such as email and SMS text messaging, to alert IT security analysts that might want to conduct forensic analysis.


# Lab

Concept
In this practice lab, you will:
- Configure the Amazon CloudWatch agent to ingest application logs.
- Integrate Amazon SNS, Amazon CloudWatch, and AWS Lambda to isolate Amazon EC2 resources.

Practice Lab Goals
- Configure the Amazon CloudWatch agent to ingest application logs.
- Integrate Amazon SNS, Amazon CloudWatch, and AWS Lambda to isolate Amazon EC2 resources.

<img width="834" height="417" alt="image" src="https://github.com/user-attachments/assets/82f4647a-58df-4310-a355-95c7cb151a15" />


### Step 1

1. Review the practice lab objectives in the Concept section.
2. Click Start Lab or Open AWS Console to begin.
3. Follow the lab instructions carefully, and use the arrows to navigate between steps.

AWS services not used in this lab are disabled in the lab environment. In addition, the capabilities of the services used in this lab are limited to what the lab requires.





### Step 2

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/6fd97d5a-59fb-4049-91e2-6a2c15cfca46" />

Concept
Amazon Simple Notification Service (Amazon SNS) is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication.

1. In the top navigation bar search box, type: sns

2. In the search results, under Services, click Simple Notification Service.
3. Go to the next step.

### Step 3

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/5eb47bc7-7825-4247-95fe-c203b196cde5" />

Concept
You can use the A2P functionality to send messages to users at scale through SMS text messaging, mobile push, and email.
 
1. On the Amazon SNS console home page, for Topic name, type: `UnauthorizedExceptionNotification`

2. Click Next step.
3. Go to the next step.


### Step 4

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9984804f-0ceb-416b-a139-86b46ba208cd" />

Concept
Standard topics can be used in many scenarios (as long as your application can process messages that arrive more than once and out of order), such as fanning out messages to media encoding, fraud detection, and critical alerting applications.
 
1. For Type, keep or choose the default topic type of Standard.
2. For Display name, type: `Notify when an unauthorized error is detected (HTTP 401)`

3. Go to the next step.

### Step 5

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/95cc9c88-cd1e-4859-9472-3c5b349f6611" />

Concept

A delivery retry policy defines how Amazon SNS retries the delivery of messages when server-side errors occur. When the delivery policy is exhausted, Amazon SNS stops retrying the delivery and discards the message, unless a dead-letter queue is attached to the subscription.
 
1. At the bottom of the page, review the other options that can be configured.
2. Click Create topic.
3. Go to the next step.


### Step 6


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/66c52c3c-4936-4503-8733-1f8845e458d6" />

Concept
For email type subscriptions, you must confirm the subscription before the email address can start to receive messages.

1. In the success alert, review the message.
2. On the Subscriptions tab, review to see that this topic currently has no subscriptions.

- You subscribe an AWS Lambda function to this topic in a later step. 

3. Go to the next step.

### Step 7

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/e67d5563-2b58-40f8-85b9-defdecd4fd1d" />

1. In the top navigation bar search box, type: instances

2. In the search results, under Features, click Instances.
3. Go to the next step.




### Step 8

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/3c77e761-b9ce-42f8-8a3f-61c1e726b84a" />

Concept 
Use an instance profile to pass an AWS Identity and Access Management (IAM) role to an Amazon Elastic Compute Cloud (Amazon EC2) instance.

1. In the Instances section, choose the checkbox to select the App-Server instance.
2. Below that section, on the Security tab, under IAM Role, review the provided role for the instance. 
3. Under Security groups, review the provided group.

- This Amazon EC2 instance is currently configured as needed, and it has the proper instance profile and security group attached to accept connections.

4. In the Instances section, for the App-Server instance, under Instance ID, select (highlight) and copy the provided ID, and then paste it in the text editor of your choice on your device.

- You will use this ID in later steps.

5. Go to the next step.

### Step 9

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/f6cb0c0e-8b8a-484e-97e2-64baf8de565b" />

Concept
AWS Systems Manager is a secure end-to-end management solution for hybrid cloud environments.

1. In the top navigation bar search box, type: ssm

2. In the search results, under Services, click Systems Manager.
3. Go to the next step.


### Step 10

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/896ed0b9-fa93-4433-a578-77b986f345a4" />

Concept
Fleet Manager, a capability of AWS Systems Manager, saves time and money by helping you manage and troubleshoot your server fleet—running in the cloud or on premises—without the need to remotely connect to those servers.

1. In the left navigation pane, click Fleet Manager.

- You can safely ignore the missing permissions alert from Systems Manager.

2. Go to the next step.


### Step 11

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9a53022e-925e-4ded-b615-c4f727f8899b" />

Concept
With Fleet Manager, you can drill down to individual nodes (services, devices, or other resources) to perform common system management tasks such as disk and file exploration, log management, Windows Registry operations, and user management from a console.

1. In the Managed Nodes section, choose the checkbox to select the available App-Server managed node.
2. Click Node actions to expand the dropdown list.
3. Choose Tools.
4. Choose Execute run command.

- This action opens a new browser tab (or window).

5. Go to the next step.


### Step 12

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/fa884873-37ef-48ea-9ca3-e8b6d2371552" />

Concept 
Systems Manager provides safe and secure remote management of your instances at scale without logging into your servers, 
replacing the need for bastion hosts, SSH, or remote PowerShell.

1. In the Command document section, choose the radio button to select AWS-ConfigureAWSPackage.
2. Go to the next step.

###  Step 13


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/24f3219a-51c3-4bb6-94bb-053aa8ee7af9" />

Concept
You can use the Amazon CloudWatch agent to collect logs from EC2 instances and on-premises servers, running either Linux or Windows Server.

1. Scroll down to Command parameters.
2. For Action, keep the default choice of Install.
3. For Installation Type, keep the default choice of Uninstall and reinstall.
4. For Name, type: AmazonCloudWatchAgent

5. Go to the next step.

###  Step 14

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/6ca3d39a-6e95-4b3b-b73c-ab77c41030dd" />

Concept
You can use Run Command, a capability of AWS Systems Manager, to automate common administrative tasks and perform one-time configuration changes at scale.
You can target hundreds of server instances by specifying targets through instance tags, resource groups, or choosing instances manually.

1. In the Target selection section, for Target selection, keep or choose the radio button to select Choose instances manually.
2. For Instances, keep or choose the checkbox to select the App-Server instance.
3. Go to the next step.


###  Step 15

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/a2875cee-2bc6-4255-b004-ded4e4883ba4" />

Concept
You can use rate controls to restrict the number of targets on which the Run Command document executes by specifying a percentage or the number of concurrent executions.

1. Click to expand the Rate control section.
2. Review the Concurrency and Error threshold settings.
3. In the Output options section, clear the checkbox to deselect Enable an S3 bucket.

- Command output can be logged to an S3 bucket or a CloudWatch log group.

4. Go to the next step.

###  Step 16

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/238c5b15-af56-4481-8b8d-12220719f7e7" />

Concept
Run Command will report detailed status information about the different states a command experiences during processing, and about each managed node that processed the command.

1. At the bottom of the page, click Run.
2. Go to the next step.


###  Step 17

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/bda56d2a-84fe-484e-a1ca-835e7b34730a" />

Concept
You can attempt to cancel a command as long as the service shows that it's in either a Pending or Executing state. However, even if a command is still in one of these states, we can't guarantee that the command will be canceled and the underlying process stopped.

1. In the success alert, review the message.
2. In the Command status section, review to see that the command was successfully completed.

- If the status is still Processing, click the refresh icon above the section.
- While the Run Command is processing, you are provided data such as # of targets, # completed, and # of errors.

3. In the Targets and outputs section, choose the radio button to select the available instance ID.
4. Click View output.



### Step 18

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/42e3211f-38fd-4fb1-a6b2-f19c778a2663" />


Concept
A composite Systems Manager document (SSM document) is a custom document that performs a series of actions by running one or more secondary SSM documents. Composite documents promote infrastructure as code by helping you create a standard set of SSM documents for common tasks such as bootstrapping software or domain-joining instances.

1. In the Step 1 section, review the command output.

- Step 1 was skipped because it's required only when the target instance is on a Windows platform.
 


###  Step 19


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/b1a91463-c2e5-4454-91dd-dfbaccd2aab5" />

Concept
The command output can display a maximum of 48,000 characters. Output exceeding that limit can be sent to either an S3 bucket or to CloudWatch Logs.

1. In the Step 2 section, click to expand Output.
 

### Step 20

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/ab3ba0ee-01a3-44f3-9aad-1cc72730617c" />



1. Review the Step 2 command output.

- This output shows that the AmazonCloudWatchAgent was successfully installed.

2. In the left navigation pane, click Session Manager.
 


### Step 21

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/77395566-351e-4780-b88a-edb6463d61dc" />

Concept
Session Manager, a capability of AWS Systems Manager, provides secure and auditable node management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys.

1. On the Sessions tab, click Start session.
2. Go to the next step.

###  Step 22

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9d2cf62a-2847-4d15-9c39-f0f7351d9885" />

Concept
Leaving inbound SSH ports and remote PowerShell ports open on your managed nodes greatly increases the risk of entities running unauthorized or malicious commands on the managed nodes.

1. In the Specify target step, under Target instances, choose the App-Server instance.
2. Click Start session.

- The session opens in a new browser tab (or window).

 

### Step 23

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/3fb5e68e-2231-454f-b01f-8e4a5dc53df1" />

Concept
The operating system (OS) user, ssm-user, is the default when a Session Manager session is started.

1. To go to the ssm-user home directory, in the terminal window, at the command prompt, run (type the command and press Enter):

```shell
cd ~
```

2. To list the contents of the directory, run:

```shell
ls -ltr
```

- The files staged are for running a Flask application. The application will log access attempts to the record.log file.

3. To check the current status of the CloudWatch agent, run:

```shell
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status
```

- You can also copy-paste this text. If you receive an undefined value when you paste this, try again.

4. Review the returned output.

- The status currently shows that the CloudWatch agent is stopped and has not yet been configured.

 
### Step 24

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/ce7bcd46-fd88-4635-ab69-144e1733d080" />

Concept
The CloudWatch agent is open source under the MIT license, and it is hosted on GitHub. If you would like to build, customize, or contribute to the CloudWatch agent, see the GitHub repository for the latest instructions.

1. To start the CloudWatch agent configuration wizard, run: 

```shell
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
```
2. Review the Welcome message.

### Step 25

Concept
The CloudWatch agent is available as a package in Amazon Linux 2. If you are using this OS, you can install the package by entering the following command:

```shell
sudo yum install amazon-cloudwatch-agent
```

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/37d0a75a-467a-4d3f-a2b6-a96708e8c2a8" />

- The configuration wizard walks you through a series of questions. To answer each question, type the number for the correct option, and then press Enter.


1. For each of the first 6 questions, after you read the question, choose (in order):

linux (1)
EC2 (1)
root (2)
no (2)
no (2)
no (2)


### Step 26


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/d797aa37-c0a0-4e67-9aa6-0a68cfcf8c9f" />

Concept
By default, log data is stored in CloudWatch Logs indefinitely. However, you can configure how long to store log data in a log group. Any data older than the current retention setting is deleted.
 
1. For "Do you have any existing CloudWatch Log Agent?", choose no (2).
2. For "Do you want to monitor any log files?", choose yes (1).
3. For Log file path, type:

```shell
/home/ssm-user/record.log
```

4. For Log group name, to keep the default, press Enter.
5. For Log group class, choose STANDARD (1).
6. For Log stream name, to keep the default, press Enter.
7. For Log Group Retention in days, choose option 5 (7 day retention).


###  Step 27


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/1823d812-12fb-4765-97db-4d25e5739579" />

Concept
After you have a CloudWatch agent configuration saved in Parameter Store, a capability of AWS Systems Manager, you can use it to install and configure the agent at-scale by using Systems Manager.

1. For "Do you want to specify any additional log files to monitor?", choose no (2).
2. For "Do you want the CloudWatch agent to also retrieve X-ray traces?", choose no (2).
3. Review the contents of the saved config file and its location.
4. Go to the next step.

###  Step 28

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/f1deb1d1-d1b6-4e84-b1fe-813a5f007e0f" />

Concept
Parameter Store provides secure, hierarchical storage for configuration data management and secrets management. 
You can store data—such as passwords, database strings, Amazon Machine Image (AMI) IDs, and license codes—as parameter values.

1. For "Do you want to store the config file in the SSM parameter store?", choose yes (1).
2. For "What parameter store name do you want to use to store your config?", to keep the default, press Enter.
3. For "Which region do you want to store the config in parameter store?", to keep the default, press Enter.
4. For "Which AWS credentials should be used to send json config to parameter store?", choose option 1.
5. Review to make sure that the configuration was successfully written to the parameter store.

### Step 29

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/66c431cc-1818-40ec-a69f-fb3ff05f3e52" />

1. To start the CloudWatch agent, run:
   
```shell
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -s -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json
```
2. Review the output.


### Step 30

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/8edece9c-f59b-42a4-92b2-75ffd432edd8" />


Concept
CloudWatch monitors your AWS resources and the applications that you run on AWS in real time. 
You can use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications.

1. Return to the AWS Management Console in the other browser tab. 
2. In the top navigation bar search box, type: cloudwatch

3. In the search results, under Services, click CloudWatch.


### Step 31

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/7ae4b153-a95b-4c1c-9406-fdc351169359" />

Concept
You can use CloudWatch Logs to centralize the logs from all of your systems, applications, and AWS services that you use, in a single, highly scalable service. 
You can then view the logs, search them for specific error codes or patterns, filter them based on specific fields, or archive them securely for future analysis.
 
1. In the left navigation pane, click to expand Logs.
2. Click Log groups.
3. In the Log groups section, click the log group named record.log.
 

### Step 32

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/7bb4acc3-1346-4469-b389-fc22a23e9049" />

Concept
A log stream is a sequence of log events that share the same source. Each separate source of logs in CloudWatch Logs makes up a separate log stream.

A log group is a group of log streams that share the same retention, monitoring, and access control settings. You can define log groups and specify which streams to put into each group. There is no limit on the number of log streams that can belong to one log group.

1. On the Log streams tab, click the available log stream (EC2 instance ID).



### Step 33

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/75d27bef-8e01-4be9-881c-aca96a6adda8" />

Concept
You can search and filter the log data coming into CloudWatch Logs by creating one or more metric filters. Metric filters define the terms and patterns to look for in log data as the data is sent to CloudWatch Logs.
 
1. In the Log events search box, type: 401

and press Enter.

- You can safely ignore any alerts.

2. Click Create metric filter.


### Step 34

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/6af85caf-49e9-4818-8624-746ae5005797" />

1. In the pop-up box, for Filter name, type: `Unauthorized-401`

2. For Metric namespace, type: `LabApplications`

3. For Metric name, paste the EC2 instance ID that you copied in an earlier step.
4. For Metric value, type: `1`

### Step 35

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9518aadb-9070-4f00-b242-408d3b2ba78b" />

1. For Unit, choose Count.
2. Click Create.


###  Step 36

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/f54eacaa-fd2e-468c-8675-b411db254831" />
1. In the success alert, review the message.

###  Step 37

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/0971b324-a27d-475c-a34e-9cedae2cb6b4" />


Concept
AWS Lambda is a serverless, event-driven compute service in which you can run code for virtually any type of application or backend service without provisioning or managing servers.

1. In the top navigation bar search box, type: lambda

2. In the search results, under Services, click Lambda.
3. Go to the next step.

### Step 38

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/6ad70e52-390c-44d8-a671-016198bde921" />

1. In the left navigation pane, click Functions.
2. In the Functions section, click the labFunction-Traffic-Generator function.

- This Lambda function mimics a malicious actor, trying to brute-force guess a password, thereby generating HTTP 401 errors.
- You can safely ignore any other Lambda functions you see that are not displayed in the screenshot example.

<img width="1377" height="511" alt="image" src="https://github.com/user-attachments/assets/29b05c55-6a37-4c98-aa86-7b56ce37edc7" />

```python
"""
This lambda function generates login logs
"""
import os, json
import boto3
import logging
import requests

# It is a good practice to use proper logging.
# Here we are using the logging module of python.
# https://docs.python.org/3/library/logging.html

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Importing EC2 boto3 client and resources.
# For additional info: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#client
ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

def lambda_handler(event, context):
    #logger.info(event)
    pub_ip = get_pub_ip_from_tags("App-Server")
    
    url = f"http://{pub_ip}:8443/"
    print(url)
    for num in range(40):
        response = requests.post(url,data="username=admin&password=test123")
        print(response)

def get_pub_ip_from_tags(Tags):

    logger.info(Tags)
    response = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [
                    Tags,
                ]
            },
            {
                'Name': 'instance-state-name',
                'Values': [
                    'running',
                ]
            }
        ],
        MaxResults=5
    )
    logger.info(response['Reservations'])
    logger.info(len(response['Reservations'][0]['Instances']))


    if len(response['Reservations'][0]['Instances']) > 1 :
        logger.info(len(response['Reservations'][0]['Instances']))
        logger.info(f"Too many EC2 instances match tags, try again {len(response)}")
    else:
        #logger.info(len(response['Reservations'][0]['Instances']))
        logger.info(response['Reservations'][0]['Instances'])

    #aws:cloudformation:stack-name	IncidentResponse-LabStack
    #Name	App-Server
    logger.info(response['Reservations'][0]['Instances'][0]['PublicIpAddress'])
    
    return response['Reservations'][0]['Instances'][0]['PublicIpAddress']

```


### Step 39
<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/d7ad23f7-fd29-4043-961e-1f2243c1e62f" />

1. To create a new test event, click the Test tab.

### Step 40


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/4c55d3b3-1605-4d9d-994e-bac256ca94fe" />

1. For Event name, type: `Generate401Traffic`

- You can review and keep the default settings.

2. Click Save.
 
### Step 41

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/8fdd9698-a5cb-4e91-8c6b-17833d908be8" />

1. In the success alert, review the message.
2. Click Test.


### Step 42

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/d19d66bc-ba08-49b5-85a7-e8f198b0173c" />


1. Click to expand Details.
2. Under Log output, review the results.

- The function repeatedly tried to log in to the application by using the wrong username and password.

3. Go to the next step.

###  Step 43

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/48919fed-200f-4dd0-b546-8135c2990ea3" />

Concept
A metric alarm watches a single CloudWatch metric or the result of a math expression based on CloudWatch metrics. 
The alarm performs one or more actions based on the value of the metric or an expression relative to a threshold over a number of time periods.

1. Navigate to the Amazon CloudWatch console.

- Remember, on the top navigation bar, you can use the Services search box (or click Services) to navigate to a different service console.

2. In the left navigation pane, click All alarms.
3. In the Alarms section, click Create alarm.


### Step 44

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/06faddd1-e668-420d-87c1-154201203ed8" />

Concept
Metrics produced by AWS services are standard resolution by default. When you publish a custom metric, you can define it as either standard resolution or high resolution.

1. In the Specify metric and conditions step, click Select metric.

### Step 45

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/d4e2bb76-ceae-4636-a27e-e614a079d52e" />

Concept
When you publish a high-resolution metric, CloudWatch stores it with a resolution of 1 second. 
You can read and retrieve it with a period of 1 second, 5 seconds, 10 seconds, 30 seconds, or any multiple of 60 seconds.

1. In the pop-up box, on the Browse tab, click LabApplications.

   
### Step 46


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/b7909c87-9917-4812-810f-3a164d886150" />

Concept
A dimension further clarifies what the metric is and what data it stores. You can have up to 10 dimensions assigned to one metric, and each dimension is defined by a name and value pair.

1. Click Metrics with no dimensions.
 
### Step 47

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/e017e64c-a78b-4606-8087-768a54b025bf" />

1. Choose the checkbox to select the available metric name (EC2 instance ID).
2. Click Select metric.


### Step 48

 <img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/b30f2b6f-3ebe-493a-8b75-e9daaba8dd1c" />

 
 Concept
Additional charges apply for high-resolution alarms with periods less than one minute.

1. For Metric name, review the name (EC2 instance ID).
2. For Statistic, choose Sum.
3. For Period, choose 30 seconds.
 
###  Step 49

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/eef38f8e-c5c2-4a23-946e-e75685d50397" />

1. In the Conditions section, for Threshold type, choose Static.
2. For Define the alarm condition, choose Greater.
3. For Define the threshold value, type: `20`

4. Click to expand Additional configuration.
5. For Missing data treatment, choose Treat missing data as good.
6. Click Next.


### Step 50


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/987850fb-549e-49b2-8753-4826ce42ecb5" />

Concept
You can specify what actions an alarm takes when it changes between the OK, ALARM, and INSUFFICIENT_DATA states. The most common type of alarm action is to notify one or more people by sending a message to an Amazon SNS topic.

1. In the Configure actions step, for Alarm state trigger, choose In alarm.
2. For Send a notification to the following SNS topic, choose Select an existing SNS topic.
3. For Send a notification to..., choose UnauthorizedExceptionNotification.

- You created this SNS topic in an earlier step.

### Step 51

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/b9697258-212e-4b0f-b5d3-9748900c818e" />


Concept
Alarms based on EC2 metrics can also perform EC2 actions, such as stopping, terminating, rebooting, or recovering an EC2 instance.  

Alarms can also perform actions to scale an Auto Scaling group.

You can also configure alarms to create OpsItems in OpsCenter, a capability of AWS Systems Manager, or create incidents in Incident Manager, a capability of AWS Systems Manager.

1. At the bottom of the page, click Next.


### Step 52

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/e0a3a612-a3c6-4023-a200-813f9b717d70" />

1. In the Add name and description step, for Alarm name, type: `Unauthorized401ErrorBreach`

2. For Alarm description, on the Edit tab, type: Triggers when the number of HTTP 401 errors is greater than 20 during a 30 second period.

3. Click Next.


 
### Step 53

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/155fbb00-6187-4b6e-9885-936f7b31b173" />

1. In the Preview and create step, review the alarm configurations for accuracy.
 
### Step 54

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/10923224-89af-4626-b641-c1983f48cedd" />

1. At the bottom of the page, click Create alarm.


### Step 55

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/5bf7a9de-42d2-4991-b226-6cad5f4fb06b" />

1. In the success alert, review the message.
2. Under State, review to see that the initial state of the alarm is Insufficient data.

### Step 56

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/b0a23824-c2df-4103-8760-de3c511c469b" />

1. After a couple of minutes, under Alarms, click the refresh icon.
2. Under State, review to confirm that the alarm state has changed to OK.


### Step 57

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/0742931e-85c4-4f28-a51f-76bed984d93c" />

1. Navigate to the AWS Lambda console.
2. In the left navigation pane, click Functions.
3. In the Functions section, click the labFunction-isolator function.

- When this Lambda function is invoked, it will isolate the AWS resource (the App-Server EC2 instance). 


<img width="1393" height="521" alt="image" src="https://github.com/user-attachments/assets/88b83542-8eb5-4cbe-8108-b2672c82f57d" />

```python
"""
This lambda function isolates the instance 
for further forensic analysis.
"""
import os, json
import boto3
import logging

# It is a good practice to use proper logging.
# Here we are using the logging module of python.
# https://docs.python.org/3/library/logging.html

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')
instance_list = []

def lambda_handler(event, context):
    print(json.dumps(event))
    
    # Find the instance ID from MetricName defined 
    # in the Cloudwatch Alarm configuration. MetricName should be set to the instance-id.
    
    message = json.loads(event['Records'][0]["Sns"].get('Message'))
    instance_id = message['Trigger'].get('MetricName')
    logger.info(instance_id)
    
    # Get the VPC of the instance
    vpcId = get_instace_vpc_id(instance_id)
    
    # Call the get_instance function to generate list of all the available instances.
    get_instances()
    
    # If the instance is in the list, remove role 
    # and attach the Isolated_SG
    if instance_id in instance_list:
        try:
            remove_role(instance_id)
        except Exception as e:
            print(e)
    
        # Attach the isolated Security group
        try:
            sg_response = ec2_client.describe_security_groups(
            Filters=[
                    {
                        'Name': 'group-name',
                        'Values': [
                            'Isolated_SG',
                        ]
                    },
                ]
                )
            logger.info(sg_response)    
            if sg_response.get('SecurityGroups'):
                security_group_id = sg_response.get('SecurityGroups')[0].get("GroupId")
                logger(security_group_id)
                attach_isolated_sg(instance_id, security_group_id)
            else:
                security_group_id = create_sg(vpcId)
                attach_isolated_sg(instance_id, security_group_id)
        except Exception as e:
            print(e)
    

def get_instances():
    """
    This function gets the list of all the EC2 instances in the region.
    """
    get_instances = ec2_client.describe_instances()
    instances = get_instances['Reservations'][0].get('Instances')
    print(instances)
    for instance in instances:
        print(instance['InstanceId'])
        # print(instance['VpcId'])
        instance_id = instance['InstanceId']
        instance_list.append(instance_id)
    print(f"instance-List:{instance_list}")
    
def remove_role(instance_id):
    """
    This function removed the instance proflie attached to the instance.
    """
    describe_instance_profile_association_response = ec2_client.describe_iam_instance_profile_associations(
        Filters=[
                {
                    'Name': 'instance-id',
                    'Values': [
                        instance_id,
                    ]
                },
            ]
        )
    print(describe_instance_profile_association_response)
    association_id = describe_instance_profile_association_response['IamInstanceProfileAssociations'][0].get('AssociationId')
    
    print(association_id)
    response = ec2_client.disassociate_iam_instance_profile(
            AssociationId=association_id
            )
    
    logger.info(response)
    
    
def get_instace_vpc_id(instanceId):
    """
    This function gets the VPC Id of the instance.
    """
    instanceReservations = ec2_client.describe_instances(InstanceIds=[instanceId])['Reservations']
    for instanceReservation in instanceReservations:
        instancesDescription = instanceReservation['Instances']
        for instance in instancesDescription:
            return instance['VpcId']
            
def create_sg(vpcId):
    """
    This function creates the isolated security group with no egress access.
    """
    security_group_id = ec2_resource.create_security_group(GroupName="Isolated_SG", 
                                                     Description="Isolated SG for forensic analysis", 
                                                     VpcId=vpcId)
    security_group_id.revoke_egress(IpPermissions= [{'IpProtocol': '-1','IpRanges': [{'CidrIp': '0.0.0.0/0'}],'Ipv6Ranges': [],'PrefixListIds': [],'UserIdGroupPairs': []}])
    return security_group_id

def attach_isolated_sg(instance_id, security_group_id):
    """
    This function attach the isolated security group to the instance.
    """

    logger.info("Inside attach_sg")
    logger.info(security_group_id.id)
    
    
    response = ec2_client.modify_instance_attribute(
        Groups=[security_group_id.id],
        InstanceId=instance_id)

```

### Step 58

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/f5036a61-f73e-4a64-816b-a94a9db1140d" />

Concept
To use your function to process data automatically, add one or more triggers. 
A trigger is a Lambda resource, or a resource in another service, that you configure to invoke your function in response to lifecycle events, external requests, or on a schedule.

1. In the Function overview section, click + Add trigger.

###   Step 59


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/d6fe1c0f-e49c-4f77-901e-05624e1a5b6f" />
1. For Trigger configuration, choose SNS.


### Step 60

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/cfd5c66f-c7e8-4b1e-ae3a-20129ffb9904" />

1. For SNS topic, choose UnauthorizedExceptionNotification.
2. Click Add.

### Step 61

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/6fc36927-932b-477f-bb98-6ef1d32e3d84" />

1. In the success alert, review the message.
2. On the breadcrumb menu, click Functions.

- This is the horizontal top menu with right-pointing arrows separating page layers.

### Step 62
<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/e9fef388-caa6-42aa-9dc6-4710d0847397" />


1. In the Functions section, click the labFunction-Traffic-Generator function.
 

### Step 63

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/3ee7cf10-aa5a-4984-b6e1-3ba18e5d1045" />

1. On the Test tab, click Test.

- This invokes the CloudWatch alarm that you created earlier, which sends a notification to the SNS topic, which invokes the labFunction-isolator Lambda function.

### Step 64

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/1dc796b9-84ff-4b3d-97f5-42466f644f51" />

1. Navigate to the Amazon EC2 console.
2. On the Dashboard, in the Resources section, click Instances (running).
 

###  Step 65

 <img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9087337f-41bd-49d4-92fb-481a4728fab9" />

1. In the Instances section, choose the checkbox to select the App-Server instance.
2. Below that section, click the Security tab.
3. Under IAM Role, review to see that the original role attached to the instance was removed.
4. Under Security groups, review to see that the EC2 instance is now assigned an Isolated_SG security group.

- The Isolated_SG security group does not have ingress or egress rules attached, stopping the malicious intruder from being able to connect.
 
<img width="1178" height="582" alt="image" src="https://github.com/user-attachments/assets/ab84112b-b898-4ee8-9232-435cbece9a8d" />



Role used by both lambda functions

- Managed policy: `AWSLambdaBasicExecutionRole`
- Customer inline policy
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:Get*",
                "s3:List*",
                "s3:Put*"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": "us-east-1"
                }
            },
            "Action": [
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:CreateSecurityGroup",
                "ec2:DeleteSecurityGroup",
                "ec2:Describe*",
                "ec2:DisassociateIamInstanceProfile",
                "ec2:Get*",
                "ec2:List*",
                "ec2:ModifyInstanceAttribute",
                "ec2:ModifySecurityGroupRules",
                "ec2:RevokeSecurityGroupEgress",
                "ec2:RevokeSecurityGroupIngress",
                "ec2:UpdateSecurityGroupRuleDescriptionsEgress",
                "ec2:UpdateSecurityGroupRuleDescriptionsIngress",
                "lambda:InvokeFunction"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": "*",
            "Resource": [
                "arn:aws:lambda:us-east-1:078337410918:function:gbl_lab_monitoring",
                "arn:aws:iam::078337410918:role/LabStack-52553f06-5082-48-GblLabMonitoringgbllabmon-T0VP3vGQg1cL",
                "arn:aws:events:us-east-1:078337410918:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-18avZ16INqOK",
                "arn:aws:events:us-east-1:078337410918:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-XKzats7AwpdP",
                "arn:aws:events:us-east-1:078337410918:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-ZyzhhIjR4P2W",
                "arn:aws:events:us-east-1:078337410918:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-tNOlQQSjHDdw",
                "arn:aws:events:us-east-1:078337410918:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-kQYioz6gR1Il"
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

Trust policy
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



## DIY

<img width="842" height="425" alt="image" src="https://github.com/user-attachments/assets/f94848a1-4c37-4d02-a58b-3efa2ac1a2fb" />

DIY Goals

Create an Amazon SNS subscription to email a notification when an alarm is invoked.

Solution Validation Method

Our test service will confirm that a valid e-mail has been subscribed and confirmed to the same SNS topic that was used during the practice section. The SNS topic should also have a valid Lambda function subscription.
