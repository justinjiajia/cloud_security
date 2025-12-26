https://skillbuilder.aws/learn/YWV8QR96A5/aws-simulearn-security-policies


> Ana Silva: Hello and welcome to the city's premiere currency exchange! We are days away from a big launch of our optical character recognition application. We could use some help with a few items for this OCR application.
You
This sounds like a fun challenge. What can I do for you?
Ana Silva
The OCR application on Amazon EC2 servers processes user-submitted documents such as government ID and proof of residence. These application servers have strict security requirements. Only specific engineers can access them and only for troubleshooting or maintenance purposes.
Ana Silva
Our Compliance Department needs to access the OCR application servers to remove certain records. We want to give the compliance team an environment similar to what the engineers have but with fewer restrictions.
You
I see. So you are saying that you want two similar EC2 environments running the same application. One will only place the files while the other needs full administrative privileges. This is something we can do with IAM policies.
Ana Silva
Excellent. Can you explain how IAM policies help?
You
AWS Identity and Access Management, or IAM, provides fine-grained access control across all of AWS. Using IAM, you can specify who can access which services and resources, and under which conditions.
You
With IAM policies, you define the permissions for your workforce and systems to ensure least privilege access.
Ana Silva
This sounds like exactly what we need. Are there costs associated with IAM?
You
The IAM service is offered at no additional charge. It's just a matter of creating policies and associating them with the proper resources. The only extra costs would be for the additional Amazon EC2 resources for the Compliance Department's EC2 environment.

> Ana Silva: We already budgeted for those resources, so this sounds perfect!


### Solution Request
Restrict access to specific AWS resources by using IAM.


### Step 1
<img width="674" height="490" alt="image" src="https://github.com/user-attachments/assets/4d8f3f93-c150-4dfd-94be-f0f5e4891465" />

This solution uses Identity and Access Management (IAM) roles, assigned to instances in Amazon Elastic Compute Cloud (Amazon EC2), to give the applications that are running on the instances permissions to access a bucket in Amazon Simple Storage Service (Amazon S3).


### Step 2




<img width="664" height="487" alt="image" src="https://github.com/user-attachments/assets/c77bacd2-61fe-4f7f-976c-bdc8b110c646" />


The App-Server is assigned a role with specific Amazon S3 permissions.

### Step  3

<img width="656" height="491" alt="image" src="https://github.com/user-attachments/assets/0e52ce22-f9ae-4a1c-955b-71de62f53e46" />

The Compliance-Server, using a different role, is assigned the same permissions along with the delete permission.



###  Step 4

 <img width="667" height="488" alt="image" src="https://github.com/user-attachments/assets/54c206b2-2705-4bc5-bbfa-2498d0bdd1b1" />

Base users can list, upload, and download files through the App-Server application.


### Step 5

<img width="655" height="489" alt="image" src="https://github.com/user-attachments/assets/d1309bba-f005-4573-9647-e83833a4415b" />

Compliance officers can list, download, upload, and delete files through the Compliance-Server application.


<br>

---

<br>

## Lab 

Concept
In this practice lab, you will:
- Troubleshoot an application's permission problem to access Amazon S3.
- Add LIST and PUT S3 permissions to an IAM policy.
- Test the new permissions by uploading an image file to the application.

  <img width="662" height="483" alt="image" src="https://github.com/user-attachments/assets/f94aaf17-f87d-4b21-91f7-96e740152a70" />

Practice Lab Goals:
Troubleshoot an application's permission problem to access Amazon S3.
Add LIST and PUT S3 permissions to an IAM policy.
Test the new permissions by uploading an image file to the application.



### Step 1

Concept
In this practice lab, you will:
- Troubleshoot an application's permission problem to access Amazon S3.
- Add LIST and PUT S3 permissions to an IAM policy.
- Test the new permissions by uploading an image file to the application.
Step
1
1. Review the practice lab objectives in the Concept section.
2. Click Start Lab or Open AWS Console to begin.
3. Follow the lab instructions carefully, and use the arrows below to navigate between steps.

AWS services not used in this lab are disabled in the lab environment. In addition, the capabilities of the services used in this lab are limited to what the lab requires.



### Step 2

 
1. On this page, click the Lab Files tab.
2. Click the download icon to save the test image to your device.

- You will use this file in a later step.

3. Click the Steps tab to return to the Practice Lab steps.
4. Go to the next step.
   
<img width="322" height="206" alt="image" src="https://github.com/user-attachments/assets/840227b4-8916-4388-acfa-9e0719744982" />
Save this image as a local file called *labfile.png*


### Step 3
1. On the top navigation bar, review the Region selector to ensure that the Region is set to N. Virginia (us-east-1). 
2. In the Services search box, type:
 
ec2

3. In the search results, under Services, click EC2. 

### Step 4

Concept
Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the AWS Cloud. Using Amazon EC2 removes the need to invest in hardware up front, so you can develop and deploy applications faster.
 
