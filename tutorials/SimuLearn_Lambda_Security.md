https://skillbuilder.aws/learn/D579XW9VXM/aws-simulearn-lambda-security

## Simulated business scenario

The head of the IT department wants a solution that helps ensure that the IT cloud infrastructure meets strict data security rules. The company requires that no company data is exposed to the public internet.


>Arnav Desai
Hello! Thank you for coming. I am the head of the IT department, and I am worried about some security issues. We want to ensure that we meet our strict data security rules. In particular, our company requires that we expose no data to the public internet.
You
Sure. I am happy to help. Can you tell me more?
Arnav Desai
We recently migrated to a microservice architecture using AWS Lambda to build our applications. Our Lambda functions need to access an Amazon RDS database for data queries, and we aren't sure what configurations we need to meet our security requirements.
You
Let's start with Lambda. You can configure your Lambda functions to connect to private subnets in a virtual private cloud, which we call a VPC. After the Lambda function is VPC-enabled, you can securely access private resources, such as an Amazon RDS database.
Arnav Desai
I see. How about the database credentials? We do not want to hardcode the credentials in the Lambda function code. Is there a better way?
You
Absolutely! You can use AWS Secrets Manager to store the database credentials. Secrets Manager protects secrets, such as passwords, and you can rotate, manage, and retrieve secrets throughout their lifecycle.
You
The Lambda function can quickly retrieve the credentials with API calls to Secrets Manager.
Arnav Desai
Sounds great! However, if Lambda is in a private VPC subnet, how can we access other AWS services without going through the internet? We also need to access the Amazon S3 buckets in which we store the queried results.
You
No worries. You can use a VPC endpoint, which provides connections between a VPC and supported services, such as AWS Secrets Manager and Amazon S3, without requiring an internet gateway. Calling a service through a VPC endpoint keeps all the request traffic on the AWS network.
You
There are different types of VPC endpoints. To access Secrets Manager, for example, you can use an interface VPC endpoint.
You
To access your S3 buckets, you can create a gateway VPC endpoint that provides a private connection between the VPC and the S3 buckets. The traffic between your VPC and Amazon S3 does not leave the AWS network.
Arnav Desai
Fantastic! It sounds like your solution will help meet our security requirements.



### Solution Request
To meet the company's data security requirements, deploy an AWS Lambda function within a custom VPC that allows secure access to Amazon RDS and Amazon S3.

#### Step 1

<img width="751" height="393" alt="image" src="https://github.com/user-attachments/assets/e4b07c0e-2931-423d-a0eb-91c2d8b982af" />

In this solution, AWS Lambda accesses private resources in a virtual private cloud (VPC) without going through the public internet. 
Lambda securely retrieves database credentials from AWS Secrets Manager.

#### Step 2

<img width="753" height="400" alt="image" src="https://github.com/user-attachments/assets/654a7313-c3de-43a7-bd69-a997914c4547" />


AWS Lambda is configured to connect to private subnets in a VPC to access private resources, such as Amazon Relational Database Service (Amazon RDS).



#### Step 3

<img width="743" height="396" alt="image" src="https://github.com/user-attachments/assets/059816b5-4064-46b8-bbf0-ba2785fd83da" />

Amazon RDS is a managed relational database service. Using a VPC, you can isolate your Amazon RDS database in your own virtual network for security.


#### Step 4

<img width="750" height="397" alt="image" src="https://github.com/user-attachments/assets/b1852c38-4be0-40f6-bf4d-7eddcbfd25cb" />

Lambda retrieves database credentials from Secrets Manager through an interface VPC endpoint.


#### Step 5

<img width="742" height="391" alt="image" src="https://github.com/user-attachments/assets/0a7a94fd-027d-4959-9e6f-4a1245dc7e67" />

A VPC endpoint connects a VPC and supported services without requiring that you use an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. 
Using an interface VPC, you can connect to services powered by AWS PrivateLink.

