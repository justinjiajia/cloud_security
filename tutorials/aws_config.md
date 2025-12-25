

# Introduction to AWS Config
Lesson objectives

By the end of this lesson, you will be able to do the following:

Identify the core functionality of AWS Config.

Identify the technical concepts related to AWS Config.

Identify the key features and capabilities of AWS Config.

Identify the practical applications of AWS Config.


## AWS Config introduction

AWS Config is a service that provides a detailed view of the configuration of Amazon Web Services (AWS) resources in your account. It continuously monitors and records AWS resource configurations, which helps you audit configuration history and assess compliance with organizational policies.

 

AWS Config captures resource relationships and configuration details. This makes it possible to discover existing resources, export a complete inventory, 
and determine how a resource was configured at any point in time. Increased visibility helps you streamline compliance auditing, security analysis, 
change management, and operational troubleshooting.

AWS Config examines resource configurations and evaluates them against defined rules, 
providing insights into your infrastructure's compliance with best practices and internal policies. 
The service helps you maintain desired configurations and assess the impact of configuration changes across your AWS environment.


## AWS Config core functionality

AWS Config provides comprehensive visibility into your AWS resources, their configurations, and their relationships, helping you maintain security and governance over your cloud environment.


- Configuration recording

  AWS Config continuously monitors and records configuration changes to your AWS resources.
  It captures details about resource attributes, relationships, and current configuration settings.
  This recording happens automatically after you set up the service, creating a comprehensive configuration history that you can reference at any time.


- Configuration evaluation

  AWS Config evaluates recorded resource configurations against desired settings using rules.
  These rules can be AWS managed (predefined by AWS) or custom (created by you). When a resource is created, modified, or deleted, AWS Config compares its configuration against your rules to determine compliance status and flags any non-compliant resources.


- Configuration history and snapshots

  AWS Config maintains a configuration history for each resource, which helps you access point-in-time information about your infrastructure.
  You can generate configuration snapshots that provide a complete picture of all your resources and their settings at a specific moment.
  These historical records help with troubleshooting, audit preparation, and understanding infrastructure evolution over time.

> AWS Config monitors and records AWS resource configurations to assess compliance rules.

## AWS Config technical concepts

AWS Config operates at the intersection of cloud governance, security, and compliance, requiring familiarity with infrastructure management, policy enforcement, and resource monitoring concepts.


- Configuration items


  Configuration items are the fundamental building blocks in AWS Config. A configuration item represents a point-in-time record of the various attributes of an AWS resource, its relationships with other resources, and its current configuration. Each time a tracked resource changes, AWS Config creates a new configuration item.

  AWS Config stores these configuration items in its database, building a complete history of changes for each resource.
  This historical record becomes valuable for compliance auditing, security analysis, and troubleshooting configuration-related issues.


- Configuration streams
  Configuration streams deliver notifications about configuration changes of your AWS resources.
  When a resource is created, updated, or deleted, AWS Config records the change and sends a notification to an Amazon Simple Notification Service (Amazon SNS) topic.

  These streams provide near real-time visibility into resource modifications across your AWS environment. You can use configuration streams to trigger automated responses to specific changes, integrate with external systems, or maintain awareness of infrastructure modifications as they occur.


- Configuration rules

  Configuration rules define the desired configuration settings for your AWS resources. Each rule represents a specific configuration requirement that your resources should meet to be considered compliant.

  AWS Config evaluates your resources against these rules and reports whether they are compliant or non-compliant. This evaluation happens automatically when resources change and can also be triggered on a schedule, providing continuous assessment of your environment against your governance requirements.


- Configuration recorder

  The configuration recorder is the component that captures resource configuration changes in your AWS account. It monitors supported resources and records their current state whenever changes occur.

  You must set up and start the configuration recorder before AWS Config can track your resources. You can customize which resource types to monitor and specify where to store the configuration information, giving you control over the scope of your configuration management.


- Configuration history

  Configuration history provides a timeline of changes for your AWS resources. For each supported resource, AWS Config maintains a chronological record of all configuration changes, including what changed, when it changed, and the relationships affected.

  This historical data helps you to understand how your infrastructure evolved over time, investigate when specific settings were modified, and restore previous configurations if needed. 
  The history is accessible through the AWS Config console, API, or as files delivered to an Amazon Simple Storage Service (Amazon S3) bucket. 


- Conformance packs

  Conformance packs are collections of AWS Config rules and remediation actions that can be deployed together as a single entity.
  They help you implement governance standards across multiple accounts and AWS Regions.

  Conformance packs typically represent a specific compliance framework or internal policy set.
  AWS provides sample conformance packs for common standards to help you implement industry-recognized security best practices across your organization.

## AWS Config key features and capabilities

AWS Config offers a robust set of features designed to help you maintain visibility, control, and compliance across your AWS environment, regardless of its size or complexity.

 
###  the key features of AWS Config.

