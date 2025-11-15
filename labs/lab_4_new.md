 
# Lab 2 Using Resource-Based Policies to Secure an S3 Bucket


## Lab overview and objectives

In this lab, you will learn how to configure permissions by using AWS Identity and Access Management (IAM) identity-based and resource-based policies, such as Amazon Simple Storage Service (Amazon S3) bucket policies. You will also learn how IAM policies and resource policies define access permissions.

After completing this lab, you should be able to do the following:
- Recognize how to use IAM identity-based policies and resource-based policies to define fine-grained access control to AWS services and resources.
- Describe how an IAM user can assume an IAM role to gain different access permissions to an AWS account.
- Explain how S3 bucket policies and IAM identity-based policies that are assigned to IAM users and roles affect what users can see or modify across different AWS services in the AWS Management Console.
 

 

## Scenario


You'll create a user group called *DeveloperGroup* for developers with a specific policy attached, then create a user named *devuser*, and assign it to the *DeveloperGroup* group. Then, you'll create three Amazon S3 buckets: bucket1, bucket2, and bucket3, and explore how the group policy governs your access to these buckets.

You'll also create an IAM role, which allows access to certain buckets and their objects when the role is assumed. You will analyze different policies to better understand how they control your access level.

By the end of this lab, you will have created the architecture shown in the following diagram.


<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_security/lab3/end-arch.png" alt="Architecture now includes a state machine, three Lambda functions, SNS topic, and email report" />

 

## Login


1. Choose *Multi-session enabled* from the dropdown menu

<img width="567" height="151" alt="image" src="https://github.com/user-attachments/assets/c0fa4abd-534e-4635-a38f-6c58060e5cfc" />

2. Choose *Sign-in with root user email*, then follow the instructions to log into your account

  <img width="363" height="559" alt="image" src="https://github.com/user-attachments/assets/af7f9159-26f0-4b60-b84d-5a2ce6db9276" />


## Task 2: Create an IAM user group and a user


3. In the search box at the top left of the screen, search for and choose *IAM*. This brings you to the IAM console:
   
   <img width="926" height="214" alt="image" src="https://github.com/user-attachments/assets/5eb0f770-f3f5-4493-997a-c6765a910004" />

5. In the left navigation pane, choose *Policies*, then choose *Create policy*
  
   <img width="201" height="209" alt="image" src="https://github.com/user-attachments/assets/975d03ef-9fee-47eb-a3a8-56356ffb9a2e" />
   <img width="363" height="63" alt="image" src="https://github.com/user-attachments/assets/b02bdab5-9dc1-41f2-ba84-f6362eacb813" />


6. Choose JSON, and copy and paste the following JSON policy into the *Policy editor* text area:
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

7. Name the policy *DeveloperGroupPolicy*. Scroll down to the bottom and choose *Create policy*
   <img width="671" height="353" alt="image" src="https://github.com/user-attachments/assets/b6722a0e-9f51-43a0-82ab-69944082bffc" />

   
8. In the left navigation pane, choose *User groups*

   <img width="199" height="207" alt="image" src="https://github.com/user-attachments/assets/4d848555-8d95-41c7-8837-0554abb8d09b" />


9. Choose *Create group*

   <img width="1023" height="192" alt="image" src="https://github.com/user-attachments/assets/fb5d1b91-b803-403c-a52e-ed956de8ce70" />

10.  *DeveloperGroup*

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
    

16. Select *DeveloperGroup* to add the user to this user group. Then choose *Next*.
    <img width="1019" height="440" alt="image" src="https://github.com/user-attachments/assets/aae595e9-c320-476b-8cf2-206aa33080fc" />

17. Review the detail and choose *Create user*

You can download the user credential for later use.

<img width="1013" height="291" alt="image" src="https://github.com/user-attachments/assets/39db57dd-fc6b-4041-a4ca-14bb0d321011" />

 
## Task 3: Creating 3 S3 Buckets

1. In the search box at the top left of the screen, search for and choose *S3* and open the *S3* console:


   <img width="753" height="197" alt="image" src="https://github.com/user-attachments/assets/c3818b20-9b71-4c2c-a58c-98e0413a7809" />