#### Step 6

<img width="743" height="388" alt="image" src="https://github.com/user-attachments/assets/033f9c0d-b00e-41a8-b63a-a5139ff52735" />

Secrets Manager protects secrets, such as passwords needed to access your applications, services, and IT resources.

#### Step 7


<img width="744" height="392" alt="image" src="https://github.com/user-attachments/assets/b098acc8-db15-4123-91f0-339c497cce82" />


With the retrieved database credentials, Lambda is able to connect to Amazon RDS and make data queries.

#### Step 8

<img width="743" height="397" alt="image" src="https://github.com/user-attachments/assets/aa6178e5-5cdd-4bb0-9a0e-5782733d1c96" />


Gateway VPC endpoints provide reliable connectivity to Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB without requiring an internet or NAT gateway for your VPC.


#### Step 9

<img width="739" height="393" alt="image" src="https://github.com/user-attachments/assets/28789c55-8299-4758-b751-b3f52227c46f" />

Query results from Amazon RDS can be stored in an Amazon S3 bucket without any of the traffic leaving the AWS Network.


#### Step 10

<img width="742" height="388" alt="image" src="https://github.com/user-attachments/assets/3155a431-3c9c-4385-a587-b6db0a7a81ad" />


After a gateway VPC endpoint is configured, you can connect to more than one S3 bucket.


## Lab


Concept
In this practice lab, you will:
- Create an AWS Lambda function to connect to private subnets in a VPC.
- Retrieve database credentials from AWS Secrets Manager, through the Lambda function, to access Amazon RDS.
- Create a gateway VPC endpoint to access an Amazon S3 bucket.

<img width="742" height="395" alt="image" src="https://github.com/user-attachments/assets/24b2ca73-0a8c-4c80-89c2-75a0237394f5" />


Practice Lab Goals
Create an AWS Lambda function to connect to private subnets in a VPC.
Retrieve database credentials from AWS Secrets Manager, through the Lambda function, to access Amazon RDS.
Create a gateway VPC endpoint to access Amazon S3 buckets.


### Step 1
 
1. Review the practice lab objectives in the Concept section.
2. Click Start Lab or Open AWS Console to begin.
3. Follow the lab instructions carefully, and use the arrows to navigate between steps.

AWS services not used in this lab are disabled in the lab environment. In addition, the capabilities of the services used in this lab are limited to what the lab requires.



### Step 2

 
1. On this page, click the Lab Files tab.
2. Click the download icon to save the lab file to your device.

- You will use this file in later steps.

Backup: https://github.com/justinjiajia/cloud_security/blob/main/tutorials/resources/lambda_security_code.zip

3. Click the Steps tab to return to the Practice Lab steps.


### Step 3

Concept
AWS Lambda is a compute service that you can use to run code without provisioning or managing servers. 
 
1. In the top navigation bar search box, type:

 lambda

2. In the search results, under Services, click Lambda.


### Step 4

Concept
A function is a resource that you can invoke to run your code in AWS Lambda. 
This code processes the events that you pass into the function or that other AWS services send to the function.
 
1. In the Functions section, click Create function.

### Step 5



<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/3c9f0a00-ecb6-4964-90b0-ba35dd95c830" />


Concept
Lambda runtimes allow functions in different languages to run in the same base execution environment.
You configure your function to use a runtime that matches your programming language. 
 
1. For Function name, type: 

labFunction

2. For Runtime, on the dropdown menu, choose Python 3.13.
3. Scroll down to Permissions.




### Step 6


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/84157ffa-00fa-4456-b258-2f04df92d5a5" />

Concept
A Lambda function's execution role is an AWS Identity and Access Management (IAM) role that grants the function permission to access AWS services and resources. You provide this role when you create a function, and Lambda assumes the role when your function is invoked.
Step
6
1. Under Permissions, click to expand Change default execution role.
2. For Execution role, choose Use an existing role.
3. For Existing role, choose lambda_security_role.


