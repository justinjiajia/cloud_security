
This lab demonstrates the concepts of assuming an AWS Identity and Access Management (IAM) role from the Management Console. As a member of the cloud team at AnyCompany, your company requires that all users who need access to AWS must not have the IAM permissions attached directly to their users identities. Instead, the users permissions only allow them to assume an IAM role which has the required permissions. The company's policy also requires that least privilege concepts are strictly applied where possible. The lab is based on a break/fix scenario where you are presented with a problem of a user failing to switch roles from the Management Console. You need to troubleshoot and fix the issue. High-level guidance and references are provided to assist in fixing the issue. The detailed solution instructions are provided in a hidden collapsible section which you can expand.

https://skillbuilder.aws/learn/68UNZXPYUZ/lab--troubleshooting--iam-access-issues

# Troubleshooting - IAM Access Issues
SPL-TF-200-SITIAI-1 - Version 1.0.7

© 2025 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. All trademarks are the property of their owners.

Note: Do not include any personal, identifying, or confidential information into the lab environment. Information entered may be visible to others.

# Lab overview


This lab demonstrates the concepts of assuming an AWS Identity and Access Management (IAM) role from the Management Console.

As a member of the cloud team at AnyCompany, your company requires that all users who need access to AWS must not have the IAM permissions attached directly to their users identities. Instead, the users permissions only allow them to assume an IAM role which has the required permissions. The company’s policy also requires that least privilege concepts are strictly applied where possible.

The lab is based on a break/fix scenario where you are presented with a problem of a user failing to switch roles from the Management Console. You need to troubleshoot and fix the issue.

High-level guidance and references are provided to assist in fixing the issue. The detailed solution instructions are provided in a hidden collapsible section which you can expand.

## Objectives
By the end of this lab, you will be able to do the following:

- View and update IAM permissions of a user identity-based policy to allow the user to assume an IAM role.
- View and update IAM role trust policy to allow a user to assume an IAM role.
- Apply least privilege concepts.
- Verify the solution.


## Technical knowledge prerequisites
To successfully complete this lab, you should have a basic knowledge of:

- Navigating through the AWS Management Console.
- AWS Identity and Access Management (IAM).
 

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Note: A hint, tip, or important guidance.
 Hint: A hint to a question or challenge.
 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Knowledge check: An opportunity to check your knowledge and test what you have learned.
 Answer: An answer to a question or challenge.


 
## Lab environment

The following diagram shows the lab scenario:


<img width="752" height="391" alt="image" src="https://github.com/user-attachments/assets/0bc6805e-7fb5-42ac-8d4c-4c9152eb5a29" />

Lab scenario. More details in the image description.

Image description: The following list details the major resources in the lab:

- An IAM user named Operator-User.
- An IAM role named Operator-Role which need to be assumed by the Operator-User.
- An Amazon Elastic Compute Cloud (Amazon EC2) instance named CommandHost.
- Session Manager, a capability of AWS Systems Manager to allow connecting to the EC2 instance.
- An IAM user AWSLabUser. This is how you can login to the console to troubleshoot and fix the issue.


### Lab scenario

A new user Operator-User is starting in the company and need access to AWS. The user have been given access to the console. 
The user is also have been given the following instructions on how to perform his/her duties on AWS:

- Login to the AWS Management Console with the provided Operator-User credentials.
- Switch to an IAM role (assume role) named Operator-Role using the AWS Management Console.
- Once the role is assumed, start a Systems Manager session to connect to the CommandHost instance.
- Run some required scripts from the CommandHost prompts.


As a member of the cloud team, you receive a complain that the Operator-User is logging to the AWS Management Console but failing to assume the assigned IAM role. 
Hence, the user is unable perform the duties of his/her role. Your task is to troubleshoot the issue and fix it while applying least privilege concepts in your solution.
 
<img width="269" height="388" alt="image" src="https://github.com/user-attachments/assets/9566d5c7-0fa2-4554-b38c-5dd1dd9482a6" />

## Task 1: Accessing the lab

In this task, you are introduced on how to access the lab using the Operator-User IAM user and how to attempt switching roles to assume the Operator-Role IAM role.

When you followed the instructions in the Start lab section, you are logged to the console with the AWSLabUser. This is the user representing the cloud team member who needs to troubleshoot and fix the issue.

You also need to access the AWS Management Console as the Operator-User who is not able to assume the role. You can use this access to reproduce the issue of the user and also to verify the solution after you remediate the issue.

