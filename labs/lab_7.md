



<img width="2014" height="1114" alt="image" src="https://github.com/user-attachments/assets/05f9cfb8-743e-4cee-a249-17a8f6665702" />


<img width="1562" height="486" alt="image" src="https://github.com/user-attachments/assets/6fefb18a-0349-484e-b6eb-dc655f8afcc5" />


<img width="998" height="369" alt="image" src="https://github.com/user-attachments/assets/ceb8d67f-b7c6-4eb3-add5-ed19f7916f9f" />



# Lab 7 Remediating an Incident by Using AWS Config and Lambda


## Lab overview and objectives



In this lab, you will learn how to use the AWS Config service to monitor changes to specific resources in your AWS account. You will discover how to use the service to identify changes that could be a security concern, such as a user modifying an Amazon Elastic Compute Cloud (Amazon EC2) security group. Furthermore, you will then gain practical experience by integrating AWS Config with AWS Lambda to automatically remediate specific security incidents of concern.

 

After completing this lab, you should be able to do the following:

- Explain how to use AWS Identity and Access Management (IAM) roles to grant AWS services access to other AWS services.
- Enable AWS Config to monitor resources in an AWS account.
- Create and enable a custom AWS Config rule that uses a pre-created Lambda function.
- Test the behavior of an AWS Config rule to ensure it's working as intended.
- Analyze Amazon CloudWatch logs to audit when AWS Config rules are invoked.

   

## Scenario

During this lab, your responsibility is to monitor Amazon EC2 security group settings in an AWS account. You will define which inbound ports should and shouldn't be open in a security group. Your will configure a solution to automatically remediate an incident where someone modifies a security group's inbound rules and they no longer conform with the desired configuration.

When you start the lab, your AWS account will contain two IAM roles and a Lambda function. It will also contain a default VPC with a default security group in it and a custom VPC named Lab VPC, which has a security group named LabSG1 in it.

The following diagram shows the architecture that was created for you in AWS at the beginning of the lab.

<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_security/lab7/start-arch.png" alt="Starting architecture" width=600 />


During the lab, you will configure the AWS Config service to create an inventory of specific resources in one Region of your AWS account. You will then create an AWS Config rule.

By the end of this lab, you will have created the architecture shown in the following diagram.

<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_security/lab7/end-arch.png" alt="Ending architecture" width=600 />


After you build the solution, a security incident will be remediated through the steps described in the following table.

| Step | Explanation |
|------|--------------------------------|
| 1    | The AWS Config rule will monitor for any changes to security groups that are tracked in the AWS Config resources inventory.  |
| 2    | When the rule notices that changes were made to a security group, the rule will invoke the Lambda function.    |
| 3    | The function will remediate the situation by updating the desired inbound rule configuration for the security group. |



 <br>

---

## Task 1: Preparing your lab environment with CloudFormation


In this task, you will provision an SNS (short for Simple Notification Service) topic and subscribe your email address using a CloudFormation template. This topic will be used in subsequent tasks to deliver email alerts to you about important activity that occurs in the AWS account.

1. Visit <a href="console.aws.amazon.com/console/home">https://console.aws.amazon.com/console/home</a>. Then choose *Multi-session enabled* from the dropdown menu in the top right of the screen.

   <img width="500"  src="https://github.com/user-attachments/assets/c0fa4abd-534e-4635-a38f-6c58060e5cfc" />

2. Choose *Sign-in using root user email*. Then follow the instructions to log into your root account.

   <img width="300"  src="https://github.com/user-attachments/assets/af7f9159-26f0-4b60-b84d-5a2ce6db9276" />
 

3. Once logged in, in the search bar at the top of the screen, search for and select *CloudFormation*.
   
   <img width="500"  src="https://github.com/user-attachments/assets/da3a6769-ce22-4e62-8293-a549afa4fcc4" />


4. Right-click the [link]() and download a CloudFormation template to your computer