Managed policy: AWSLambdaBasicExecutionRole
Customer inline policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": "us-east-1"
                }
            },
            "Action": [
                "lambda:InvokeFunction",
                "s3:Get*",
                "s3:Put*",
                "s3:List*",
                "secretsmanager:List*",
                "secretsmanager:Describe*",
                "secretsmanager:Get*",
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface",
                "ec2:DescribeNetworkInterfaces"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": "*",
            "Resource": [
                "arn:aws:lambda:us-east-1:393401899741:function:gbl_lab_monitoring",
                "arn:aws:iam::393401899741:role/LabStack-52553f06-5082-48-GblLabMonitoringgbllabmon-UPmUxxCgsFVx",
                "arn:aws:events:us-east-1:393401899741:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-YrCG7xJX64TN",
                "arn:aws:events:us-east-1:393401899741:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-wXNp6l9sc2B0",
                "arn:aws:events:us-east-1:393401899741:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-JVbF8N9hjDfc",
                "arn:aws:events:us-east-1:393401899741:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-z6JFoP7fORmW",
                "arn:aws:events:us-east-1:393401899741:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-s7YKhCkG4aTE",
                "arn:aws:events:us-east-1:393401899741:rule/LabStack-52553f06-5082-48-GblLabMonitoringmonitorin-F9Giq3btHJ6z"
            ],
            "Effect": "Deny"
        },
        {
            "Action": "lambda:PutProvisionedConcurrencyConfig",
            "Resource": "*",
            "Effect": "Deny"
        }
    ]
}
```

trust policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```
   
4. Click to expand Additional Configurations.
5. Scroll down to Enable VPC.



### Step 7


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/e3260cdb-9ecc-47bb-a7d6-504ac03d8961" />

Concept
You can configure a Lambda function to connect to private subnets in a virtual private cloud (VPC) to access private resources, such as databases, cache instances, or internal services. 
 
1. To connect the Lambda function to your VPC, choose the check box to select Enable VPC.
2. For VPC, choose the VPC with Name: LabVPC.



### Step 8

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/a91cf0c2-a385-40f8-ab22-fda9664f4988" />

Concept
When you connect a Lambda function to a VPC, Lambda assigns your function to a Hyperplane ENI (elastic network interface) for each subnet in your function's VPC configuration. There is no additional charge for using a VPC or a Hyperplane ENI. 

You can connect your Lambda function to private subnets in your VPC to access private AWS resources. We also recommend that you connect to more than one subnet in your VPC.
 
1. For Subnets, in the search box, type: `lambda`

2. Choose the check boxes to select the two subnet names that contain lambda_subnet.

- You are selecting lambda_subnetSubnet1 and lambda_subnetSubnet2.

### Step 9

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/42fbe063-9bed-471f-b52a-c4d13c9d77a7" />

1. For Security groups, choose the check box to select the default VPC security group.
2. Click Create function.

- The function might take 5–10 minutes to be created.

### Step 10

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/1f36ad72-fc08-4fb2-a4c1-487f7fa0d8c2" />

Concept
AWS Lambda layers provide a convenient way to package libraries and other dependencies that you can use with your Lambda functions. Using layers reduces the size of uploaded deployment archives and helps you deploy your code faster.
 
1. In the success alert, review the message.

- You might need to wait for the success alert to appear.

2. To add a layer to your Lambda function, in the Function overview section, click Layers.

### Step 11

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/ef4f18d5-3675-4f56-9ff5-bd28ec35ca1d" />

Concept
A layer is a .zip file archive that can contain additional code or data. A layer can contain libraries, a custom runtime, data, or configuration files. Layers promote code sharing and separation of responsibilities so that you can iterate faster on writing business logic.
 
1. In the Layers section, click Add a layer.

### Step 12


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/3bc40591-a834-4acc-9d9a-0400c33579cc" />
 
