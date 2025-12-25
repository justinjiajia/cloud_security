https://skillbuilder.aws/learn/6E2F4RVDA2/aws-cloudtrail-getting-started

# Introduction to AWS CloudTrail
 

In this lesson, you will learn the following:

How CloudTrail works
What problems CloudTrail solves
The benefits of CloudTrail
CloudTrail pricing



## What does CloudTrail do?

AWS CloudTrail is an Amazon Web Services (AWS) service that helps you enable operational and risk auditing, governance, and compliance of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail. Events include actions taken in the AWS Management Console, AWS Command Line Interface (AWS CLI), and AWS SDKs and APIs.


CloudTrail is enabled on your AWS account when you create it. When activity occurs in your AWS account, that activity is recorded in a CloudTrail event. 
You can conveniently view recent events in the CloudTrail console by going to Event history. 



Using CloudTrail, you can view, search, download, archive, analyze, and respond to account activity across your AWS infrastructure. 
CloudTrail helps identify who took which action, which resources were acted on, when the event occurred, and other details. 
Using the information collected by CloudTrail, you can analyze and respond to activity in your AWS account. 
Optionally, you can activate CloudTrail Insights on a trail to help you identify and respond to unusual activity.

> CloudTrail records AWS account activity, which you can view in the console's Event history.


### Which problems does CloudTrail solve?

With AWS CloudTrail, you can monitor your AWS activity comprehensively. 
You can gain visibility into users and resource activity by obtaining a history of all the AWS API calls made in your account. 
With CloudTrail, you can monitor API calls made by using the AWS Management Console, the AWS SDKs, the command line tools, and higher-level AWS services. 
You can identify which users and accounts called AWS APIs for services that support CloudTrail.
Additionally, you can identify the source IP address from which the calls were made, and when the calls occurred. This helps during operational, security incident troubleshooting, and also helps in risk auditing, governance, and compliance of your AWS account.



With CloudTrail, you can do the following:

<img width="200" src="https://github.com/user-attachments/assets/ecb6c089-9a3b-4576-94cf-67245157ab40" />
Centralize a collection of activity data to manage multi-Region and multi-account environments.

<img width="200" src="https://github.com/user-attachments/assets/42415696-15b9-48ca-a6bd-bc4cfed29be4" />
Audit by automatically recording and storing activity logs.


<img width="200" src="https://github.com/user-attachments/assets/07135a2e-3e28-454e-af73-bd6c4c72384b" />
Integrate with SQL query syntax for log analysis.

<img width="200" src="https://github.com/user-attachments/assets/1ed3da44-294f-4842-bedb-26cf3c10ab97" />
Address regulatory and compliance requirements for auditing.

<img width="200" src="https://github.com/user-attachments/assets/295177db-1783-43ab-be7b-46b620710256" />
Monitor data usage, detect exfiltration, and adjust AWS IAM roles' permissions.

<img width="200" src="https://github.com/user-attachments/assets/13239157-d62f-4531-a147-f42ceab44dc3" />
Build security automation by tracking and responding to threats, and use CloudTrail Insights to detect unusual activity.

<img width="200" src="https://github.com/user-attachments/assets/5fd45fbd-2625-457a-9520-77a3d839808b" />
Troubleshoot security and operational issues by tracking changes in your accounts.

<img width="200" src="https://github.com/user-attachments/assets/5fbbb3fa-73e4-4f14-9c49-0eda1f71606d" />
Detect operation issues by integrating with Amazon CloudWatch Logs.

### What are the benefits of CloudTrail?

To learn more about the benefits of CloudTrail, expand each of the following five benefit sections.


- Search and analytics
  With CloudTrail search and analytics, you can do the following:

  - Retrieve a 90-day event history of your management events from the CloudTrail console or API.  
  - Narrow down to the relevant time period, API operation, username, or resource.
  - Query audit logs alongside performance and monitoring logs using integration with CloudWatch Logs.
  - Consider more than 20 AWS Partner integrations for operational and security solutions.

- Search and analytics for data management and analysis
  Search and analytics offer powerful capabilities for data management and analysis.
  With CloudTrail, you can retrieve a 90-day event history of management events through the console or API. You can also narrow down results by time period, API operation, username, or resource, and query audit logs alongside performance logs using CloudWatch Logs integration. Additionally, you can explore over 20 AWS Partner integrations for operational and security solutions.


