https://skillbuilder.aws/learn/S8ZA3HS5C9/aws-security-best-practices-monitoring-and-alerting

# Course Introduction
 

Threats are continuously changing. For many organizations, they are increasing in volume and severity as operations become more and more dependent on digital resources. Addressing these threats is important to an organization's ability to operate, and in some cases is a legal requirement. Security controls can be organized and implemented in a variety of ways.

This course will equip you to use a standards-based approach to security so that you can benefit from the knowledge and experience of a wide range of industry best practices to secure your workload. 

 
After completing this training, you will be able to:

Configure service and application logging.
Analyze logs, findings, and metrics centrally.
Automate response to events as much as possible.

 
## Using best practices in your organization

Imagine that you work for AnyCompany, a growing startup. AnyCompany and their workload hosted in AWS are expanding quickly. AnyCompany recently had a third-party perform a security audit, to ensure they are meeting compliance and regulatory requirements, as well as protecting their customer’s data. The auditors specialize in cloud security; they have aligned their findings to the AWS well-architected framework, controls from the National Institute of Standards (NIST) Cyber Security Framework (CSF), and provided recommendations based on best practices.

Based on this premise, consider the learning objectives in this course as a guide for using best practices to strengthen the organization's security posture.

# Introduction to Monitoring and Alerting
 
> If all vulnerabilities could be discovered and mitigated in advance of their exploitation, then detective controls would not be needed.
> However, in reality this is difficult, if not impossible (given zero-day vulnerabilities, for example). You must be able to detect threats that evade preventive controls.
> AWS provides tools and features so you can see what's happening within your account and across your organization.
> Before looking at the lifecycle of logging and alerting, you should familiarize yourself with core AWS services. This course will also discuss key features of related services that can enhance visibility and responses: Amazon GuardDuty, AWS Security Hub, and AWS Trusted Advisor.


## Basic service introduction

### Amazon CloudWatch

CloudWatch is a service that provides visibility and monitoring of activities performed on or by AWS services and resources. This includes many aspects of services and systems that facilitate reporting on their health and performance. This information also provides valuable security insights.

CloudWatch collects data from cloud resources in the form of logs or events and can create visualizations of this information to help you monitor performance. With this visibility, you can detect spikes or anomalies within your infrastructure and determine which actions to take. You can create and set alarms to provide notifications or even initiate an automated response action when metric thresholds are exceeded.


#### Collect and store logs

 

With the Amazon CloudWatch Logs service, you can collect and store logs from your resources, applications, and services in near real time. There are three main categories of logs:

- Vended logs: These are natively published by AWS services on your behalf. Currently, Amazon VPC Flow Logs and Amazon Route 53 logs are the two supported types.
- Logs published by AWS services: Currently, more than 30 AWS services publish logs to CloudWatch. They include Amazon API Gateway, AWS Lambda, CloudTrail, and many others.
- Custom logs: These are logs from your own application and on-premises resources.

CloudWatch Logs Agents are available for Linux and Windows operating systems (within or outside AWS).

- Export data to Amazon Simple Storage Service (Amazon S3) for analytics.
- Stream to Amazon OpenSearch Service (successor to Amazon Elasticsearch Service) or Lambda.

### AWS CloudTrail

CloudTrail facilitates governance, compliance, operational auditing, and risk auditing.

CloudTrail provides event history of activity, including actions taken through the AWS Management Console, AWS Software Development Kits (SDKs), command line tools, and other AWS services by logging the application programming interface (API) calls that are made by AWS services.

This visibility into your AWS account activity is a key aspect of security and operational best practices. 
You can use CloudTrail to view, search, download, archive, analyze, and respond to account activity across your AWS infrastructure. 
A CloudTrail record captures critical information (who, what, when, where, and how) needed to correlate events and discover bad actors and actions associated with security incidents. 

### VPC Flow Logs

With VPC Flow Logs, you can capture information about the Internet Protocol (IP) traffic traversing network interfaces within your virtual private cloud (VPC). 
Flow log data can be published to CloudWatch Logs or Amazon S3. After you create a flow log, you can retrieve and view its data in the chosen destination.

A key benefit to flow log data is that it is collected outside the path of your network traffic and therefore does not affect network throughput or latency. 
You can create or delete flow logs without any risk of impact to network performance.

---

# Logging Network Traffic
 

## Using VPC Flow Logs

VPC Flow Logs can be turned on per elastic network interface, per subnet, or per VPC* to help you with several tasks, such as:

- Diagnosing overly restrictive security group rules

- Monitoring the traffic that is reaching your instance

- Determining the direction of the traffic to and from the network interfaces

* When turned on on an Amazon Virtual Private Cloud (Amazon VPC) or subnet, VPC Flow Logs allows logging for all interfaces in the VPC or subnet.

Turning on VPC Flow Logs on an entire VPC or subnet may generate a very large volume of logs, therefore you should:

- Filter for desired results, based on need.
- Think before turning on VPC Flow Logs on an entire VPC or subnet. (Will you use it?)

Flow logs can be sent to an Amazon S3 bucket or CloudWatch Logs, where you set up alarms or visualize the data. 

- Use S3 Lifecycle policies to manage large amounts of log data by moving logs to the appropriate storage tier or expiring log files that are no longer needed.
- Query logs in Amazon S3 using Amazon Athena or analyze data with CloudWatch Logs with Insights.

## Flow log configuration example

In this example:

- A flow log (fl-aaa) has been created to capture accepted traffic for the network interface for instance A1. The log records are published to an Amazon S3 bucket. 
- A second flow log is created to capture all traffic for subnet B. These flow log records are published to CloudWatch Logs. The flow log (fl-bbb) captures traffic for all network interfaces in subnet B. 
- There are no flow logs that capture traffic for instance A2's network interface.
 


<img width="800" alt="Example topology for this log configuration scenario" src="https://github.com/user-attachments/assets/e600838d-c6fa-4a3b-941f-5d62fd17e93c" />


## Anatomy of a log

Each network interface that produces a flow log is assigned its own unique log stream. Although flow logs do not capture real-time log streams for your network interfaces, they can still provide valuable information for security monitoring, alerting, or troubleshooting. To understand what to log and how to apply the information to meet your needs, you must be familiar with what a flow log captures and how you can filter or specify certain traffic to collect or log. There are two formats that logs can be collected and stored in: 

- Default format
- Custom format

### Default format

With the default format, the flow log records include version 2 fields, in the order shown in the following example log. Later versions added additional fields that can be used with custom logs. You cannot customize or change the default format. To capture any additional fields or a different subset of the default fields, you must specify a custom format. 

### Example log

The following example log shows Remote Desktop Protocol (RDP) traffic (destination port 3389, TCP protocol 6) sent to network interface eni-1235b8ca123456789 
in account 123456789010 was rejected. You can refer to the Amazon Virtual Private Cloud User Guide for information about the remaining fields.

