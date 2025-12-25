 
https://skillbuilder.aws/learn/531665225Z/auditing-amazon-simple-storage-service-amazon-s3-security


# Introduction to auditing Amazon S3 security

> You were recently hired to lead the security team at an airline company. Your manager approaches you to discuss the current situation at the company.
> There have been a lot of articles in the news recently about companies who had data leak incidents. We hired you because we need to be proactive about our security.
> We need you to implement an auditing strategy for the company to detect any potential security weaknesses and prevent incidents.
> First, focus on securing our data that we store in Amazon S3. We have terabytes of data and we need to make sure it is safe.


## Why is auditing important?

It is important to always be aware of and prepared for security risks that can emerge in your AWS infrastructure. Auditing your infrastructure gives you insights into your AWS account. You can monitor changes, and detect and proactively respond to any security weaknesses and incidents.

**By auditing, you can detect WHO made WHAT changes, WHEN the changes were made, and HOW the changes were made.**


## What should you audit?

Think about what security weaknesses can materialize in your company's AWS infrastructure; specifically, your Amazon S3 resources. 
How can you prevent those weaknesses from happening or be notified if they happen?


> What security risks do we have when it comes to Amazon S3? What should we be auditing?
> Access to S3 buckets.
> While we have some public S3 buckets, most are private. We already set them to private. What more can we do?
> Remember access can change and new S3 buckets can be created. We want to audit these changes and be notified of any public or outside access.
> Yes. It would be disastrous if our private S3 buckets became public. That could compromise our customer data or our internal airline files.
> What other security risks do we have when it comes to Amazon S3?
> Settings in your Amazon S3 account.
> What type of settings?
> Our S3 buckets have settings such as versioning which can be turned on and off.
>  Yes.  Many of our S3 buckets have versioning to protect against accidental deletion of data and it would not be good if versioning got disabled.
> What other security risks do we have when it comes to Amazon S3?
> Actions taken within Amazon S3.
> What sort of actions can be taken in our Amazon S3 account?
> Items can be written to S3 buckets or even full S3 buckets can be deleted.
> Our company is already doing an excellent job of having least access privilege permissions set up so only the right people have access. Is all this auditing necessary?
> Yes. While this is all precautionary, it is important to be prepared. Mistakes happen.
> It is important to be prepared for mistakes.
> Whether improper actions in your account are done accidentally or intentionally, you want to have the proper auditing and monitoring in place. Scroll down to learn more about auditing Amazon S3.


### AWS tools for auditing Amazon S3

AWS has tools that help you audit permissions, settings, and actions. 

#### AWS CloudTrail and Amazon S3 server access logs
Log actions that happen in your Amazon S3 account.
Analyze your logs for patterns and insights using Amazon CloudWatch and Amazon Athena.

#### AWS Config
Check that you have the intended and recommended settings in your Amazon S3 account (such as logging, blocked public access, and versioning).
As these rules are found, automatically get notifications with Amazon Simple Notification Service (Amazon SNS) or automatically take remediation actions using AWS Lambda.

#### AWS IAM Access Analyzer
Receive alerts for questionable access to your Amazon S3 buckets and remediate the issue by removing access.

#### AWS Trusted Advisor
Ensure your account follows AWS recommended best practices.



# Introduction to logging with Amazon S3

>Based on your insights your manager agrees the company should start collecting detailed records of requests made to the company's Amazon S3 buckets. She wants to learn more information on logging.
> What sort of details do we want to get from these logs?
> We want to get records of actions taken by users or roles in Amazon S3.
> It seems like we will be logging a lot of data. Can we then search through the log records to filter them or identify trends?
> Yes.
>Great. Let's get that set up!

<img width="800" src="https://github.com/user-attachments/assets/8d0c68f8-09d4-4660-9513-93891a46414c" />
Help your manager collect log records of Amazon S3 requests and then search through the logs to gain insights.


## Logging with Amazon S3

When you use logging with Amazon S3, you can record actions taken by users, and services on your Amazon S3 resources. You can then use the log records for auditing and compliance purposes.

You can log Amazon S3 actions using server access logs or AWS CloudTrail logs.

### Introduction to server access logging

Server access logging is a mechanism that provides detailed records for requests made to an S3 bucket. 