1. For Layer source, choose Custom layers.
2. For Custom layers, choose the layer name that starts with labfunctionlayer.
3. For Version, choose a version.

- Only one version should be available in the list. The available version number might not be 1, depending on the number of times you created the Lambda function with this custom layer. Any version number will work.

4. Click Add.


### Step 13


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/c3bb5e93-7cb4-41e3-ae14-4e7b9e96f2e5" />

Concept
You can use layers only with AWS Lambda functions deployed as a .zip file archive. 
Step
13
1. In the Function overview section, next to Layers, review the number (1). 
	
- One layer is added.

2. On the Code tab, click Upload from to expand the dropdown menu.
3. Choose .zip file.


### Step 14


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/f8d0bd10-d4e8-4fd3-85ef-e55243b0602f" />

Concept
You can also upload an updated .zip file to change the function code. If the code is larger than 3 MB, or if you need to add libraries, or for languages that the editor doesn't support (Java, Go, C#), you must upload your function code as a .zip archive. If the .zip file archive is smaller than 50 MB, you can upload the .zip file archive from your local machine. If the file is larger than 50 MB, upload the file to the function from an Amazon S3 bucket.
Step
14
1. In the pop-up box, click Upload.
2. Choose the lambda_security_code.zip file that you downloaded at the beginning of the lab.
3. Click Save.


### Step 15


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9bfe8004-440d-427f-87c9-15f632d2722c" />

Concept
Using the code editor on the AWS Lambda console, you can write, test, and view the execution results of your Lambda function code.
 
1. In the success alert, review the message.
2. Scroll down to the Code source section.

```python
"""
This lambda function loads data to the mysql test server.
The Lambda function also gets custom queries against the database.
The results is then saved to the S3 Bucket.
"""

import json
import sys
import pymysql
import os
import csv
import os
import boto3
import base64
from botocore.exceptions import ClientError
import logging
import db

# It is a good practice to use proper logging.
# Here we are using the logging module of python.
# https://docs.python.org/3/library/logging.html

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize class DB
database = db.DB()

# Declare the secrets manager arn and region
secret_name = os.environ['secret_arn']
region_name = "us-east-1"

def lambda_handler(event, context):
    
    # Call the get_secrets() function to get data from Secrets manager
    result = get_secret()
    result = json.loads(result)
    
    # Retreive RDS details from the Secrets manager response
    host = result.get('host')
    port = result.get('port')
    username = result.get('username')
    password = result.get('password')
    db_name = result.get('dbname')
    
    logger.info(f"host = {host}")
    logger.info(f"username = {username}")
    logger.info(f"password = {password}") 
    logger.info(f"db_name={db_name}") 
    
###### START: Uncomment below section to test RDS connection ######
    
    # try:
    #     conn = pymysql.connect(host=host, user=username, passwd=password, db=db_name, connect_timeout=5)
    #     cursor = conn.cursor()
    # except pymysql.MySQLError as e:
    #     logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    #     logger.error(e)
    #     sys.exit()
    
    # logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
    
    # cursor.execute("SHOW TABLES LIKE 'talentpool'")
    # result = cursor.fetchone()
    
    # if not result:
    #     load_data()
    # else:
    #     custom_query(host,username,password,db_name,port)

###### END: Uncomment section to test RDS connection ######

def custom_query(host,username,password,db_name,port):
    
    custom_sql = """
        SELECT * FROM talentpool
        WHERE occupation LIKE 'Toxicologist';
        """
    
    custom_query = database.query(custom_sql,host,username,password,db_name,port)
    logger.info(custom_query)
    
    with open('/tmp/results.json', 'w') as f:
        f.write(json.dumps(custom_query))
    filename = '/tmp/results.json'

    # Boto3 - s3 Client
    # You will use the client to upload files to S3 bucket
    # More Info: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_object
    
###### START: Uncomment below section to test S3 connection ######

    # s3 = boto3.client('s3')
    
    # try:
    #     response = s3.upload_file(
    #         filename,
    #         Bucket='Enter_your_bucket_name',
    #         Key='results.json'
    #         )
    #     logger.info('File Uploaded Successfully')
    # except ClientError as e:
    #     logging.error(e)
    #     logger.info('File Not Uploaded')
        
###### End: Uncomment above section to test S3 connection ######    
    
def load_data():
    """
    This code loads the data in the database server using the data.csv file.
    The data.csv file contains the sample data generated using Faker.
    """
    
    # Call the get_secrets() function to get data from Secrets manager
    result = get_secret()
    result = json.loads(result)
    
    # Retreive RDS details from the Secrets manager response
    host = result.get('host')
    port = result.get('port')
    username = result.get('username')
    password = result.get('password')
    db_name = result.get('dbname')
    
    # Read the data.csv file
    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        talentpool = list(reader)
    
    # Define the SQL statement to create table
    talentpool_sql = """
        create table talentpool (
        first_name nvarchar(200),
        last_name nvarchar(200),
        occupation nvarchar(200),
        company nvarchar(200),
        dob nvarchar(200),
        country nvarchar(200)
        );
        """
    
    # Initiate connection to database    
    conn = pymysql.connect(host=host, user=username, passwd=password, db=db_name, connect_timeout=5)
    cursor = conn.cursor()

    logger.info("Creating talentpool table")
    conn.cursor().execute(talentpool_sql)
    conn.commit()
    logger.info('done')

    logger.info("Populating talentpool table")
    for item in talentpool:
        sql = """INSERT INTO `talentpool` (first_name,last_name,occupation,company,dob,country) VALUES (%s,%s,%s,%s,%s,%s);"""
        try:
            with conn.cursor() as cur:
                cur.execute(sql, (item["first_name"], item["last_name"], item["occupation"], item['company'], item['dob'],
                                  item["country"]))
                conn.commit()
        except:
            logger.info(("Unexpected error! ", sys.exc_info()))
            sys.exit("Error!")
    
    conn.close()

def get_secret():
    """
    This code retreives RDS details from the secrets manager.
    """
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    
    # Getting the secrets from secrets manager
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        return get_secret_value_response.get('SecretString')
    except ClientError as e:
        print(e)

```



