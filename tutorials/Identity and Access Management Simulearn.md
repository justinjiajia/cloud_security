
https://skillbuilder.aws/learn/KUT6BB8X9E/aws-simulearn-identity-and-access-management



Alejandro Rosalez
Greetings! Thank you for heeding my call. I just started as the security admin here at the library. My first project is to lock down Amazon S3 folder access. Can you show me how?
You
Nice to meet you. I'm sure I can help. Tell me more about the project. Who, or what, needs to access the Amazon S3 folders?
Alejandro Rosalez
Each employee has their own Amazon S3 folder where they can store their private information, such as project plans, meeting notes, and other stuff. Currently, the folders are not locked down as they should be, so information is accessible by others.


You
That's not good. Sounds like an IAM policy variable might be needed here. Are you using IAM roles or IAM user groups to manage users?
Alejandro Rosalez
I have no idea. When a new employee starts, I just create a new folder in our S3 bucket and name it based on their username. What are IAM policy variables?

ou
An IAM policy variable is a placeholder that you can use when you don't know the exact value of a resource or condition key when you write the policy. It's a great way to write dynamic IAM policies that allow access to resources based on a user attributes, such as username.
Alejandro Rosalez
Sounds useful. Can you explain what IAM roles are?


You
An IAM role is an AWS Identity and Access Management identity that you can create in your account that has specific permissions. An IAM role is similar to an IAM user, in that it is an AWS identity with permission policies that determine what the identity can and cannot do on AWS. You can use roles to delegate access to users, applications, or services that don't normally have access to your AWS resources
Alejandro Rosalez
No. I don't think we are currently using IAM roles. What are IAM user groups?

You
An IAM user group is a collection of IAM users. With user groups, you can specify permissions for multiple users, which can help you manage the permissions for those users.
Alejandro Rosalez
IAM user groups don't sound familiar either. I am in big trouble if I don't know these concepts.


You
Don't worry. I can walk you through everything you need to know. One last question. Does every employee need to access their folders through the AWS Management Console?
Alejandro Rosalez
Good question. The answer is no. Librarians love to type, so many of them prefer to use the AWS Command Line Interface to interact with their Amazon S3 folders.


You
I have all the information I need. I just need a little time to build the solution.



## Solution Request

Use the AWS Identity and Access Management console to configure permissions on users' S3 buckets.

<img width="706" height="514" alt="image" src="https://github.com/user-attachments/assets/14d06a51-1401-4bb1-ae62-9b3846651b42" />

- Step 1
  This solution uses AWS Identity and Access Management (IAM) user groups and policies to secure Amazon S3 folders.

<img width="701" height="506" alt="image" src="https://github.com/user-attachments/assets/3f87cecb-62fb-4cce-b0d9-49ccc2312be9" />

- Step 2
  An IAM user group is a collection of IAM users. With user groups, you can specify permissions for multiple users, which can help you manage the permissions for those users.

<img width="688" height="511" alt="image" src="https://github.com/user-attachments/assets/a661d061-3eb0-43e9-8af6-73d00940e443" />

- Step 3
  IAM users can access AWS services, such as Amazon S3, by using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or both.

<img width="705" height="508" alt="image" src="https://github.com/user-attachments/assets/c0fb05a0-fc1c-48e2-9660-9c6f0350d4c7" />

- Step 4
  When using the AWS Management Console, a user must have a user ID and password to gain access.

<img width="685" height="502" alt="image" src="https://github.com/user-attachments/assets/5c7f62e3-399f-442e-ace6-5c8bc6264198" />

- Step 5
  To access AWS services programmatically, or use the AWS CLI, a user must use IAM access keys.

<img width="696" height="508" alt="image" src="https://github.com/user-attachments/assets/f2f18476-e0da-4af7-9da9-b01ca45ff9b2" />

- Step 6
  An IAM access key is comprised of an access key ID and a secret access key. A best practice for managing access keys is to rotate these periodically.

<img width="690" height="506" alt="image" src="https://github.com/user-attachments/assets/91f6c438-1fab-42a7-8e2d-0c1ace61d2fd" />
- Step 7
  Use Amazon EC2 Instance Connect to connect to an EC2 instance, and run the "aws configure" command to configure the AWS CLI.

