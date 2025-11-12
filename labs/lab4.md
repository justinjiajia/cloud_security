


create an S3 bucket

Name: ust-justinjia-production-bucket-001

<img width="1050" height="532" alt="image" src="https://github.com/user-attachments/assets/f4f06901-250f-487a-a488-002e0f0f6aac" />


Create another S3 bucket
Name: ust-justinjia-production-bucket-002


Create an IAM policy


Select S3 from the Service dropdown menu
<img width="781" height="453" alt="image" src="https://github.com/user-attachments/assets/c194487e-39b4-4e46-b993-7950973cf8d9" />

Tick the checkbox for *All S3 actions (s3:*)*
<img width="762" height="180" alt="image" src="https://github.com/user-attachments/assets/c93dd0c6-2f57-44a2-a73e-6266386c87da" />


Locate the *bucket* field under the Resources section, choose *Add ARNs* to restrict access.

<img width="761" height="75" alt="image" src="https://github.com/user-attachments/assets/58da9c79-950f-49d5-a05f-390eb0b26f56" />


Choose *Add ARNs*
<img width="807" height="290" alt="image" src="https://github.com/user-attachments/assets/2acf102c-4a7d-4d1c-871d-52d056233245" />


Locate the *object* field under the Resources section, choose *Add ARNs* to restrict access.
<img width="759" height="77" alt="image" src="https://github.com/user-attachments/assets/8f32d257-5391-43ac-bfa3-9c263724adee" />


Fill in the *Resource bucket name* field with the bucket name, tick the checkbox for *Any object name*
<img width="807" height="347" alt="image" src="https://github.com/user-attachments/assets/6d9f2acf-8b43-407c-87a9-56573c44a53e" />

Click Next

Policy name: *CrossAccountAccessToS3Bucket*

<img width="766" height="388" alt="image" src="https://github.com/user-attachments/assets/34130ccf-c019-4823-91d9-170257cde025" />