### Step 16

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/837da2ab-661d-412d-856d-c7043e8ebf11" />


Concept
Using AWS Secrets Manager, you can replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically. 
Step
16
1. In the lambda_function.py code, review lines 30 and 31.

- The Lambda function retrieves the database credentials from AWS Secrets Manager. 
- The value of the `secret_name` is read from the environment variable with the key, secret_arn.

### Step 17

Concept
Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. You can use Secrets Manager to rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. 
 
1. In the top navigation bar search box, type: secrets

2. In the search results, under Services, click Secrets Manager.


### Step 18

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/bf75b900-3d85-44ce-96a2-1f25466bb58b" />

Concept
In Secrets Manager, a secret consists of secret information, the secret value, plus metadata about the secret.
 
1. In the Secrets section, click the secret name that starts with DatabaseSecret.



### Step 19


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/25836c4b-67aa-4e10-9130-86f70c4f543d" />

1. In the Secret details section, under Secret ARN, click the copy icon to copy the provided ARN, and then paste it in the text editor of your choice on your device. 

- You will use this ARN in later steps.
  
`arn:aws:secretsmanager:us-east-1:393401899741:secret:DatabaseSecret3B817195-ALVfkA3kzjTT-Yt3cNx`


2. In the Secret value section, click Retrieve secret value.

### Step 20


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/650427f1-018a-4dd8-8f46-fde3e86c22c6" />


Concept
You can store a secret in key-value pairs, or choose the Plaintext tab and enter the secret in any format. A secret value can be a string or binary. 
 
1. In the Secret value section, review the key-value pairs of secrets stored in Secrets Manager.

