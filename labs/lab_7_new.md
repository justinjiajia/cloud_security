



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


In this task, you will provision two IAM Roles with proper permissions, a Lambda Function, an SNS Topic with your email address subscribed, and several VPC related resources, using a CloudFormation template.

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
   - *Upload a template file:* Click *Choose file*, then select the downloaded *lab_7_environment.yaml* file.
     
     <img width="800" src="https://github.com/user-attachments/assets/7dbbe59f-8407-4591-8bca-a33e079cb9c4" />


   - Choose *Next*

   **Step 2: Create Stack**

   - *Stack name:* *lab-environment*
   - *ITSCAccountString*: *\<your ITSC account string\>* (The string before the `@` sign of your UST email address)
   - *SubscriptionEmail*: *\<An email address to receive notifications\>* (e.g., your UST email)
     
     <img width="800" src="https://github.com/user-attachments/assets/03f4938c-9b04-4378-b8e6-397cf3984e2e" />


     
   - Choose *Next*

   > Note: The entries displayed in the *Parameters* section and requiring your inputs were defined in the *Parameters* section of the YAML template file. 

   **Step 3: Configure stack options**
   
   - Scroll down to the bottom and tick the checkbox for *"I acknowledge that AWS CloudFormation might create IAM resources with customised names."*

     <img width="800" src="https://github.com/user-attachments/assets/5e4f3bd7-27a9-4c53-95e6-b4cf1370fed9" />
   
   - Choose *Next*. 

   **Step 4: Review lab-network**

   - Choose *Submit*.

   The *template* will now be used by AWS CloudFormation to generate a *stack* of resources in the AWS account.

6. Wait for the status to change to *CREATE_COMPLETE*.

   <img width="300" src="https://github.com/user-attachments/assets/4d151a38-9428-49da-8616-f3b77ca4ec54" />

   Choose *Refresh* every 15 seconds to update the display, if necessary.

7. In the email address you provided earlier, you should receive an email notification titled *AWS Notification - Subscription Confirmation* from *EC2 SecurityGroup Change Notifications* .

   <img width="600" src="https://github.com/user-attachments/assets/89e830e5-5a1a-4737-b38e-f4319ed27e88" />

  
8. Click the link in the *"SubscribeURL"* field to subscribe your email address to the SNS Topic. Then close the tab that displays a snippet of XML source code.

You have now used the AWS CloudFormation template to provision your lab environment, including two IAM Roles, a Lambda Function,  a SNS Topic, and several VPC related resources. The purpose of these resources will become clear in subsequent tasks. 

The following diagram shows the architecture that was created for you in AWS at the beginning of the lab.

<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_security/lab7/start-arch.png" alt="Starting architecture" width=600 />

<br>

---
 
## Task 2: Examining IAM roles


In this task, you will analyze two IAM roles that were pre-provisioned for you. AWS Config and Lambda will use these roles later in the lab.

1. In the IAM console, observe the permissions granted to the *AwsConfigLambdaSGRole* role.

 - In the search box to the right of  Services, search for and choose IAM.

 - In the navigation pane, choose *Roles*.

 - Choose the *AwsConfigLambdaSGRole* link.

 - On the *Permissions* tab, expand `awsconfig_lambda_ec2_sg_role_policy`, and analyze the policy displayed.

   <img width="800" src="https://github.com/user-attachments/assets/929dc383-68d1-43f3-8fdf-b61ba4e602ef" />

   

   > **Analysis**: This is a custom role that was created for you. Later in this lab, you will attach this role to a Lambda function that you will create. This role defines the permissions that the Lambda function will have when it runs. The policy will allow the Lambda function to add or remove inbound rules on Amazon EC2 security groups. The policy will also allow the Lambda function to create and write events to CloudWatch Logs.


2. A second custom IAM role named *AwsConfigRole* was also created in the account. Let's also observe the permissions granted to it.
   
- In the navigation pane, choose Roles.

- Choose the *AwsConfigRole* link.

  <img width="800" src="https://github.com/user-attachments/assets/83684a96-dd5e-483f-a192-d9ab49c25e97" />

