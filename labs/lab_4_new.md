 
# Lab 2 Using Resource-Based Policies to Secure an S3 Bucket


## Lab overview and objectives

In this lab, you will learn how to configure permissions by using AWS Identity and Access Management (IAM) identity-based and resource-based policies, such as Amazon Simple Storage Service (Amazon S3) bucket policies. You will also learn how IAM policies and resource policies define access permissions.

After completing this lab, you should be able to do the following:
- Recognize how to use IAM identity-based policies and resource-based policies to define fine-grained access control to AWS services and resources.
- Describe how an IAM user can assume an IAM role to gain different access permissions to an AWS account.
- Explain how S3 bucket policies and IAM identity-based policies that are assigned to IAM users and roles affect what users can see or modify across different AWS services in the AWS Management Console.
 

 

## Scenario
The following diagram shows the architecture that was created for you in AWS at the beginning of the lab.

<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_security/lab3/start-arch.png" alt="Starting architecture with an IAM user, group, and policy, and S3 buckets" />

The lab environment has three preconfigured Amazon S3 buckets: bucket1, bucket2, and bucket3. The environment also has a preconfigured IAM role, which allows access to certain buckets and their objects when the role is assumed. You will analyze different policies to better understand how they control your access level.

By the end of this lab, you will have created the architecture shown in the following diagram.


<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_security/lab3/end-arch.png" alt="Architecture now includes a state machine, three Lambda functions, SNS topic, and email report" />

 

## Login


1. Choose *Multi-session enabled* from the dropdown menu

<img width="567" height="151" alt="image" src="https://github.com/user-attachments/assets/c0fa4abd-534e-4635-a38f-6c58060e5cfc" />

2. Choose *Sign-in with root user email*, then follow the instructions to log into your account

  <img width="363" height="559" alt="image" src="https://github.com/user-attachments/assets/af7f9159-26f0-4b60-b84d-5a2ce6db9276" />


3. . This brings you to the IAM console:
<img width="926" height="214" alt="image" src="https://github.com/user-attachments/assets/5eb0f770-f3f5-4493-997a-c6765a910004" />

4. In the left navigation pane, choose *Policies*, then choose *Create policy*
  
   <img width="201" height="209" alt="image" src="https://github.com/user-attachments/assets/975d03ef-9fee-47eb-a3a8-56356ffb9a2e" />
   <img width="363" height="63" alt="image" src="https://github.com/user-attachments/assets/b02bdab5-9dc1-41f2-ba84-f6362eacb813" />