- Secrets Manager stores the database credentials, such as the database login username and password, database name, and database engine.

2. Scroll down to Sample code.

### Step 21


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/3f3daab7-43f3-46b2-8a1d-ec35096d43c6" />

Concept
Secrets Manager provides code samples to call Secrets Manager APIs for retrieving the secret programmatically.
 
1. In the Sample code section, review the provided code samples.

- The code samples are written in different programming languages to retrieve the secret in your application.

```python
# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "DatabaseSecret3B817195-ALVfkA3kzjTT"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']

    # Your code goes here.

```

### Step 22

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/60481e43-82b3-426d-b349-cfb7044ef564" />


Concept
After you create the Lambda function, you can configure settings for many function capabilities and options, such as permissions, environment variables, tags, and layers.

1. Navigate to the labFunction page on the AWS Lambda console.

- Remember, on the top navigation bar, you can use the Services search box (or click Services) to navigate to a different service console.

2.  Click the Configuration tab.

### Step 23

 <img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/70c66843-4eb2-42cf-8c91-0a0d3b3db3e5" />

1. On the Configuration tab, click General configuration.
2. Click Edit.


### Step 24

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/4e3bef75-783b-49b7-943e-5098b9ec06aa" />

Concept
You can set the timeout value for a function to any value up to 15 minutes. 
When the specified timeout is reached, Lambda terminates execution of your Lambda function. As a best practice, you should set the timeout value based on your expected execution time to prevent your function from running longer than intended.
 
1. For Timeout, in the first (min) text box, type:

3

- This will increase the timeout value.

2. Click Save.

### Step 25

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/49aacd7b-bfbb-494e-b5c7-a7e40045eaa8" />

Concept
Environment variables are key-value pairs that Lambda sets in the execution environment.
 
1. In the success alert, review the message.
2. Click the Configuration tab.
3. Click Environment variables.
4. Click Edit.

### Step 26

 
1. Click Add environment variable.

### Step 27

 
 <img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/6f048f60-fbda-4203-8070-c225186d3336" />

1. For Key, type:

secret_arn

2. For Value, paste the Secrets Manager ARN that you copied in an earlier step.
3. Click Save.

### Step 28


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/a26bfecc-5c09-44b1-9de3-dfd6561a6fb4" />

1. In the success alert, review the message.
2. Click the Code tab.
3. In the left explorer pane, under Deploy, click Test.
4. On the Select test event dropdown menu, choose Create new test event.


### Step 29

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/0f7c0a01-0445-410b-a15c-38aa1bde9313" />

Concept
Using the AWS Lambda console, you can test your function locally. 
You can configure up to 10 test events per function. You can test your Lambda function in the console by invoking your function with a test event. 
A test event is a JSON input to your function. 
 
1. For Event name, type a name that you like, such as testEvent. 
2. Click Save.


### Step 30

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/4ea7cadf-2e96-455a-81b2-10fdcb142e95" />

1. After the test event is successfully saved, click Invoke.
2. On the Output tab, review Status: Succeeded.
3. Under Function Logs, review the logs. 

- Database credentials were successfully retrieved  from AWS Secrets Manager.

4. To close the Output window, click the X.
5. To close the Create new test event tab, click the X.




### Step 31

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/ffea2b13-58bf-4c42-b918-a6c857819a4c" />

1. In the lambda_function code, review lines 53–69. 

- This code block tests the Amazon Relational Database Service (Amazon RDS) connection with your Lambda function, using the retrieved database username and password. 
- The Amazon RDS database "talentpool" includes first_name, last_name, occupation, company, date of birth, and country of people. 

2. Review lines 73–78.

- This code block defines a custom query, which finds all the records with Toxicologist as occupation in the database. 


### Step 32

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/be1260cf-d5bd-4165-a24d-59990aa890c2" />