5. Choose *Create stack \> With new resources (standard)* and configure these settings.

   **Step 1: Specify template**

   - *Template source:* *Upload a template file*
   - *Upload a template file:* Click *Choose file*, then select the downloaded *lab-environment.yaml* file.
     
     <img width="800" src="https://github.com/user-attachments/assets/716e7374-d955-4cbb-9bf7-63399c0fea5d" />

   - Choose *Next*

   **Step 2: Create Stack**

   - *Stack name:* *lab-environment*
   - *SubscriptionEmail*: *\<An email address to receive notifications\>* (e.g., your UST email)
     
     <img width="800" src="https://github.com/user-attachments/assets/0db16807-5181-411c-b7d1-8d3ff525035c" />

     
   - Choose *Next*

   **Step 3: Configure stack options**
   
   - Scroll down to the bottom and tick the checkbox for *"I acknowledge that AWS CloudFormation might create IAM resources with customised names."*

   <img width="800" src="https://github.com/user-attachments/assets/5e4f3bd7-27a9-4c53-95e6-b4cf1370fed9" />
   
   - Keep all the other settings as default.
   - Choose *Next*. 

   **Step 4: Review lab-network**

   - Choose *Submit*.

   The *template* will now be used by AWS CloudFormation to generate a *stack* of resources in the AWS account.

6. Wait for the status to change to *CREATE_COMPLETE*.

   <img width="300" src="https://github.com/user-attachments/assets/1714a343-8496-4e22-9f0b-836b00afdf7e" />


   Choose *Refresh* every 15 seconds to update the display, if necessary.

7. In the email address you provided earlier, you should receive an email notification titled *AWS Notification - Subscription Confirmation* from *Login Failure Notifications* .

   <img width="500" src="https://github.com/user-attachments/assets/0220c818-9af1-474c-8c9d-447ae6841ad0" />
  
9. Click the *Confirm subscription* link to confirm the subscription of your email address to an SNS Topic created by the stack.

    <img width="500" src="https://github.com/user-attachments/assets/5d875a99-d6e4-4dbb-a2c9-d0f29f157a52" />

    Then, close the tab that displays *Subscription confirmed!* 

    > Amazon SNS is a fully managed messaging service that provides the ability to send messages to users at scale through SMS, mobile push, and email. 


You have now used your first AWS CloudFormation template to provision the lab environment, including an SNS topic and an IAM role. The purpose of the IAM role will become clear in task 2. We will take a deep dive into automating infrastructure deployment with CloudFormation in the later part of today's class.

<br>

---
 
## Task 1: Examining and updating IAM roles


In this task, you will analyze two IAM roles that were pre-provisioned for you in the lab environment. You will also update the permissions of one of the roles. AWS Config and Lambda will use these roles later in the lab.

 3. In the IAM console, observe the permissions granted to the AwsConfigLambdaSGRole role.

 - In the search box to the right of  Services, search for and choose IAM.

 - In the navigation pane, choose Roles.

 - Choose the ***AwsConfigLambdaSGRole*** link.

 - On the Permissions tab, expand `awsconfig_lambda_ec2_sg_role_policy`.

   <img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_security/lab7/awsconfig_lambda_ec2_sg_role_policy.png"  width=700 />

   The following IAM policy document (formatted in JSON) displays:
   <details><summary>Permission policy document</summary>
   <pre lang="json"><code>
    {
       "Version":"2012-10-17",
       "Statement":[
           {
              "Action":[
                  "logs:CreateLogGroup",
                  "logs:CreateLogStream",
                  "logs:PutLogEvents"
              ],
              "Resource":"arn:aws:logs:*:*:*",
              "Effect":"Allow"
           },
           {
              "Action":[
                  "config:PutEvaluations",
                  "ec2:DescribeSecurityGroups",
                  "ec2:AuthorizeSecurityGroupIngress",
                  "ec2:RevokeSecurityGroupIngress"
              ],
              "Resource":"*",
              "Effect":"Allow"
           }
       ]
   }</code></pre></details>
   <details><summary>IAM role trust policy</summary>
   <pre lang="json"><code>
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
   }</code></pre>
   </details>

   > **Analysis**: This is a custom role that was created for you. Later in this lab, you will attach this role to a Lambda function that you will create. This role defines the permissions that the Lambda function will have when it runs. The policy will allow the Lambda function to add or remove inbound rules on Amazon EC2 security groups. The policy will also allow the Lambda function to create and write events to CloudWatch logs.
   
   > The subsequent configuration step for this:
   > <img width="700" alt="image" src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_security/lab7/lambda_role.png" />



A second custom IAM role was also created for you in the account. You will look at that role and modify it in the next set of steps.

 

4. Update the permissions that are granted to the AwsConfigRole IAM role.

 - In the navigation pane, choose Roles.

 - Choose the AwsConfigRole link.

   <img width="700" alt="image" src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_security/lab7/AwsConfigRole.png" />