Server access logging is disabled by default. Enable server access logging to start receiving logs. 
Logs are delivered on a best effort basis in terms of how complete they are and how timely they are, but this is not guaranteed. 
Log records are generally delivered within a few hours and it is rare to lose log records. 
There is no charge for enabling access logging, nor for PUT operations for log files. 
You are only charged for storage of the logs and for GET operations on the files. 
You can use object lifecycle management to minimize storage costs.

https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html#LogDeliveryBestEffort
https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html


### Why use server access logging

Actions taken on your S3 bucket get logged with server access logging into another S3 bucket.
Server access logging helps keep your account secure with access auditing, and gives you visibility into **object-level operations** on your data in Amazon S3. 
Server access logging can also provide insights into user and application behaviors as well as provide clarity around your Amazon S3 bill.

<img width="1403" height="626" alt="image" src="https://github.com/user-attachments/assets/1b4301b3-f7e7-4048-b253-5101d544b6bd" />

## Introduction to AWS CloudTrail

AWS CloudTrail is a service that provides records of actions taken by a user, role, or service in your AWS Account.
You can use CloudTrail to audit your account by logging and monitoring all activity. You can also use CloudTrail to detect unusual activity in your account. 


<img width="800" src="https://github.com/user-attachments/assets/d84144cb-e4b7-479c-9932-b244e6ac458b" />

### Why use CloudTrail for logging S3 actions

Actions taken on your S3 bucket get logged by CloudTrail and then the logs are put into another S3 bucket.
Logging Amazon S3 actions with AWS CloudTrail helps keep your account secure by providing access auditing and analysis.


## Analyzing logs with Amazon Athena

### Introduction to Amazon Athena

Amazon Athena is an interactive query service that makes it easy for you to analyze data in Amazon S3 using standard SQL. 
You do not need to manage any infrastructure with Athena, and you pay only for the queries that you run.

### Why use Amazon Athena for analyzing logs

<img width="800" src="https://github.com/user-attachments/assets/5cb79d52-8aeb-4446-b8e4-e1e8f8cef27f" />

Actions taken on your S3 bucket get logged and then those logs can be analyzed by Amazon Athena.
Once you enable server access logs and store them in your target S3 bucket, you might want to analyze or search through them. 
Logs are not automatically analyzed by Amazon S3, and you might have a lot of data. To analyze all your Amazon S3 data, you can use Amazon Athena.


# Using server access logging


- Source bucket
  The S3 bucket that you are auditing and logging.


- Target bucket
  The target S3 bucket where log files are delivered.

- Log Delivery group
  Amazon S3 uses a special log delivery account, called the Log Delivery group, to write server access logs.
  The Log Delivery group requires write permissions to write the logs to the target S3 bucket.
  When you use the console to enable logging, AWS automatically updates the access control list (ACL) on the target bucket to grant write permissions to the Log Delivery group.


## Logs

Server access logs give you visibility into detailed object-level operations on your data. 
The log files are text files that have one line for each log record. Each log record represents one request and consists of space-delimited fields.

The fields relate to operation, requester, resource, and session information.


Example log record:

```
79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be awsexamplebucket1 [06/Feb/2019:00:00:38 +0000] 192.0.2.3 79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be 3E57427F3EXAMPLE REST.GET.VERSIONING - "GET /awsexamplebucket1?versioning HTTP/1.1" 200 - 113 - 7 - "-" "S3Console/0.4" - s9lzHYrFp76ZVxRcpX9+5cjAnEH2ROuNkd2BHfIa6UkFVdtjf5mKR3/eTPFvsiP/XV/VLi31234= SigV2 ECDHE-RSA-AES128-GCM-SHA256 AuthHeader awsexamplebucket1.s3.us-west-1.amazonaws.com TLSV1.1
```
https://docs.aws.amazon.com/AmazonS3/latest/userguide/LogFormat.html


### Enabling server access logging

- Step 1:

  <img width="800" src="https://github.com/user-attachments/assets/ca5635f3-b977-4ff4-aa87-c169773d8d61" />

  In the buckets list of the Amazon S3 console, select the bucket you would like to enable server access logging for.

- Step 2
  
  <img width="1095" height="329" alt="image" src="https://github.com/user-attachments/assets/c0de46bc-dae1-4c77-b2d1-6e4dc3bbd839" />

  Select Properties.

- Step 3
  <img width="800" src="https://github.com/user-attachments/assets/5775f3a8-4459-406f-8aa1-6db9bc410a10" />
  In the Server access logging section, select Edit.