2. Choose *Create bucket*
   <img width="312" height="176" alt="image" src="https://github.com/user-attachments/assets/95c03432-69ee-4102-ae6e-842acfb0a3dc" />

3. Configure the bucket details in the Create bucket wizard:
   - ***IMPORTANT FOR GRADING*** Bucket name: *ust-\<ITSC accoutn string\>-bucket1*
     <img width="1223" height="375" alt="image" src="https://github.com/user-attachments/assets/c5684ece-213d-4e96-9bff-687a1e0f2930" />

   - Keep the default settings for the rest of the options
     > Note: By default, new buckets don't allow public access. Diving deeper into this goes beyond the scope of this lab, but it's important to note.
   - Review the settings, and then choose *Create bucket* at the bottom of the page. 
     

4. Repeat step 3 to create two more buckets. Name them *ust-\<ITSC accoutn string\>-bucket2* and *ust-\<ITSC accoutn string\>-bucket3*, respectively.

In the end, you should see three buckets present in the *General purpose buckets* list.

<img width="816" height="240" alt="image" src="https://github.com/user-attachments/assets/d2b8be79-db12-44ee-b238-183cbba158a4" />

<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_security/lab3/start-arch.png" alt="Starting architecture with an IAM user, group, and policy, and S3 buckets" />


   
## Task 4: Accessing the console as an IAM user

1. Get back to the IAM console. Choose *Users* in the left navigation pane. Then choose *devuser*.
 
<img width="1057" height="376" alt="image" src="https://github.com/user-attachments/assets/7b1310c6-8003-4e4b-bc03-8790491b8915" />

2. Copy the *Console sign-in link*, open a new browser tab, and paste the url into the address bar. Then hit Enter.
3. Choose *Sign into new session* to proceed to the sign-in page

<img width="777" height="52" alt="image" src="https://github.com/user-attachments/assets/163bb537-f888-4994-9292-446e2f0bcacb" />

3. Log in as the IAM user named `devuser`. 

   <img width="335" height="534" alt="image" src="https://github.com/user-attachments/assets/000c0354-9772-49e7-8aa6-c0a9c77bfdbe" />

   - For IAM user name, enter *devuser*
   - For Password, enter *isom5140_devuser* (the password you created before for this IAM user).
   - Note that the pre-populated *Account ID or alias* field should contain a different account ID in your case.
   - Choose *Sign in*.

4. The AWS Management Console displays. Make sure you're in the *us-east-1* Region.   

   <img width="317" height="211" alt="image" src="https://github.com/user-attachments/assets/e3634272-d421-4d83-8046-4d5eed754757" />

 

## Task 4: Attempting read-level access to AWS services

Now that you are logged in to the console as the IAM user named *devuser*, you will explore the level of access that you have to a few AWS services, including Amazon Elastic Compute Cloud (Amazon EC2), Amazon S3, and IAM.

 
1. Open the Amazon EC2 console

   <img width="1014" height="284" alt="image" src="https://github.com/user-attachments/assets/5e54946d-e198-4887-9c9f-733557ee0e38" />


2. In the left navigation pane, choose *EC2* > *Dashboard*.
   <img width="213" height="440" alt="image" src="https://github.com/user-attachments/assets/8306b25e-9e72-4400-b4dd-93d99d56c0b7" />

Many  API Error messages display. This is expected.


3. Attempt some actions in the Amazon EC2 console:

   - In the left navigation pane, choose *Instances*.

   - In the *Instances* list, a message displays *"You are not authorized to perform this operation. User: arn:aws:iam::245221346334:user/devuser is not authorized to perform: ec2:DescribeInstances because no identity-based policy allows the ec2:DescribeInstances action"*.


4. Choose Launch instances. Scroll down and choose the *Key pair name* drop down list.

A message displays *"You are not authorized to perform this operation."*

<img width="831" height="339" alt="image" src="https://github.com/user-attachments/assets/bf76d4fa-4b21-4592-aa31-77782a31b311" />

Notice that Key pair name is a required setting that must be configured if you want to launch an instance. This is just one of many indications that you will not be able to launch an EC2 instance with the permissions that have been granted to you as the devuser.