- On the Permissions tab, expand the ***S3Access*** policy, which is already attached to this role.
  <details>
    <summary>Permission policy document</summary>
    <pre lang="json"><code>
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Condition": {
                    "StringLike": {
                        "s3:x-amz-acl": "bucket-owner-full-control"
                    }
                },
                "Action": [
                    "s3:PutObject*"
                ],
                "Resource": [
                    "arn:aws:s3:::*/AWSLogs/*/*"
                ],
                "Effect": "Allow"
            },
            {
                "Action": [
                    "s3:GetBucketAcl"
                ],
                "Resource": "arn:aws:s3:::*",
                "Effect": "Allow"
            }
        ]
    }</code></pre></details>

    <br>

    
  <details>
    <summary>IAM role trust policy</summary>
    <pre lang="json"><code>    
    {
        "Version": "2008-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "config.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }</code></pre></details>
    
  Currently, this role grants permissions to get the bucket access control lists (ACLs) of Amazon Simple Storage Service (Amazon S3) buckets and upload objects to an S3 bucket if certain conditions are met. These permissions will allow AWS Config to write CloudWatch log files to Amazon S3.

- Near the top of the tab, choose **Add permissions** > **Attach policies**.
- To search for policies related to AWS Config, in the  Search box, search for Config and press Enter.
- Select the ***AWS_ConfigRole*** policy.
- Choose Add permissions, which is located in the lower-right corner.
    <img width="800" alt="image" src="https://github.com/user-attachments/assets/fe1c4166-f48c-4f75-adae-a8fd35b82921" />

  The policy grants read-level access (mostly Get, List, and Describe actions) to many AWS services.

  > **Analysis**: You will grant **AWS Config** the ability to use this role when you configure AWS Config in the next task. The role defines the permissions that **AWS Config** will have when monitoring one of the Regions in the AWS account.

 

In this task, you analyzed the permissions that are granted to an IAM role that a Lambda function will use later in the lab. You also updated and analyzed the permissions granted to an IAM role that AWS Config will use in the next task.

 

## Task 2: Setting up AWS Config to monitor resources

In this task, you will configure AWS Config to monitor specific resources in a Region in the AWS account.

 

5. Set up AWS Config.
- In the search box to the right of  Services, search for and choose **AWS Config**.
- Choose Get started, and configure the following settings:
  - Under Recording strategy. Choose Specific resource types.
  - Resource type: Choose ***AWS EC2 SecurityGroup***. For Frequency choose ***Continuous***.

    <img width="800" alt="image" src="https://github.com/user-attachments/assets/97d12181-fc2d-4d9b-9a02-543287397824" />
  
  - IAM role for AWS Config Choose ***Choose a role from your account***.
  - Existing roles: Choose AwsConfigRole.

    <img width="800" alt="image" src="https://github.com/user-attachments/assets/4903df0f-216e-467f-9e57-fb459c52c6d3" />

    > Note: Recall that AwsConfigRole was the second role that you analyzed in the previous task.
  
  - In the Delivery channel section, notice that AWS Config will store findings in an S3 bucket by default. Keep the default settings, and choose Next.
    
    <img width="800" alt="image" src="https://github.com/user-attachments/assets/3da7869c-3d7a-4b74-9de6-c66d9717fbc0" />
  
  - On the AWS Managed Rules page, choose Next at the bottom of the page.
  - Review the AWS Config setup details, and then choose Confirm.

    <img width="800" alt="image" src="https://github.com/user-attachments/assets/d176f4fd-8518-45b1-8a1b-83440b2e81a7" />


A banner appears briefly, and then the AWS Config Dashboard displays.

6. To observe the resource inventory that AWS Config created, in the navigation pane, choose Resources.

   The Resource Inventory page displays and lists the Amazon EC2 resources in your account.
   
   > Note: If the resources list displays a message saying that your resources are being discovered, wait a few minutes. It might take a few minutes for AWS Config to identify all of your resources.
   
   > **Analysis**: Recall that you configured AWS Config to inventory EC2 Security Group type resources. The Amazon EC2 security groups that were pre-provisioned in the Region where you set up AWS Config are included in the inventory. However, notice that many other resource types also appear in the inventory. AWS Config tracks resources related to the resources that you are primarily interested in, because related resources can affect the behavior of the primary resources. The lab environment that you are working in includes many of these related resources (such as internet gateways and network ACLs).

 

In this task, you set up the AWS Config service in one Region in the AWS account to monitor specific resources of interest. You then observed how AWS Config created an inventory of resources.

 

## Task 3: Modifying a security group that AWS Config monitors