3. In your preferred browser, open a new Private, Incognito, or InPrivate window.

4. Copy the ConsoleAccessURL value that is listed to the left of these instructions. Paste the URL into the new web browser window you just opened and press Enter.
5. In the IAM user sign in page:
- For IAM username, enter `Operator-User`.
- For the Password, paste the **OperatorUserPassword** value listed to the left of these instructions.
- Choose *Sign in*.

You are logged in to the Console Home page as the Operator-User.

Now, you assume the Operator-Role IAM role from the AWS Management Console to verify the user issue.

6. At the upper-right corner of the page, choose the Operator-User drop-down menu, and then choose Switch role.
7. If you are presented with a Switch role page that has a Get started in 3 simple steps section, then choose Switch Role.
8. On the Switch Role page:

- For Account, copy and paste the **AWSAccountID** value listed to the left of these instructions.
- For Role, enter `Operator-Role`.
- For Display Name, leave blank as this is just a descriptive name.

9. Choose Switch Role.

The following message is displayed Invalid information in one or more fields. Check your information or contact your administrator. This indicates that the role switch is not successful and confirms the user issue.

You can re-visit this section whenever you need guidance on how to login as the Operator-User and switch roles to assume the Operator-Role IAM role.

 Congratulations! You are now familiar with accessing the lab using the Operator-User IAM user and attempting to switch roles to assume the Operator-Role IAM role.

## Task 2: Troubleshooting and remediating the issue and verifying the solution

In this task, you attempt to troubleshoot and remediate the issue preventing the Operator-User from assuming the Operator-Role. You also verify the solution.

After you confirmed the user issue in the previous task, you need to switch back to the browser tab of the console logged with the AWSLabUser user to troubleshoot and remediate the issue. The AWSLabUser has the required permissions to solve the issue.

10. Choose the AWS Management Console browser tab which has the AWSLabUser at the upper-right corner of the page to troubleshoot and remediate the Operator-User issue.
Your solution should allow the Operator-User to assume the Operator-Role successfully and also should strictly adhere to the following least privilege guidelines:

- The Operator-User has the permissions to only assume the Operator-Role.
- The Operator-Role can only be assumed by the Operator-User.

<img width="984" height="383" alt="image" src="https://github.com/user-attachments/assets/692c19ac-be4b-41e4-a104-c1a2bbe7ec2c" />


Hint:
- You are not allowed to create new identity-based policies. However, you can use pre-configured customer managed policies.
  The pre-configured policies names you are allowed to use starts with IAM-User-Policy.
  <img width="982" height="472" alt="image" src="https://github.com/user-attachments/assets/1c8e6e2c-bbca-4e5d-b292-91cfc8328df0" />
- If you get denied access when attempting to solve the issue, this means you do not have enough permissions and hence you need to solve the issue using a different way.



## Do it yourself
 Hint: Here are some references to assist you in solving the issue:

- [Using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html).
- [Troubleshooting IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_cant-assume-role).
- [How to use trust policies with IAM roles](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/).
 Note: While navigating through the IAM console pages, you may get a message at the bottom of some IAM console pages indicating that You need permissions for some access-analyzers actions. You can ignore this error safely as it is not required to complete the lab.

## Solution
Expand the Detailed instructions below for the full solution.


