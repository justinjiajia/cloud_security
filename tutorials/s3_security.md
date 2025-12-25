 
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


  <img width="800" src="https://github.com/user-attachments/assets/96bfdd86-3549-4f79-ab56-21f0644d4d58" />

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

<img width="800" src="https://github.com/user-attachments/assets/de15c770-c18e-40e3-a203-938b892e4b9e" />

https://www.youtube.com/watch?v=SSB5q0lAP0Q

https://repost.aws/knowledge-center/athena-tables-search-cloudtrail-logs

https://repost.aws/knowledge-center/find-cloudtrail-object-level-events


# Comparing server access logging to CloudTrail logging


While Amazon S3 server access logging and CloudTrail object-level logging might seem similar, there are a few distinct differences.

CloudTrail logging is more detailed and structured than server access logging. CloudTrail logging is more advanced, but also has additional costs.

Both have events and fields that are not logged by the other.

<img width="700" src="https://github.com/user-attachments/assets/823fb149-906c-4c5c-b578-8a61e85e60f8" />

 

| Server access logging | CloudTrail logging |
|---|---|
| Logs bucket and object operations using Amazon S3 APIs. | Logs bucket and object operations using Amazon S3 APIs.|
| Only enabled at the bucket level so actions such as creating or deleting a bucket will not be included. | Can be enabled to log at the account, bucket, and object level. |
| Logs lifecycle transitions, expirations, and restores. | |
| Logs keys in a batch delete operation. | |
| Contains fields for Object Size, Total Time, Turn-Around Time, and HTTP Referrer for log records. | |
| Logs authentication failures. | Does not deliver logs for requests that fail authentication, but includes logs for requests in which authorization fails and requests that are made by anonymous users. |
| | Includes full payload details (such as the ACL definition). |
| Only gives a canonical user ID for the user. | Gives more user identity details such as username, ARN, and account ID. |
| | Able to log a subset of objects (prefix) instead of the full bucket. |
|  |Able to filter what events should be logged. |



Take a look at the log record examples side-by-side. Both examples show the PutObject action being performed on the S3 bucket, testloggingbucket123.
 
#### Server access log record

```
3821464d42485af42e0bce69f7390662d957281dcc71ca434dc55abdb03928b0 testloggingbucket123 [03/Dec/2020:02:41:17 +0000] 72.0.2.3 arn:aws:sts::111222333444:assumed-role/MyAdminAccess/AMSPortalWebsite+P-username 4RDM0X7KAX9P6Y6Y REST.PUT.OBJECT testobject.rtf "PUT /testobject.rtf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLWVhc3QtMSJHMEUCIQD13q2bJkGeThL9Z3wXRk1Ai4mUiDbj%2B3BPOihaxnfeZAIgI%2Bk8MI6bdSwRF%2FDZB0KuzbZ628%2F9qg2QHd%2BrUqigMItP%2F%2F%2F2F%2F%2F%2F%2FARAAGgw1NjI4OTEwNjY0NTIiDKGWiTLvpbx7RfuU3yreAqwQQt57MlhKQCDSMY6slqQvwFDuz7tK5rn%2FZa4jlSdgwWAFblJwaLjPUaLSxgnP1C02IKc0%2B1kpqE1B5agUdEXiKglIMCc%2FLvSQa8PDF9BL5G9XtJElCJtr1bTZU0ESDW90BJqrqFKHOr7rsZnPVytbDoBG%2BU8%2BKHmT2F%2FmeY%2B3cu5H0%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20201203T024116Z&X-Amz-SignedHeaders=content-md5%3Bcontent-type%3Bhost%3Bx-amz-acl%3Bx-amz-storage-class&X-Amz-Expires=300&X-Amz-Credential=ASIAYGDXMBRKKBQFGWWY%2F20201203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX HTTP/1.1" 200 - - 353 44 17 "https://s3.console.aws.amazon.com/s3/upload/testloggingbucket123?region=us-east-1" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36" - 2s9K0NCVQz1oGy7yDvMhvlGeS+iQscrRVT3/1wSt5NFGAgOuoYBRJPqkuFHnyvXOrA9w3PltI8U= SigV4 ECDHE-RSA-AES128-GCM-SHA256 QueryString testloggingbucket123.s3.us-east-1.amazonaws.com TLSv1.2
```