In this task, you will configure new inbound rule settings in one of the security groups that is listed in the AWS Config resource inventory. The purpose is to effectively emulate a security incident. Some of the inbound rule settings that you will define during this task won't match the desired settings, which you will define in a later task.

 

Locate the security group in the Lab VPC.

In the search box to the right of  Services, search for and choose VPC.

In the navigation pane, choose the Filter by VPC box, and choose Lab VPC.

In the navigation pane, choose Security groups.

At least two security groups are defined in this VPC.

Select the LabSG1 security group.

 

Add inbound rules to the security group to allow HTTP, HTTPS, SMTPS, and IMAPS network traffic.

Choose the Inbound rules tab, and then choose Edit inbound rules.

Notice that one inbound rule for HTTP connections is already defined.

For the existing rule, change Source to Anywhere-IPv4.

Choose Add rule and configure the following:

Type: Choose HTTPS.

Source: Choose Anywhere-IPv4.

Choose Add rule again and configure the following:

Type: Choose SMTPS.

Source: Choose Anywhere-IPv4.

Choose Add rule again and configure the following:

Type: Choose IMAPS.

Source: Choose Anywhere-IPv4.

Choose Save rules.


<img width="800" alt="image" src="https://github.com/user-attachments/assets/bee3d7fc-29db-4a00-8fd9-da14d1e76d6d" />

The inbound rules should now look like the rules in the following screenshot (although your security group rule IDs are different).

previously configured inbound rules

 

In this task, you located a security group in the Lab VPC and defined three new inbound rules in the security group. Later in this lab, you will observe these modifications are identified as a security incident and remediated.

 

## Task 4: Creating an AWS Config rule that calls a Lambda function
In this task you configure an AWS Config rule to invoke a pre-created Lambda function. The rule and the function will work together to ensure that monitored Amazon EC2 security groups have only the desired inbound rules.

 

9. Go to the i AWS Details section and copy the value for LambdaFunctionARN to your clipboard.
    <details><summary>LambdaFunctionARN</summary>
     <pre><cod>arn:aws:lambda:us-east-1:818542204083:function:awsconfig_lambda_security_group</cod></pre>
    </details>
    > Note: You will use the ARN in the next set of steps.

 

10. Create a new AWS Config rule that will invoke the Lambda function whenever monitored Amazon EC2 security groups are modified.

- Navigate to the AWS Config console.
- In the navigation pane, choose Rules.
  Currently, AWS Config doesn't have any rules defined.
- Choose Add rule.
- For Select rule type, choose Create custom Lambda rule.
  <img width="821" alt="image" src="https://github.com/user-attachments/assets/1127bb26-d551-433e-a75e-62f8cd66ebab" />
- Choose Next.
- On the Configure rule page, configure the following:
  - AWS Lambda function ARN: Paste in the Lambda function ARN that you copied.
  - Name: Enter EC2SecurityGroup
  - Description: Enter Restrict inbound ports to HTTP and HTTPS
    <img width="779" alt="image" src="https://github.com/user-attachments/assets/c6deae88-b7ac-44e6-84e3-adc44e74a0f7" />
  - Trigger type: Select When configuration changes.
  - Scope of changes: Choose Resources.
  - Resource type: Choose AWS EC2 SecurityGroup.
    AWS EC2 SecurityGroup appears in the resources area.
    <img width="780" alt="image" src="https://github.com/user-attachments/assets/28d60cfb-90ac-43ad-8f46-ed7355b7d92b" />
  - In the Parameters section, add a parameter with the following settings:
    
    - Key: debug
    - Value: true
    <img width="778" alt="image" src="https://github.com/user-attachments/assets/a786bec3-b96c-41ae-b199-e75a703ea2d2" />
    
    > Note: Any parameters that you define here will be passed by this AWS Config rule to the EC2SecurityGroup Lambda function. 

- Choose Next, and then choose Save.

 
11. Observe the AWS Config EC2SecurityGroup rule details.

- Choose the ***EC2SecurityGroup*** link.
- In the Resources in scope section, choose the Noncompliant dropdown menu, and choose All.
  In the Rule details section, notice the Last successful evaluation field. Initially, this field displays Not available; however, after a few minutes, a timestamp will display.
  <img width="800" alt="image" src="https://github.com/user-attachments/assets/8bc0a028-40bc-4a68-8e22-dea6714b8d0e" />
  > Note: The initial evaluation might take a few minutes to complete. This same evaluation will also occur when any security group that is within scope is modified in the future.
  > Notice the Amazon EC2 security group resources that are listed as in scope.
  > While the initial evaluation occurs, the Compliance value will be No results available. After several minutes, the value for each security group resource changes to Compliant. Wait until you see that it is compliant.