5. Choose JSON, and copy and paste the following JSON policy into the *Policy editor* text area:
   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Action": [
                   "cloudformation:Describe*",
                   "cloudformation:Get*",
                   "cloudformation:List*",
                   "iam:Describe*",
                   "iam:GetAccountAuthorizationDetails",
                   "iam:GetGroup",
                   "iam:GetGroupPolicy",
                   "iam:GetPolicy",
                   "iam:GetRole",
                   "iam:GetRolePolicy",
                   "iam:GetUser",
                   "iam:GetUserPolicy",
                   "iam:List*",
                   "logs:Desc*",
                   "logs:Get*",
                   "logs:List*",
                   "s3:CreateBucket",
                   "s3:ListAllMyBuckets",
                   "s3:ListBucket",
                   "s3:PutAccountPublicAccessBlock",
                   "s3:PutBucketOwnershipControls",
                   "s3:PutBucketPublicAccessBlock",
                   "sts:AssumeRole"
               ],
               "Resource": "*",
               "Effect": "Allow"
           }
       ]
   }
   ```
  
   - Notice that the policy does not allow any Amazon EC2 actions.
   - Notice the IAM actions that the policy allows. When you accessed the IAM dashboard, you saw a message that stated that you did not have `iam:GetAccountSummary` authorization. That action is not permitted in this policy document. However, many read-level IAM permissions are granted. For example, you are able to review the details for this policy.
   - Notice the Amazon S3 actions that the policy allows. No object-related actions are granted, but some actions related to buckets are allowed.

6. Name the policy *DeveloperGroupPolicy*. Scroll down to the bottom and choose *Create policy*
   <img width="671" height="353" alt="image" src="https://github.com/user-attachments/assets/b6722a0e-9f51-43a0-82ab-69944082bffc" />

   
7. In the left navigation pane, choose *User groups*

   <img width="199" height="207" alt="image" src="https://github.com/user-attachments/assets/4d848555-8d95-41c7-8837-0554abb8d09b" />


8. Choose *Create group*

   <img width="1023" height="192" alt="image" src="https://github.com/user-attachments/assets/fb5d1b91-b803-403c-a52e-ed956de8ce70" />

9.  *DeveloperGroup*

   <img width="1011" height="204" alt="image" src="https://github.com/user-attachments/assets/bd8c0500-48f2-4551-b59c-f049658719ce" />


10. In the *Attach permissions policies* pane, search for the policy we just created. Tick the checkbox to attach the policy to the user group to be created:

    <img width="1005" height="356" alt="image" src="https://github.com/user-attachments/assets/6584991c-9f4b-4ce1-9669-b7372ac87e63" />

11. Choose *Create user group* to create the *DeveloperGroup* goup.

12. Choose the Permissions tab. Notice that an IAM policy named `DeveloperGroupPolicy` is attached to this IAM group. Choose the plus icon to the left of `DeveloperGroupPolicy` to display the policy details.
    
    <img width="1057" height="636" alt="image" src="https://github.com/user-attachments/assets/894a23ab-bee4-4b9f-81f8-8604c1f86a98" />


    Review the IAM policy details.

13. In the left navigation pane, choose *Users*, then choose *Create user*
    
    <img width="154" height="172" alt="image" src="https://github.com/user-attachments/assets/cd1094a9-dbf2-40d3-87dc-86e4f026d432" />


14. Name the user *devuser*, select the checkbox *Provide user access to the AWS Management Console - optional*. Choose *Custom password*. Deselect *Users must create a new password at next sign-in - Recommended*
    
<img width="1015" height="514" alt="image" src="https://github.com/user-attachments/assets/8beae043-7ad5-4fef-8ef0-1a323ca4e8fc" />

15. Choose *Next*
    

16. Select *DeveloperGroup* to add the user to this user group
    <img width="1019" height="440" alt="image" src="https://github.com/user-attachments/assets/aae595e9-c320-476b-8cf2-206aa33080fc" />

 
## Task 1: Creating 3 S3 Buckets


 

## Task 1: Accessing the console as an IAM user

At the top of these instructions, choose  Start Lab.

The lab session starts.

A timer displays at the top of the page and shows the time remaining in the session.

 Tip: To refresh the session length at any time, choose  Start Lab again before the timer reaches 00:00.

 

Before you continue, wait until the circle icon to the right of the AWS  link in the upper-left corner turns green. When the lab environment is ready, the AWS Details panel will also display.

 Warning: Do NOT choose the AWS link to connect to the console in this lab. You will access the console in a different way than you do in most labs.

 

Log in as the IAM user named `devuser`:

Choose the  AWS Details link at the top of the page.
| Key       | Value                         |
|------------------------|--------------------------------------------------------|
| IAMUserPassword        | igw-0fac7dc1135331224                                  |
| AccountID              | 219682743605                                           |
| IAMUserLoginURL        | https://219682743605.signin.aws.amazon.com/console     |
| Region                 | us-east-1                                              |


Copy the IAMUserLoginURL value, and load it in a new browser tab.

For IAM user name, enter devuser

For Password, enter the IAMUserPassword value from the AWS Details panel on the lab instructions page.

Choose Sign in.

The AWS Management Console displays.

 Warning: To avoid issues, do NOT change the Region during this lab unless instructed.


Logged in as 

<img width="250" alt="image" src="https://github.com/user-attachments/assets/41b3995d-7516-4e54-b123-ccacf84749b0" />




Arrange the AWS Management Console tab so that it displays next to these instructions. Ideally, you will be able to see both browser tabs at the same time so that you can follow the lab steps more easily.
 

## Task 2: Attempting read-level access to AWS services

Now that you are logged in to the console as the IAM user named devuser, you will explore the level of access that you have to a few AWS services, including Amazon Elastic Compute Cloud (Amazon EC2), Amazon S3, and IAM.

 

Open the Amazon EC2 console:

From the  Services menu, choose Compute > EC2.

In the left navigation pane, choose EC2 Dashboard.

Many  API Error messages display. This is expected.

Attempt some actions in the Amazon EC2 console:

In the left navigation pane, choose Instances.

In the Instances list, a message displays You are not authorized to perform this operation.

Choose Launch instances

Scroll down and choose the Key pair name drop down list.

A message displays You are not authorized to perform this operation.

Notice that Key pair name is a required setting that must be configured if you want to launch an instance. This is just one of many indications that you will not be able to launch an EC2 instance with the permissions that have been granted to you as the devuser.

In the Summary panel on the right, choose Cancel.

 

To explore what you can access in the Amazon S3 console, from the  Services menu, choose Storage > S3.

Three buckets are listed. The bucket names are unique, but one bucket name contains bucket1, another contains bucket2, and the third contains bucket3.

In the list of buckets, notice that the Access column displays the message  Insufficient permissions for all three buckets. This is expected.

 

## Task 3: Analyzing the identity-based policy applied to the IAM user

You have observed how the devuser IAM user is unable to access certain information and actions in both the Amazon S3 console and Amazon EC2 console. In this task, you will look at the IAM policy details that apply to devuser to understand why you can't perform these actions.

 

8. Access the IAM console, and observe user and group membership settings:

- From the  Services menu, choose Security, Identity, & Compliance > IAM.
  On the IAM dashboard page, notice that you do not have permissions to view certain parts of the page. Both messages state User: arn:aws:iam:::user/devuser is not authorized to perform: iam:GetAccountSummary on resource: *. This is expected.

- In the left navigation pane, choose User groups.
- Choose the DeveloperGroup group name.
  On the Users tab, notice that `devuser` is a member of this IAM group.

- 

  > Note: When a policy is attached to a group, the policy applies to any IAM users who are members of the group. Therefore, this policy currently governs your access to the console, because you are logged in as devuser, who is a member of this IAM group.

 

9. 