5. In the *Summary* panel on the right, choose *Cancel*.

6. Open the Amazon S3 console to explore what you can access. Three buckets are listed with unique names.

7. Open the IAM dashboard page, notice that you do not have permissions to view certain parts of the page. The message states *"User: arn:aws:iam:::user/devuser is not authorized to perform: iam:GetAccountSummary on resource:"*. 

## Task 3: Analyzing the identity-based policy applied to the IAM user

In this task, you will look at the IAM policy details that apply to *devuser* to understand why you can't perform these actions.


1. Access the IAM console, and observe user and group membership settings:

- In the left navigation pane, choose *User groups*.
- Choose the *DeveloperGroup* group name. On the Users tab, notice that `devuser` is a member of this IAM group.


  > Note: When a policy is attached to a group, the policy applies to any IAM users who are members of the group. Therefore, this policy currently governs your access to the console, because you are logged in as devuser, who is a member of this IAM group.

 
2. Save the policy to a file on your computer:
To copy the JSON-formatted policy to your clipboard, choose Copy.
Open a text editor on your local computer, and paste the policy that you just copied.
Save the policy document as DeveloperGroupPolicy.json to a location on your computer that you will remember.


## Task 4: Attempting write-level access to AWS services

Any action that you attempt when you interact with an AWS service is an API call, whether you are using the console, AWS Command Line Interface (AWS CLI), or AWS software development kits (SDKs). All attempted API calls are recorded in the AWS CloudTrail event logs.

In this task, you will attempt to make two API calls that require write-level access within Amazon S3. The first action is to create an S3 bucket, and the second action is to upload an object to that bucket. After you attempt the two tasks, you will again analyze the policy attached to the IAM group to analyze why you could or could not perform the specific API calls.

1. Attempt to create an S3 bucket:
   - Navigate to the Amazon S3 console.
   - Choose Create bucket
   - For Bucket name, enter *ust-* followed by your initials and a random four-digit number; for example, *ust-zbq1234*.

 
You successfully created an S3 bucket.

2. Access the bucket, and attempt to upload an object:

   - Choose the bucket named *"ust-\<your ITSC account string\>-bucket1"* from the *General purpose buckets* list.
   - Choose *Upload*, and then choose *Add files*.
   - Browse to and choose the *DeveloperGroupPolicy.json* file that you saved earlier.
   - Choose *Upload*.

A message displays *Upload failed*.

3.  On the *Files and folders* tab on the lower part of the page, in the Error column, choose the *Access Denied* link.

    <img width="449" height="113" alt="image" src="https://github.com/user-attachments/assets/0b1663c2-6a2b-402a-aec9-03267c9de99f" />

    The message states *"You don't have permissions to upload files and folders"*. Choose *Close*.

4. You can repeat the previous steps for the rest of the general purpose buckets. You'll encounter the same error when attempting upload files

4. Review the policy details for Amazon S3 access:

   Return to the text editor where you copied the *DeveloperGroupPolicy.json* document.

   Review the policy details to understand why you were able to create an S3 bucket but couldn't upload objects to it.

Tip: The Service Authorization Reference document provides a list of actions that each AWS service supports. For information about Amazon S3 actions, open the IAM documentation page, and then open the Service Authorization Reference document. In the left navigation pane, expand Actions, resources, and condition keys, and then choose Amazon S3. In the Actions defined by Amazon S3 section, the table lists every possible Amazon S3 action that can be granted or denied, along with a description of the action.

## Task 4: Add a resource-based policy 

1. Keep the current tab open. Switch to the tab that holds the session for your account root user. Then navigate to the S3 console

2. choose the bucket named *"ust-\<ITSC account string\>-bucket1"* from the *General purpose buckets* list.

3. Choose the *Permissions* tab, and locate the *Bucket policy* section. Then choose *Edit*.
 

   <img width="1059" height="634" alt="image" src="https://github.com/user-attachments/assets/3fca7de3-38f7-496f-982f-0b81bdc3b7d1" />


