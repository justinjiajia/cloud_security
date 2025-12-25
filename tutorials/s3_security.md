<img width="1680" height="391" alt="image" src="https://github.com/user-attachments/assets/aea1ed00-de74-44a1-a824-c67712fa9c8d" />https://skillbuilder.aws/learn/531665225Z/auditing-amazon-simple-storage-service-amazon-s3-security


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


<img width="1000" src="https://github.com/user-attachments/assets/d84144cb-e4b7-479c-9932-b244e6ac458b" />

### Why use CloudTrail for logging S3 actions

Actions taken on your S3 bucket get logged by CloudTrail and then the logs are put into another S3 bucket.
Logging Amazon S3 actions with AWS CloudTrail helps keep your account secure by providing access auditing and analysis.


## Analyzing logs with Amazon Athena

### Introduction to Amazon Athena

Amazon Athena is an interactive query service that makes it easy for you to analyze data in Amazon S3 using standard SQL. 
You do not need to manage any infrastructure with Athena, and you pay only for the queries that you run.

### Why use Amazon Athena for analyzing logs

<img width="1680" height="406" alt="image" src="https://github.com/user-attachments/assets/5cb79d52-8aeb-4446-b8e4-e1e8f8cef27f" />

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

  <img width="1106" height="399" alt="image" src="https://github.com/user-attachments/assets/ca5635f3-b977-4ff4-aa87-c169773d8d61" />

  In the buckets list of the Amazon S3 console, select the bucket you would like to enable server access logging for. 