#### CloudTrail log record

```json
"eventVersion":"1.07",

"userIdentity":{

    "type":"AssumedRole",

    "principalId":"ABCDEFGHIJKLMN1234567:AMSPortalWebsite+P-username",

    "arn":"arn:aws:sts::111222333444:assumed-role/MyAdminAccess/AMSPortalWebsite+P-username",

    "accountId":"111222333444", 

   "accessKeyId":"ABCDEFGHIJKLMNOPQRST",

    "sessionContext":{

        "sessionIssuer":{

            "type":"Role",

            "principalId":"ABCDEFGHIJKLMN1234567",

            "arn":"arn:aws:iam::111222333444:role/MyAdminAccess",

            "accountId":"111222333444","userName":"MyAdminAccess"

        },

        "attributes":{

            "creationDate":"2020-12-03T02:35:13Z",

            "mfaAuthenticated":"false"

        }

    }

},

"eventTime":"2020-12-03T02:41:17Z",

"eventSource":"s3.amazonaws.com",

"eventName":"PutObject",

"awsRegion":"us-east-1",

"sourceIPAddress":"72.0.2.3",

"userAgent":"[Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36]","requestParameters":{

    "X-Amz-Date":"20201203T024116Z",

    "bucketName":"testloggingbucket123",

    "X-Amz-Algorithm":"AWS4-HMAC-SHA256",

    "x-amz-acl":"private",

    "X-Amz-SignedHeaders":"content-md5;content-type;host;x-amz-acl;x-amz-storage-class",

    "Host":"testloggingbucket123.s3.us-east-1.amazonaws.com",

    "X-Amz-Expires":"300",

    "key":"testobject.rtf",

    "x-amz-storage-class":"STANDARD"

},

"responseElements":null,

"additionalEventData":{

    "SignatureVersion":"SigV4",

    "CipherSuite":"ECDHE-RSA-AES128-GCM-SHA256",

    "bytesTransferredIn":353.0,

    "AuthenticationMethod":"QueryString", 

   "x-amz-id-2":"2s9K0NCVoGyvMhvlGeS+iQscrRVT3/1wSt5NFGAgOoYJPqkuFHnyvXOrA9PlU=",

    "bytesTransferredOut":0.0

},

"requestID":"4RDM0X7KAX9P6Y6Y",

"eventID":"5cfae053-cb4f-46ff-b80b-a822000ff8de",

"readOnly":false,

"resources":[{

    "type":"AWS::S3::Object",

    "ARN":"arn:aws:s3:::testloggingbucket123/testobject.rtf"

    },

    {

    "accountId":"111222333444",

    "type":"AWS::S3::Bucket",

    "ARN":"arn:aws:s3:::testloggingbucket123"

}],

"eventType":"AwsApiCall",

"managementEvent":false,

"recipientAccountId":"111222333444",

"eventCategory":"Data"
```

<img width="710" height="539" alt="image" src="https://github.com/user-attachments/assets/7563fe49-c96b-48e4-be19-00b56753b778" />

<img width="699" height="447" alt="image" src="https://github.com/user-attachments/assets/f28dfa79-81ce-40f9-bb3a-4740e6399d4e" />


<img width="701" height="336" alt="image" src="https://github.com/user-attachments/assets/b0891114-81d1-4970-ad91-60898002989b" />

https://docs.aws.amazon.com/AmazonS3/latest/userguide/logging-with-S3.html


# Introduction to AWS Config

When auditing Amazon S3, logging is a great first step, but you might also want to be more proactive and get notified of certain changes to your Amazon S3 environment.

> These logs are great, but can I get email notifications if an S3 bucket is open to the public?
> Yes.
> Great. Let's get that set up!

<img width="800" src="https://github.com/user-attachments/assets/903d5da3-7c67-475d-b001-b15d66269ea9" />
Get your manager set up so she receives email notifications when Amazon S3 buckets are open to the public.

By the end of this section, you will: 

- Set up an AWS Config rule to watch your Amazon S3 buckets to see if they are open to the public.
- Use Amazon SNS to send email notifications to inform you of your non-compliant bucket.

## What is AWS Config?

AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. 

AWS Config continuously monitors and records your AWS resource configurations. This automates the evaluation of recorded configurations against the set configurations and notifies you when a configuration is not compliant. With AWS Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. This enables you to simplify compliance auditing, security analysis, change management, and operational troubleshooting.

