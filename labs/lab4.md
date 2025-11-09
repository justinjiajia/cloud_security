

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