1. On the EC2 Dashboard, in the Resources section, click Instances (running).
2. Go to the next step.


### Step 5
 
1. In the Instances section, choose the check box to select the App-Server instance.
2. Under Public IPv4 address, click the copy icon to copy the provided address, and then paste the address in the text editor of your choice on your device.

- You will use this address in later steps.

54.224.157.218

### Step 6

 <img width="1116" height="720" alt="image" src="https://github.com/user-attachments/assets/39e04ccf-2c0d-4700-bd6a-4d6643fb7537" />

1. In a new browser tab (or window) address bar, paste the IP address that you just copied.

- The application runs on port 8443 of the App-Server instance.

2. At the end of the pasted URL, type:

:8443 

and press Enter.

- The address should be in the format http://x.x.x.x:8443. Note the colon before 8443.
- The address will be different from what is displayed in the screenshot example.

3. At the top of the page, review the AccessDenied error for ListObjects.

- The application is attempting to get the contents of the Amazon Simple Storage Service (Amazon S3) bucket, but it is receiving an error because it does not have the ListObjects permission.

4. Return to the Amazon EC2 console in the previous browser tab (not shown).

- Keep the current browser tab

### Step 7

 
1. In the top navigation bar search box, type:

s3

2. In the search results, under Services, click S3.


### Step 8

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/40c2ff40-4caf-4556-816a-5310821ad188" />

Concept
Amazon Resource Names (ARNs) uniquely identify AWS resources. Referencing an ARN is required when you need to specify a resource unambiguously across all of AWS, such as in AWS Identity and Access Management (IAM) policies, Amazon Relational Database Service (Amazon RDS) tags, and API calls.
 
1. In the Buckets section, choose the radio button to select the bucket name that starts with corp-.
2. Click Copy ARN, and then paste the ARN in your text editor.

- You will use the ARN in later steps.

arn:aws:s3:::corp-393401899741-a1d2e030


### Step 9

 
1. In the top navigation bar search box, type:

ec2

2. In the search results, under Services, click EC2.
3. Go to the next step.

### Step 10


1. On the EC2 Dashboard, in the Resources section, click Instances (running).
2. Go to the next step.

### Step 11

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/84a0aa2c-f887-4a52-822e-c92b9c856307" />

Concept
An IAM role is an IAM identity that you can create in your account that has specific permissions. Users and resources can assume the role and obtain temporary security credentials for their session. 
 
1. In the Instances section, choose the check box to select the App-Server instance.

-  In this lab, the App-Server will assume the role, ec2_base_role.

2. In the Security tab, scroll down to IAM Role.
3. Click ec2_base_role.

- The role opens on the AWS Identity and Access Management (IAM) console.

### Step 12

Concept
You can use IAM roles to grant permissions to applications running on your instances that need to use a bucket in Amazon S3. You can specify permissions for IAM roles by creating a policy in JSON format.
 
1. On the Permissions tab, scroll down to Policy name.
2. Next to the policy name, InstanceBasicRoleDefaultPolicyB8CA29A6, click the plus sign (+) to expand the editor window.
3. Click Edit (Not shown).
 


### Step 13


Concept
The visual editor on the IAM console guides you through creating a policy without having to write JSON syntax.
 
1. On the Modify permissions page, choose Visual.
2. Under S3 (1 action), click to expand Actions.

-  Be sure to do this for the S3 (1 action) permission because two permissions are displayed.


### Step 14

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/dc91917f-4879-426d-837b-1ca4a2e7f5c5" />

  Concept
IAM roles are designed so that your applications can securely make API requests from your instances without requiring you to manage the security credentials that the applications use. 
 
1. For Access level, click to expand the List options.
2. Choose ListBucket.

### Step 15

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/2748d115-4782-407f-a0c0-5faea0e30296" />

Concept
An Amazon EC2 instance automatically assumes the role assigned to it at startup. Instead of creating and distributing your AWS credentials, you can delegate permission to the EC2 instance to make API requests by using an IAM role.  
 
1. Click to expand Resources.

- After adding the permission, you must specify the Amazon Resource Name (ARN) of the bucket the permission will apply to.

2. For bucket, click Add ARNs.


### Step 16

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/d5dd1338-1644-4183-b4b3-cc413be712e4" />

 Concept
ARNs are delimited by colons, and they are composed of segments, which are the parts separated by colons. The specific components and values used in the segments of an ARN depend on which AWS service the ARN is for. 
 
1. In the pop-up box, paste the S3 bucket ARN that you just copied. 

- You may need to clear the default text in the box before pasting.
- Your bucket ARN will look different from what is displayed in the screenshot example.

- After pasting the bucket ARN, the bucket name will be filled in automatically. 

2. Click Add ARNs.

### Step 17

1. For Actions, review to ensure that ListBucket appears.
2. For Resources, review to ensure that the bucket ARN appears.
3. Scroll down to the bottom of the page, and then click Next (not shown).