Concept
Amazon Relational Database Service (Amazon RDS) is a collection of managed services that helps you set up, operate, and scale databases in the cloud. 
Using Amazon RDS, you can also run your database instances in a VPC so that you can isolate your database instances and connect to your existing IT infrastructure through an industry-standard encrypted IPsec VPN.
 
1. To uncomment the code block of lines 53–69, select (highlight) lines 53–69.
2. On the Code source navigation bar, click the three horizontal lines to expand the dropdown menu.
3. Choose Edit.
4. To uncomment the code block, choose Toggle Line Comment.

- Be sure to keep the indentations in the Python code blocks.

5. To save the updated function, click Deploy.

### Step 33

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/229a58bf-e5a6-4135-8ab4-336c41027be7" />

1. In the success alert, review the message.
2. To test the Amazon RDS connection, under Test Events, click testEvent and then click the Run arrow.

- The test might take 1–2 minutes because it has to load the data.

### Step 34

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/ffea0b41-a5f8-4d9f-8cda-02894d0c05cf" />

Concept
Lambda executes your function on your behalf. The handler in your Lambda function receives and then processes the sample event. The Execution results section displays the execution status as succeeded and also displays the function execution results returned by the return statement.
 
1. On the Output tab, review Status: Succeeded.
2. Under Function Logs, review the logs. 

- The Lambda function has successfully created and populated the talentpool table in the Amazon RDS database.

### Step 35

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/c9cc657b-3092-411f-a010-6f200308e84c" />

Concept
Amazon Virtual Private Cloud (Amazon VPC) helps you launch AWS resources into a virtual network that you've defined. 
This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS. You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways.
 
1. Navigate to the Amazon VPC console.

- You can type "vpc" in the top navigation bar search box.

2. In the left navigation pane, click Endpoints.
3. In the Endpoints section, click Create endpoint.


### Step 36

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/e1a4973d-d997-41d6-baf9-080ed1d192d3" />

Concept
A VPC endpoint enables connections between a VPC and supported services without requiring that you use an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.
 
1. In the Endpoint settings section, for Name tag, type a name that you like.
2. To search for Amazon S3 services, in the Services section search box, type:

s3

3. Choose Service Name = com.amazonaws.us-east-1.s3.

### Step 37

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/b4074b8b-8f8d-4607-8374-a3c9a9202ed7" />

Concept
Gateway endpoints provide reliable connectivity to Amazon Simple Storage Service (Amazon S3) and Amazon DynamoDB without requiring an internet gateway or a NAT device for your VPC. Gateway endpoints do not enable AWS PrivateLink.

With an interface VPC endpoint (interface endpoint), you can connect to services powered by AWS PrivateLink. The interface endpoints are network interfaces that serve as an entry point for traffic that is destined to an AWS service.
 
1. Choose the service name that has a Type of Gateway.
2. For VPC, choose the VPC name that includes (LabVPC).
3. Scroll down to Route tables.

### Step 38

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9770b6a6-c9e9-40ad-b74f-188430b788d6" />


Concept
Route tables control the routing of traffic between your VPC and another service. When you create a gateway endpoint, you select the VPC route tables for the subnets that you enable. There is no additional charge for using gateway VPC endpoints.
 
1. In the Route tables section, choose the two check boxes to select the subnet names that include lambda_subnet:

- You are selecting Lab/LabVPC/lambda_subnetSubnet1 and Lab/LabVPC/lambda_subnetSubnet2.

2. Scroll down to the bottom of the page, and then click Create endpoint (not shown).

### Step 39
1. In the success alert, review the message.


### Step 40


<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/f090795a-4e49-44d2-8f60-b4daeb827ff3" />

Concept
Amazon Simple Storage Service (Amazon S3) is an object storage service offering industry-leading scalability, data availability, security, and performance.
 
1. Navigate to the Amazon S3 console.
2. In the General purpose buckets section, click the bucket name that ends with -practice. 