- Step 4
  
  <img width="800" src="https://github.com/user-attachments/assets/baa321f5-69b0-41b5-a12d-50aa855129c0" />


  Under Server access logging, select Enable. Enter the name of the target S3 bucket you want to receive the log record objects. (The target bucket must be in the same account and Region as the source bucket and must not have a default retention period(opens in a new tab) configuration.)
  Select Save changes.

- After a few hours, you can see logs in your target bucket.


### Analyzing server access logs with Amazon Athena

To analyze server access logs with Amazon Athena, you need to create a structure. In Athena, you can create a database and then create a table that points to your target S3 bucket.

Once you have set up your table, you can use SQL commands in Athena to query your access logs.

<img width="1680" height="406" alt="image" src="https://github.com/user-attachments/assets/405a0d12-8582-4278-ab5e-67a44b281970" />


https://www.youtube.com/watch?v=NZ8P5imrfGU

https://repost.aws/knowledge-center/analyze-logs-athena


# Using AWS CloudTrail

## Components of CloudTrail

 
- Event
  A record of an activity in an AWS account.
  
  - Management events (control plane operations): Management operations performed on resources such as security or logging operations.
    Management events are enabled by default.
    
  - Data events (data plane operations): Resource operations performed on resources such as getting or putting objects in an S3 bucket.
    Data operations are disabled by default.

- Trail

  A trail enables CloudTrail to deliver log files to an Amazon S3 bucket, CloudWatch logs, and CloudWatch events.


- Log bucket

  The target S3 bucket where logs files are delivered.

## Logs

CloudTrail logs contain detailed API tracking for your operations. The log files are JSON files that can include records for each event.

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html

Example log record:

```json
"eventVersion": "1.08",
"userIdentity": {
    "type": "AssumedRole",
    "principalId": "ABCDEFGHIJKLMN1234567:AMSPortalWebsite+P-username",
    "arn": "arn:aws:sts:: 111222333444:assumed-role/MyAdminAccess/AMSPortalWebsite+P-username",
    "accountId": "111222333444",
    "accessKeyId": "ABCDEFGHIJKLMNOPQRST",
    "sessionContext": {
        "sessionIssuer": {
            "type": "Role",
            "principalId": "ABCDEFGHIJKLMN1234567",
            "arn": "arn:aws:iam:: 111222333444:role/MyAdminAccess",
            "accountId": "111222333444",
            "userName": "MyAdminAccess"
        },
        "webIdFederationData": {},
        "attributes": {
            "mfaAuthenticated": "false",
            "creationDate": "2020-12-03T13:33:46Z"
        }
    }
},
"eventTime": "2020-12-03T13:40:55Z",
"eventSource": "s3.amazonaws.com",
"eventName": "GetBucketVersioning",
"awsRegion": "us-east-1",
"sourceIPAddress": "72.0.2.3",
"userAgent": "[S3Console/0.4, aws-internal/3 aws-sdk-java/1.11.888 Linux/4.9.217-0.3.ac.206.84.332.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.262-b10 java/1.8.0_262 vendor/Oracle_Corporation]",
"requestParameters": {
    "bucketName": "testloggingbucket123",
    "Host": "s3.amazonaws.com",
    "versioning": ""
},
"responseElements": null,
"additionalEventData": {
    "SignatureVersion": "SigV4",
    "CipherSuite": "ECDHE-RSA-AES128-SHA",
    "bytesTransferredIn": 0,
    "AuthenticationMethod": "AuthHeader",
    "x-amz-id-2": "2s9K0NCVoGyvMhvlGeS+iQscrRVT3/1wSt5NFGAgOoYJPqkuFHnyvXOrA9PlU=",
    "bytesTransferredOut": 113
},
"requestID": "38B1A4190D231413",
"eventID": "13f1b7af-8770-4185-871f-ed554f9821dd",
"readOnly": true,
"resources": [
    {
        "accountId": "111222333444",
        "type": "AWS::S3::Bucket",
        "ARN": "arn:aws:s3:::testloggingbucket123"
    }
],
"eventType": "AwsApiCall",
"managementEvent": true,
"eventCategory": "Management",
"recipientAccountId": "111222333444",
"vpcEndpointId": "vpce-a11b22c"
```

## Amazon S3 API calls logged with CloudTrail

CloudTrail can log three different levels of Amazon S3 API calls:

- account-level actions

  These are actions in Amazon S3 that apply to the full account and not specific objects or buckets.
  For example, getting the PublicAccessBlock configuration for your account.