- CloudTrail Insights
  Identify and respond to unusual operational activity, such as the following:

  - Spikes in resource provisioning
  - Bursts of AWS Identity and Access Management (IAM) management actions
  - Gaps in periodic maintenance activity
  - Automate the analysis of API calls and usage patterns
  - Detect any unusual activity
  - Detect unusual error rate activity in your AWS account
  
  CloudTrail Insights provides swift identification and response to unusual operational activity, including unexpected spikes in resource provisioning, bursts of IAM management actions, and gaps in periodic maintenance.
  You can automate analysis of API calls and usage patterns to detect any unusual activity, in addition to identifying unusual error rate activity within your AWS account.


- Trails for CloudTrail
  With trails for CloudTrail, you can do the following:

  - Collect and store management and data events from multi-Region and multi-account environments.
  - Store the logs for a custom period of time to meet regulatory requirements.
  - Integrate trails for CloudTrail to store activity in CloudWatch Logs or AWS CloudTrail Lake.
  - Filter data events using advanced event selectors.
  
  Trails for CloudTrail efficiently collects and retains management and data events across multi-Region and multi-account environments.
  You can customize log retention duration to comply with regulatory needs.
  You can also integrate trails with CloudWatch Logs or CloudTrail Lake to store activity and use advanced event selectors for seamless filtering of data events.


- AWS CloudTrail Lake
  The following features describe CloudTrail Lake:

  - It is a managed data lake that helps organizations aggregate, immutably store, and query events recorded by CloudTrail for auditing, security investigation, and operational troubleshooting.
  - It has a fully immutable collection of events.
  - The event data store is optimized for search using SQL queries.
  - It provides events management across multiple accounts and Regions within your AWS Organization in one central location.
  - You can filter events using advanced event selectors.
  
  CloudTrail Lake is a managed data lake designed for organizations to aggregate, securely store, and query CloudTrail events for auditing, security investigation, and operational troubleshooting.
  It ensures the full immutability of collected events and offers optimized event data storage for efficient search using SQL queries.
  With CloudTrail Lake, you can conveniently manage events from multiple accounts and Regions within your AWS Organization, all in one centralized location.
  Additionally, you can use advanced event selectors for seamless event filtering.



https://aws.amazon.com/cloudtrail/features/



> CloudTrail offers benefits such as search analytics, data management, and analysis through features like CloudTrail Insights, trails for CloudTrail, and AWS CloudTrail Lake.

### How much does CloudTrail cost?

Use CloudTrail to quickly discover vulnerabilities in AWS workloads:

- Validate sensitive data.
- Assess AWS usage for compliance.
- Decrease visibility for business-critical data.
- Protect web applications.

With CloudTrail, you can record three types of events:

- Management events capture control plane actions, such as creating or deleting Amazon Simple Storage Service (Amazon S3) buckets. 
- Data events capture high-volume data plane actions, such as reading or writing an Amazon S3 object. 
- CloudTrail Insights events capture unusual write-management API activity in your account. 

Depending on how you are using CloudTrail, you might use one of the following pricing models. To learn about a cost tier, choose the appropriate tab.

- AWS Free tier
  With the AWS Free Tier, you can log and search events with event history for activity from the most recent 90-day history of your account’s management events.
  You can also use your ﬁrst trail of recorded management events delivered to Amazon S3. When creating an organizational trail, this type of trail is considered your ﬁrst trail.


- AWS Paid Tier
  With the Paid Tier, you can have additional copies of management events delivered to Amazon S3. You can also have data events delivered to Amazon S3 or CloudTrail Insights.

https://aws.amazon.com/cloudtrail/pricing/

## Knowledge check

 
 
1. Which problems does AWS CloudTrail solve?

- [x] It provides auditing, security monitoring, and operational troubleshooting by tracking user activity and API usage.
- It offers automatic remediation for any suspicious activity.

- It provides recommendations to improve security posture.
- It automatically stores account activity for 7 years for audit purposes.
- It automatically tracks management and data events without any configuration, providing a holistic view during audits.

 
Correct. CloudTrail provides auditing capabilities, security monitoring, and operational troubleshooting by effectively tracking user activity and API usage.


 
2. What are the benefits of using AWS CloudTrail? (Select THREE.)

- [x] Integrate with SQL tools, such as Amazon Athena, for log analysis. 
- Eliminate the need to set up a secure environment.
- [x] Audit AWS account and API activity. 

- [x] Integrate with a purpose-built data lake for auditing, security investigation, and operational troubleshooting. 

- Store event history automatically for 7 years.

- Monitor resource performance metrics.

 Correct.  CloudTrail offers integration with SQL tools, such as Athena, for log analysis.
  It also offers auditing of AWS account and API activity and integration with a purpose-built data lake for auditing, security investigation, and operational troubleshooting.


---


# Architecture and Use Cases
 
In this lesson, you will learn the following:

The technical concepts of CloudTrail
Typical use cases for CloudTrail
Specify the requirements to implement CloudTrail in a real-world scenario



## How is CloudTrail used to architect a cloud solution?

You can configure CloudTrail to deliver CloudTrail events to CloudWatch Logs. 
You can then use CloudWatch Logs Insights to search and analyze your log data in CloudWatch Logs. Using CloudWatch Logs Insights, you can perform queries against your log data to gather speciﬁc information that CloudTrail has captured and recorded. For example, you can create a query to show the number of console logins that have occurred in a speciﬁc time period. 


<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/ac82ac3d-2001-494c-995c-df811672bf28" />

<img width="599" height="351" alt="image" src="https://github.com/user-attachments/assets/13d9ac36-17ea-4d9f-801f-ad649396fa55" />


1. AWS CloudTrail

   You can configure CloudTrail to deliver CloudTrail events to CloudWatch Logs.

2. Amazon CloudWatch

   The monitoring and management service provides data and actionable insights for AWS applications.

3. CloudWatch Logs

   You can send CloudTrail Logs to CloudWatch to query data.
   
4. CloudWatch Logs Insights

   You can use CloudWatch Logs Insights to search and analyze log data in CloudWatch Logs.
   Using CloudWatch Logs Insights, you canperform queries against your log data to gather specific information that CloudTrail has captured and recorded.
   For example, you can create a query to show the number of console logins for a specific time period.


### How can CloudTrail events be used in security audits?

For auditing, when you store log files in a dedicated S3 bucket in a separate administrative domain, you can enforce strict security controls and duty segregation. Restricting access to this S3 bucket will decrease the chances of unauthorized and unfettered access to the logs. You can also use S3 Object Lock for governance or compliance mode to restrict any changes to the logs. With these controls in place, if any AWS account credentials become compromised, the logs won’t be lost because they are stored in a separate domain. 

For more information about setting up a separate AWS account for this purpose, 
see [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html) in the AWS CloudTrail User Guide.

### What are the basic technical concepts of CloudTrail?

 
- Event history
  With event history, you can view, search, and download the past 90 days of activity in your AWS account.


- CloudTrail events
  An event in CloudTrail is the record of an activity in an AWS account. There are three types of events that can be logged in CloudTrail: management events, data events, and CloudTrail Insights events.


- Trails for CloudTrail
  By using trails for CloudTrail, you can archive, analyze, and respond to changes in your AWS resources.
  A trail is a conﬁguration that helps deliver events to an S3 bucket that you specify. You can also deliver and analyze events in a trail with CloudWatch Logs and CloudWatch Events.

  You can create three types of trails.
  The ﬁrst, a multi-Regional trail, applies to all Regions.
  The second trail type applies to one Region.
  This option is available only in AWS CLI, and we recommend using multi-Region trails, rather than a single Regional trail.
  The ﬁnal trail type is an organizational trail that applies to your entire organization.


- Management events
  Management events provide information about control plane operations for resources in your AWS account. Management events include actions taken when conﬁguring security groups, launching instances, or setting up logging.


- Data events
  Data events provide information about the data plane operations performed on or in a resource. Data events include object-level actions taken against S3 buckets and objects, Amazon DynamoDB object-level activity on tables, and AWS Lambda function activity. They also include additional AWS services that support data events.


- Insights events
  CloudTrail Insights events capture unusual activity in your AWS account.
  Insights events are logged only when CloudTrail detects changes in your account's API usage that diﬀer signiﬁcantly from the account's typical usage patterns. It does this by establishing a baseline of your AWS activity and then creating an Insight event when new activity passes this baseline threshold.


- CloudTrail Lake
 
  CloudTrail Lake is a managed data lake that helps organizations aggregate, immutably store, and query events recorded by CloudTrail for auditing, security investigation, and operational troubleshooting.
  With CloudTrail Lake, you can query CloudTrail data using SQL.
  It also includes sample queries that can help users get started with writing queries for common scenarios.
  An example is identifying records of all activities performed by a user to help accelerate security investigations.
  The immutable nature of storage, coupled with a default retention window of 7 years, helps customers meet compliance requirements. CloudTrail Lake supports collecting events from multiple Regions and AWS accounts.

>  CloudTrail logs AWS account activity for analysis through event history and trails delivered to an S3 bucket, with additional analysis options through CloudWatch.

### What are typical use cases for CloudTrail?

CloudTrail is essential for auditing user activity, actively identifying security incidents, and troubleshooting operational issues, 
making it a versatile tool for enhancing security and operational efficiency.  

- Audit Activity
  Monitor, store, and validate activity events for authenticity. Quickly generate audit reports that internal policies and external regulations might require.  