Notice that the Annotation column displays Permissions were modified.

 

In this task, you configured an AWS Config rule to invoke the pre-created lambda function. The rule and the function will work together to monitor and remediate any undesired updates to inbound rules for monitored Amazon EC2 security groups. 

 

## Task 5: Revisiting the security group configuration
Now that the initial AWS Config compliance evaluation has occurred, you will reexamine the LabSG1 security group. You will observe whether the security incident changes (the modifications that you made to the inbound rules) were noticed and then remediated.

 

Analyze the inbound rules defined on the LabSG1 security group.

Navigate to the VPC console.

In the navigation pane, choose the Filter by VPC box, and choose Lab VPC.

In the navigation pane, choose Security groups.

Select the LabSG1 security group.

On the Inbound rules tab, notice that only HTTP and HTTPS traffic is permitted.

The inbound rules should now look like the rules in the following screenshot (although your security group rule IDs are different).

<img width="800" alt="image" src="https://github.com/user-attachments/assets/0deb2742-741b-4d97-bb92-93a32cd10c56" />


> **Analysis**: Recall that you defined inbound rules for SMTPS and IMAPS, as well as HTTP and HTTPS, on this security group. However, the rules for SMTPS and IMAPS no longer exist. Also, recall that you set the IP version for all rules to only IPv4, but now the HTTP and HTTPS rules are defined for IPv4 and IPv6.

In summary, you modified the inbound rules in this security group to look like the ones in the following screenshot. However, they have been significantly modified to look like the previous screenshot.

previously configured inbound rules

 

16. Analyze the Lambda function code.

 - Navigate to the Lambda console.
 - In the navigation pane, choose Functions.
 - Choose the awsconfig_lambda_security_group function link.
   <details><summary>The function's template generated from the function's configuration (see task 1 for how Policies in it might be specified (through AwsConfigLambdaSGRole))</summary>
    <pre><code>
    # This AWS SAM template has been generated from your function's configuration. If
    # your function has one or more triggers, note that the AWS resources associated
    # with these triggers aren't fully specified in this template and include
    # placeholder values. Open this template in AWS Infrastructure Composer or your
    # favorite IDE and modify it to specify a serverless application with other AWS
    # resources.
    AWSTemplateFormatVersion: '2010-09-09'
    Transform: AWS::Serverless-2016-10-31
    Description: An AWS Serverless Application Model template describing your function.
    Resources:
      awsconfiglambdasecuritygroup:
        Type: AWS::Serverless::Function
        Properties:
          CodeUri: .
          Description: ''
          MemorySize: 128
          Timeout: 300
          Handler: index.lambda_handler
          Runtime: python3.12
          Architectures:
            - x86_64
          EphemeralStorage:
            Size: 512
          EventInvokeConfig:
            MaximumEventAgeInSeconds: 21600
            MaximumRetryAttempts: 2
          PackageType: Zip
          Policies:
            - Statement:
                - Action:
                    - logs:CreateLogGroup
                    - logs:CreateLogStream
                    - logs:PutLogEvents
                  Resource: arn:aws:logs:*:*:*
                  Effect: Allow
                - Action:
                    - config:PutEvaluations
                    - ec2:DescribeSecurityGroups
                    - ec2:AuthorizeSecurityGroupIngress
                    - ec2:RevokeSecurityGroupIngress
                  Resource: '*'
                  Effect: Allow
          RecursiveLoop: Terminate
          SnapStart:
            ApplyOn: None
          Tags:
            cloudlab: c103198a2383324l10620395t1w818542204083
          RuntimeManagementConfig:
            UpdateRuntimeOn: Auto
    </code></pre>
   </details>
   

- In the Code source section, open the awsconfig_lambda_security_group.py file that you imported.
  <img width="800" alt="image" src="https://github.com/user-attachments/assets/d6330c74-3de9-44ac-b380-e6a7a4fe96ab" />
  
  <a href="https://github.com/justinjiajia/certifications/blob/main/aws/cloud_security/labs/source/lab7_lambda_code.py">Python code</a>
 
Observe the following details:

On line 2, the function `imports boto3`, which is the AWS SDK for Python.