- Resource discovery and inventory

  AWS Config automatically discovers supported resources in your AWS account and maintains an up-to-date inventory. This inventory includes resource attributes, configurations, and relationships with other resources.
  The discovery process runs continuously, so newly created resources are quickly added to your inventory. You can export this inventory data to analyze resource usage patterns, identify orphaned resources, or maintain an accurate record of your cloud assets for compliance purposes.


- Configuration snapshots and history

  AWS Config creates point-in-time snapshots of your resource configurations and maintains a detailed history of changes. These snapshots capture the complete state of monitored resources at specific moments.

  The configuration history shows what changed, when it changed, and who made the change. This historical record is invaluable for troubleshooting issues, preparing for audits, and understanding how your infrastructure has evolved over time.


- Compliance monitoring and reporting

  AWS Config evaluates your resources against rules that represent your ideal configuration settings. It continuously checks compliance and provides detailed reporting on which resources meet your requirements and which need attention.
  The compliance dashboard gives you a visual overview of your compliance status, and detailed reports help you identify specific non-compliant resources and understand why they failed. This ongoing assessment helps you maintain governance standards and quickly address deviations.

### the key capabilities of AWS Config.


- Multi-account, multi-Region aggregation

  AWS Config can aggregate configuration and compliance data from multiple AWS accounts and Regions into a single view. This capability is essential for organizations managing complex environments spread across different accounts and geographical locations.

  The aggregated view helps you maintain consistent governance across your entire AWS environment without having to switch between accounts or Regions. You can identify compliance trends, spot configuration drift, and enforce standardized policies throughout your organization.


- Automated remediation

  AWS Config supports automated remediation of non-compliant resources through Automation, a capability of AWS Systems Manager. When a resource fails a compliance check, AWS Config can trigger a predefined remediation action to fix the issue.

  This automation reduces the manual effort required to maintain compliance and decreases the time between detecting and resolving configuration issues. You can customize remediation actions based on your specific requirements and operational procedures.


- Resource relationship tracking

  AWS Config maps and tracks relationships between your AWS resources, providing visibility into how resources are connected and interdependent. This relationship data helps you understand the potential impact of changes and troubleshoot complex issues.

  For example, you can see which security groups are associated with which Amazon Elastic Compute Cloud (Amazon EC2) instances.
  You can also see which AWS Identity and Access Management (IAM) roles are attached to which AWS Lambda functions.
  This relationship mapping is particularly valuable when assessing the security implications of configuration changes or planning infrastructure modifications.

https://aws.amazon.com/config/features/


## AWS Config practical business applications

 
- Compliance management and reporting 

  Organizations use AWS Config to demonstrate compliance with internal policies and external regulations.
  The service continuously evaluates resources against compliance rules and generates detailed reports that auditors can review.

  A financial services company might use AWS Config to verify that all S3 buckets containing customer data are encrypted and not publicly accessible.
  This automated compliance checking reduces the manual effort required for audit preparation and provides evidence that security controls are functioning correctly.

- Security incident investigation

  Security teams rely on AWS Config to investigate potential security incidents by examining the configuration history of affected resources. This historical data helps determine when and how security vulnerabilities were introduced.

  When investigating unauthorized access to a resource, security analysts can use AWS Config to review configuration changes leading up to the incident. They can identify when security group rules were modified, IAM permissions were expanded, or encryption settings were disabled, helping pinpoint the root cause of the security breach.

- Change management and tracking
  IT operations teams use AWS Config to maintain a complete record of infrastructure changes for troubleshooting and governance purposes. The configuration timeline shows who changed what and when, creating accountability and traceability.

  During a service disruption, operations staff can review the AWS Config history to identify recent changes that might have caused the issue. This capability reduces mean time to resolution by quickly narrowing down potential causes and providing context about the environment before the problem occurred.

- Resource optimization and cost management

  Finance and cloud operations teams use AWS Config to identify unused or non-standard resources that might represent unnecessary costs.
  The resource inventory helps spot opportunities for consolidation or retirement.

  A company might use AWS Config to find unattached Amazon Elastic Block Store (Amazon EBS) volumes,
  idle load balancers, or oversized instances that don't match standard configurations. By addressing these inefficiencies, organizations can reduce cloud spending and maintain appropriate governance controls.


## Check your knowledge

The following section will check your understanding of AWS Config.

1. What is a core function of AWS Config?


- Providing vulnerability scanning for Amazon EC2 instances
- Continuously monitoring and recording configuration changes to AWS resources
- Automatically scaling applications based on demand
- Managing the deployment of infrastructure as code (IaC) templates

 
AWS Config continuously monitors and records configuration changes to AWS resources, which is one of its core functions.

2. What is a technical concept related to AWS Config?


- Resource groups organize AWS Config rules into logical collections.
- Execution roles determine which users can access the AWS Config console.
- Configuration items represent point-in-time records of AWS resource attributes and settings.
- Deployment pipelines automate the delivery of AWS Config rules.

 
Configuration items are a fundamental technical concept in AWS Config, representing point-in-time records of AWS resource attributes and settings.

3. What is a key feature of AWS Config?

- Managed database backup and restoration capabilities
- Automatic provisioning of resources based on templates