<img width="1680" height="194" alt="image" src="https://github.com/user-attachments/assets/ec826f4c-951e-4824-96d0-e43519dca32b" />

<img width="898" height="121" alt="image" src="https://github.com/user-attachments/assets/dd048d6a-d58a-4e14-92dc-4ef7b9804c3b" />

1. `account-id`

   The AWS account ID of the owner of the source network interface for which traffic is recorded.
   If the network interface is created by an AWS service (for example, when creating a VPC endpoint or Network Load Balancer), the record may display unknown for this field.
 
2. `interface-id`

   The ID of the network interface for which the traffic is recorded.
 
3. `srcaddr`

   The source address for incoming traffic, or the IPv4 or IPv6 address of the network interface for outgoing traffic on the network interface.
   The IPv4 address of the network interface is always its private IPv4 address.
 

5. `dataddr`

   The destination address for outgoing traffic, or the IPv4 or IPv6 address of the network interface for incoming traffic on the network interface.
   The IPv4 address of the network interface is always its private IPv4 address.

6. `srcport`: The source port of the traffic

7. `dstport`: The destination port of the traffic

8. `protocol`

   The Internet Assigned Numbers Authority (IANA) protocol number of the traffic.
 

9. `action`

   The action that is associated with the traffic:
   - ACCEPT — The recorded traffic was permitted by the security groups and network access control lists (network ACLs).
   - REJECT — The recorded traffic was not permitted by the security groups or network ACLs.
 

### Custom format

With a custom format, you can specify which fields are included in the flow log records and in which order. This way, you can create flow logs that are specific to your needs and omit fields that are not relevant. Using a custom format can simplify log processing and the need to extract specific information from the published flow logs. You can specify any number of the available flow log fields, but you must specify at least one. 

Additional fields include a variety of information such as Region, az-id, tcp-flags (set), traffic-path, flow-direction and more. 
VPC Flow Logs do not provide payload visibility into traffic.


## Exempt traffic (not logged)

Not all traffic traversing your network is captured by VPC Flow Logs. It is important to understand what types of traffic are not captured.


Attention: Flow logs do not capture all traffic. Ensure that you understand the types of traffic that a flow log will not capture.


- Traffic generated by instances when they contact the Amazon Domain Name System (DNS) server; if you use your own DNS server, then all traffic to that DNS server is logged

- Traffic generated by a Windows instance for Amazon Windows license activation

- Traffic to and from 169.254.169.254 for instance metadata

- Traffic to and from 169.254.169.123 for the Amazon Time Sync Service

- DHCP traffic

- Mirrored traffic

- Traffic to the reserved IP address for the default VPC router

- Traffic between an endpoint network interface and a Network Load Balancer network interface


## Publishing logs

Flow logs can be published to Amazon S3 or CloudWatch Logs. See a comparison below of how flow log records are published to either of these destinations.
   
- Amazon S3

  - Publish log flow data into an existing Amazon S3 bucket you specify. 
  - Flow log records for each monitored network interface are published to log file objects stored in the bucket. 
  - Flow log capturing data for a VPC publish flow log records for all of the network interfaces in the selected VPC. 

- AWS CloudWatch Logs

  - Publish flow log data into a log group.
  - Each network interface has a unique log stream in the log group. 
  - Log streams contain flow log records. You can create multiple flow logs that publish data to the same log group. 
  - If the same network interface is present in one or more flow logs in the same log group, it has one combined log stream. 


## Traffic Mirroring

Traffic Mirroring is an Amazon Virtual Private Cloud (Amazon VPC) feature that you can use to copy network traffic from an elastic network interface of Amazon EC2 instances and then send it to outside security and monitoring appliances.

These appliances can be deployed as individual instances or as a fleet of instances behind a Network Load Balancer with a User Datagram Protocol listener. Traffic Mirroring supports filters and packet truncation so that you only extract traffic of interest to monitor using monitoring tools of your choice.

- Detect network and security anomalies—You can extract traffic of interest from any workload in a VPC and route it to the detection tools of your choice. You can detect and respond to attacks more quickly than is possible with traditional log-based tools.