- On the Permissions tab, two inline policies named  *S3Access* and *SNSPublish* respectively, and an AWS managed policy named *AWS_ConfigRole* are already attached to this role.

    
  > **Analysis**: The *S3Access* policy grants permissions to get the bucket access control lists (ACLs) of Amazon Simple Storage Service (Amazon S3) buckets and upload objects to an S3 bucket if certain conditions are met. These permissions will allow AWS Config to write CloudWatch log files to Amazon S3.

  > The *SNSPublish* policy grants permissions to the role to publish updates to the SNS Topic created by the CloudFormation stack in task 1.
  
  > The *AWS_ConfigRole* policy grants read-level access (mostly Get, List, and Describe actions) to many AWS services.
  
In the next task, you will grant **AWS Config** the ability to use this role when you configure AWS Config. The role defines the permissions that **AWS Config** will have when monitoring AWS resources in the AWS account.



<br>

---



## Task 3: Setting up AWS Config to monitor resources

In this task, you will configure AWS Config to monitor specific resources in a Region in the AWS account.

1. Set up a customer managed configuration recorder in AWS Config
   
- In the search box at the top left corner, search for and choose **AWS Config**.
  
- Choose *Get started*, and configure the following settings:

  <img width="800" src="https://github.com/user-attachments/assets/6cecef49-aa12-42d1-877d-54ab721f1167" />

- Under *Recording strategy*. Choose *Specific resource types*.
- *Resource type*: Choose ***AWS EC2 SecurityGroup***. For Frequency choose ***Continuous***.

  <img width="800" src="https://github.com/user-attachments/assets/05f9cfb8-743e-4cee-a249-17a8f6665702" />
  
- *IAM role for AWS Config*: Choose ***Choose a role from your account***.
- *Existing roles*: Choose ***AwsConfigRole***.

  <img width="800" src="https://github.com/user-attachments/assets/4903df0f-216e-467f-9e57-fb459c52c6d3" />

  > Note: Recall that AwsConfigRole was the second role that you analyzed in the previous task.
  
- In the *Delivery channel* section, notice that AWS Config will store findings in an S3 bucket by default.
- Tick the checkbox for *Stream configuration changes and notifications to an Amazon SNS topic*
- Select ***Choose a topic from your account***
- *SNS topic name*: Select the SNS Topic created in task 1 from the dropdown menu, i.e., *ust-\<your ITSC account string\>-config-topic*
  > This setting allows you to receive email alerts reactive to any configuration changes made to the monitored resources.
  
- Keep the default settings, and choose *Next*.
    
  <img width="800" src="https://github.com/user-attachments/assets/81bd8b30-a7c1-42e1-b1ae-f8e2b71153d9" />

  
  
- On the *Step 2: Rules* page, choose *Next* at the bottom of the page.
- Review the AWS Config setup details, and then choose *Confirm*.

  <img width="800" src="https://github.com/user-attachments/assets/60526c9c-7805-4109-a34d-ac16c36ce513" />



A banner appears briefly, and then the AWS Config Dashboard displays.

You should also receive several email notifications with subject lines that begin with something like *[AWS Config:us-east-1] AWS::EC2::SecurityGroup*. These notifications indicate that the AWS Config recorder has discovered EC2 security group resources in your account and has published the corresponding events to the configured SNS topic, which then delivered them to your email subscription. 

2. In the left navigation pane, choose *Resources* to review the resource inventory that AWS Config is currently recording.

   <img width="800" src="https://github.com/user-attachments/assets/fcf06a9b-6278-42d8-b6ff-313d239205de" />


 

   The *Resource inventory*  page lists two security groups that AWS Config is recording, along with the default configuration recorder you set up in step 1. Your security group IDs will differ, but they should resemble the ones shown in the reference screenshot.
     
   Recall that in step 1, you configured AWS Config to record resources of type *EC2 SecurityGroup*, which is why these security groups now appear in the inventory.
   
   > Between the two security groups, one is the default security group that is automatically created with the VPC defined in the CloudFormation YAML template. Every new VPC in AWS includes a default security group.
   > The second security group is named *LabSG1*. It is also defined in the YAML template and is intended for experimentation and testing in the later steps of this lab. 

 
- Select one of the security groups — preferably *LabSG1*  — and then choose *Resource timeline* to display all configuration items that AWS Config has captured for this resource so far.
  
  <img width="800" src="https://github.com/user-attachments/assets/93414497-1d9c-443e-a641-4769ecb76177" />

  **Important: Keep this browser tab open**. You will return to the *Resource timeline* view to observe configuration changes as you proceed through the lab.  
     
  > AWS Config uses the configuration recorder to continuously capture configuration changes for supported resource types.
  > In the  *Resource timeline* view, AWS Config not only shows the configuration items, but also provides links to related AWS CloudTrail events (from CloudTrail Event history) to help you see the full context of each configuration change.  These CloudTrail correlations are performed on a best-effort basis and might not be available for every change.
 