<img width="678" height="506" alt="image" src="https://github.com/user-attachments/assets/d5eb3b1e-81c3-48dd-8e01-5cf8e3475358" />


- Step 8
  You manage access to AWS by creating policies and attaching them to IAM identities (users, groups of users, or roles) or AWS resources.

<img width="693" height="519" alt="image" src="https://github.com/user-attachments/assets/25a5cf5e-628c-4e8c-b6f8-9917f8f91b0e" />

- Step 9
  A policy is an object on AWS that, when associated with an identity or resource, defines their permissions. Permissions in the policies determine whether the request is allowed or denied.
  Most policies are stored on AWS as JSON documents.

<img width="703" height="513" alt="image" src="https://github.com/user-attachments/assets/0a29c7db-f23a-4ec1-96b8-3bd9cf5e896b" />

- Step 10
  Policy variables, such as ${aws:username}, allow one policy that can be used for many users.
  When the policy is evaluated, the variables are replaced with values that come from the context of the request.

<img width="693" height="513" alt="image" src="https://github.com/user-attachments/assets/4e7254fa-e383-434b-b46c-870ddf450082" />

- Step 11
  When a user does not require access to the AWS Management Console, the console can be disabled.
  Any operations that require access to Amazon S3, such as uploading an image to an S3 bucket, will need to be done through the AWS CLI.


## practice lab


<img width="681" height="516" alt="image" src="https://github.com/user-attachments/assets/258eb53e-c3d0-435c-991c-7c8ccc50708f" />


Concept
In this practice lab, you will:
- Create an IAM policy by using policy variables.
- Assign IAM users and policies to a user group.
- Generate CLI credentials for a user. 
- Configure the AWS CLI to use an access key and secret key for a user.

Practice Lab Goals

- Create an IAM policy by using policy variables.
- Assign IAM users and policies to a user group.
- Generate CLI credentials for a user.
- Configure the AWS CLI to use an access key and secret key for a user.


 


### Step 1
1. Review the practice lab objectives in the Concept section.
2. Click Start Lab or Open AWS Console to begin.
3. Follow the lab instructions carefully, and use the arrows below to navigate between steps.

AWS services not used in this lab are disabled in the lab environment. In addition, the capabilities of the services used in this lab are limited to what the lab requires. 


### Step 2

1. In the top navigation bar search box, type: s3

2. In the search results, under Services, click S3.
 

### Step 3

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/eeaa805a-c9a2-4fe7-9c26-c3ba778179fa" />

Concept
Amazon S3 has a flat structure (instead of a hierarchy, like you would see in a file system). However, the Amazon S3 console supports the folder concept to group objects and help efficiently organize your data.

1. On the Objects tab, review the two bucket names that start with corp-, one for each user defined in the system.
2. Click the bucket name that starts with iam-lab-.

### Step 4


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/e56f0630-557b-4cb8-8c8d-5a7c6c8444b5" />


 Concept
A policy is an object in AWS that, when associated with an identity or resource, defines its permissions. AWS evaluates these policies when an AWS Identity and Access Management (IAM) principal (user or role) makes a request.
 
1. On the Objects tab, choose the check box to select the lab_s3_policy.json file.
2. Click Download.

- The file downloads to your device. 