<details>
  <summary><h4> Detailed instructions</h4></summary>
  There are two things involved when assuming an IAM role:

  - The IAM entity (Operator-User in this example) must have permissions to assume the role in its identity-based policy.
  - The IAM role (Operator-Role in this example) trust policy must allow the Operator-User to assume the role.
  
  To troubleshoot, you need to check both of them.
  
  11. Choose the AWS Management Console browser tab which has the AWSLabUser at the upper-right corner of the page.
  
  12. At the top of the AWS Management Console, in the search bar, search for and choose IAM.
  13. In the navigation pane at the left of the page, under Access management, choose Users.
  14. In the Users page, choose the link for Operator-User.
  
  In the Operator-User page, under the Permission tab, check the available Permissions policies.
  
  Note that there are no policies attached to the Operator-User user. You do not have permissions to create new policies, but you have the permission to attach pre-configured identity-based policies.
  
  In the navigation pane at the left of the page, under Access management, choose Policies.
  You have the permission to attach the following policies to the Operator-User user:
  
  IAM-User-Policy-1
  IAM-User-Policy-2
  IAM-User-Policy-3
  Expand the  beside each of the above policies names to view their permissions.
   Knowledge check: Which one of the above policies allow the user to assume the role while following least privilege concepts?
  
  Answer
  Select  beside the IAM-User-Policy-3.
  
  From the Actions  drop-down menu, select Attach.
  
  Locate the Operator-User user.
  
   Note: You can use the search box to search for the user or scroll down through the list.
  
  Select  beside the Operator-User.
  
  Choose Attach policy.
  
  Now, the Operator-User user has the permissions to assume the Operator-Role role.
  
  Next, you need to check the Operator-Role role trust policy which defines who can assume the role.
  
  In the navigation pane at the left of the page, under Access management, choose Roles.
  
  In the Roles page, locate the Operator-Role role and choose its link.
  
   Note: You can use the search box to search for the role or scroll down through the list. There might be multiple pages of roles names.
  
  In the Operator-Role page, choose the Trust relationships tab.
  The Trusted entities is an IAM trust policy which defines who can assume the role. This is defined by the Principal in the trust policy.
  
  Note that the Principal defined in the policy is the ec2.amazonaws.com which is the EC2 service. This works well if you need an EC2 instance to assume the role. Clearly, this is another factor causing the issue you are troubleshooting.
  
  Recall that your solution need to follow least privilege concepts and the role can only be assumed by the Operator-User user. The trust policy must be updated.
  
  Choose Edit trust policy.
  
  Select the existing policy and delete it.
  
  In the Edit trust policy pane, add the following policy after replacing the INSERT_ACCOUNT_ID placeholder value with the AWSAccountID value that is listed to the left of these instructions.
  
  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Principal": {
              "AWS": "arn:aws:iam::INSERT_ACCOUNT_ID:user/Operator-User"},
              "Action": "sts:AssumeRole"
          }
      ]
  }
  ```
  Choose Update policy.
  The role trust policy is now updated to allow only the Operator-User user to assume the role.

  
</details>

 


### Verify the solution
Now, verify the solution and check how strictly you applied least privilege concepts.

30. Choose the AWS Management Console browser tab which has the Operator-User user at the upper-right corner of the page to attempt assuming the Operator-Role role.

At the upper-right corner of the page, choose the Operator-User drop-down menu, and then choose Switch role.

If you are presented with a Switch role page that has a Get started in 3 simple steps section, then choose Switch Role.

On the Switch Role page:

For Account, copy and paste the AWSAccountID value listed to the left of these instructions.
For Role, enter Operator-Role.
For Display Name, leave blank as this is just a descriptive name.
Choose Switch Role.
 Note: If the following message is displayed Invalid information in one or more fields. Check your information or contact your administrator. This indicates that the role switch is not successful and the problem is not solved. Try troubleshooting and remediating the issue again.

If your solution is correct, you are redirected to the Console Home page and you can note that the logged entity is the Operator-Role at the upper-right corner of the page.

This indicates that you solved the issue.

 Congratulations! You have successfully remediated the IAM issue preventing the user from assuming the role and verified your solution by assuming the role.

Conclusion
 Congratulations! You have now successfully:

Viewed and updated IAM permissions of a user identity-based policy to allow the user to assume an IAM role.
Viewed and updated IAM role trust policy to allow a user to assume an IAM role.
Verified the solution.


 

## Additional resources
- [Digital Course: Introduction to AWS Identity and Access Management (IAM)](https://explore.skillbuilder.aws/learn/course/external/view/elearning/120/introduction-to-aws-identity-and-access-management-iam).
  
- [Digital Course: AWS Identity and Access Management (IAM) - Troubleshooting](https://explore.skillbuilder.aws/learn/course/external/view/elearning/15564/troubleshooting-aws-identity-and-access-management-iam).
  
- [Digital Course: Deep Dive with Security: AWS Identity and Access Management (IAM)](https://explore.skillbuilder.aws/learn/course/external/view/elearning/104/deep-dive-with-security-aws-identity-and-access-management-iam).
- [Lab: Introduction to AWS Identity and Access Management (IAM)](https://explore.skillbuilder.aws/learn/course/external/view/elearning/880/introduction-to-aws-identity-and-access-management-iam).



## CloudFormation Templates

Cannot load

<img width="1041" height="426" alt="image" src="https://github.com/user-attachments/assets/d0b924e3-2c34-4f8c-a6d9-cbaa4d6d4852" />