4. Copy and paste the JSON policy below into the *Policy* text area. Then choose *Save changes*
   
	```json
	{
		"Version": "2012-10-17",
		"Statement": [
			{
				"Effect": "Allow",
				"Principal": {
					"AWS": "arn:aws:iam::245221346334:user/devuser"
				},
				"Action": "s3:*",
				"Resource": [
					"arn:aws:s3:::ust-justinjia-bucket1",
					"arn:aws:s3:::ust-justinjia-bucket1/*"
				]
			},
			{
				"Effect": "Deny",
				"Principal": {
					"AWS": "arn:aws:iam::245221346334:user/devuser"
				},
				"Action": "s3:DeleteBucket",
				"Resource": "arn:aws:s3:::ust-justinjia-bucket1"
			}
		]
	}
	```



    <img width="1055" height="496" alt="image" src="https://github.com/user-attachments/assets/64fefee6-12ba-49db-9976-55e2561e4819" />

5. Keep the current tab open. Switch to the tab that holds the session for the *devuser* user.

6. Choose *"ust-\<ITSC account string\>-bucket1"* again, and attempt to upload the *DeveloperGroupPolicy.json* document again. This time the file was uploaded successfully. 

7. Select the *DeveloperGroupPolicy.json* document from the *Objects*list. Choose *Delete*. Follow the instruction to confirm deletion in the *Delete objects* wizard. The file was successfully deleted.

   <img width="1177" height="312" alt="image" src="https://github.com/user-attachments/assets/4f2f9b7a-d5e9-4cb8-b887-bd2b7c50d239" />

8. From the breadcrumbs in the upper-left corner of the page, choose *Buckets*.
   
   <img width="350" height="34" alt="image" src="https://github.com/user-attachments/assets/a1c77933-1cc9-4720-9da0-65002f1b62e9" />

9. Select *"ust-\<ITSC account string\>-bucket1"*. Then choose *Delete*, and confirm deletion in the *Delete bucket* wizard.
    
    <img width="785" height="415" alt="image" src="https://github.com/user-attachments/assets/57ac67e6-4176-4478-87f7-ada882990f1a" />

   A message displays *"You are not authorized to perform this operation.*.

   <img width="1174" height="195" alt="image" src="https://github.com/user-attachments/assets/3f0d9282-940c-4b12-87ed-403c339f54dc" />

-


##


1. Keep the current tab open. Switch to the tab that holds the session for the account root user.
2. Open the *IAM* console, and choose *Policies* in the left navigation pane
3. Choose *Create policy*. This time, you'll use the visual policy editor to create and configure a policy 

4. Select S3 from the Service dropdown menu
   
   <img width="781" height="453" alt="image" src="https://github.com/user-attachments/assets/c194487e-39b4-4e46-b993-7950973cf8d9" />

5. Tick the checkbox for *All S3 actions (s3:*)*
   
   <img width="762" height="180" alt="image" src="https://github.com/user-attachments/assets/c93dd0c6-2f57-44a2-a73e-6266386c87da" />


6. Locate the *bucket* field under the *Resources* section, choose *Add ARNs* to restrict access.

   <img width="761" height="75" alt="image" src="https://github.com/user-attachments/assets/58da9c79-950f-49d5-a05f-390eb0b26f56" />

7. Type the name of the 2nd bucket, i.e., *ust-\<ITSC account string\>-bucket2*: in the *Resource bucket name* field on the popup window. Then choose *Add ARN*

   <img width="604" height="215" alt="image" src="https://github.com/user-attachments/assets/e70750a9-b4cd-4170-8eb1-d10019393d81" />

8. Locate the *object* field under the *Resources* section, choose *Add ARNs* to restrict access.
   
   <img width="759" height="77" alt="image" src="https://github.com/user-attachments/assets/8f32d257-5391-43ac-bfa3-9c263724adee" />


9. Fill in the *Resource bucket name* field with the same bucket name, and tick the checkbox for *Any object name*. Then choose *Add ARN*

   <img width="606" height="265" alt="image" src="https://github.com/user-attachments/assets/69f45872-dabe-4962-9a89-ee3ba13309c7" />


10. Click Next

11. Type *Bucket2AccessPolicy* in the *Policy name* field. Then choose *Create policy* at the bottom right corner.

    <img width="974" height="296" alt="image" src="https://github.com/user-attachments/assets/e5d2fede-c69a-423f-9b4b-7b63b116fd3f" />