- You will use this S3 bucket for this practice lab.
- You will use another S3 bucket, with a name ending with -diy, in the upcoming DIY section of this solution.

### Step 41

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/6678a2ef-552b-43bf-adea-a5c6e214bc7f" />


1. Above the Objects tab, select (highlight) and copy the S3 bucket name, and then paste it in your text editor.

- You will use this bucket name in a later step. 

2. On the Objects tab, review to ensure that the S3 bucket is currently empty.


### Step 42

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/fd331f45-8aea-4e0f-875b-068daa0b642c" />

1. Navigate to the labFunction page on the AWS Lambda console.
2. To view the lambda_function.py code, scroll down to the Code source section.

### Step 43

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/3fddb297-bd57-4960-95b0-e83dea295828" />


Concept
You can query data from Amazon RDS, and then export the results directly into files stored in an S3 bucket. 
 
1. In the lambda_function code, review the code block of lines 93–104. 

- The code tests the Lambda connection with Amazon S3. 
- If successful, File Uploaded Successfully is printed in the log.

2. On line 98, to replace Enter_your_bucket_name, paste the -practice S3 bucket name that you copied in an earlier step.
3. Uncomment lines 93–104.

- You practiced uncommenting lines in an earlier step.
- Be sure to keep the indentations in the Python code blocks.

4. To save the updated function, click Deploy.


### Step 44

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/1b9fd62c-9a6a-4e92-b62c-cdd26f2185d5" />


 
1. In the success alert, review the message.
2. To test the Amazon S3 connection, hover over testEvent and click the Run arrow.



### Step 45

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/9032ed68-ef7d-4894-9915-805859dc8755" />

 
1. On the Execution results tab, review Status: Succeeded. 
2. Under Function Logs, review the logs.

- The query results of the Amazon RDS were successfully uploaded to the S3 bucket.

### Step 46

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/4c9e02cb-a31f-45ef-8308-0dad254dcf34" />


Concept
To store your data in Amazon S3, you work with resources known as buckets and objects. A bucket is a container for objects. An object is a file and any metadata that describes that file.
 
1. Navigate to the Amazon S3 console.
2. In the General purpose buckets section, click the bucket name that ends with -practice.


### Step 47

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/e230008c-adf3-4280-8fdf-df861ab110f4" />

1. On the Objects tab, click the results.json file.

- This new object was added to the S3 bucket.
- If you do not see the file, click the refresh icon.


### Step 48

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/2e79a8f4-31b6-45ab-9f05-af1537ff7810" />

Concept
After the object is in the bucket, you can open it, download it, and move it. When you no longer need an object or a bucket, you can clean up your resources.
 
1. To download the Amazon RDS queried results to your device, click Download.


### Step 49

<img width="1147" height="740" alt="image" src="https://github.com/user-attachments/assets/1f766f15-983d-4aa1-b6f6-0279aaa63fbc" />

1. On your device, open the downloaded results.json file with a text editor or JSON viewer, and then review the Amazon RDS queried results.

- The results include the people in the database with Toxicologist as their occupation.


### DIY 

DIY Goals
Update the custom Amazon RDS query in the lambda_function code to find all people records with Data Scientist as the occupation.
Run the Lambda function test event again.
Make sure the new query results are placed into the provided DIY S3 bucket. 


<img width="749" height="397" alt="image" src="https://github.com/user-attachments/assets/3403d2bc-9548-4f06-ad7e-ef7330d8608e" />

Solution Validation Method
Our test service will validate that your specified S3 bucket received the file that contains the results of the new custom query of the Amazon RDS database. 

Hint: 
1. Update the lambda_function code as follows:
- Change the custom query in Amazon RDS to find records with Data Scientist as the occupation.
- Change the S3 bucket name to the one that ends with -diy. Check the buckets in the Amazon S3 console. This DIY bucket was provisioned for you.

2. The same gateway VPC endpoint that you created in the practice lab can be used here. There is no need to create another endpoint.