- Identify security incidents
  Detect unauthorized access using the who, what, and when information in CloudTrail events. Respond with rules-based Amazon EventBridge alerts and automated workﬂows.
  
- Troubleshoot operational issues
  Continuously monitor API usage history using machine learning (ML) models to spot unusual activity in your AWS accounts and then determine the root cause.


### What else should I keep in mind about CloudTrail?

When using AWS CloudTrail, remember to consider factors such as managing costs, using CloudTrail Insights for threat detection, and copying events to CloudTrail Lake for data analysis. The essential role of CloudTrail in auditing user activity and troubleshooting operational issues enhances security and efficiency in AWS. To learn more, expand each of the following three sections.


- CloudTrail costs
  Remember that CloudTrail provides the ﬁrst trail for CloudTrail for delivery of all management events included in the AWS Free Tier.
  If you conﬁgure more than one trail, additional charges will occur.
  If you use other underlying services, such as CloudWatch Logs, to deliver a copy of CloudTrail logged events to CloudWatch Logs, additional charges will occur. CloudTrail Lake offers 7 years of storage and is priced based on amount of storage used and data scanned from SQL querying on the logs. CloudTrail insights is priced based on the total amount of events analyzed.


- CloudTrail Insights
  CloudTrail Insights is not automatically activated, and you must explicitly turn it on.
  When you turn on CloudTrail Insights events for a trail, CloudTrail starts monitoring the write management events captured by that trail for unusual patterns. You can activate CloudTrail Insights events on individual trails in your account by using the console, AWS CLI, or AWS SDKs. You can also activate CloudTrail Insights events across your organization by using an organizational trail configured in your AWS Organizations management account. You can turn on CloudTrail Insights events by choosing the radio button in your trail definition.


- Copying trail events to CloudTrail Lake
  Continuously monitor API usage history using ML models to spot unusual activity in your AWS accounts and then determine the root cause.

https://aws.amazon.com/cloudtrail/resources/?blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc


## Knowledge check

 
Which use case is an example for AWS CloudTrail?

- Detect unauthorized access.
- Prevent distributed denial of service (DDoS) attacks on servers.
- Monitor resource usage.

- Provide vulnerability assessments for Amazon Elastic Compute Cloud (Amazon EC2).

- Throttle API activity in an AWS account.

 
Correct. The detection of unauthorized access is indeed an example of a use case for CloudTrail.


---

# How Do I Use CloudTrail to Look Up Event History?
 
In this lesson, you will learn how to launch and interact with the basic components for AWS CloudTrail in the AWS Management Console.


## How do I use the AWS Management Console to look up Event history for CloudTrail?

In this demo, you will learn how to use CloudTrail to access Event history in the AWS Management Console.  

https://www.youtube.com/watch?v=pFEsYm3kldM

---

# How Do I Use AWS CLI with AWS CloudTrail?
 

In this lesson, you will learn how to use AWS Command Line Interface, or AWS CLI, with CloudTrail.


 

## How do I use AWS CLI with CloudTrail?