- bucket-level actions
  These are actions that are taken on S3 buckets.  For example, changing a bucket policy.


- object-level actions
  These are actions that are taken on objects in an Amazon S3 bucket. For example, putting, getting, or deleting objects.

By default, account-level and bucket-level actions are recorded with CloudTrail. CloudTrail logging for object-level actions can be enabled by configuring CloudTrail in the properties of the bucket.

https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudtrail-logging.html  

### Enabling object-level logging

- Step 1

  <img width="1302" height="694" alt="image" src="https://github.com/user-attachments/assets/f7d6f8f1-65d2-4395-ba5d-acf314ca98e0" />

  Open the AWS CloudTrail console and choose Dashboard from the navigation menu.

- Step 2

  Select Create trail.

- Step 3

  <img width="800" src="https://github.com/user-attachments/assets/82fe6d9e-075f-4fdb-84c2-76657d7ccbb5" />

  Choose trail attributes including a trail name and a target S3 bucket for the logs. Then select Next.

- Step 4

  <img width="800" src="https://github.com/user-attachments/assets/32e0458d-ef84-4c8b-897c-8e24e11eabc7" />

  Choose the log types you would like. For object-level logging, check the checkbox for Data events.

- Step 5


  <img width="864" height="550" alt="image" src="https://github.com/user-attachments/assets/96bfdd86-3549-4f79-ab56-21f0644d4d58" />

  Under Data events, choose S3 as the data event source. 
  You can leave data event logging on for all buckets, or choose an individual bucket.
  Select Next when you finish adding all your log events.

- Step 6

  Review your trail and select Create trail.


## Analyzing CloudTrail logs with Amazon CloudWatch

In addition to sending CloudTrail logs to Amazon S3, you can also send them to Amazon CloudWatch. 

Using CloudWatch, you can monitor the logs and take specific actions based on the logs, such as invoking an AWS Lambda function, or sending an SNS notification. 

You can also use CloudWatch to search through your logs to filter events based on specific criteria.  

<img width="800" src="https://github.com/user-attachments/assets/0dfd6822-31a6-42b1-ad16-1bfb2e2de172" />


https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SearchDataFilterPattern.html

CloudWatch log insights can also be used to query specific log fields to sort or filter your logs. This can help you visualize the data.

https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html


## Analyzing CloudTrail logs with Amazon Athena

Using Athena with CloudTrail logs is even easier than server access logs. With server access logs, you had to go to the Athena console to create a database and table, but with CloudTrail logging, Athena will automatically create a table for you.

To use Athena with CloudTrail logs, simply go to the CloudTrail event history and select Run advanced queries in Amazon Athena.

Once your table is set up in Amazon Athena, you can then query your logs.

<img width="1680" height="721" alt="image" src="https://github.com/user-attachments/assets/de15c770-c18e-40e3-a203-938b892e4b9e" />

https://www.youtube.com/watch?v=SSB5q0lAP0Q

https://repost.aws/knowledge-center/athena-tables-search-cloudtrail-logs

https://repost.aws/knowledge-center/find-cloudtrail-object-level-events


# Comparing server access logging to CloudTrail logging


While Amazon S3 server access logging and CloudTrail object-level logging might seem similar, there are a few distinct differences.

CloudTrail logging is more detailed and structured than server access logging. CloudTrail logging is more advanced, but also has additional costs.

Both have events and fields that are not logged by the other.

<img width="1420" height="1372" alt="image" src="https://github.com/user-attachments/assets/823fb149-906c-4c5c-b578-8a61e85e60f8" />

 

| Server access logging | CloudTrail logging |
|---|---|
| Logs bucket and object operations using Amazon S3 APIs. | |
| Only enabled at the bucket level so actions such as creating or deleting a bucket will not be included. | Can be enabled to log at the account, bucket, and object level. |
| Logs lifecycle transitions, expirations, and restores. | |
| Logs keys in a batch delete operation. | |
| Contains fields for Object Size, Total Time, Turn-Around Time, and HTTP Referrer for log records. | |
| Logs authentication failures. | Does not deliver logs for requests that fail authentication, but includes logs for requests in which authorization fails and requests that are made by anonymous users. |
| Only gives a canonical user ID for the user. | Gives more user identity details such as username, ARN, and account ID. |
| Includes full payload details (such as the ACL definition). | |
| Able to log a subset of objects (prefix) instead of the full bucket. | |
| Able to filter what events should be logged. | |
