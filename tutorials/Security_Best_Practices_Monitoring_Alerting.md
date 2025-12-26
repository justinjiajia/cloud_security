

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

1.
<img width="305" height="220" alt="image" src="https://github.com/user-attachments/assets/a56b83df-32e5-4d46-98a0-18380b3afb95" />

2.
<img width="315" height="148" alt="image" src="https://github.com/user-attachments/assets/7a96ed08-dfff-4268-8ba6-43589cba4498" />

3.
<img width="315" height="213" alt="image" src="https://github.com/user-attachments/assets/b955fd00-4a7d-48de-81ba-457121591846" />

4.
<img width="313" height="210" alt="image" src="https://github.com/user-attachments/assets/992ad0e1-b451-4970-ae60-91256361c731" />

5. srcport: The source port of the traffic
6. dstport: The destination port of the traffic
7.
   <img width="319" height="150" alt="image" src="https://github.com/user-attachments/assets/e1b0163b-eb70-44e7-b89f-21c2d93501f0" />

8.
<img width="316" height="291" alt="image" src="https://github.com/user-attachments/assets/7b2cdde9-aa0a-4a9a-8f72-351bd368a2b9" />

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
- Log prefix changes from "/AWSLogs/<accountID>/" to "/AWSLogs/<OrganizationID>/".
- There is no more updating of the bucket policy.

Watch out for multiple trails when turning on CloudTrail in an existing organization.


## AWS KMS encryption



You can encrypt CloudTrail logs through AWS Key Management Service (AWS KMS). 
By default, the files are encrypted using the S3 server-side encryption (SSE-S3) and then transparently decrypted when you read them. 
Optionally, you can specify an AWS KMS key (SSE-KMS) and it will be used to encrypt your log files. 
 
