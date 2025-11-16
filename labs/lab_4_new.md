 
# Lab 2 Using IAM to secure AWS resources


## Lab overview and objectives

In this lab, you will learn how to configure permissions by using AWS Identity and Access Management (IAM) identity-based and resource-based policies, such as Amazon Simple Storage Service (Amazon S3) bucket policies. You will also learn how IAM policies and resource policies define access permissions.

After completing this lab, you should be able to do the following:
- Recognize how to use IAM identity-based policies and resource-based policies to define fine-grained access control to AWS services and resources.
- Describe how an IAM user can assume an IAM role to gain different access permissions to an AWS account.
- Explain how S3 bucket policies and IAM identity-based policies that are assigned to IAM users and roles affect what users can see or modify across different AWS services in the AWS Management Console.
 

 

## Scenario


You'll create a user group called *DeveloperGroup* for developers with a specific policy attached, then create an IAM user named *devuser*, and assign it to the *DeveloperGroup* group. Then, you'll create three Amazon S3 buckets: *bucket1*, *bucket2*, and *bucket3*, and explore how the group policy governs your access to these buckets.

You'll also create an IAM role, which allows access to certain buckets and their objects when the role is assumed. You will analyze different policies to better understand how they control your access level.

By the end of this lab, you will have created the architecture shown in the following diagram.


<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_security/lab3/end-arch.png"  width=800 />

 

## Task 1: Logging in as the account root user


1. Visit <a href="console.aws.amazon.com/console/home">https://console.aws.amazon.com/console/home</a>. Then choose *Multi-session enabled* from the dropdown menu in the top right of the screen.

   <img width="500"  src="https://github.com/user-attachments/assets/c0fa4abd-534e-4635-a38f-6c58060e5cfc" />

2. Choose *Sign-in using root user email*. Then follow the instructions to log into your root account.

   <img width="300"  src="https://github.com/user-attachments/assets/af7f9159-26f0-4b60-b84d-5a2ce6db9276" />

   Note that you may need to access the authenticator app on your phone and provide the MFA code if MFA has been turned on for your account root user.

Once logged in, let's verify that your account is part of an AWS Organization.

3. In the search bar at the top of the screen, search for and select *AWS Organization*. 

   <img width="500" alt="image" src="https://github.com/user-attachments/assets/44f08afb-6c3f-4466-8973-d7f74537d08d" />

   This will bring you to the AWS Organizations console, where you have limited access.
   
   <img width="800" alt="image" src="https://github.com/user-attachments/assets/5b10d2ee-627f-43ab-a337-5cef6ab12672" />



4. Select *Leave this organization*. You will encounter the following error message:
   

   <img width="500"  src="https://github.com/user-attachments/assets/6197006d-d00c-4104-9718-77518990157b" />

   This is an expected behavior. A *Deny* statement in the *Service Control Policy* (SCP) applied to your Organization Unit is explicitly blocking the *organizations:LeaveOrganization* action.
   
<br/>

   
## Task 2: Creating an IAM user group and an IAM user


1. In the search box at the top left of the screen, search for and choose *IAM*. This brings you to the IAM console:
   
   <img width="800"  src="https://github.com/user-attachments/assets/5eb0f770-f3f5-4493-997a-c6765a910004" />

2. In the left navigation pane, choose *Policies*. Then choose *Create policy*.
  
   <img width="200"  src="https://github.com/user-attachments/assets/975d03ef-9fee-47eb-a3a8-56356ffb9a2e" />  

   <br/>
   <img width="300"  src="https://github.com/user-attachments/assets/b02bdab5-9dc1-41f2-ba84-f6362eacb813" />