On line 9, REQUIRED_PERMISSIONS are defined. This array includes the desired ingress (inbound) IP permissions for Amazon EC2 security group resources that are in scope of the AWS Config rule that you defined.

```python
REQUIRED_PERMISSIONS = [
{
    "IpProtocol" : "tcp",
    "FromPort" : 80,
    "ToPort" : 80,
    "UserIdGroupPairs" : [],
    "IpRanges" : [{"CidrIp" : "0.0.0.0/0"}],
    "PrefixListIds" : [],
    "Ipv6Ranges": [
        {
            "CidrIpv6": "::/0"
        }
    ]
},
{
    "IpProtocol" : "tcp",
    "FromPort" : 443,
    "ToPort" : 443,
    "UserIdGroupPairs" : [],
    "IpRanges" : [{"CidrIp" : "0.0.0.0/0"}],
    "PrefixListIds" : [],
    "Ipv6Ranges": [
        {
            "CidrIpv6": "::/0"
        }
    ]
}]
```

The required permissions are defined in the format that the `describe_security_groups()` API call requires. This call is invoked on line 117.
 

For more information about this API call, see the [AWS SDK for Python documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_security_group_rules).

On line 129, the function checks whether the `debug` parameter is included in the AWS Config rule. Recall that this was a parameter you configured when you defined the AWS Config rule in task 4. If debug is set to true then the Lambda function code will print additional debugging information when it runs. You can see examples of this throughout the Lambda code.

 

In this task, you observed the logic for the Lambda function to detect and remove the additional permissions for SMTPS (TCP port 465) and IMAPS (TCP port 993) in the security group.

> **Analysis**: The security incident (when you modified the inbound rules) occurred *before* you created the AWS Config rule and Lambda function to remediate such incidents. During initial rule validation, AWS Config detected the security incident.

> If you were to modify the security group again, an AWS Config compliance evaluation would be initiated. The evaluation would invoke the Lambda function, and your changes would be reverted so that the inbound rules again match the desired settings. The default security groups are being similarly monitored and would have their settings remediated if changed.

 

## Task 6: Using CloudWatch logs for verification

In this task, you will analyze **CloudWatch** logs and filter the log entries to find evidence of the remediation.

 

Locate the logs that show evidence of the changes that the AWS Config rule and its associated Lambda function made to the security group.

In the search box to the right of  Services, search for and choose CloudWatch.

In the navigation pane, expand  Logs and then choose Log groups.

Choose the awsconfig_lambda_security_group log group link.

One or more log stream entries are visible in the log streams list.


<img width="928" alt="image" src="https://github.com/user-attachments/assets/3e115875-559f-4f64-a423-ac00e20cc787" />

Choose Search all.

In the Filter events search field, enter revoking for and then press Enter.

<img width="800" alt="image" src="https://github.com/user-attachments/assets/fecc9fc5-68ad-42fb-8aa2-3e36f29e16b8" />

Expand  each log event and review the contents.

<img width="800" alt="image" src="https://github.com/user-attachments/assets/a840831a-fca2-4fd0-a54e-c0b5e338154a" />

Each event provides details about the action that the Lambda function took. In one of the events, you should find details showing that the inbound rules that you manually added for SMTPS (TCP port 465) and IMAPS (TCP port 993) were removed.

The other filtered events logged the changes to the other two security groups that exist in your account. These security groups are also in the resources inventory that your AWS Config rule is monitoring.

In this task, you observed evidence in the CloudWatch logs that AWS Config invoked the Lambda function to automatically revoke the modifications that were made to the security group.

 

Submitting your work
To record your progress, choose Submit at the top of these instructions.

 

When prompted, choose Yes.

After a couple of minutes, the grades panel appears and shows you how many points you earned for each task. If the results don't display after a couple of minutes, choose Grades at the top of these instructions.

 Tip: You can submit your work multiple times. After you change your work, choose Submit again. Your last submission is recorded for this lab.

 

To find detailed feedback about your work, choose Submission Report.


## Delete AWS Config Recorder:

log in as an admin user
 

Go to the AWS Config Console and select the correct Region.

In the left navigation pane, choose Settings.

On the "General" tab, find the Recording section.

Toggle the recording switch to Off and save the changes.


```shell
aws configservice delete-configuration-recorder --configuration-recorder-name default
```

More relevant shell commands:

```shell
# Getting all recorders quickly, especially for automation.
aws configservice list-configuration-recorders
# Inspecting specific settings of the main (customer-managed) recorder.
aws configservice describe-configuration-recorders
 
```
