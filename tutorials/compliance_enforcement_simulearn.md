
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