- Automatic instance recovery after hardware failures
- Point-in-time snapshots of your resource configurations

 
AWS Config creates point-in-time snapshots of your resource configurations, which is a key feature that helps maintain a historical record of your infrastructure.

4. What is a practical business application of AWS Config?


- Marketing campaign optimization through usage analytics
- Security incident investigation through configuration history review
- Customer relationship management through resource tagging
- Employee performance tracking through resource utilization
 
A practical business application of AWS Config is security incident investigation, 
where teams review configuration history to determine when and how security vulnerabilities were introduced.


# Technical Overview for AWS Config


## Lesson objectives

By the end of this lesson, you will be able to do the following:

- Identify the elements of the AWS Config service architecture.
- Identify the key service integrations for AWS Config.


## AWS Config architecture

AWS Config architecture centers around capturing, storing, and evaluating resource configurations across your AWS environment.
The service processes configuration data through several components that work together to provide comprehensive visibility and governance.

<img width="1680" height="961" alt="image" src="https://github.com/user-attachments/assets/36bb3733-b4c5-4c61-bc05-5ff22e7955f5" />

<img width="1006" height="589" alt="image" src="https://github.com/user-attachments/assets/c5c91df8-d221-4383-b62c-25a03c57b920" />

1. Initial detection
AWS Control Tower identifies VPC Flow Logs configuration changes or violations through continuous monitoring of the AWS environment.

2. Lambda processing
A Lambda function receives the detection event from AWS Control Tower and processes the information to determine appropriate remediation steps.

3. CloudFormation deployment
AWS CloudFormation receives instructions from the Lambda function and initiates the stack set deployment across specified accounts.

4. AWS Config rule evaluation
The AWS Config rule performs Regional scans of all virtual private clouds (VPCs), evaluating their flow log status. VPCs without flow logs enabled are marked as non-compliant resources.

5. Automation trigger
When a VPC is marked non-compliant, the Automation document automatically triggers to begin the remediation process.

6. Remediation action
Using the assigned IAM role permissions, the Automation document executes predefined remediation steps to configure flow logs on non-compliant VPCs.

7. Flow log creation
Amazon Virtual Private Cloud (Amazon VPC) creates and configures the flow logs according to the specified requirements, with logs being stored in the designated archival bucket.

8. Logs archival
VPC Flow Logs are automatically archived to the specified S3 bucket in the log archive account for retention and analysis.

## AWS Config integrations

AWS Config works with numerous AWS services to extend its capabilities and provide a comprehensive governance solution for your cloud environment.


- Amazon S3

  AWS Config uses Amazon S3 to store configuration history files, snapshots, and evaluation results. This integration provides durable, long-term storage for your configuration data.

  S3 buckets serve as the repository for all the detailed configuration information that AWS Config collects. You can access this data directly from Amazon S3 for custom analysis or integration with other systems, and apply S3 lifecycle policies to manage retention according to your requirements.


- Amazon SNS

  - AWS Config sends notifications about configuration changes and compliance evaluations to Amazon SNS topics. These notifications keep you informed about important events in your environment.
  - When resources are created, modified, or deleted, or when compliance status changes, AWS Config publishes messages to your configured SNS topic. You can subscribe various endpoints to these topics to build automated workflows triggered by configuration changes. Endpoints include resources such as email addresses, Lambda functions, or Amazon Simple Queue Service (Amazon SQS) queues.

- AWS CloudTrail
  AWS Config integrates with AWS CloudTrail to provide context about who made configuration changes. This integration helps establish accountability and traceability.
  While AWS Config records what changed in your resources, CloudTrail records who performed the API calls that caused those changes. Together, these services give you complete visibility into both the technical details of changes and the human or system actors responsible for them.


- AWS Organizations
  AWS Config works with AWS Organizations to deploy configuration rules and conformance packs across multiple accounts. This integration supports centralized governance at scale.
  Organization administrators can define configuration rules once and apply them consistently across all accounts in the organization. This capability helps you maintain governance standards throughout your AWS environment without having to configure each account individually.


- Lambda

  AWS Config uses Lambda functions to evaluate custom configuration rules. With this integration, you can create specialized compliance checks for your unique requirements.

  When you define a custom rule, you provide a Lambda function that contains the evaluation logic. AWS Config invokes this function on a schedule or whenever relevant resources change, giving you flexibility to implement complex or organization-specific compliance checks.


- AWS Systems Manager

  AWS Config integrates with Systems Manager to automate remediation of non-compliant resources. This integration helps maintain continuous compliance with minimal manual intervention.
  When AWS Config detects a non-compliant resource, it can trigger an Automation document to correct the issue. For example, if a security group is found with overly permissive rules, an Automation document can automatically modify the rules to match your security requirements.


- Amazon EventBridge
  AWS Config works with Amazon EventBridge to trigger automated responses to configuration changes and compliance events. This integration supports event-driven architecture for configuration management.

  EventBridge can detect AWS Config events and route them to target services based on rules you define. With this capability, you can build sophisticated workflows that respond to specific configuration changes or compliance violations, such as creating tickets, sending alerts, or executing remediation scripts.