If you have the AWS CLI installed and conﬁgured, you can look up events for CloudTrail by calling the appropriate commands. 
For more information about installing the command prompt locally on your machine, see [AWS Command Line Interface](https://aws.amazon.com/cli).

If you do not have the AWS CLI installed, you can use AWS CloudShell to issue CLI commands. 
You can access CloudShell by searching for the service in the AWS Management Console. For more information, see [AWS CloudShell](https://aws.amazon.com/cloudshell).

### What about the code?

You can look up CloudTrail management events for the last 90 days for the current AWS Region using the aws cloudtrail lookup-events command. 
The aws cloudtrail lookup-events command shows events in the AWS Region where they occurred.

To look up an event for a trail, expand the following two lookup-events commands to look up API activity events by the attribute EventName.


#### Look up events for a trail


The following lookup-events command looks up API activity events by the attribute EventName.



Input

```shell
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue= ConsoleLogin
```


Output

```shell
{
"Events": [
{
"EventId": "654ccbc0-ba0d-486a-9076-dbf7274677a7",
"Username": "my-session-name",
"EventTime": "2021-11-18T09:41:02-08:00",
"CloudTrailEvent": "{\"eventVersion\":\"1.02\",\"userIdentity\":      {\"type\":\"AssumedRole\",\"principalId\":\"AROAJIKPFTA72SWU4L7T4:my-session-name\",\"arn\":\"arn:aws:sts::123456789012:assumed-role/my-role/my-session-name\",\"accountId\":\"123456789012\",\"sessionContext\":{\"attributes\":{\"mfaAuthenticated\":\"false\",\"creationDate\":\"2016-01-26T21:42:12Z\"},\"sessionIssuer\":{\"type\":\"Role\",\"principalId\":\"AROAJIKPFTA72SWU4L7T4\",\"arn\":\"arn:aws:iam::123456789012:role/my-role\",\"accountId\":\"123456789012\",\"userName\":\"my-role\"}}},\"eventTime\":\"2016-01-26T21:42:12Z\",\"eventSource\":\"signin.amazonaws.com\",\"eventName\":\"ConsoleLogin\",\"awsRegion\":\"us-east-1\",\"sourceIPAddress\":\"72.21.198.70\",\"userAgent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36\",\"requestParameters\":null,\"responseElements\":{\"ConsoleLogin\":\"Success\"},\"additionalEventData\":{\"MobileVersion\":\"No\",\"MFAUsed\":\"No\"},\"eventID\":\"654ccbc0-ba0d-486a-9076-dbf7274677a7\",\"eventType\":\"AwsConsoleSignIn\",\"recipientAccountId\":\"123456789012\"}",
"EventName": "ConsoleLogin",
"Resources": []
}
]
}
```

#### Look up the last 10 events
–
To see the ten latest events, type the following command



Input

```shell
aws cloudtrail lookup-events --max-items 10
```

Output

```shell
{

    "NextToken": "kbOt5LlZe++mErCebpy2TgaMgmDvF1kYGFcH64JSjIbZFjsuvrSqg66b5YGssKutDYIyII4lrP4IDbeQdiObkp9YAlju3oXd12juy3CIZW8=", 

    "Events": [

        {

            "EventId": "0ebbaee4-6e67-431d-8225-ba0d81df5972", 

            "Username": "root", 

            "EventTime": 1424476529.0, 

            "CloudTrailEvent": "{

                  \"eventVersion\":\"1.02\",

                  \"userIdentity\":{

                        \"type\":\"Root\",

                        \"principalId\":\"111122223333\",

                        \"arn\":\"arn:aws:iam::111122223333:root\",

                        \"accountId\":\"111122223333\"},

                  \"eventTime\":\"2015-02-20T23:55:29Z\",

                  \"eventSource\":\"signin.amazonaws.com\",

                  \"eventName\":\"ConsoleLogin\",

                  \"awsRegion\":\"us-east-2\",

                  \"sourceIPAddress\":\"203.0.113.4\",

                  \"userAgent\":\"Mozilla/5.0\",

                  \"requestParameters\":null,

                  \"responseElements\":{\"ConsoleLogin\":\"Success\"},

                  \"additionalEventData\":{

                         \"MobileVersion\":\"No\",

                         \"LoginTo\":\"https://console.aws.amazon.com/console/home",

                         \"MFAUsed\":\"No\"},

                  \"eventID\":\"0ebbaee4-6e67-431d-8225-ba0d81df5972\",

                  \"eventType\":\"AwsApiCall\",

                  \"recipientAccountId\":\"111122223333\"}", 

            "EventName": "ConsoleLogin", 

            "Resources": []

        }

    ]

}        
```

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-cli.html
https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/lookup-events.html


## How can I learn more about CloudTrail?

To learn more about CloudTrail, choose from the following nine links.

[CloudTrail service webpage](https://aws.amazon.com/cloudtrail/)

To access an overview of CloudTrail, including links to other resources, choose the following button.

 
[API reference](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/Welcome.html)

To learn more about the API actions for CloudTrail, choose the following button.

 
[AWS CLI reference](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/)

To learn more about the subcommands of the CloudTrail command in AWS CLI, choose the following button.

 
[CloudFormation reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_CloudTrail.html)

To learn more about the resource types you can define in CloudFormation, choose the following button.

 
[AWS SDK reference](https://builder.aws.com/build/tools)

For more information about AWS SDKs, including how to download and install them, choose the following button.

 
[CloudTrail FAQs](https://aws.amazon.com/cloudtrail/faqs/)
To visit the frequently asked questions for CloudTrail, choose the following button.

 
[AWS Cloud Operations and Migrations Blog](https://aws.amazon.com/blogs/mt/category/management-tools/aws-cloudtrail/)
To visit various blog posts related to CloudTrail management, choose the following button.

 
[AWS Security Blog](https://aws.amazon.com/blogs/security/tag/aws-cloudtrail/)
To visit various blog posts related to CloudTrail security, choose the following button.

 
[AWS News Blog](https://aws.amazon.com/blogs/aws/tag/amazon-cloud-trail/)
To visit various blog posts related to CloudTrail news, choose the following button.