permissions defined in the *CrossAccountAccessToS3Bucket* policy
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListAccessPointsForObjectLambda",
                "s3:GetAccessPoint",
                "s3:PutAccountPublicAccessBlock",
                "s3:ListAccessPoints",
                "s3:CreateStorageLensGroup",
                "s3:ListJobs",
                "s3:PutStorageLensConfiguration",
                "s3:ListMultiRegionAccessPoints",
                "s3:ListStorageLensGroups",
                "s3:ListStorageLensConfigurations",
                "s3:GetAccountPublicAccessBlock",
                "s3:ListAllMyBuckets",
                "s3:ListAccessGrantsInstances",
                "s3:PutAccessPointPublicAccessBlock",
                "s3:CreateJob"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::ust-justinjia-production-bucket-001/*",
                "arn:aws:s3:::ust-justinjia-production-bucket-001"
            ]
        }
    ]
}
```


To use the policy, I need to associate it with an IAM principal, 

Next, I'll create an IAM role and attach this *CrossAccountAccessToS3Bucket* policy to it

Select *AWS account*

<img width="769" height="464" alt="image" src="https://github.com/user-attachments/assets/c1b264d5-da70-4ebf-816f-9aa45e5ebe39" />

 



<img width="760" height="356" alt="image" src="https://github.com/user-attachments/assets/68fd6ec9-021d-4109-92c6-21cf0cc048e0" />

<img width="252" height="448" alt="image" src="https://github.com/user-attachments/assets/c20719b6-677b-438e-9129-ff5bd00c087e" />


<img width="782" height="298" alt="image" src="https://github.com/user-attachments/assets/39adf3bd-f155-4ce7-8402-2e9e387faf0d" />


Call the role: *AccessToS3BucketFromOtherAccountsRole*

<img width="1098" height="378" alt="image" src="https://github.com/user-attachments/assets/3e04af27-bb0b-43df-8b20-0511907e33ad" />

Trust policy

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Principal": {
                "AWS": "245221346334"
            },
            "Condition": {}
        }
    ]
}
```

<img width="1101" height="587" alt="image" src="https://github.com/user-attachments/assets/d1af6ed6-f09a-4883-bbba-1c2e04635d2c" />


Link to switch roles in console: *https://signin.aws.amazon.com/switchrole?roleName=AccessToS3BucketFromOtherAccountsRole&account=135056809391*

ARN:  *arn:aws:iam::135056809391:role/AccessToS3BucketFromOtherAccountsRole*


Trusted entities of the *AccessS3BucketFromAnotherAccount* role
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::245221346334:root"
            },
            "Action": "sts:AssumeRole",
            "Condition": {}
        }
    ]
}
```

---

<in my account>

now configure your *admin* user to have an inline policy

<img width="800" height="302" alt="image" src="https://github.com/user-attachments/assets/cf118876-39b4-4695-a737-7ccc63649243" />

Choose JSON, then copy and paste the JSON policy below:

<img width="1022" height="378" alt="image" src="https://github.com/user-attachments/assets/ff288f55-5603-4a7d-bc92-684af4908b6e" />



```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Action": "sts:AssumeRole",
			"Resource": "arn:aws:iam::135056809391:role/AccessToS3BucketFromOtherAccountsRole"
		}
	]
}
```

name this inline policy *AccessToS3BucketInAnotherAccountPolicy*
and create it

<img width="1018" height="504" alt="image" src="https://github.com/user-attachments/assets/12d56852-b3a6-4a7d-aba3-08a4489148e2" />



Now I want to log in as the admin user

<img width="799" height="409" alt="image" src="https://github.com/user-attachments/assets/01e3cc34-6b67-477e-a5ef-51220bcd57be" />

copy the *Console sign-in link*, and Choose *enable console access*

<img width="526" height="269" alt="image" src="https://github.com/user-attachments/assets/e4da86cb-5ed4-433b-a365-a3551227cafc" />

<img width="524" height="352" alt="image" src="https://github.com/user-attachments/assets/c4a3b200-c449-461b-9471-ec473e5e9e57" />

copy and paste console password

<img width="332" height="388" alt="image" src="https://github.com/user-attachments/assets/0ab32235-7901-4d25-a050-ea1952e75048" />


Choose Switch role.

If you have opted in to multi-session support, choose Add session and select Switch role.
<img width="280" height="162" alt="image" src="https://github.com/user-attachments/assets/175bf20b-322d-4583-ae41-ce91cbdc6354" />


ARN:  *arn:aws:iam::135056809391:role/AccessS3BucketFromAnotherAccount*


<img width="814" height="591" alt="image" src="https://github.com/user-attachments/assets/5000d4bb-00c0-4373-a919-6e91cf8c7abd" />

<img width="1038" height="400" alt="image" src="https://github.com/user-attachments/assets/8dd7acad-ba16-40d5-8ade-7b316d628ec7" />


https://github.com/justinjiajia/certifications/blob/main/aws/cloud_security/labs/lab6.md


use iam role 

<img width="520" height="842" alt="image" src="https://github.com/user-attachments/assets/bf2c8eee-3d16-4861-b944-ce263189836f" />

<img width="1132" height="635" alt="image" src="https://github.com/user-attachments/assets/288e5921-9869-4df4-95be-737c599b5857" />

<img width="872" height="566" alt="image" src="https://github.com/user-attachments/assets/0aa3c4d3-829b-4009-8afc-23730101abcb" />


<img width="893" height="409" alt="image" src="https://github.com/user-attachments/assets/9d84b724-a728-4874-8768-0efd7683eb7e" />




Name: EC2InstanceS3ReadOnly


<img width="872" height="297" alt="image" src="https://github.com/user-attachments/assets/46a589f0-ccd9-41c4-920c-20fefe7c06d0" />


- In the secition of Select trusted entities:



<img width="879" height="356" alt="image" src="https://github.com/user-attachments/assets/767d60b0-6f26-4e8d-8aa8-22163c3a5c78" />

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Principal": {
                "Service": [
                    "ec2.amazonaws.com"
                ]
            }
        }
    ]
}
```

ec2-without-role

ec2-with-role



<img width="749" height="359" alt="image" src="https://github.com/user-attachments/assets/e3436a50-7ebe-4722-a353-b2ee12a2a075" />

<img width="742" height="212" alt="image" src="https://github.com/user-attachments/assets/1aa17603-0ad7-4c5a-a2dd-789d47d3d8e5" />


<img width="741" height="258" alt="image" src="https://github.com/user-attachments/assets/4af73cdc-9881-41f7-bdfc-c4da6fccfacb" />


 

```shell
aws configure
```

Create an admin user, and attach AmazonEC2FullAccess and IAMFullAccess to the user


<img width="880" height="241" alt="image" src="https://github.com/user-attachments/assets/ea6a8124-0334-4832-965b-4da3f0fb0787" />
<img width="872" height="377" alt="image" src="https://github.com/user-attachments/assets/5ce51c43-a197-4199-8628-80c0e5848279" />

<img width="874" height="290" alt="image" src="https://github.com/user-attachments/assets/2a63475b-2927-4fa6-aab6-a85c3a62b6bd" />


Create an access key for the admin user:

<img width="652" height="97" alt="image" src="https://github.com/user-attachments/assets/84b0400b-e5a0-42c7-859d-f59a8790cd9e" />


```shell
aws ec2 associate-iam-instance-profile --instance-id i-xxxxxxxxxxxxxxxxx --iam-instance-profile Name="EC2InstanceS3ReadOnly"
```

<img width="666" height="125" alt="image" src="https://github.com/user-attachments/assets/faf6da6e-fb89-4f9b-863a-1b2132cf75d9" />

remove the configured credential.
the ec2 will then use the attached instance profile.

interface operations:

<img width="941" height="277" alt="image" src="https://github.com/user-attachments/assets/c0c2f1ce-0258-46c3-8495-3572d37dc4fe" />

<img width="960" height="233" alt="image" src="https://github.com/user-attachments/assets/008041fd-2162-498a-a96e-85a70fb1bad5" />

Choose Update IAM role

```shell
aws s3 ls
```

<img width="712" height="258" alt="image" src="https://github.com/user-attachments/assets/e12220f5-1061-4c55-8748-12371d8417f8" />

```shell
wget https://raw.githubusercontent.com/justinjiajia/cloud_security/refs/heads/main/labs/resources/AWS_logo_RGB.png
```

```shell
aws s3api get-object --bucket ust-cloud-security-test --key AWS_logo_RGB.png downloaded.png
```

<img width="1161" height="95" alt="image" src="https://github.com/user-attachments/assets/1916d426-e4d4-4f45-929d-30788737629f" />


now edit bukkect policy

<img width="888" height="622" alt="image" src="https://github.com/user-attachments/assets/79fd766d-fbb5-4795-abab-e0f48661022c" />

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::245221346334:user/admin"
            },
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::ust-cloud-security-test",
                "arn:aws:s3:::ust-cloud-security-test/*"
            ]
        }
    ]
}
```
```shell
aws s3api get-object --bucket ust-cloud-security-test --key AWS_logo_RGB.png downloaded.png
```

<img width="1011" height="253" alt="image" src="https://github.com/user-attachments/assets/66d82873-db7f-42c6-8cc8-4842bf109a28" />