## Why use AWS Config?

AWS Config enables you to evaluate your resources for compliance by evaluating your resources against your desired configuration. You can review changes to your configurations and your configuration history.

## Why use AWS Config to audit Amazon S3?

When using Amazon S3, you can keep track of your configurations using AWS Config. Examples include checking if logging is enabled for your buckets, checking for public access, checking if your buckets require SSL, and checking if versioning is enabled.


# Using AWS Config

## Components of an AWS Config implementation
 


- AWS Config rules

  AWS Config rules represent the ideal configuration settings of your AWS resources. AWS Config evaluates the current configuration settings of your AWS resources against the AWS Config rules. If an AWS resource does not match the AWS Config rule, it is marked as noncompliant.


 For more information, see [Evaluating Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html).
  
 AWS provides managed or predefined AWS Config rules that you can use. You can also create custom AWS Config rules.
 
 - Managed rules

   Predefined, customizable rules that AWS Config uses to evaluate whether your AWS resources comply with common best practices.
   See the documentation for an up to date [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html).

 - Custom rules
   Rules created by you that are watched by AWS Config. You use AWS Lambda functions to create logic that evaluates whether the AWS resources comply with your rule.
   To create a custom rule, see [Getting Started with Custom Rules for AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_getting-started.html).

- Resource type

  AWS Config rules act on AWS resources. When using AWS Config to audit Amazon S3, you can create rules for the following resources: 

  - S3 buckets.
  - Account public access blocks.
  
  For an updated list of resources, see [Supported Resource Types: Amazon S3](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#amazonsimplestorageservice).
 


- Amazon S3 target bucket

  AWS Config stores configuration details in an Amazon S3 bucket that you specify. Configuration history files contain details about the resources that changed. Each file includes resources of one type, such as Amazon Elastic Compute Cloud (Amazon EC2) instances or Amazon Elastic Block Store (Amazon EBS) volumes.

  In order for AWS Config to send configuration details to the S3 bucket, you must give the bucket the proper permissions. For details on the required permissions, see [Permissions for the Amazon S3 Bucket](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html).


- Amazon SNS topic

  You can choose to have AWS Config send configuration changes and notifications to an Amazon SNS topic.
  For an updated list of notifications that AWS Config can send to Amazon SNS,
  see [Notifications that AWS Config Sends to an Amazon SNS topic](https://docs.aws.amazon.com/config/latest/developerguide/notifications-for-AWS-Config.html).


- IAM role

  When using AWS Config you will also need to create IAM roles to give AWS Config the appropriate permissions.
  With permissions enabled, AWS Config can take the desired actions such as writing to the target S3 bucket and publishing to the SNS topic.
  To learn more, see [Permissions for the IAM Role Assigned to AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html).


- Remediation actions

  AWS Config allows you to remediate noncompliant resources that are evaluated by AWS Config Rules using AWS Systems Manager Automation documents.

  AWS Config provides a set of managed automation documents with remediation actions. You can also create and associate custom automation documents with AWS Config rules.

  To learn more about remediation actions, see [Remediating Noncompliant AWS Resources by AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html).


## AWS Config managed rules for Amazon S3

- s3-bucket-logging-enabled: Checks whether logging is enabled for your S3 buckets.
- s3-bucket-public-read-prohibited: Checks that your Amazon S3 buckets do not allow public read access.
- s3-bucket-public-write-prohibited: Checks that your Amazon S3 buckets do not allow public write access.
- s3-bucket-ssl-requests-only: Checks whether S3 buckets have policies that require requests to use Secure Socket Layer (SSL).
- s3-bucket-versioning-enabled: Checks whether versioning is enabled for your S3 buckets. Optionally, the rule checks whether MFA delete is enabled for your S3 buckets.

https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html


- Step 1: On the AWS Config console, select Settings.
- Step 2: Specify the resource types that you want AWS Config to record.
- Step 3: Set up an Amazon S3 bucket to receive a configuration snapshot on the request and configuration history.

  <img width="638" height="151" alt="image" src="https://github.com/user-attachments/assets/03b80186-8c2e-423d-8df4-2844252922f8" />

- Step 4: Set up an Amazon Simple Notification Service (Amazon SNS) topic to send configuration stream notifications.

  <img width="553" height="175" alt="image" src="https://github.com/user-attachments/assets/673dc344-f038-4a1f-98f6-6b2724b5ac03" />

- Step 5: Grant AWS Config the permissions it needs to access the Amazon S3 bucket and the SNS topic. Select Next.
  <img width="809" height="125" alt="image" src="https://github.com/user-attachments/assets/fe757fec-7949-4a1b-a388-0c6680c3df1a" />

- Step 6:  Specify the rules that you want AWS Config to use to evaluate compliance information for the recorded resource types. Select Next.

  <img width="1095" height="394" alt="image" src="https://github.com/user-attachments/assets/ba7e91cc-a2dc-4af4-acff-34429e1dce36" />


- Review your choices and then select Confirm.

## Identifying buckets open to the public using AWS Config


  <img width="800" src="https://github.com/user-attachments/assets/56140e62-4540-4425-a4a9-1cc534e2b893" />

  https://aws.amazon.com/blogs/security/how-to-use-aws-config-to-monitor-for-and-respond-to-amazon-s3-buckets-allowing-public-access/

# Introduction to AWS IAM Access Analyzer

You now know how to get notified of public access to your Amazon S3 buckets, but you might also want to get notified of S3 buckets that get accessed from other AWS accounts.

>Your manager is excited to see she now receives email notifications for public buckets and other security concerns.
> These notifications for public access are great, but is it possible other sorts of unintended access can be given to S3 buckets?
>Yes. S3 buckets can be configured to allow access to other AWS accounts.
>Oh that wouldn't be good.
> Can I be notified of worrisome changes to permissions to S3 buckets?
>Yes.
>Great. Let's get that set up!


 <img width="1680" height="424" alt="image" src="https://github.com/user-attachments/assets/ff2f1a4f-fe26-4158-a74b-4f74e1477488" />

By the end of this section, you will be able to:
- Set up AWS IAM Access Analyzer for Amazon S3.


- Use Access Analyzer to review your policies, block public access, and receive an S3 report.


## What is Access Analyzer?

AWS IAM Access Analyzer helps you identify the resources in your organization and accounts that are shared with an external entity. This lets you identify unintended access to your resources and data. For each instance of a resource that is shared outside of your account, Access Analyzer generates a finding. Findings include information about the access and the external principal that it is granted to. You can review findings to determine whether the access is intended and safe, or the access is unintended and poses a security risk.

## Why use Access Analyzer for monitoring access in Amazon S3?

Access Analyzer for S3 alerts you to S3 buckets that are configured to allow access to anyone on the internet or other AWS accounts, including AWS accounts outside of your organization. 

<img width="1680" height="389" alt="image" src="https://github.com/user-attachments/assets/12b25308-967d-48ab-a3fa-3dc10893647a" />


# Using Access Analyzer for Amazon S3

## Requirements for using Access Analyzer

In order to use AWS IAM Access Analyzer, you need to:
- Enable Access Analyzer.
- Give Access Analyzer the proper permissions.

### Enabling Access Analyzer

To enable Access Analyzer, you must create an analyzer in each Region in which you want to monitor access to your resources.

- Step 1: In the AWS IAM console, under Access reports, choose Access analyzer .

  <img width="915" height="602" alt="image" src="https://github.com/user-attachments/assets/4662db7a-0eed-456f-bda9-c156c1a6d709" />

  <img width="740" height="499" alt="image" src="https://github.com/user-attachments/assets/378a8dad-715a-4cae-b44f-10dfdd6df645" />

  

- Step 2: Choose Create analyzer.
  <img width="1139" height="594" alt="image" src="https://github.com/user-attachments/assets/01641eed-e72a-4003-82cf-f377ad676cba" />

- Step 3: On the Create analyzer page, confirm that the Region displayed is the Region where you want to enable Access Analyzer. 

  <img width="1227" height="553" alt="image" src="https://github.com/user-attachments/assets/259262df-af3c-4cfe-af24-1e7b991916da" />

- Step 4

  <img width="846" height="711" alt="image" src="https://github.com/user-attachments/assets/621e14a8-96e5-41ce-b96d-95b5deef37d9" />

  Enter a name for the analyzer.
  Choose the zone of trust for the analyzer. This can be your account or your organization (if your account is the Organizations management account or delegated administrator account).
  Add any tags that you want to apply to the analyzer.
  Choose Create Analyzer.

  Note: When you create an analyzer to enable Access Analyzer, a service-linked role named AWSServiceRoleForAccessAnalyzer is created in your account (or if enabled for the organization, the service-linked role is added to each account of your organization).  


### IAM permissions for Access Analyzer

To successfully configure and use Access Analyzer, the account you use must be granted the required permissions.
To access and use all Access Analyzer features, you can apply the IAMAccessAnalyzerFullAccess managed policy to the account.

https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#access-analyzer-permissions
https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html


## Access Analyzer findings

For each public or shared bucket, you receive findings into the source and level of public or shared access. 
Each time a resource-based policy is modified, Access Analyzer analyzes the policy. If the updated policy shares a resource that is already identified in a finding, but with different permissions or conditions, a new finding is generated for that instance of the resource sharing. If the access in the first finding is removed, that finding is updated to Resolved status.

 

### Components of an Access Analyzer for S3 finding
 

- Bucket name: The resource (S3 bucket) of the finding.

- Discovered by Access Analyzer: When Access Analyzer for S3 discovered the public or shared bucket access.
- Shared through: How the bucket is shared—through a bucket policy, a bucket ACL, or an access point policy. A bucket can be shared through both policies and ACLs.


- Status: The status of the bucket finding. Access Analyzer for S3 displays findings for all public and shared buckets.  
  - Active ‐ Finding has not been reviewed.
  - Archived ‐ Finding has been reviewed and confirmed as intended.
  - Resolved - Finding has been reviewed and unintended access has been resolved. (Does not show up in Amazon S3 console).
  - All ‐ All findings for buckets that are public or shared with other AWS accounts, including AWS accounts outside of your organization.


- Access level

  Access permissions granted for the bucket:
  - List ‐ List resources.
  - Read ‐ Read but not edit resource contents and attributes.
  - Write ‐ Create, delete, or modify resources.
  - Permissions ‐ Grant or modify resource permissions.
  - Tagging ‐ Update tags associated with the resource.
 


## Reviewing access policies

When using Access Analyzer to analyze Amazon S3 resources, findings can be found both in the AWS IAM console under Access Analyzer, and in the Amazon S3 console under Access Analyzer for S3. Resolved findings will not show up in the Amazon S3 console, but you can view them in the AWS IAM console.

You should review all active findings in your account to determine whether the permissions are intended. 

Select a finding to view the permissions that are causing the alert.

If the permissions in the finding are intended, you can archive the finding by selecting Archive. If not, you should resolve the issue by editing or removing the inappropriate permissions from the bucket ACL, bucket policy, or access point policy. 

<img width="600" src="https://github.com/user-attachments/assets/f753e608-f17b-4677-a8d8-1a4b2c6b38a4" />

- Bucket ACL

  
  - In the Amazon S3 console, select the bucket you would like to update.
  - Select Permissions.
  
  - Select Edit in the Access Control List box.
  
  - Review your bucket ACL, and make changes as required.
    For more information, see [How do I set ACL bucket permissions?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/set-bucket-permissions.html).

- Bucket policy

  - In the Amazon S3 console, select the bucket you would like to update.
  - Select Permissions.

  - Select Edit in the Bucket policy box.
  
  - Review or change your bucket policy as required.
  
    For more information, see [How do I add an S3 Bucket policy?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-bucket-policy.html).



- Access point policy
  
  - In the Amazon S3 console, select the bucket you would like to update.
  - Select Access points.
  
  - Choose the access point name.
  
  - Select Edit policy.
  
  - Review or change access as required.
  
    For more information, see [Managing and using Amazon S3 access points](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/access-points-manage.html).

Once you update the resource, the status for the finding will update to Resolved. Once you get to zero active findings, you know that any new active findings that are generated are from a recent change in your environment.

## Blocking public access

Access Analyzer for Amazon S3(opens in a new tab) also lets you quickly and easily block all public access for an S3 bucket. In the Amazon S3 console, select Access analyzer for S3 under Dashboards. There, choose the S3 bucket and then select Block all public access.

<img width="1550" height="335" alt="image" src="https://github.com/user-attachments/assets/32dff06c-e187-424f-b636-ce76d64bd95c" />

https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-analyzer.html#blocking-public-access-access-analyzer


> Your manager sees that you set up Access Analyzer for S3. Now she needs you to teach her how to take action on these findings.
> I see I have a new finding from Access Analyzer for S3. It is informing me that one of our partner airlines has access to this S3 bucket. The partner is supposed to have access. What should I do?
> Archive the finding.
> This other finding shows an S3 bucket that is public. This is very bad and should not be publicly accessible. How do I fix it?
> Look at the finding to see where this public access is shared through and what the access level is. Then go to the permissions and update them.
> Once I fix the permissions, how do I make sure the finding isn't still in my active findings list?
> No need to do anything. Access Analyzer will mark it as resolved once the permissions are changed.
> Great!
> Great work! Your manager now understands how to monitor the Access Analyzer for S3 findings. Scroll down to learn more about handling Amazon S3 findings with Access Analyzer.


## Handling Amazon S3 findings with Access Analyzer

The following video walks through enabling Access Analyzer. You will also learn about reviewing, archiving, resolving findings, and blocking public access.

https://www.youtube.com/watch?v=5ipJtR7uKUs


## Downloading an S3 report

You can use Access Analyzer for Amazon S3 to download a CSV report of your bucket findings.

https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-analyzer.html#downloading-bucket-report-s3


# Introduction to AWS Trusted Advisor

You now know how to log events from your Amazon S3 account and how to be notified of potential security risks to your Amazon S3 buckets. The next step would be to make sure your Amazon S3 account compares well against AWS best practice checks.

> Your manager is very happy about all the proactive steps you have taken to keep the airline's Amazon S3 data secure.
> You have done great work keeping us up to date with best practices. Is there a way to ensure that we keep up with AWS best practices in the future?
> Yes.
> Great. Let's get that set up!


<img width="1680" height="877" alt="image" src="https://github.com/user-attachments/assets/1c6448c7-8363-44d3-9029-03cba16094e6" />
Help your manager stay up to date with AWS recommendations and compare your AWS configuration to those recommendations.


By the end of this section, you will be able to:
-  Use AWS Trusted Advisor to scan your configuration and give you recommendations.
- Integrate Trusted Advisor with Amazon CloudWatch to detect and react to changes.

## What is Trusted Advisor?

AWS Trusted Advisor is an online tool that gives you guidance to ensure you are following AWS best practices from security, performance, fault tolerance, service limits, and cost optimization perspectives.

AWS Trusted Advisor draws upon best practices learned from serving hundreds of thousands of AWS customers. Trusted Advisor inspects your AWS environment, and makes recommendations when opportunities exist to save money, improve system availability and performance, or help close security gaps.

Trusted Advisor checks compare your AWS configuration to best practices related to:

- Cost optimization
- Security
- Fault tolerance
- Performance
- Service limits

## Why use Trusted Advisor?


<img width="1680" height="877" alt="image" src="https://github.com/user-attachments/assets/69072980-534a-47bd-8b48-15d19663a623" />

Trusted Advisor scans your configuration and provides recommendations based on best practices, from security, performance, and cost savings perspectives. The tool contains a dashboard with findings that give you detailed descriptions of how to improve your AWS configuration.

You can also sign up for weekly email notifications summarizing your saving estimates and the current status of your Trusted Advisor checks. Sign up for these notifications by navigating to the Trusted Advisor console and selecting Preferences.
 

## Integration of Trusted Advisor with CloudWatch

You can use Amazon CloudWatch Events to detect and react to changes in the status of Trusted Advisor checks. Then, based on the rules that you create, CloudWatch Events invokes one or more target actions when a check status changes to the value you specify in a rule. Depending on the type of status change, you might want to send notifications, capture status information, take corrective action, initiate events, or take other actions.

You can select the following types of targets when using CloudWatch Events as a part of your Trusted Advisor workflow:

- AWS Lambda functions
- Amazon Kinesis streams
- Amazon Simple Queue Service (Amazon SQS) queues
- Built-in targets (CloudWatch alarm actions)
- Amazon Simple Notification Service (Amazon SNS) topics

https://docs.aws.amazon.com/awssupport/latest/user/cloudwatch-events-ta.html

# Using Trusted Advisor for Amazon S3
AWS Trusted Advisor has best practice checks that are specific to Amazon S3.
 

- Amazon S3 bucket permissions

  Amazon S3 bucket permissions check for buckets in Amazon S3 that have open access permissions.
  Bucket permissions that grant List access to everyone can result in higher than expected charges if objects in the bucket are listed by unintended users at a high frequency. Bucket permissions that grant Upload/Delete access to everyone create potential security vulnerabilities by allowing anyone to add, modify, or remove items in a bucket. This check examines explicit bucket permissions and associated bucket policies that might override the bucket permissions.


- Amazon S3 bucket logging

  Amazon S3 bucket logging checks the logging configuration of Amazon S3 buckets.

  When server access logging is enabled, detailed access logs are delivered hourly to a bucket that you choose. An access log record contains details about each request, such as the request type, the resources specified in the request, and the time and date the request was processed. By default, bucket logging is not enabled. You should enable logging if you want to perform security audits or learn more about users and usage patterns.


- Amazon S3 bucket versioning

  Amazon S3 bucket versioning checks for Amazon S3 buckets that do not have versioning enabled, or have versioning suspended.

  When versioning is enabled, you can easily recover from both unintended user actions and application failures. Versioning allows you to preserve, retrieve, and restore any version of any object stored in a bucket. You can use lifecycle rules to manage all versions of your objects as well as their associated costs by automatically archiving objects to the Glacier storage class or removing them after a specified time period. You can also choose to require multi-factor authentication (MFA) for any object deletions or configuration changes to your buckets.

https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html

> Our Amazon S3 account is now being audited for changes and notifying me of questionable behavior. You also helped the team learn about how to compare our AWS account to recommended best practices.


# Knowledge

1. Which tools will allow you to log object-level operations in your Amazon S3 buckets? (Select TWO)

- Amazon Athena
- Amazon CloudWatch
- AWS CloudTrail
- AWS Config
- AWS IAM Access Analyzer
- AWS Trusted Advisor
  
Both Amazon S3 server access logging and AWS CloudTrail allow you to collect object-level logs.


2. What tool lets you send an Amazon SNS notification or invoke an AWS Lambda function based on your AWS CloudTrail logs?

- Amazon Athena
- Amazon CloudWatch
- AWS Config
- AWS IAM Access Analyzer
 
You can send CloudTrail logs to Amazon CloudWatch. Using CloudWatch you can monitor the logs and take specific actions based on the logs such as invoking a Lambda function, or sending an SNS notification.

3. Which logging tool guarantees log delivery?

- server access logging
- AWS CloudTrail

 
AWS CloudTrail logging guarantees log delivery. Server access logging does not guarantee the completeness nor timeliness of your logs, but it is rare to lose log records.

4. Which tools check if your Amazon S3 buckets allow public read access? (Select THREE)

- Amazon CloudWatch
 
- AWS Config
 
- AWS CloudTrail
 
- AWS IAM Access Analyzer
 
- AWS Trusted Advisor
 
- Server access logs
 
 
AWS Config has a managed rule s3-bucket-public-read-prohibited that checks whether your S3 buckets allow public read access.
AWS IAM Access Analyzer checks your bucket policy, bucket ACL, and access point policy for public access.
AWS Trusted Advisor has an Amazon S3 Bucket Permissions check for public access permissions for your S3 buckets.


5. When Access Analyzer findings show an unintended permission and you fix it, what status does the finding display?

- Active
 
- Archived
 
- Resolved
 
- Unintended
 
- Intended
 
 
When Access Analyzer first has a new finding the status is Active. Once you fix the finding, the status changes to Resolved.


6. Which tool checks that your logging is enabled for Amazon S3 buckets? (Select TWO)

- Amazon CloudWatch
- AWS Config
 
- AWS CloudTrail
 
- AWS IAM Access Analyzer
 
- AWS Trusted Advisor
 
- Server access logs

 
AWS Config has a managed rule s3-bucket-logging-enabled that checks whether your Amazon S3 buckets have logging enabled.

AWS Trusted Advisor's Amazon S3 Bucket Logging checks the logging configuration of your Amazon S3 bucket.



7. Which tool lets you analyze your server access logs to find insights?

- Amazon Athena
 
- Amazon CloudWatch
 
- AWS CloudTrail
 
- AWS Config
 
- AWS IAM Access Analyzer
 
Amazon Athena lets you analyze server access logs.