In this task, you configured AWS Config to monitor EC2 security groups in your AWS account and inspected their recorded configuration history.

<br>

---

## Task 4: Emulating a security incident


In this task, you will configure new inbound rule settings in the security group *LabSG1* (one listed in the AWS Config resource inventory). The purpose is to effectively emulate a security incident. Some of the inbound rule settings that you will define during this task won't match the desired settings, which you will define in a later task.

 
1. Locate the security group in the *Lab VPC*.

- Go to the VPC console. In the left navigation pane, choose the *Filter by VPC* box, and choose *Lab VPC*.

  <img width="800" src="https://github.com/user-attachments/assets/5db602ac-2d88-48ae-bab3-99bd2ccd67aa" />


- In the navigation pane, choose *Security groups*.

  You will see two security groups defined in this VPC.

- Select the *LabSG1* security group.

 

2. Add inbound rules to the security group to allow **HTTP**, **HTTPS**, **SMTPS**, and **IMAPS** network traffic.

- Choose the Inbound rules tab, and then choose Edit inbound rules.
- Notice that one inbound rule for HTTP connections is already defined.


- Choose Add rule again and configure the following:

  - Type: Choose *SMTPS*.
  - Source: Choose *Anywhere-IPv4*.

- Choose Add rule again and configure the following:

  - Type: Choose *IMAPS*.
  - Source: Choose *Anywhere-IPv4*.

- Choose *Save rules*.

  The inbound rules should now look like the rules in the following screenshot (although your security group rule IDs are different).

  <img width="1095" height="236" alt="image" src="https://github.com/user-attachments/assets/10e2eb02-d014-4161-b4cb-d35caf3f9bde" />


  **Important: Keep this bowswer tab open**. You will come back to investigate the effect of remediation in task 5.
  
3. After making the change, return to the browser tab that shows the *Resource timeline* for the affected security group, and refresh the page so that the latest configuration data is displayed.

   <img width="800" alt="image" src="https://github.com/user-attachments/assets/32eb3b35-b150-4c42-b965-5babaa54e486" />


   You should now see a new configuration item that reflects the security group update, along with the correlated CloudTrail event.

As before, AWS Config has streamed this configuration change to the configured Amazon SNS topic, which then forwarded an email notification to your subscribed address for alerting. 

In this task, you located a security group in the lab VPC and added three new inbound rules to it. Later in the lab, these changes will be treated as a security incident and automatically remediated by the configured AWS Config rule and its remediation workflow. 
 

 
<br>

---

## Task 5: Creating an AWS Config rule that calls a Lambda function

In this task, you configure an AWS Config rule to invoke a pre-created Lambda Function. The rule and the function will work together to ensure that monitored Amazon EC2 security groups have only the desired inbound rules.

 
1. In the search box at the top left of the screen, search for *Lambda* and choose to open the console in a new browser tab.

   <img width="500" src="https://github.com/user-attachments/assets/8839b3cc-7132-414a-91f7-dc7a5577d052" />

2. Choose the *awsconfig_lambda_security_group* link in the *Functions* list. This is the Lambda Function created by the CloudFormation stack in task 1.

   <img width="800" src="https://github.com/user-attachments/assets/0565218c-baed-4711-8acd-cb38c0bca284" />


   **Important: Keep the browser tab open**. You'll return to this page for copying the Lambda function ARN and exploring its code.
   


3. Create a new AWS Config rule that will invoke the Lambda Function whenever monitored Amazon EC2 security groups are modified.

- Switch over to the AWS Config console.
- In the navigation pane, choose *Rules* (not *Rules* under *Aggregator*).
  
  Currently, AWS Config doesn't have any rules defined.
 
- Choose *Add rule*.
- For *Select rule type*, choose ***Create custom Lambda rule***.
  
  <img width="800" src="https://github.com/user-attachments/assets/1127bb26-d551-433e-a75e-62f8cd66ebab" />

  This allows us to define a Lambda function with  custom code to evaluate whether monitored AWS resources comply with the rule.
  
- Choose *Next*.
  