3. Choose the edit the policy using the JSON editor. Copy and paste the following JSON-formatted policy into the *Policy editor* text area:
   
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
	                "iam:GetPolicyVersion",
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
	                "s3:PutEncryptionConfiguration",
	                "sts:AssumeRole"
               ],
               "Resource": "*",
               "Effect": "Allow"
           }
       ]
   }
   ```
  
   - Notice that the policy does not allow any Amazon EC2 actions.
     
   - Notice the IAM actions that the policy allows. When you access the IAM dashboard later via *devuser*, you'll see a message that states that you do not have `iam:GetAccountSummary` authorization. That action is not permitted in this policy document. However, many read-level IAM permissions are granted. For example, you are able to review the details for this policy.
     
   - Notice the Amazon S3 actions that the policy allows. No object-related actions are granted, but some actions related to buckets are allowed.

4. Name the policy *DeveloperGroupPolicy*. Scroll down to the bottom and choose *Create policy*.
   
   <img width="800"   src="https://github.com/user-attachments/assets/b6722a0e-9f51-43a0-82ab-69944082bffc" />

   
5. In the left navigation pane, choose *User groups*.

   <img width="200"  src="https://github.com/user-attachments/assets/4d848555-8d95-41c7-8837-0554abb8d09b" />


6. Choose *Create group*.

   <img width="800"    src="https://github.com/user-attachments/assets/fb5d1b91-b803-403c-a52e-ed956de8ce70" />

7. Type *DeveloperGroup* in the *User group name* field.

   <img width="800"  src="https://github.com/user-attachments/assets/bd8c0500-48f2-4551-b59c-f049658719ce" />


8. In the *Attach permissions policies* pane, search for the policy we just created. Tick the checkbox next to it to attach this policy to the new user group.

    <img width="800"   src="https://github.com/user-attachments/assets/6584991c-9f4b-4ce1-9669-b7372ac87e63" />

9. Choose *Create user group* to create the goup.

10. Choose the *Permissions* tab. Notice that an IAM policy named *DeveloperGroupPolicy* is attached to this IAM group. Choose the plus icon to the left of *DeveloperGroupPolicy* to display the policy details. Review the IAM policy details.

    <img width="800" src="https://github.com/user-attachments/assets/cd4c46e2-16d9-4acd-a776-60bf9992d289" />
 


Next, you'll create a new IAM user and assign it into the *DeveloperGroup* group.

11. In the left navigation pane, choose *Users*. Then choose *Create user*.
    
    <img width="200"  src="https://github.com/user-attachments/assets/cd1094a9-dbf2-40d3-87dc-86e4f026d432" />


12. Configure the IAM user details:

    - User name: *devuser*
    - Tick the checkbox for *Provide user access to the AWS Management Console - optional*.
    - Choose *Custom password*.
    - Password: *isom5140_devuser*.
    - Deselect *Users must create a new password at next sign-in - Recommended*.
    - Choose *Next*  
    <br/>
    <img width="800" src="https://github.com/user-attachments/assets/8beae043-7ad5-4fef-8ef0-1a323ca4e8fc" />

    
13. Select *DeveloperGroup* to add the user to this user group. Then choose *Next*.
    
    <img width="800" src="https://github.com/user-attachments/assets/aae595e9-c320-476b-8cf2-206aa33080fc" />

14. Review the details and choose *Create user*

	<img width="800" src="https://github.com/user-attachments/assets/39a500a4-27b5-48f2-bd3b-9b657737b052" />


    You can download the user credential for later use.


<br/>
   
 
## Task 3: Creating three S3 Buckets

1. In the search box at the top left of the screen, search for and choose *S3* to open the *S3* console:

   <img width="800"  src="https://github.com/user-attachments/assets/c3818b20-9b71-4c2c-a58c-98e0413a7809" />

2. Choose *Create bucket*.
   
   <img width="400" src="https://github.com/user-attachments/assets/95c03432-69ee-4102-ae6e-842acfb0a3dc" />

3. Configure the bucket details in the *Create bucket* wizard:
   
   - **(IMPORTANT FOR GRADING!)** Bucket name: *ust-\<ITSC accoutn string\>-bucket1*.
     
     <img width="1223" height="375" alt="image" src="https://github.com/user-attachments/assets/c5684ece-213d-4e96-9bff-687a1e0f2930" />

   - Keep the default settings for the rest of the options.
     
     > Note: By default, new buckets don't allow public access. Diving deeper into this goes beyond the scope of this lab, but it's important to note.
   
   - Review the settings, and then choose *Create bucket* at the bottom of the page. 
     

4. Repeat step 3 to create two more buckets. Name them *ust-\<ITSC accoutn string\>-bucket2* and *ust-\<ITSC accoutn string\>-bucket3*, respectively.


In the end, you should see 3 buckets present in the *General purpose buckets* list.

   <img width="800"   src="https://github.com/user-attachments/assets/d2b8be79-db12-44ee-b238-183cbba158a4" />



<br/>
   
## Task 4: Logging in as an IAM user


1. Open the IAM console. Choose *Users* in the left navigation pane. Then choose *devuser* in the *Users* pane.
 
   <img width="800" src="https://github.com/user-attachments/assets/628cb403-3c9a-4d5d-a1c8-9b9433d6f626" />



2. Click on the *Security credentials* tab, and copy the link shown in the *Console sign-in link* field.

3. Keep the current tab (where you're signed in as the root user) open. Open a new browser tab, paste the URL you just copied into the address bar, and press Enter.



4. Choose *Sign into new session* to proceed to the login page.

   <img width="600" src="https://github.com/user-attachments/assets/163bb537-f888-4994-9292-446e2f0bcacb" />

5. Log in using the IAM user named *devuser*. Please note that the Account ID or alias field is pre-populated with your account ID.

   <img width="300" src="https://github.com/user-attachments/assets/f18e3caf-81ce-4a97-a319-460642ecdc43" />

   - For IAM user name, enter *devuser*
   - For Password, enter *isom5140_devuser* (the password you created before for this IAM user).
   - Choose *Sign in*.

6. The AWS Management Console displays. Make sure you're in the *us-east-1* Region.   

   <img width="300" alt="image" src="https://github.com/user-attachments/assets/e3634272-d421-4d83-8046-4d5eed754757" />

 <br/>

## Task 5: Attempting read-level access to AWS services

Now that you are logged in to the console as the IAM user named *devuser*, you will explore the level of access that you have to a few AWS services, including Amazon Elastic Compute Cloud (Amazon EC2), Amazon S3, and IAM.

1. Open the Amazon EC2 console.

   <img width="800"  src="https://github.com/user-attachments/assets/5e54946d-e198-4887-9c9f-733557ee0e38" />


2. In the left navigation pane, choose *Dashboard*.
   
   <img width="200" src="https://github.com/user-attachments/assets/8306b25e-9e72-4400-b4dd-93d99d56c0b7" />

   Many API Error messages display. This is expected.


3. Attempt some actions in the Amazon EC2 console:

   - In the left navigation pane, choose *Instances*.

   - In the *Instances* list, a message displays *"You are not authorized to perform this operation. User: arn:aws:iam::\<account-id\>:user/devuser is not authorized to perform: ec2:DescribeInstances because no identity-based policy allows the ec2:DescribeInstances action"*.


4. Choose *Launch instances*. Scroll down and choose the *Key pair name* drop down list.

   A message displays *"You are not authorized to perform this operation."*

   <img width="800"  src="https://github.com/user-attachments/assets/bf76d4fa-4b21-4592-aa31-77782a31b311" />

   Notice that Key pair name is a required setting that must be configured if you want to launch an instance. This is just one of many indications that you will not be able to launch an EC2 instance with the permissions that have been granted to you as the devuser.

5. In the *Summary* panel on the right, choose *Cancel*.

6. Open the Amazon S3 console to explore what you can access. Three buckets are listed with unique names.

7. Open the IAM dashboard page, notice that you do not have permissions to view certain parts of the page. The message states *"User: arn:aws:iam:::user/devuser is not authorized to perform: iam:GetAccountSummary on resource:"*. 


<br/>

## Task 6: Analyzing the identity-based policy applied to the IAM user

In this task, you will look at the IAM policy details that apply to *devuser* to understand why you can't perform these actions.


1. Keep the current browser tab open. Switch to the browser tab that hosts the session for the account root uers.

2. Access the IAM console, and observe user and group membership settings:

   - In the left navigation pane, choose *User groups*.
     
   - Choose the *DeveloperGroup* group name. On the Users tab, notice that `devuser` is a member of this IAM group.

   > Note: When a policy is attached to a group, the policy applies to any IAM users who are members of the group. Therefore, this policy currently governs your access to the console, because you are logged in as devuser, who is a member of this IAM group.

 
3. Save the policy to a file on your computer:
   
   - To copy the JSON policy to your clipboard, choose *Copy*.
   - Open a text editor on your local computer, and paste the policy that you just copied.
   - Save the policy document as *DeveloperGroupPolicy.json* to a location on your computer that you will remember.


<br/>

## Task 7: Attempting write-level access to AWS services

In this task, you will attempt to perform two actions that require write-level access within Amazon S3. The first action is to create an S3 bucket, and the second action is to upload an object to that bucket. 

After you attempt the two tasks, you will again analyze the policy attached to the IAM group to analyze why you could or could not perform the specific actions.

1. Keep the current browser tab open. Switch to the browser tab that hosts the session for the *devuser* user.

2. Attempt to create an S3 bucket:
   
   - Navigate to the Amazon S3 console.
   - Choose Create bucket
   - For Bucket name, enter *ust-* followed by your initials and a random four-digit number; for example, *ust-zbq1234*.


   You successfully created an S3 bucket.

3. Access the *ust-\<your ITSC account string\>-bucket1* bucket, and attempt to upload an object:

   - Choose the bucket named *"ust-\<your ITSC account string\>-bucket1"* from the *General purpose buckets* list.
   - Choose *Upload*, and then choose *Add files*.
   - Browse to and choose the *DeveloperGroupPolicy.json* file that you saved earlier.
   - Choose *Upload*.

   A message displays *Upload failed*.

4. On the *Files and folders* tab on the lower part of the page, in the *Error* column, choose the *Access Denied* link.

    <img width="500"  src="https://github.com/user-attachments/assets/0b1663c2-6a2b-402a-aec9-03267c9de99f" />

    The message states *"You don't have permissions to upload files and folders"*. Choose *Close*.

5. You can repeat the previous steps for the rest of the general purpose buckets. You'll encounter the same error when attempting upload files

6. Return to the text editor where you copied the *DeveloperGroupPolicy.json* document. Review the policy details to understand why you were able to create an S3 bucket but couldn't upload objects to an existing bucket.

Tip: The *Service Authorization Reference* document provides a list of actions that each AWS service supports. For information about Amazon S3 actions, open the [IAM documentation](https://docs.aws.amazon.com/iam/) page, and then open the *Service Authorization Reference* document. In the left navigation pane, expand Actions, resources, and condition keys, and then choose Amazon S3. In the Actions defined by Amazon S3 section, the table lists every possible Amazon S3 action that can be granted or denied, along with a description of the action


## Task 8: Configuring a resource-based policy 

In this task, you'll configure a resource-based policy to allow an existing S3 bucket to accept file uploads. This will show you how resource-based policies can grant IAM identities permissions to perform actions, as long as those actions aren't explicitly denied by their identity-based policies.


1. Keep the current browswer tab open. Switch back to the tab where you're signed in as the root user. Then navigate to the Amazon S3 console.

2. From the *General purpose buckets* list, select the bucket named *"ust-\<ITSC account string\>-bucket1"*.

3. Click on the *Permissions* tab, find the *Bucket policy* section, and then click *Edit*.
 

   <img width="800" src="https://github.com/user-attachments/assets/3fca7de3-38f7-496f-982f-0b81bdc3b7d1" />


4. Copy and paste the JSON policy below into the *Policy* text area. Make sure to replace all ARNs having placeholders in place with the correct ARNs in your environment. Then choose *Save changes*
   
	```json
	{
		"Version": "2012-10-17",
		"Statement": [
			{
				"Effect": "Allow",
				"Principal": {
					"AWS": "arn:aws:iam::<account id>:user/devuser"
				},
				"Action": "s3:*",
				"Resource": [
					"arn:aws:s3:::ust-<ITSC account string>-bucket1",
					"arn:aws:s3:::ust-<ITSC account string>-bucket1/*"
				]
			},
			{
				"Effect": "Deny",
				"Principal": {
					"AWS": "arn:aws:iam::<account id>:user/devuser"
				},
				"Action": "s3:DeleteBucket",
				"Resource": "arn:aws:s3:::ust-<ITSC account string>-bucket1"
			}
		]
	}
	```
 
	<img width="800" src="https://github.com/user-attachments/assets/e4ad384b-0fbc-4952-a8c3-e2b55e5229e7" />


5. Keep the current tab open. Now switch to the browser tab where you're signed in as *devuser*.

6. Choose *"ust-\<ITSC account string\>-bucket1"*, and try uploading the *DeveloperGroupPolicy.json* file again. This time, the upload should succeed!

7. Select the uploaded *DeveloperGroupPolicy.json* document from the *Objects* list. Choose *Delete*. Follow the instructions in the *Delete objects* wizard to confirm. The file should then be successfully deleted.

   <img width="800" src="https://github.com/user-attachments/assets/4f2f9b7a-d5e9-4cb8-b887-bd2b7c50d239" />

8. From the breadcrumbs in the upper-left corner of the page, choose *Buckets*.
   
   <img width="400"  src="https://github.com/user-attachments/assets/a1c77933-1cc9-4720-9da0-65002f1b62e9" />

9. Select *"ust-\<ITSC account string\>-bucket1"*. Then choose *Delete*, and confirm the deletion in the *Delete bucket* wizard.
    
    <img width="800" src="https://github.com/user-attachments/assets/57ac67e6-4176-4478-87f7-ada882990f1a" />

   A message displays *"You are not authorized to perform this operation"*.

   <img width="800" src="https://github.com/user-attachments/assets/3f0d9282-940c-4b12-87ed-403c339f54dc" />


<br/>


## Task 9: Assuming an IAM role to access AWS resources

In this task, you will try to access *bucket2* by using a role while logged in as the devuser IAM user. 

1. Keep the current tab open. Switch to the browser tab  where you're signed in as the root user.
2. Open the *IAM* console, and choose *Policies* in the left navigation pane.
   
3. Choose *Create policy*. This time, you'll explore how to use the visual policy editor to create and configure a policy. 

   - Select S3 from the Service dropdown menu.
   
     <img width="800" src="https://github.com/user-attachments/assets/c194487e-39b4-4e46-b993-7950973cf8d9" />

   - Tick the checkbox for *All S3 actions (s3:*)*.
   
     <img width="800" src="https://github.com/user-attachments/assets/c93dd0c6-2f57-44a2-a73e-6266386c87da" />


   - In the *Resources* section, find the *bucket* field, and click *Add ARNs* to specify which bucket this applies to.

     <img width="800" src="https://github.com/user-attachments/assets/58da9c79-950f-49d5-a05f-390eb0b26f56" />

   - In the popup window, type the name of the 2nd bucket, i.e., *ust-\<ITSC account string\>-bucket2*: in the *Resource bucket name* field. Then choose *Add ARN*.

     <img width="600" src="https://github.com/user-attachments/assets/e70750a9-b4cd-4170-8eb1-d10019393d81" />

   - Find the *object* field and click *Add ARNs* to specify which objects this policy applies to.
   
     <img width="800" alt="image" src="https://github.com/user-attachments/assets/8f32d257-5391-43ac-bfa3-9c263724adee" />


   - Fill in the *Resource bucket name* field with the same bucket name, and tick the checkbox for *Any object name*. Then choose *Add ARN*.

     <img width="600" src="https://github.com/user-attachments/assets/69f45872-dabe-4962-9a89-ee3ba13309c7" />


   - Click *Next*.

   - Type *Bucket2AccessPolicy* in the *Policy name* field. Then choose *Create policy* at the bottom right of the page.

     <img width="800" src="https://github.com/user-attachments/assets/e5d2fede-c69a-423f-9b4b-7b63b116fd3f" />

4. In the *Policies* pane, search for the policy you just created. Click the plus icon to the left of the policy name to review the policy.

   <img width="800" src="https://github.com/user-attachments/assets/82278249-8c2e-4b17-a6c3-04176b4d2199" />

Next, you'll create an IAM role and attach this *Bucket2AccessPolicy* policy to it (Remember: to use the policy, you need to associate it with an IAM principal).

5. Choose *Roles* in the left navigation pane. Then choose *Create roles*, and configure the role settings:
    
   - Select *AWS account* under the *Trusted entity type* section, and choose *This account* under the *An AWS account* section. Then choose *Next*
    
     
	 <img width="800" src="https://github.com/user-attachments/assets/070c0773-abff-4bd9-a0c7-a0f93dc26b98" />


   - Search for the policy you just created. Tick the checkbox for the policy. Then choose *Next*

     <img width="800" src="https://github.com/user-attachments/assets/709cca07-905e-4a9f-96ab-b1ca04c4d465" />

   - Call the role *Bucket2AccessRole*. Then choose *Create role* at the bottom right corner
    
     <img width="800" src="https://github.com/user-attachments/assets/0495b9f1-eb0a-49a1-baa8-0c678a167ed9" />

The trust policy for the role we just created doesn't fully meet our requirements. Next, you'll refine it to restrict access so that only the IAM user *devuser* can assume this role.

6. Choose the *Bucket2AccessRole* role from the *Roles* list.


7. Click on the *Trust relationships* tab. Then choose *Edit trust policy*.


	<img width="800" src="https://github.com/user-attachments/assets/e4084b4d-6c0e-44fe-bd63-19574baac081" />



8. In the *Edit trust policy* text area, find the *Principal* block. Replace the *root* part of the ARN with *user/devuser* (keeping the account ID). You can also remove the *Condition* block. Then click *Update policy*.


> Note: Using *"arn:aws:iam::\<account id\>:root"* in an IAM policy does not restrict access to just the root user. Instead, it grants access to the entire AWS account, meaning it can apply to any user or role within it. In this step, you're actually making the policy more secure by narrowing that broad access down to a specific IAM user.
    

Next, you'll test if you can assume the *Bucket2AccessRole* role while logged in as the IAM user *devuser*.

9. Copy the URL in the *Link to switch roles in console* field

   <img width="800" src="https://github.com/user-attachments/assets/7151a16e-2a28-417d-be54-2c7e372a9f79" />

    
	<img width="800" src="https://github.com/user-attachments/assets/dbce9432-fae2-4543-b5a8-803b49ea8109" />

10. Open a new browser tab, and paste the URL into the address bar. Then press *Enter*.
    
11. Choose *devuser* under the *Switch from* section. Then choose *Switch role*.
    
    <img width="800" src="https://github.com/user-attachments/assets/55fb4aa8-7d6f-41ef-8cb1-cefa2b28f5c2" />

Now you're logged in as the *Bucket2AccessRole* role.

   <img width="500" src="https://github.com/user-attachments/assets/4be2b921-9346-4fcc-be57-3bde04d990fd" />

You can head over to the Amazon S3 console and test whether you can upload files into the *ust-\<ITSC account string\>-bucket2* bucket.

12. Once you've finished testing, look for and click your profile at the top right of the screen. Then in the dropdown menu, choose the down-pointing triangle next to *Sign out of all sessions*. Choose *Sign out of current session* to only log out of the current IAM role session.

    <img width="300" src="https://github.com/user-attachments/assets/351f7470-25f9-468e-a63e-42b427c6187e" />

Next, you'll test if you can assume the *Bucket2AccessRole* role while signed in as the account root user.

13. Open a new browswer tab, and paste the URL copied from the *Link to switch roles in console* into the address bar. This time, try to switch roles from the account root user. You'll encounter the following error message:
    
    <img width="800"  src="https://github.com/user-attachments/assets/5341773b-eb72-44f5-ac91-5a10afde1819" />


<br/>

## Challenge tasks

### Challenge task 1: Verifying the role of the "sts:AssumeRole" action

1. Switch to the browser tab where you are signed in as the root user.
2. In the IAM console, locate the *DeveloperGroupPolicy* policy and edit it to remove the "sts:AssumeRole" action from its policy statement.
3. Save the policy changes.
4. Switch back to the browser tab where you are logged in as the IAM user *devuser*.
5. Attempt to assume the *Bucket2AccessRole* again. Verify whether the action is still permitted.
6. Switch to the browser tab where you are signed in as the root user. Add the "sts:AssumeRole" action back to the *DeveloperGroupPolicy* policy.

<br/>

### Challenge task 2: Allowing cross-account access

1. Remain in the browser tab where you are signed in as the root user.
2. In the IAM console, locate the *Bucket2AccessRole* role.
3. Ask a neighbor for their AWS Account ID.
4. Edit the role's *Trust Policy*. Add a new principal that specifies your neighbor's account ID, granting them permission to assume this role.
5. Copy the *Link to switch roles in console* for the role and share it with your neighbor. Verify if they can successfully assume the role and access the three S3 buckets in your account.