- Implement compliance and security controls—Many AWS services are already verified to meet regulatory and compliance requirements like those that mandate monitoring and logging.
  For more information, see the [Services in Scope](https://aws.amazon.com/compliance/services-in-scope) page.


### Reasons for mirroring traffic

Traffic Mirroring is another way to perform monitoring. From a security perspective, you can use this to deploy out-of-band intrusion detection and analysis tools. 
Prior to the availability of traffic monitoring, there was no way to look at our traffic as a bit-by-bit copy. The only options were to route traffic through another instance, which essentially changes some of the information within the traffic, or deploy local collection agents on instances. 

Target intrusion detection devices or analysis tools can be deployed as individual instances or as a fleet of instances behind a Network Load Balancer. 
Traffic mirroring also supports filters and packet truncation, so you only extract only traffic of interest.

Note: When turned on, the AWS GuardDuty Service performs some network threat and anomaly detection using the VPC Flow Log data, but it is limited based on the contents of a flow log. Remember, flow logs do not capture an exact copy of traffic. 
Application layer data, for example, is not considered in a VPC Flow log. GuardDuty is still an important tool for layering defenses, providing anomaly detection on AWS API calls through AWS CloudTrail analysis.


You can mirror traffic from any EC2 instance that is powered by the AWS Nitro system.

#### Components:

- Target—The destination for mirrored traffic. A single instance or appliance or a load balancer connecting to a fleet.
- Filter—A set of rules that defines the traffic that is of interest. Traffic that will be copied in the traffic mirror session.
- Session—An entity that describes Traffic Mirroring from a source to a target using filters.

  <img width="800" src="https://github.com/user-attachments/assets/9167c18e-40b7-4b14-977e-11b12692ef50" />
  A simple topology and arrangement of the components in a scenario where Traffic Mirroring is configured.

Monitoring network traffic can be accomplished with AWS Security services or solutions from third-party vendors.  
Third-party solutions require the use of Traffic Mirroring unlike AWS services.  

https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html


# Logging User and API Traffic


## CloudTrail workflow

CloudTrail is turned on on your AWS account when you create it. 
When activity occurs in your AWS account, that activity is recorded in a CloudTrail event. 
With CloudTrail being turned on by default, you can log into CloudTrail and review your Event History. 
In this view, not only do you see the last 7 days of events, you can also select a specific event to view more information about it. 

To access your CloudTrail log files directly or archive them for auditing purposes past the 7-day window, you can create a specific trail and specify the S3 bucket for log file delivery. Creating a trail (as opposed to just viewing the default CloudTrail information) also lets you deliver events to CloudWatch Logs and CloudWatch Events for further action.


<img width="800" src="https://github.com/user-attachments/assets/7293fc07-cc18-4bea-ab1a-30637a2440cd" />

<img width="800" src="https://github.com/user-attachments/assets/c20d6eb1-2def-4b0d-ac31-d83100f111ac" />

1. Capture: Record activity in AWS services as CloudTrail events.
    
- CloudTrail captures actions made directly by the user or on behalf of the user by an AWS service.
- For example, an AWS CloudFormation CreateStack call can result in additional API calls to Amazon Elastic Compute Cloud (Amazon EC2),
  Amazon Elastic Block Store (Amazon EBS), or other services as required by the CloudFormation template.
- You can identify if the action was taken by an AWS service with the invokedby field in the CloudTrail event.

2. Store: CloudTrail delivers events to the CloudTrail console, Amazon S3 buckets, and, optionally, CloudWatch logs.    

3. Act: Use CloudWatch alarms and events to take action when important events are detected.
4. Review: View recent events in the CloudTrail console or analyze log files with Athena.
5. Support: Use the CloudTrail data collection to support compliance auditing, operational troubleshooting, security analysis, and automated compliance remediation.


## CloudTrail destinations

<img width="800" src="https://github.com/user-attachments/assets/a6c0b91b-f992-43a3-bb64-64d181a93c48" />

Example topology depicting various CloudTrail destination options
 

- CloudTrail records API calls in your account and delivers a log file to your selected destination (S3 bucket or CloudWatch Log).
- (Optional) Receive a notification when CloudTrail publishes new log files to your Amazon S3 bucket with Amazon Simple Notification Service (Amazon SNS). 
- Multiple Partners offer integrated solutions to analyze log files.

CloudTrail typically delivers logs within an average of about 15 minutes of an API call. This time is not guaranteed. 
Review the [AWS CloudTrail Service Level Agreement](http://aws.amazon.com/cloudtrail/sla) for more information.


## Security benefits and uses of CloudTrail logging


- Security analysis: Perform security analysis and detect user behavior patterns by ingesting CloudTrail API call history into log management and analytics solutions such as CloudWatch Logs, CloudWatch Events, Athena, Amazon OpenSearch Service, or another third-party solution.
  
- Compliance aid: CloudTrail facilitates compliance with internal policies and regulatory standards by providing a history of API calls in your AWS account.
  
- Automated remediation: Detect data exfiltration by collecting activity data on S3 objects through object-level API events recorded in CloudTrail. After data is collected, use other AWS services, such as Amazon EventBridge and Lambda, to initiate response procedures.

## Log dissection

In the following code block, select each numbered marker to learn more about each section.

<img width="800" src="https://github.com/user-attachments/assets/7dc59d37-0e54-4a08-9107-91042f0c8782" />
<img width="604" height="384" alt="image" src="https://github.com/user-attachments/assets/c0998f2d-acba-411d-8ef5-48fc945e85d0" />


1. Who made the API call?

   The information within the userIdentity entry provides information about who made the API call.

    ```json
    "userIdentity": {
    "type": "IAMUser",
    "principalid": "AIDAJDPLRKLG7UEXAMPLE",
    "arn": "arn:aws:iam::123456789012:user/Alice"
    }
    ```

2. When was the API call made?
   
   The eventTime entry displays the time of the event.
   
    ```json
    "eventTime": "2021-03-18T14:30:07Z"
    ```
    
3. What was the API call?

   The eventName entry provides information about what specific API call was made.
   
    ```json
    "eventName": "StartLogging"
    ```
4. Where was the API call issued from?

   The awsRegion and sourceIPAddress entries provide information about where the API call was initiated.
   
    ```json
    "awsRegion": "us-west-2",
    "sourceIPAddress": "72.21.198.64",
    ```
    
5. Which resources were accessed?

   The requestParameters provides information about which resources were used or acted upon through the API call.
   
    ```json
    "requestParameters": {
    "name": "Default"
    ```    

## CloudTrail configuration 

You can configure two types of trails:

- A trail that applies to one Region
- A trail that applies to all Regions
  - This is the default setting when you create a trail in the CloudTrail console.


## Best practice configuration


Best practice recommendations help strengthen your security posture.

You can configure CloudTrail to deliver log files from multiple Regions to a single S3 bucket for a single account. 
When you change an existing single-Region trail to log all Regions, CloudTrail logs events from all Regions in your account. 
As long as CloudTrail has permissions to write to the target S3 bucket, the bucket for a multi-Region trail does not have to be in the trail's home Region.

- Logging events in a single region is not recommended.

### Multi-Region configuration

To confirm that a trail applies to all Regions, the "IsMultiRegionTrail" element should show true in the CloudFormation template.

```json
{
    "IncludeGlobalServiceEvents": true, 
    "Name": "my-trail", 
    "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/my-trail", 
    "LogFileValidationEnabled": false, 
    "IsMultiRegionTrail": true, 
    "IsOrganizationTrail": false,
    "S3BucketName": "my-bucket"
}
```

<img width="600" src="https://github.com/user-attachments/assets/ab09dcf3-dd66-4264-ad4c-fa91cf136857" />

The Multi-region trail setting is enabled in the AWS Management Console, as shown in the image here.


### Single-Region trail

With CloudTrail, you can configure up to five trails per Region. 
A trail that is applied to all Regions would count as one trail per Region. 

If you have a Region-specific need, possibly based on compliance or regulatory requirements, 
you might want to create a separate trail in a Region that is specific to that Region and for a specific purpose only.


#### Example use case

World map showing existing AWS Regions and Regions coming soon
You may have workloads in different Regions that have different compliance requirements.

Imagine you have workloads in two Regions:

- Asia Pacific (Sydney)
- US East (N. Virginia)

<img width="1063" height="573" alt="image" src="https://github.com/user-attachments/assets/ce5efca1-0100-4749-87b4-61862e16b908" />

#### Distinct requirements

The workload located in US East (N/ Virginia) requires data residence in the US only based on a regulatory requirement. 
Furthermore, it requires a considerably longer retention period than the logs from any of your other Region's workloads.

- Create a trail in the Asia Pacific (Sydney) Region that applies to all AWS Regions. This trail also exists as a trail in the US East (N. Virginia) Region.
- Create a trail in the US East (N. Virginia) Region that applies to this Region only.

Analyzing, storing, or preparing log files is streamlined in this example for the US East (N. Virginia) Region by excluding logs from the other Region, 
where the requirements do not exist. 


### Centralizing CloudTrail logging

Many-to-one centralization

- From multiple Regions into one S3 bucket (all-Regions/one-account)
- From multiple accounts into one account's S3 bucket

Centralized CloudTrail logging is a generally recommended deployment to ensure integrity of logs. 
This is also the recommended deployment when an organization has a dedicated security team or managed service provider that will be exclusively handling the logs.

#### Centralizing logs without AWS Organizations

 
<img width="600" src="https://github.com/user-attachments/assets/26e6d66d-fb08-41cb-979a-8ad02a2691f5" />
Example topology depicting log centralization without using AWS Organizations


- Turn on CloudTrail for account 111111111111.
- Update the Amazon S3 bucket policy.
- Turn on CloudTrail for account 222222222222.
- Turn on CloudTrail for account 3333333333.

#### Centralizing logs through AWS Organizations

 <img width="1441" height="793" alt="image" src="https://github.com/user-attachments/assets/f40ecabe-7564-4332-8a0f-0f67e627cf9d" />

Example topology depicting log centralization using AWS Organizations

- Turn on CloudTrail once in the management account and have it applied to all AWS accounts.
- Log prefix changes from `"/AWSLogs/<accountID>/"` to `"/AWSLogs/<OrganizationID>/"`.
- There is no more updating of the bucket policy.

Watch out for multiple trails when turning on CloudTrail in an existing organization.


## AWS KMS encryption



You can encrypt CloudTrail logs through AWS Key Management Service (AWS KMS). 
By default, the files are encrypted using the S3 server-side encryption (SSE-S3) and then transparently decrypted when you read them. 
Optionally, you can specify an AWS KMS key (SSE-KMS) and it will be used to encrypt your log files. 


 <img width="800" src="https://github.com/user-attachments/assets/df915377-30f7-4d8d-8ff8-9708ec2d7fd6" />
<img width="828" height="343" alt="image" src="https://github.com/user-attachments/assets/8b8d2021-9512-405a-88de-8460895c8336" />

1. Create an AWS KMS key: Create or use an existing KMS key and apply key policy to allow AWS CloudTrail to encrypt and the SecOps engineers to decrypt the logs.

2. Specify the KMS key: Specify the key to CloudTrail.
3. Retrieve the object: Use the S3 GetObject API call to retrieve the desired log file.
4. Decrypt the log files: The SecOps engineer uses the key to decrypt the log files.



## Storing logs in Amazon S3

<img width="1493" height="531" alt="image" src="https://github.com/user-attachments/assets/37147a50-b1e1-433a-89de-9d1444cb1604" />

- A default descriptive folder structure makes it efficient to store log files from multiple accounts and Regions in the same S3 bucket.
- A detailed log file name helps identify the contents of the log file.
- A unique identifier in the file name prevents overwriting log files.


### Amazon S3 lifecycle management

You can define an S3 object lifecycle configuration rule to move log objects to different storage classes or delete them during their lifecycle, according to your security policy or regulatory requirements.

A lifecycle configuration comprises a set of rules with predefined actions that you want Amazon S3 to perform on objects during their lifetime.

- Transition actions

  define when objects transition to another Amazon S3 storage class. For example, move a log object to the Amazon S3 Infrequent Access storage class 30 days after creation or archive objects to the S3 Glacier storage class 1 year after creation.
  
- Expiration actions
  specify when the objects expire (are deleted) on your behalf.
  Note: This option deletes all objects in the bucket that meet the criteria regardless of the file type. When an object has been expired, it cannot be recovered.


#### Log storage lifecycle example

Let's assume the following rule has been set up for a target bucket used to hold CloudTrail logs:

<img width="1144" height="573" alt="image" src="https://github.com/user-attachments/assets/f6a4b607-ea99-47b1-8d5b-cb5074b3bcdf" />
The movement and retrieval options available for CloudTrail logs based on a defined S3 lifecycle

- Transition to Glacier 30 days after creation date.
- Expire 100 days after creation date.


 <img width="1437" height="290" alt="image" src="https://github.com/user-attachments/assets/9c4ef9be-9652-4096-adc8-839e4377717c" />
<img width="834" height="135" alt="image" src="https://github.com/user-attachments/assets/b52c8394-daa7-4409-9f89-c4d653482445" />

1. January 1
   Day 0: The object is uploaded to the target bucket on January 1 and the creation date is set to the same date.

2. January 31

   Day 30: 30 days after the creation date, on January 31, the lifecycle policy takes effect and the object's storage class transitions to Glacier.

3. April 11
   Day 100: 100 days after the object's creation, on April 11 (non-leap year), the lifecycle policy takes effect and the object expires.


### Integrity validation

To determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it, you can use CloudTrail log file integrity validation. Validated log files are invaluable in security and forensic investigations. 

This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing. You can use the AWS Command Line Interface (AWS CLI) to validate the files in the location where CloudTrail delivered them.

Once you turn on log file integrity validation, CloudTrail will start delivering digest files on an hourly basis to the same S3 bucket where you receive your CloudTrail log files, but with a different prefix.

CloudTrail log files are delivered to: `/optional_prefix/AWSLogs/AccountID/CloudTrail/*`

CloudTrail digest files are delivered to: `/optional_prefix/AWSLogs/AccountID/CloudTrail-Digest/*`


## CloudTrail best practices

 
- Turn on in all Regions

  - Unused Regions are tracked.
  - A single configuration step is required.

- Turn on log file validation
  - Log file integrity is ensured.
  - Validated log files are invaluable in security and forensic investigations.
  - Industry standard algorithms (SHA-256 or SHA-256 with RSA) are used.
  - CloudTrail starts delivering digest files on an hourly basis.
  - Digest files contain hash values of log files delivered, signed by CloudTrail.

- Encrypt logs
  - Log files are encrypted using SSE-S3 by default.
  - You can choose to encrypt using SSE-KMS.
  - Amazon S3 will decrypt on your behalf if your credentials have decrypt permissions.

- Integrate with CloudWatch Logs
  - A simple search is provided.
  - You can configure alerting on events.

- Centralize logs from all accounts
  - You can configure all accounts to send logs to a central security account.
  - There is a reduced risk for log tampering.
  - This can be achieved with AWS Organizations.
  - This can be combined with S3 cross-Region replication.

- Apply lifecycle policies to logging buckets
  - This limits the storage costs of log files.
  - This prevents manual pruning and the risk of altering of log files.
  - You can automate archiving of log files for long-term storage.
 
# Log Analytics
 
## Amazon OpenSearch Service for Analytics

Amazon OpenSearch Service streamlines the performance of interactive log analytics, real-time application monitoring, and more. 
You can use Amazon OpenSearch Service to centralize and analyze logs from disparate applications and systems across your network and enhance threat detection and incident management.

<img width="800" src="https://github.com/user-attachments/assets/855127be-f784-4708-9702-9e1ec1b48831" />

<img width="800" src="https://github.com/user-attachments/assets/f7a2de8e-3a7b-4928-acda-5af594414794" />

1. Capture, process, and load data into Amazon OpenSearch Service
2. OpenSearch dashboards and kibana are built in
3. Search, analyze, and visualize logs to get real-time insights

   
 OpenSearch Service is an open source, distributed search and analytics suite derived from Elasticsearch. Amazon OpenSearch Service offers the latest versions of OpenSearch, support for 19 versions of Elasticsearch (1.5 to 7.10 versions), and visualization capabilities powered by OpenSearch dashboards and Kibana (1.5 to 7.10 versions).

### Loading streaming data into Amazon OpenSearch Service

You can load streaming data into your Amazon OpenSearch Service from many different sources. Some sources, such as Amazon Kinesis Data Firehose and CloudWatch Logs, have built-in support for Amazon OpenSearch Service. Others, such as Amazon S3, Amazon Kinesis Data Streams, and Amazon DynamoDB, use Lambda functions as event handlers. The Lambda functions respond to new data by processing it and streaming it to your domain. See the [Amazon OpenSearch Service Developer Guide](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations.html) for more information about delivering streaming data to the OpenSearch service. 


### Amazon OpenSearch Service advantages

- Secure log analysis: The service offers encryption, authentication, authorization, and auditing features. It includes integrations with Active Directory, LDAP, SAML, Kerberos, JSON web tokens, and more. Amazon OpenSearch Service also provides fine-grained, role-based access control to indices, documents, and fields. 

- Compliance assistance

- Support for multiple query languages: Amazon OpenSearch Service supports domain-specific language (DSL), OpenSearch SQL, and OpenSearch Piped Processing Language (PPL).


- Integration with open source tools: OpenSearch and Kibana dashboards are built in. The service integrates with Logstach and allows direct access to Elasticsearch APIs and plugins such as Kuromoji, Phonetic Analysis, Ingest Processor Attachment, Ingest User Agent Processor, and Mapper Murmur3.


- Event monitoring and alerting: Use machine learning anomaly detection based on the Random Cut Forest (RCF) algorithm to automatically detect anomalies as your data is ingested. Combine this with alerting to send notifications to stakeholders. 


 ## OpenSearch and the ELK stack

The ELK stack fulfills a need in the log analytics space, providing a log management and analytics solution for gaining valuable insights on failure diagnosis, application performance, and infrastructure monitoring. 

Although you can choose to deploy and manage the ELK stack yourself with Apache 2.0 licensed versions of Elasticsearch and Kibana (up until version 7.10.2), there is an open source alternative to the ELK stack with OpenSearch, OpenSearch Dashboards, and Logstash through AWS.

 

- E = Elasticsearch

  Elasticsearch is a distributed search and analytics engine built on Apache Lucene. Support for various languages, high performance, and schema-free JSON documents makes Elasticsearch an ideal choice for various log analytics and search use cases.

  On January 21, 2021, Elastic NV announced that they would change their software licensing strategy. New versions are not open source and do not offer users the same freedoms.

  To ensure that the open source community and AWS users continue to have a secure, high-quality, fully open source search and analytics suite, AWS introduced the OpenSearch project, a community-driven, ALv2 licensed fork of open source Elasticsearch and Kibana.

- L = Logstash

  Logstash is an open source data ingestion tool to collect data from a variety of sources, transform it, and send it to your desired destination. With prebuilt filters and support for more than 200 plugins, Logstash users can ingest data regardless of the data source or type.

  The open source version of Logstash (Logstash OSS) provides a convenient way to use the bulk API to upload data into your Amazon OpenSearch Service domain. The service supports all standard Logstash input plugins, including the Amazon S3 input plugin.

  Amazon OpenSearch Service currently supports the following Logstash output plugins depending on your Logstash version, authentication method, and whether your domain is running Elasticsearch or OpenSearch:

  - Standard Elasticsearch plugin

  - logstash-output-amazon_es, which uses IAM credentials to sign and export Logstash events to OpenSearch Service

  - logstash-output-opensearch, which currently only supports basic authentication  


- K = Kibana
  Kibana is a data visualization and exploration tool for reviewing logs and events. Kibana offers straightforward interactive charts, prebuilt aggregations and filters, and geospatial support. It is the preferred choice for visualizing data stored in Elasticsearch.

  The open source successor for Kibana in OpenSearch is OpenSearch Dashboards. Amazon OpenSearch Service provides an installation of OpenSearch Dashboards with every Amazon OpenSearch Service domain.


### Partner solutions

In addition to the Amazon OpenSearch Service, there are numerous AWS Partners that offer services and products to enhance log processing and analytics. The AWS Partner Network (APN) and AWS Marketplace are robust resources for finding solutions to meet unique organizational requirements.

<img width="1680" height="745" alt="image" src="https://github.com/user-attachments/assets/48fd779e-1106-48ae-b424-649147184745" />
There are numerous Partner solutions available to enhance logging, analytics, and alerting, such as those depicted in the logos shown here.


# Visibility with Amazon CloudWatch
 
## Indicators of Compromise

Indicators of Compromise (IoC) are largely similar in cloud environments to how they are in traditional IT environments. Alerting on anomalies is helpful in recognizing potential malware, malicious activities, or other indicators of a compromised system. Some of the types of anomalies that may be recognized through the use of CloudWatch alarms include:

<img width="400" height="401" alt="image" src="https://github.com/user-attachments/assets/a6ff2f98-82ed-466f-ab71-51d261359b62" />
A malware infection often produces indicators of compromise in the affected system.


- Abnormal CPU utilization
- Significant or sudden increases in database reads
- HTML response sizes
- Mismatched port-application traffic
- Unusual DNS requests
- Unusual outbound network traffic
- Anomalies in privileged user account activity
- Geographical irregularities (source or destination of traffic)
- Unusually high traffic at irregular hours
- Multiple, repeated, or irregular log-in attempts

## CloudWatch Alarms

You can create two types of alarms: a metric alarm and a composite alarm. 

Metric alarms watch a single CloudWatch metric or the result of a math expression based on CloudWatch metrics. The alarm performs one or more actions based on the result, such as sending a notification to an Amazon SNS topic, performing an Amazon EC2 action or an Amazon EC2 Auto Scaling action, or creating an OpsItem or incident in AWS Systems Manager.

A metric alarm has the following possible states:

- OK – The metric or expression is within the defined threshold.

- ALARM – The metric or expression is outside the defined threshold.

- INSUFFICIENT_DATA – The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.

### Composite alarms

With composite alarms, you can combine multiple alarms into alarm hierarchies. This reduces alarm noise by initiating just once when multiple alarms are initiated at the same time. You can use this to provide an overall state for a grouping of resources such as an application, AWS Region, or Availability Zone.

> Currently, composite alarms only support an action of notifying SNS topics. 


<img width="400" height="401" alt="image" src="https://github.com/user-attachments/assets/e785502b-29c6-473e-b97e-23cb6f53b9e0" />
> Attention: False positives and false negatives can be issues with logging. Composite alarms can help balance what you capture to reduce false positives and can catch false negatives based on an accumulation of other indicators.


A single event in a complex environment can generate multiple alarms. A continuous large volume of alarms can overwhelm you or mislead the triage and investigation process. If this happens, you can end up dealing with alarm fatigue or wasting time reviewing false positives. 

With composite alarms, you can add logic and group alarms into a single high-level alarm, initiated when the underlying conditions are met. This means you can introduce intelligent decisions and minimize false positives.

Composite alarms are created using one or more alarm states combined with Boolean operators AND, OR, and NOT and constants TRUE and FALSE. A composite alarm is initiated when its expression evaluates to be TRUE.


> False positive: An alert that incorrectly indicates that malicious activity is occurring.

## Using CloudWatch anomaly detection 

When you turn on anomaly detection for a metric, CloudWatch applies statistical and machine learning algorithms. These algorithms continuously analyze metrics of systems and applications, determine normal baselines, and surface anomalies with minimal user intervention.

The algorithms generate an anomaly detection model. The model generates a range of expected values that represent normal behavior. With this feature, you can create anomaly detection alarms based on a metric's expected value. This type of metric alarm doesn't have a static threshold. Instead, the alarm compares the metric's value to the expected value based on the anomaly detection model. You can initiate an alarm when a metric value is above or below the band of expected values.

<img width="544" height="183" alt="image" src="https://github.com/user-attachments/assets/84a5aff8-00a8-4084-9130-6b3b9d40faee" />

A CPU utilization graph

In a graph with anomaly detection, the expected range of values is shown as a wide gray band. If the metric's actual value goes beyond this band, it is shown as red (the points extending above the wide band) during that time.



<img width="552" height="183" alt="image" src="https://github.com/user-attachments/assets/df6f9cb0-e9b0-4812-aafd-ec53152bef3b" />
A CPU utilization graph with a baseline change



Anomaly detection algorithms account for the seasonality and trend changes of metrics. 
The seasonality changes could be hourly, daily, or weekly, as shown in this example.


### Alarm actions

You can specify what actions an alarm takes when it changes state between the `OK`, `ALARM`, and `INSUFFICIENT_DATA` states. 
These actions may include one or many of the following:

- Notify one or more people by sending a message to an Amazon SNS topic.
- Perform EC2 actions (for alarms based on EC2 metrics).
- Perform actions to scale an Auto Scaling group.
- Initiate a Lambda function.
- Create OpsItems in Systems Manager Ops Center or create incidents in AWS Systems Manager Incident Manager (performed only when the alarm goes into ALARM state).

<img width="1333" height="749" alt="image" src="https://github.com/user-attachments/assets/5ce759e9-6724-41f1-b390-08e6fb5e722c" />
API activity notification example


### CloudWatch Synthetics
 
- Synthetic Monitoring
  You can use CloudWatch Synthetics to create canaries, configurable scripts that run on a schedule, to monitor your endpoints and APIs. 

- Why use a canary?
  Canaries follow the same routes and perform the same actions as a customer, which makes it possible for you to continually verify your customer experience even when you don't have any customer traffic on your applications. By using canaries, you can discover issues before your customers do! 

- CloudWatch Synthetics Demo
  CloudWatch Synthetics can be used to create canaries to monitor your endpoints and APIs. Synthetics canaries help you to continually verify your customer experience, discovering issues before your customers do and reacting quickly to fix them. You can use CloudWatch Synthetics to monitor your REST APIs, URLs, and website content, and perform checks for unauthorized changes from phishing, code injection, and cross-site scripting.  To learn more, view the demo video here https://www.youtube.com/watch?v=hF3NM9j-u7I


https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html


# Enhancing Monitoring and Alerting
 
## Amazon GuardDuty

Logs are also a useful source of information for automated threat detection. GuardDuty is a managed, continuous security monitoring service that analyzes and processes events from several sources, such as VPC Flow Logs, CloudTrail management event logs, CloudTrail Amazon S3 data event logs, and DNS logs. It uses threat intelligence feeds, such as lists of malicious IP addresses and domains, and machine learning to identify unexpected and potentially unauthorized and malicious activity within your AWS environment. GuardDuty is a passive service; however, it can be used in a multi-service workflow to initiate remediation through Lambda or other AWS services and features.

<img width="980" height="320" alt="image" src="https://github.com/user-attachments/assets/5ea5724f-6526-44df-9654-f15c4af56b06" />

<img width="605" height="193" alt="image" src="https://github.com/user-attachments/assets/93da6049-9ee9-4191-a805-2c90e2163f4e" />

1. Turn on GuardDuty
   With a few clicks in the AWS Management Console, monitor all your AWS accounts without additional security software or infrastructure to deploy or manage.

2. Continuously analyze
   
   Automatically analyze network and account activity at scale and provide broad, continuous monitoring of your AWS accounts. Review events through CloudTrail logs, VPC Flow Logs, and DNS logs.

3. Intelligently detect threats

   GuardDuty combines managed rule-sets, threat intelligence from AWS Security and third-party intelligence partners, anomaly detection, and machine learning to efficiently detect malicious or unauthorized behavior.

4. Take action
   Review detailed findings in the console, integrate into event management or workflow systems, or initiate Lambda for automated remediation or prevention.

- One-click activation without architectural or performance impact
- Continuous monitoring of AWS accounts and resources
- Instant On provides findings in minutes
- No agents, no sensors, no network appliances
- Global coverage, regional results
- Built-in anomaly detection with machine learning
- Partner integrations for additional protections

### GuardDuty data sources
 


- DNS logs
  - DNS logs are based on queries made from EC2 instances to known questionable domains.
  - DNS logs are in addition to Route 53 query logs. Route 53 is not required for GuardDuty to generate DNS based findings.

- VPC flow logs
  - Flow logs for VPCs do not need to be turned on to generate findings. Data is consumed through independent duplicate stream.
  - Turn on VPC Flow Logs to augment data analysis (charges apply).

- CloudTrail events

  - CloudTrail history of AWS API calls used to access the console, SDKs , AWS CLI, and so on, parsed by GuardDuty.
  - Identification of user and account activity including source IP address is used to make the calls.


Protect data wherever it goes. You can't protect what you don't know about, so visibility is key. You can combine visibility with continuous monitoring through GuardDuty.

<img width="800" src="https://github.com/user-attachments/assets/f0abaa97-02eb-488b-9038-10a45340b90f" />
An example workflow using GuardDuty that enhanced an organization's ability to respond to threats indicated by various logging systems


### GuardDuty findings

When GuardDuty detects suspicious or unexpected behavior, it generates a finding. A finding is a notification that contains the details about a potential security issue that GuardDuty discovers. One very useful piece of information in the finding details is a finding type. The purpose of the finding type is to provide a concise yet readable description of the potential security issue. 

<img width="800" src="https://github.com/user-attachments/assets/de8105e5-a8a7-4bea-8ee5-1a9e612da22d" />

Summary and line details for various findings detected by GuardDuty

For example, the GuardDuty `UnauthorizedAccess:EC2/SSHBruteForce` finding type quickly informs you that somewhere in your AWS environment, an EC2 instance has been targeted by an attacker trying to gain access.

https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-format.html


## AWS Security Hub

 

Security Hub is a fully managed AWS service offering that is turned on within a Region in minutes and aggregates findings across a customer's accounts. 

With Security Hub, you can manage security and compliance findings in one location, reducing the time spent wrangling data from different locations within the AWS Management Console. 

In addition to the default insights that are provided by AWS and AWS Partners, you can also create your own insights to track issues that are unique to their environment. This benefit provides you with a certain level of customization that can come in handy when dealing with company security requirements and regulations.

### Security standards and controls

Security Hub provides controls for the following standards.

- Center for Internet Security (CIS) AWS Foundations

- Payment Card Industry Data Security Standard (PCI DSS)

- AWS Foundational Security Best Practices

### Exploring CIS AWS Foundations

Depending on your organization's needs, you may choose to select a standard such as the CIS AWS Foundations Benchmark standard. 
Let's explore this standard and how Security Hub helps you to meet it.



#### Compliance check

<img width="904" height="502" alt="image" src="https://github.com/user-attachments/assets/f2e1185a-b43e-4f8e-af7f-6f97cba3af27" />
Example CIS AWS Foundations compliance statistics from Security Hub

<img width="1680" height="865" alt="image" src="https://github.com/user-attachments/assets/1f7cdb8d-8202-4e41-a192-f905f3a90898" />
Example CIS AWS Foundations compliance rules

<img width="1680" height="774" alt="image" src="https://github.com/user-attachments/assets/2cea944a-6f2b-4568-99a6-98045669a521" />
Example CIS AWS Foundations compliance rule findings and details through AWS Security Hub


Example of checks includes:

- Ensure that no root account access key exists.
- Ensure that multi-factor authentication (MFA) is turned on for all IAM users who have a console password.
- Ensure that the S3 bucket CloudTrail logs to is not publicly accessible.
- Security Hub conducts 43 continuous automated checks against CIS AWS Foundations Benchmark rules.
- Custom actions and remediation can be setup to correct noncompliant rules and send notifications.
 
### Remediation with Security Hub

Security Hub integrates with EventBridge, helping you create custom response and remediation workflows. Response and remediation actions can be fully automated or they can be initiated manually in the console. You can also use Systems Manager Automation documents, AWs Step Functions, and Lambda functions to build automated remediation workflows that can be initiated from Security Hub.

#### Auto or manual remediation?
 

- Automatic remediation is best when there is a low risk of a negative impact to the workloads in the account. For example, you would not want an auto remediation that stops an EC2 instance because that could jeopardize your workload.
  
- Manual remediation is best for anything that has the potential to impact business objectives. This type of intervention is slower, but notifications can help expedite response. This is also an option that should be used to test newly created automatic remediations, before they are put into a production environment.

> Even for low-impact workloads, automatic remediation should be thoroughly tested before being deployed into a production environment.


#### Auto remediation example

An example of a safe and good use for auto remediation is CloudTrail logging. It is a best practice to have CloudTrail logging on. If it is turned off, whether accidentally or maliciously, an auto remediation task could be set up to turn CloudTrail logging back on. 

With CloudTrail logging back on, it can automatically resolve the finding in the Security Hub workflow status and send an SNS message to the security team to let them know it was remediated.


<img width="1673" height="665" alt="image" src="https://github.com/user-attachments/assets/38c3e449-61c9-4622-ae24-14e1ea1a9430" />

<img width="838" height="366" alt="image" src="https://github.com/user-attachments/assets/410c5a6f-f2b4-43a6-908a-0b5cd5f7ce11" />

1. Step 1

   Integrated services send their findings to Security Hub.
 
2. Step 2
   From the Security Hub console, you’ll choose a custom action for a finding. Each custom action is then emitted as a CloudWatch event.

3. Step 3
   The CloudWatch event rule initiates a Lambda function. This function is mapped to a custom action based on the custom action’s Amazon Resource Name (ARN).

4. Step 4
   Depending on the particular rule, the Lambda function that is invoked will perform a remediation action on your behalf.


   
Read more about how to implement this auto remediation from the AWS security blog [Automated Response and Remediation with AWS Security Hub](https://aws.amazon.com/blogs/security/automated-response-and-remediation-with-aws-security-hub/).


  
## Centralized logging solution overview

The following diagram presents an architecture you can automatically deploy in about 30 minutes, using an implementation guide and accompanying CloudFormation templates (provided by AWS). This solution contains log ingestion, log indexing, and visualization. The implementation guide and CloudFormation template are provided free of charge; however, the customer is responsible for the cost of running and using various services contained within the solution.

<img width="1377" height="873" alt="image" src="https://github.com/user-attachments/assets/5051d9e1-0570-4260-bf86-6d60f0a0cef9" />

<img width="885" height="571" alt="image" src="https://github.com/user-attachments/assets/67b441a0-1380-4a0c-b7aa-305547d0b80d" />

1. Log ingestion
   
   CloudWatch Logs destinations deploy in the primary account and are created with the required permissions in each of the selected Regions. CloudWatch Logs subscription filters can be configured for log groups to be streamed to the Centralized Logging account.

2. Log indexing

   A centralized Kinesis Data Streams and Kinesis Data Firehose are provisioned to index log events on the centralized Amazon OpenSearch Service domain. The CloudWatch Logs destinations created to stream log events have Kinesis Data Streams as their target. After the log events stream to Kinesis Data Streams, the service invokes a Lambda function to transform each log event to an Amazon OpenSearch Service document, which is then put into Kinesis Data Firehose. You can monitor Kinesis Data Firehose while it sends custom CloudWatch Logs containing detailed monitoring data for each delivery stream.

3. Log indexing
   A centralized Kinesis Data Streams and Kinesis Data Firehose are provisioned to index log events on the centralized Amazon OpenSearch Service domain. The CloudWatch Logs destinations created to stream log events have Kinesis Data Streams as their target. After the log events stream to Kinesis Data Streams, the service invokes a Lambda function to transform each log event to an Amazon OpenSearch Service document, which is then put into Kinesis Data Firehose. You can monitor Kinesis Data Firehose while it sends custom CloudWatch Logs containing detailed monitoring data for each delivery stream.

   https://aws.amazon.com/solutions/
   https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch


# Auditing Your AWS Environment
 
## AWS Audit Manager

Continuous assessments of your environment provide a way to maintain your security posture, compliance standing, and readiness for an audit. Audit Manager is a managed service that helps you to establish a framework of choice, along with standard or custom configuration for policies, procedures, and activities (known as controls).
 
- Provides an automated and continuous process. 
- Collects and reviews data. 
- Assesses whether controls are operating effectively.
  
Continuous and automated gathering of evidence related to your EC2 instances and other AWS resources helps streamline risk assessment and compliance with regulations and industry standards. This process helps you maintain a continuous, audit-ready posture across your compute resources.   


> The evidence that is collected through Audit Manager might not include all the information about your AWS usage that is needed for an audit performed by an enforcing entity. Audit Manager is a valuable resource but it is NOT a substitute for legal counsel or compliance experts.


### Using Audit Manager

With Audit Manager, you can build custom frameworks, either from scratch to address your organizational requirements or based on existing frameworks with your necessary modifications. You can use one of the many prebuilt frameworks available with the service if you don't require any modifications or additions to the assessment. Next, we will examine the steps in assessing your environment. 


#### Choose a framework

<img width="800" src="https://github.com/user-attachments/assets/9c317229-02e3-4209-8c3e-6a3224b7864e" />

- There are numerous frameworks, specific to industry, location-based regulatory guidance, and international standards.

- Here, you can see the NIST Cybersecurity Framework is selected.

#### Exploring framework controls

<img width="800" src="https://github.com/user-attachments/assets/0b62a047-ab20-4b00-982a-d69f8f822b07" />

- Each framework has a number of controls assigned.
- Controls are categorized by type and data source.
- Data source is the service or artifact from which the evidence is derived.

#### Define the audit scope by selecting:

<img width="800" src="https://github.com/user-attachments/assets/baa89a88-cce3-4a68-a91b-2e068747a923" />

- Accounts in scope
- Services in scope
- Audit owners

>Audit owners drive the audit preparation across your organization and have full permission to manage the assessment they are assigned to.

#### Gather evidence

<img width="853" height="203" alt="image" src="https://github.com/user-attachments/assets/dec6be61-1013-45c2-8219-5132e234d093" />

- Evidence is automatically collected and stored in folders with a default name of the date it was collected.  
- You can also manually upload evidence. This is required by some control types.

### Evidence folder summary

The summary section provides a high-level overview of the items in the evidence folder.

<img width="1630" height="406" alt="image" src="https://github.com/user-attachments/assets/a24933a6-dc89-483e-96e0-f1d7b1b1fc97" />

1. Control name
   The name of the control associated with the evidence folder

2. Added to assessment report
   The number of evidence items that were manually selected for inclusion in the assessment report

3. Total evidence
   The total number of evidence items in the evidence folder

4. Resources
   The total number of AWS resources that were assessed when generating the evidence in this folder

5. User activity
   The number of evidence items that fall under the user activity category; This evidence is collected from AWS cCloudTrail logs

6. Configuration data
   The number of evidence items that fall under the configuration data category;
   this evidence is collected from configuration snapshots of other AWS services such as AWS EC2, Amazon S3, or IAM

7. Manual
   The number of evidence items that fall under the manual category; This evidence is uploaded manually

8. Compliance check
   The number of evidence items that fall under the compliance check category;
   This evidence is collected from AWS Config or AWS Security Hub
   
9. Compliance check status
   The number of issues that were reported directly from AWS Config, AWS Security Hub, or both.
   
### Compile a report

After you select the evidence to include in your assessment report, you can generate the final assessment report to share with auditors.
When you generate an assessment report, it is placed in the S3 bucket that you designated as your assessment report destination.
For more information about generating a report, see the [Audit Manager User Guide](https://docs.aws.amazon.com/audit-manager/latest/userguide/generate-assessment-report.html).


### Reducing effort

The controls offered by Audit Manager through the prebuilt frameworks do not guarantee that you will pass an assessment associated with that framework. Instead, they help reduce effort and time in your assessment preparation and review. 
In addition to Audit Manager, AWS Artifact should be used to help gather supplemental evidence to assist in the assessment preparation and review. 


## AWS Trusted Advisor

Trusted Advisor provides recommendations that help you follow AWS best practices. Trusted Advisor evaluates your account by using checks. These checks identify ways to optimize your AWS infrastructure, improve security and performance, reduce costs, and monitor service quotas. You can then follow the check recommendations to optimize your services and resources. Remember that Trusted Advisor is a passive service; it cannot perform remediation on its findings.

 <img width="1170" height="628" alt="image" src="https://github.com/user-attachments/assets/59d53ece-6487-421f-a7ca-31cad573b44b" />


The AWS Trusted Advisor dashboard

Some of the security configuration checks of your AWS environment include: Open ports

- Unrestricted access
- CloudTrail logging
- S3 bucket permissions
- MFA
- Password policy
- DB access risk
- DNS records
- Load balancer config

AWS Basic Support and AWS Developer Support customers can access core security checks and all checks for service quotas. AWS Business Support and AWS Enterprise Support customers can access all checks, including cost optimization, security, fault tolerance, performance, and service quotas. 
For a complete list of checks and descriptions, see the [Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/) check reference. 


## IAM credential report

Verification is an important part of security. Are your users following security best practices? To prevent compromise in your environment, it is important that MFA is turned on for administrative-level users, passwords are regularly changed, and unused or stale credentials are being removed after they are no longer needed.

To verify these and other security issues, you can generate a credential report that lists your IAM users and the status of their AWS security credentials. This can be download as a CSV file. These reports contain details such as whether MFA is activated, when their password was last rotated, and more. You can generate a new report as often as every 4 hours.

<img width="1680" height="869" alt="image" src="https://github.com/user-attachments/assets/fdd76ba6-cd71-488e-8071-30dfbe9a9c2b" />
An IAM credential report; highlighted areas show accounts where MFA has been turned on


https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html


# Knowledge check

1. Which services can VPC Flow Log records be published to? (SELECT TWO)

- [x] Amazon CloudWatch Logs
- Amazon DynamoDB
- [x] Amazon S3
- AWS CloudTrail
- Amazon RDS

 
The two destinations that VPC Flow logs can be published to are Amazon S3 and Amazon CloudWatch Log

2. Which of the following may be used to capture the event history of user and API activity?

- [x] AWS CloudTrail
- VPC Flow Logs
- Amazon CloudWatch
- Amazon EventBridge

 
AWS CloudTrail provides event history of user and API activity

3. Amazon CloudWatch Metrics can be used to alarm when certain metrics are exceeded. An exceeded metric may be an Indicator of Compromise (IoC). 



Which of the following are common IoCs that can monitor with CloudWatch? (SELECT TWO)

- Repeated attempts to access websites such as social media or streaming services
- Insider threats copying information to personal drives
- [x] Unusually high traffic at irregular hours
- [x] Abnormal CPU utilization
- Social engineering attempts such as phishing

 
Abnormal CPU utilization and unusually high traffic at irregular hours may be indicators of compromise.

CloudWatch Metrics cannot capture or alarm instances of insider threats copying information to personal drives or social engineering.

Repeated attempts to access websites such as social media or streaming services alone are not indicators of compromise. 


4. AWS CloudTrail can do provide all of the following except: 

- Discover and troubleshoot security and operational issues by capturing a comprehensive history of changes that occurred in an AWS account
- [x] Provide managed anomaly detection and automated response to alarms
- Increase visibility into user and resource activity
- Simplify compliance audits by automatically recording and storing activity logs for an AWS account

 
AWS CloudTrails does not provide managed anomaly detection and automated response to alarms.

5. AWS CloudTrail log file integrity validation is invaluable in security and forensic investigations. Which industry standard algorithm is used for validation hashing?

- SHA-256
- DES
- MD5
- AES

 
SHA-256 is the industry standard algorithm used for validation hashing.

 