- On the *Configure rule* page, configure the following:

   
  - *Name*: Enter ***EC2SecurityGroup***
  - *Description*: Enter ***Restrict inbound ports to HTTP and HTTPS***
    
    <img width="800" src="https://github.com/user-attachments/assets/c6deae88-b7ac-44e6-84e3-adc44e74a0f7" />
    
  - Copy the *Function ARN* field from the tab that displays the Lambda console. Then paste the copied ARN into the *AWS Lambda function ARN* field on the *Configure rule* page.
    
    <img width="400" src="https://github.com/user-attachments/assets/dc4d808d-515a-45ad-a06f-47accece16f1" />
    
  - Trigger type: Select ***When configuration changes***.
  - Scope of changes: Choose ***Resources***.
  - *Resource type*: Choose ***AWS EC2 SecurityGroup***.
    
    <img width="800" src="https://github.com/user-attachments/assets/8cd00982-5642-42ea-97ab-6686f1052fb8" />

  - In the Parameters section, add a parameter with the following settings:
    
    - Key: ***debug***
    - Value: ***true***
      
      <img width="800" src="https://github.com/user-attachments/assets/a786bec3-b96c-41ae-b199-e75a703ea2d2" />
    
    > Note: Any parameters that you define here will be passed by this AWS Config rule to the Lambda function. 

- Choose *Next*, and then choose *Save*.

 
4. Observe the AWS Config *EC2SecurityGroup* rule details.

- Choose the *EC2SecurityGroup* link.
  
- In the *Resources in scope* section, choose the *Noncompliant* dropdown menu, and choose ***All***.
  
  In the *Rule details* section, notice the *Last successful evaluation* field. Initially, this field displays *Not available*; However, after just a moment (refresh the browser tab if needed), a timestamp will display with a green tick icon prepended.

  <img width="800" src="https://github.com/user-attachments/assets/b1983d0c-de97-470f-8ad3-18a7d5ad77a8" />


  While the initial evaluation occurs, the *Compliance* column will show *No results available*. After just a moment, the value for each security group resource changes to *Compliant*. Wait until you see that it is compliant.

  Notice that the *Annotation* column displays *Permissions were modified. 2 new revocation(s). 2 new authorization(s).*.

5. Return to the browser tab that shows the *Resource timeline* for *LabSG1*, and refresh the page to show the latest configuration changes.

   <img width="800" src="https://github.com/user-attachments/assets/f69caf31-187d-434c-ba0b-87a67463f90b" />


You should also receive several email notifications about the configuration updates to the monitored resources.
 

In this task, you configured an AWS Config rule to invoke the pre-created Lambda function. The rule and the function will work together to monitor and remediate any undesired updates to inbound rules for monitored Amazon EC2 security groups. 


<br>

---

 

## Task 6: Revisiting the security group configuration

Now that the initial AWS Config compliance evaluation has occurred, you will re-examine the *LabSG1* security group. You will observe whether the security incident changes (the modifications that you made to the inbound rules) were noticed and then remediated.

 

1. Analyze the inbound rules defined on the *LabSG1* security group.

- Switch to the browser tab that shows the *LabSG1* security group details, and refresh the page to load the latest configuration.

- On the Inbound rules tab, notice that only HTTP and HTTPS traffic is permitted.

  The inbound rules should now look like the rules in the following screenshot (although your security group rule IDs are different).

  <img width="800" src="https://github.com/user-attachments/assets/0dfcb234-4be5-4c19-943d-b68d8d83cf54" />


  > Recall that in task 4, you added two extra inbound rules to this security group to allow SMTPS and IMAPS traffic. However, those SMTPS and IMAPS rules no longer exist, and an additional HTTP rule has been added. This indicates that your manual changes were evaluated and automatically remediated by the Lambda function attached to the AWS Config rule.
 
 

2. Analyze the Lambda function code.

- Navigate to the Lambda console.
- In the navigation pane, choose *Functions*.
- Choose the *awsconfig_lambda_security_group* function link.