12. Search for the policy you just created. Click the plus icon to the left of the policy name to review the policy

    <img width="982" height="502" alt="image" src="https://github.com/user-attachments/assets/82278249-8c2e-4b17-a6c3-04176b4d2199" />


To use the policy, you need to associate it with an IAM principal,  Next, you'll create an IAM role and attach this *Bucket2AccessPolicy* policy to it

13. Choose *Roles* in the left navigation pane. Then choose *Create roles*
    
14. Select *AWS account* under the *Trusted entity type* section, and choose *This account* under the *An AWS account* section. Then choose *Next*
    
    <img width="975" height="495" alt="image" src="https://github.com/user-attachments/assets/0b2c4e82-1ada-4986-855b-5fc146ae45c1" />

15. Search for the policy you just created. Tick the check box for the policy. Then choose *Next*
    <img width="972" height="312" alt="image" src="https://github.com/user-attachments/assets/709cca07-905e-4a9f-96ab-b1ca04c4d465" />

16. Call the role  *Bucket2AccessRole*. Then choose *Create role* at the bottom right corner
    
    <img width="974" height="285" alt="image" src="https://github.com/user-attachments/assets/0495b9f1-eb0a-49a1-baa8-0c678a167ed9" />

17. Choose the *Bucket2AccessRole* role from the *Roles* list
    <img width="979" height="238" alt="image" src="https://github.com/user-attachments/assets/9b18bf1a-3902-4fdf-9967-89d3b6555f2b" />

18. Choose the *Trust relationships* tab. Then choose *Edit trust policy*

    <img width="976" height="505" alt="image" src="https://github.com/user-attachments/assets/f319c720-421f-40a8-9043-38d2b14d70e4" />

19. Copy and paste the JSON policy below to the *Edit trust policy* text area. Choose *Update policy*
    ```json
    {
		"Version": "2012-10-17",
		"Statement": [
			{
				"Effect": "Allow",
				"Principal": {
					"AWS": "arn:aws:iam::245221346334:user/devuser"
				},
				"Action": "sts:AssumeRole"
			}
		]
	}
    ```

20. Copy the URL in the *Link to switch roles in console* field
    
	<img width="972" height="485" alt="image" src="https://github.com/user-attachments/assets/dbce9432-fae2-4543-b5a8-803b49ea8109" />

21. Open a new browser tab, and paste the URL into the address bar. Hit *Enter*
22. Choose *devuser* under the *Switch from* section. Then choose *Switch role*
    
    <img width="812" height="578" alt="image" src="https://github.com/user-attachments/assets/55fb4aa8-7d6f-41ef-8cb1-cefa2b28f5c2" />

Now you're log in as the *Bucket2AccessRole* role.

    <img width="430" height="91" alt="image" src="https://github.com/user-attachments/assets/4be2b921-9346-4fcc-be57-3bde04d990fd" />

You can navigate to the S3 console and check if you're able to upload files into the *ust-\<ITSC account string\>-bucket2*.

23. After experimentation, choose the downward pointing triangle to the right of *Sign out of all sessions*. Choose *Sign out of current session* to only log off the current role session.
   <img width="264" height="545" alt="image" src="https://github.com/user-attachments/assets/351f7470-25f9-468e-a63e-42b427c6187e" />

	
25. Open a new browswer tab, and paste the URL copied from the *Link to switch roles in console*  into the address bar. This time, choose switch role from the root user account. You'll run into an error message as follows:
    
    <img width="812" height="121" alt="image" src="https://github.com/user-attachments/assets/5341773b-eb72-44f5-ac91-5a10afde1819" />


## Cross account access

1. Switch to the tab that holds the session for your root user account
2. Open the IAM console, Choose *Roles* in the left navigation pane, and then choose the *Bucket2AccessRole* role from the *Roles* list.
3. Choose the *Trust relationships* tab. Then choose *Edit trust policy*
4. Edit the *Principal* block to allow *devuser* in one of your neighbor's account to assume the *Bucket2AcessRole* in your account.