3. Open the file in the text editor of your choice (not shown). 

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": [
                "arn:aws:s3:::corp-${aws:username}"
            ],
            "Condition": {
                "StringLike": {
                    "s3:prefix": [
                        "",
                        "${aws:username}*"
                    ]
                }
            }
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject*"
            ],
            "Resource": "arn:aws:s3:::corp-${aws:username}/*"
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": "s3:GetBucketLocation",
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Sid": "VisualEditor3",
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "*"
        }
    ]
}
```


### Step 5

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9e71840d-9454-42fd-ac08-90638b3dfaf3" />

Concept
You can use the visual editor in the AWS Management Console to create and edit customer managed policies without ever using JSON. An IAM policy document consists of one or more policy statements.
 
1. Review the main components of an IAM policy document:

- Version: Policy language version
- Sid: Optional statement ID
- Resource: List of resources to which the action applies
- Condition: Apply policy if condition is true
- Effect: Allow or deny
- Action: List of actions allowed or denied

2. Select (highlight) and copy all the text from your text editor.

- You use this text in a later step.

###  Step 6

Concept
AWS Identity and Access Management (IAM) provides the infrastructure necessary to control authentication and authorization for your AWS account.

1. In the top navigation bar search box, type: iam

2. In the search results, under Services, click IAM.

### Step 7

Concept
An AWS managed policy is a standalone policy that is created and administered by AWS. These policies are designed to provide permissions for many common use cases.

1. In the left navigation pane, click Policies.
2. In the Policies section, click Create policy.

### Step 8
1. In the Specify permissions step, click the JSON tab.
2. Select (highlight) and delete the existing statement.

### Step 9

Concept
When you write the policy, use IAM policy variables as placeholders when you don't know the exact value of a resource or condition key.

1. Paste the policy that you copied in an earlier step.
2. Click Next.

### Step 10
1. In the Review and create step, for Policy name, type: 



2. For Description, type a description that explains the purpose of the policy, such as Policy to grant S3 bucket access to users.
3. Scroll down to the bottom of the page, and then click Create policy (not shown).


### Step 11

Concept
Remember that an AWS managed policy is a standalone policy that is created and administered by AWS. 
You can also create standalone policies that you administer in your own AWS account. This is known as a customer managed policy.

1. In the success alert, review the message.
2. To filter the policy results, in the Policies search box, type: lab

3. Under Type, review the type for the new policy.
4. In the left navigation pane, click User groups.

### Step 12

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/8b7b94cf-597a-409f-8011-c5ae7c84c574" />

Concept
An IAM user group is a collection of IAM users. With user groups, you can specify permissions for multiple users, which can help you manage the permissions for those users.
 
1. In the User groups section, click s3-private-bucket-access.
 

### Step 13

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/581f4a4c-5664-4b46-891d-ba7618de0265" />

Concept
A user group can contain many users, and a user can belong to multiple user groups.
 
1. On the Users tab, click Add users.

### Step 14
Concept
Your AWS account does not have a default user group that automatically includes all users. 
If you want to have a user group like that, you must create it and assign each new user to it.

1. Choose the two check boxes to select both user names.
2. Click Add users.

### Step 15
1. On the Users tab, review to confirm that both users were successfully added to the group.
2. Select (highlight)and copy the user names that starts with `hruser-`, and then paste it in your text editor.
   
hruser-39c40400
- You use this value in a later step.

3. Click the Permissions tab.

### Step 16
1. In the Permissions policies section, click Add permissions to expand the dropdown list.
2. Choose Attach policies.

### Step 17

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/62c4b794-64d9-4dc4-a21f-ba347950315a" />

1. In the Other permission policies search box, type:  lab_s3_policy

and press Enter.

2. Choose the check box to select lab_s3_policy.
3. Click Attach policies.

### Step 18
 
 Concept
Group names can be a combination of up to 128 letters, digits, and these characters: + = , . @ _ - 
Group names are not case sensitive.

1. In the success alert, review the message.


### Step 19

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/5e6f501c-a076-4a9a-bd14-f0a9d560f3f4" />

Concept
AWS Secrets Manager is a secrets management service that helps you protect access to your applications, services, and IT resources.
 
1. In the top navigation bar search box, type: secrets

2. In the search results, under Services, click Secrets Manager.

### Step 20

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/bcaab260-fb88-473a-81f0-ad10729ef543" />

1. On the Secrets page, click the secret name that starts with secretlabpassword.
2. Go to the next step. 



### Step 21

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/1f679881-dca9-4d18-9634-1393d24cb932" />

1. On the Overview tab, click Retrieve secret value.
2. Scroll down to view the Secret value section.

   
### Step 22

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/919b0a4a-ea5b-4996-8024-f356f623f3e3" />



Concept
Secrets Manager encrypts at rest using encryption keys that you own and store in AWS Key Management Service (AWS KMS). You can control access to the secret by using IAM policies. 
 
1. On the Plaintext tab, select (highlight) and copy the provided value, and then paste it in your text editor.

- You use this value in later steps.
nk^Oqn?n7N:~[u2<4T%H(RLA5$ic6a(u

### Step 23

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/fc874c43-c0d0-43bc-a121-21776b65e09f" />

 
1. On the top navigation bar, click to expand the user menu.
2. For Account ID, click the copy icon to copy the account number.  

- You use the Account ID in the next step.

  604656597602

### Step 24


Concept
When you first create an AWS account, you begin with one identity that has complete access to all AWS services and resources in the account. This identity is called the AWS account root user.
 
1. In a new private browser tab (or window) address bar (not shown), type:

https://us-east-1.console.aws.amazon.com/console/home

- To open an incognito window in Chrome, for example, use Ctrl+Shift+N or Cmd+Shift+N.

2. Under Sign in, choose IAM user.
3. For Account ID, paste the account number that you just copied.
4. Click Next.

### Step 25


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/1ab9b6fe-637c-4a92-991b-3199a37cffbf" />
1. For IAM user name, paste the hruser- username that you copied in an earlier step.
2. For Password, paste the secret password that you copied in an earlier step. 
3. Click Sign in.
4. Go to the next step.



### Step 26
1. On the top navigation bar, review to confirm that you are now signed in as hruser-.
2. In the Services search box, type:
 
3. In the search results, under Services, click S3.


### Step 27

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/11c8a6f7-0593-4095-a652-53c71a7784da" />


1. On the General purpose buckets tab, click the bucket name that starts with corp-hruser-.


### Step 28
<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/edf580de-0337-4771-adf6-c5432f2a5ca3" />

1. On the Objects tab, review the mygoals.txt file.
2. Choose the check box to select mygoals.txt.
3. Click Open.

- A new browser tab opens and displays the contents of the mygoals.txt file.


### Step 29

1. Review to see the private notes that hruser1 created. 
2. Close the browser tab that displays the notes (not shown).


### Step 30

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/712fe8cd-a9bb-4a0e-b93c-433d78d8b912" />

1. In the left navigation pane, click General purpose buckets.
2. On the General purpose buckets tab, click the bucket name that starts with corp-fnuser-.
3. Go to the next step.


### Step 31
<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/b7bcf8ea-a8fd-40ab-aa44-69503c0b779d" />

1. In the error alert, review to see that, when signed in as hruser-, you do not have access to view the contents of the corp-fnuser- bucket.
2. You can now close the private browsing window and go back to using the AWSLabsUser account (not shown).


### Step 32

1. In the top navigation bar search box, type: `iam`

2. In the search results, under Services, click IAM.
3. Go to the next step.


### Step 33


1. In the left navigation pane, click Users.
2. In the Users section, click the user name that starts with fnuser-.
3. Go to the next step.

### Step 34

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/4617e4f9-906f-4908-9bf8-23993ff4ff18" />

Concept
For increased security, we recommend that you configure multi-factor authentication (MFA) to help protect your AWS resources. You can enable MFA for IAM users or for the AWS account root user.

1. Click the Security credentials tab.
2. Click Manage console access.


### Step 35

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9280a525-f3c0-4d80-b788-41cf128d3abb" />

1. In the pop-up box, review your ability to quickly disable console access for a user.
2. Click Cancel.

### Step 36

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/02dc1921-ebbb-4730-a41e-58d2cc4c6650" />

Concept
Access keys are long-term credentials for an IAM user or for the AWS account root user. You can use access keys to sign programmatic requests to the AWS CLI or AWS API.
 
1. In the Access keys section, review the access keys information.
2. Click Create access key.


### Step 37


1. In the Access key best practices & alternatives step, for Use case, choose Command Line Interface (CLI).
2. Scroll down to the bottom of the page. 


### Step 38


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/f6b1abfe-5818-4498-9a29-931f62e44cdb" />

Concept
AWS CloudShell is a browser-based shell that makes it easier to securely manage, explore, and interact with your AWS resources. CloudShell is pre-authenticated with your console credentials.
 
1. Review Alternatives recommended.
2. Choose the check box to confirm your understanding of the alternatives recommendation.
3. Click Next.

### Step 39
 Concept
A common best practice is to use tags to describe the purpose of AWS resources.
 
1. In the Set description tag step, click Create access key.


### Step 40

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/5a50c829-0d45-406c-bd66-2f1a9ece0e3f" />


 Concept
Access keys consist of two parts: an access key ID  and a secret access key. Like a username and password, you must use both the access key ID and secret access key together to authenticate your requests.
 

1. In the Retrieve access keys step, click the copy icon for both the Access key and Secret access key, and paste them in your text editor.

- You use these in a later step.

AKIAYZSCXPJRP3TLC6W7
te1F+bPyFQ+Gt/TxDhpecQpP15ruSdNUlkW9NBhu

2. Click Done.
3. In the pop-up box (not shown), click Continue.

### Step 41

Concept
Session Manager is a fully managed AWS Systems Manager capability. 
With Session Manager, you can manage your Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, and on-premises servers and virtual machines (VMs).
 
1. In the top navigation bar search box, type: session manager

2. In the search results, under Features, click Session Manager.
 
### Step 42
<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/29071333-6d35-4ce6-978f-61159c06d209" />

Concept
Session Manager provides secure and auditable node management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys.
 
1. Click Start session.
2. Go to the next step.

### Step 43

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/59c802d4-568c-47da-b354-a10fde10b1b6" />

Concept
You can also use Session Manager to comply with corporate policies that require controlled access to managed nodes, strict security practices, and fully auditable logs with node access details, while providing end users with one-click, cross-platform access to your managed nodes.
 
1. In the Specify target step, in the Target instances section, choose Lab-instance.
2. Click Start session.

### Step 44

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/ef40233c-2b22-4b96-9c5f-6ca94a1cea68" />

Concept
Use the "aws s3 ls" command to list Amazon S3 objects and common prefixes under a prefix or all S3 buckets.
 
1. To login as the ec2-user, in the terminal window, at the command prompt, run (type the command and press Enter): 

```shell
sudo su - ec2-user
```

2. To change to the root directory, run:

```shell
cd ~ 
```
3. To list the contents of the directory, run:

```shell
ls -l
```
4. Review to confirm that the Zassy.png file appears.
5. To list S3 buckets, run:

```shell  
aws s3 ls
```

6. Review to see that you currently do not have ListBuckets permission.


### Step 45

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/31866575-3790-40db-bc2b-f96f7322101c" />

Concept
The "aws configure" command is the fastest way to set up your AWS CLI installation. When you enter this command, the AWS CLI prompts you for four pieces of information:
- Access key ID
- Secret access key
- AWS Region
- Output format
 
1. In the terminal, run:

```shell  
aws configure
```

2. For AWS Access Key ID, paste the value that you copied in an earlier step, and then press Enter.
3. For AWS Secret Access Key, paste the value that you copied in an earlier step, and then press Enter.
4. For Default region name, run:

```shell  
us-east-1
```
5. For Default output format, run:

```shell  
json
```


### Step 46

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/b2d59958-77c2-4f6e-ad5a-dc3b1ba60f99" />

Concept
Use the "aws s3 cp" command to copy objects to and from Amazon S3 buckets.
 
1. In the terminal, run:

```shell  
aws s3 ls 
```

- With the fnuser- CLI credentials configured, you now have access to list all S3 buckets.

2. Copy-paste the bucket names that start with corp-fnuser- and corp-hruser- in your text editor.
3. In the terminal, replacing the placeholder with the bucket name that starts with corp-fnuser-, run

```shell  
aws s3 ls <corp-fnuser-name>
```
	
4. Review to confirm that you have access to view the corp-fnuser- S3 bucket.
5. In the terminal, replacing the placeholder with the bucket name that starts with corp-hruser-, run:

```shell  
aws s3 ls <corp-hruser-name>
```

6. Review the permission error.
7. To copy the todo_list.txt file from Amazon S3 to the current directory and keep the same file name, run:

```shell 
aws s3 cp s3://<corp-fnuser-name>/todo_list.txt .
```

- Make sure to include the . (period) at the end of the command.

8. To see the contents of the file, run:

```shell
more todo_list.txt
```


## DIY

<img width="686" height="514" alt="image" src="https://github.com/user-attachments/assets/87cebea8-ad1f-4ad2-88e1-7fa6ebdc7fea" />

DIY Goals
Disable AWS Management Console access for fnuser-.
Use Session Manager to connect to the LabInstance.
Upload the Zassy.png file to the fnuser1 folder in corp-fnuser bucket by using the AWS CLI.


```shell
ls
Zassy.png  todo_list.txt
```
```shell
aws s3 cp ~/Zassy.png s3://corp-fnuser-39c40400/fnuser1/Zassy.png
```