- In the *Code source* section, open the *index.py* file.
  
  <img width="800" alt="image" src="https://github.com/user-attachments/assets/d6330c74-3de9-44ac-b380-e6a7a4fe96ab" />
 
  Observe the following details:

  - On line 2, the function `imports boto3`, which is the AWS SDK for Python.

  - On line 9, `REQUIRED_PERMISSIONS` are defined. This array includes the desired ingress (inbound) IP permissions for Amazon EC2 security group resources that are in scope of the AWS Config rule that you defined.

    ```python
    REQUIRED_PERMISSIONS = [
    {
        "IpProtocol" : "tcp",
        "FromPort" : 80,
        "ToPort" : 80,
        "UserIdGroupPairs" : [],
        "IpRanges" : [{"CidrIp" : "0.0.0.0/0"}],
        "PrefixListIds" : []
    },
    {
        "IpProtocol" : "tcp",
        "FromPort" : 443,
        "ToPort" : 443,
        "UserIdGroupPairs" : [],
        "IpRanges" : [{"CidrIp" : "0.0.0.0/0"}],
        "PrefixListIds" : []
    }]
    ```

  - The `evaluate_compliance` function on line 42 is the workhorse of this Python script. This function handles both checking compliance and automatically fixing non-compliant security groups.  
      - Evaluation:
        
        The function checks if the actual security group permissions match the `REQUIRED_PERMISSIONS`, and stores the comparison results in two list:
           - `authorize_permissions`: Rules that should be present (`REQUIRED_PERMISSIONS`) but are missing from the current setup.
           - `revoke_permissions`: Rules that are currently present but should not be there (i.e., any rule not in `REQUIRED_PERMISSIONS`).
      
      - Remediation:

        If any differences are found, the remediation occurs in two distinct phases:
          - Revoke unwanted rules: If `revoke_permissions` list is not empty, it calls `revoke_security_group_ingress` to remove the unwanted rules.
          - Authorize required rules: If `authorize_permissions` list is not empty, it calls `authorize_security_group_ingress` to add the missing, required rules.

  - In this Lambda code, any line that calls `print()`  writes logs to CloudWatch Logs, because Lambda automatically sends everything written to stdout/stderr to a CloudWatch Logs log stream.       

 

In this task, you observed the logic for the Lambda function to detect and remove the additional permissions for SMTPS (TCP port 465) and IMAPS (TCP port 993) in the security group, and add required permissions.

> Note that the security incident (when you modified the inbound rules in task 4) occurred *before* you created the AWS Config rule and Lambda function to remediate such incidents (in task 5). During initial rule validation, AWS Config detected the security incident, and triggered the .

> If you were to modify the security group again, an AWS Config compliance evaluation would be initiated. The evaluation would invoke the Lambda function, and your changes would be reverted so that the inbound rules again match the desired settings. The default security groups are being similarly monitored and would have their settings remediated if changed.


<br>

---

## Task 7: Using CloudWatch logs for verification

In this task, you will analyze **CloudWatch** logs and filter the log entries to find evidence of the remediation.

 
1. Locate the logs that show evidence of the changes that the AWS Config rule and its associated Lambda function made to the security group.

- Go to the CloudWatch console.

- In the navigation pane, expand  *Logs* and then choose *Log Management*.

- Choose the *awsconfig_lambda_security_group* log group link.

  One or more log stream entries are visible in the *Log streams* list.


  <img width="800" src="https://github.com/user-attachments/assets/dac9bde7-df55-4890-9648-ac2396a99c7a" />


- Choose *Search all log streams*.

- In the *Filter events* search field, enter ***revoking for*** and then press Enter.

  <img width="800" alt="image" src="https://github.com/user-attachments/assets/65df695e-aaa8-4130-a6dd-371c15592c39" />

- Expand  each log event and review the contents.

  > Each event provides details about the action that the Lambda function took. In one of the events, you should find details showing that the inbound rules that you manually added for SMTPS (TCP port 465) and IMAPS (TCP port 993) were removed.
 

In this task, you observed evidence in the CloudWatch logs that AWS Config invoked the Lambda function to automatically revoke the modifications that were made to the security group.

 


## After-class task: Clean up all lab resources

 

1. Stop AWS Config Recorder

- Go to the AWS Config Console.

- In the left navigation pane, choose *Settings*.

- On the *Customer managed recorder* tab, choose *Stop Recording* in the *Recorder* section.

  <img width="800" src="https://github.com/user-attachments/assets/fbb7336f-6c9e-4c03-a181-445de3b70866" />

  > Note: Neither stopping nor deleting the recorder will delete the configuration history files already delivered to your Amazon S3 bucket. You must manage and delete those files separately if needed.



<img width="999" height="297" alt="image" src="https://github.com/user-attachments/assets/1adf27e7-6f05-47f4-be80-eb6233c6aee2" />
Type confirm when you are prompted to confirm the deletion.

2. Delete the *lab-environment* stack

- Navigate to the *CloudFormation* console.
- On the *Stacks* page, select and delete all listed stacks in the reverse order of their creation.
   
 