- You have added the permission to list the contents of the corp-xxxx bucket.


### Step 18
Concept
All actions are implicitly denied until a policy explicitly allows them. A DENY statement will always override an ALLOW statement.
 
1. Click Save changes.


Trust policy

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

Policy:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "ec2:DescribeInstances",
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::pu-base-buckets-v1-provision-lab/9af79db3-4e50-42c9-8d04-7b74727c2bbe/*",
                "arn:aws:s3:::corp-393401899741-a1d2e030/*",
                "arn:aws:s3:::corp-393401899741-a1d2e030"
            ]
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::data-393401899741-a1d2e030/*"
        },
        {
            "Sid": "VisualEditor3",
            "Effect": "Deny",
            "Action": "lambda:PutProvisionedConcurrencyConfig",
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor4",
            "Effect": "Deny",
            "Action": "*",
            "Resource": [
                "arn:aws:lambda:us-east-1:393401899741:function:gbl_lab_monitoring",
                "arn:aws:iam::393401899741:role/LabStack-52553f06-5082-48-GblLabMonitoringgbllabmon-xT1HTw4S8aNC",
                "arn:aws:events:us-east-1:393401899741:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-fIK70respfUY",
                "arn:aws:events:us-east-1:393401899741:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-qaHHfbjN8io9",
                "arn:aws:events:us-east-1:393401899741:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-Bj7KD1K9bFL8",
                "arn:aws:events:us-east-1:393401899741:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-K9GlnkLvtldp",
                "arn:aws:events:us-east-1:393401899741:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-AwixLC2BvXsu"
            ]
        }
    ]
}
```

### Step 19

<img width="1116" height="720" alt="image" src="https://github.com/user-attachments/assets/12ae685f-89fd-4243-b4a9-a7259990ef45" />

1. Return to the web application in the other browser tab, and then, on the top navigation bar, click the refresh icon.

- The error should disappear and the application should now work.
- If the error persists, try waiting a few minutes, then closing and reopening the tab.  

2. Click Choose File.


 ### Step 20
 
1. Choose the labfile.png file that you downloaded at the beginning of the lab.
2. Review the file preview.
3. Click Submit.


 ### Step 21

 <img width="2232" height="1440" alt="image" src="https://github.com/user-attachments/assets/4692ede2-68fe-4a9b-b855-d22045731359" />

1. At the top of the page, review the new error in the application.

- The Access Denied error states PutObject as the source API call.
- The application can now list the contents of the bucket, but the application cannot write objects to the bucket.

 ### Step 22

Concept
IAM policy changes take effect immediately after they are saved.
 
1. Return to the IAM console in the previous browser tab, and then, on the Permissions tab, scroll down to Policy name.
2. Next to the policy name, InstanceBasicRoleDefaultPolicyXXXXXX, click the plus sign (+).
3. In the policy file code, review to see that the ListBucket action and the corp bucket ARN are now listed.
4. Click Edit.


 ### Step 23

 <img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/55965722-44b2-4d1f-a3b3-5feff5153ae2" />

1. On the Visual editor tab, click to expand S3 (2 actions).
2. Click to expand Actions allowed.
3. For Access level, click to expand the Write options.
4. Scroll down.


 ### Step 24
 <img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/e63cf489-5a0d-4a87-9bdf-9889ea314610" />

1. Choose PutObject.
2. Under Resources, for object, review the ARN.

- The /* at the end of the ARN applies permissions to all objects in the bucket. 

3. Scroll down to the bottom of the page, and then click Next (not shown).


 ### Step 25
1. In the Summary section, for S3, under Access level, review the actions allowed.

- The Amazon S3 allowed actions are list, read, and write.

2. Click Save changes.


 ### Step 26

 <img width="1116" height="720" alt="image" src="https://github.com/user-attachments/assets/c1ba6ea1-aa36-449c-a011-591104f845d7" />

1. Return to the web application browser tab, and then, on the top navigation bar, click the refresh icon.

- A success message should appear at the top of the page, and the file should be displayed at the bottom of the page.

- If an error appears, go back to the InstanceBasicRoleDefaultPolicy edit page and visually confirm the PutObject permission was successfully added.


## DIY


<img width="652" height="487" alt="image" src="https://github.com/user-attachments/assets/728ee8a1-0ccc-4422-b1b0-a28c4f2ab323" />


DIY Goals
Troubleshoot the compliance officer's application errors.
Adjust the IAM policy statements attached to the ec2_compliance_role.
Add the DELETE Object permission to the S3 policy.
Solution Validation Method
We will verify that the IAM role for Compliance-Server has been assigned the following permissions: s3:ListBucket, s3:GetObject, s3:PutObject, and s3:DeleteObject. 

Hints:
1. Browse the Compliance-Server Application using its public IP address and port 8443.
2. The resources for Compliance-Server reside only in the corp bucket.
3. Remove any unwanted statements in the policy - the only statements that should exist are the ones listed above.
