https://skillbuilder.aws/learn/NHAM6FHVS8/aws-control-tower-getting-started/


# Introduction to AWS Control Tower
 
By the end of this lesson, you will be able to do the following:

Identify the core functionality of AWS Control Tower.

Identify the technical concepts related to AWS Control Tower.

Identify the key features and capabilities of AWS Control Tower.

Identify the practical applications of AWS Control Tower.



## AWS Control Tower introduction

AWS Control Tower is a service that provides a streamlined way to set up and govern a secure, multi-account Amazon Web Services (AWS) environment. It automates the creation of a landing zone based on best practices, which establishes a baseline environment for your AWS journey.


 

AWS Control Tower orchestrates multiple AWS services to create a secure, multi-account environment known as a landing zone. 
This centralized approach integrates AWS Organizations, AWS IAM Identity Center, AWS CloudTrail, and AWS Config to provide comprehensive account management and logging capabilities. 
Through AWS Control Tower Account Factory and guardrails, AWS Control Tower streamlines account creation and enforces compliance and security standards across your company's AWS infrastructure.


## AWS Control Tower core functionality

AWS Control Tower delivers three primary functions that work together to help you govern your AWS environment at scale. These functions create a foundation for your cloud operations that balances centralized control with team autonomy.


- Landing zone setup

  AWS Control Tower automates the creation of a well-architected multi-account environment based on AWS best practices. This landing zone includes a logically separated organizational structure with dedicated accounts for management, log archive, and audit purposes.

  The landing zone setup process configures core services like AWS Organizations, IAM Identity Center, and centralized logging. This automation saves you significant time compared to manually building these foundational elements and helps prevent configuration errors.


- Guardrails implementation

  Guardrails are high-level rules that provide ongoing governance for your AWS environment. They help you implement compliance requirements by preventing deployment of resources that don't conform to your policies.

  AWS Control Tower offers two types of guardrails. Preventive guardrails use service control policies (SCPs) to stop actions before they occur.
  Detective guardrails use AWS Config rules to identify non-compliant resources after they are created. This dual approach helps maintain security and compliance across your organization.


- Account factory provisioning

  Account Factory provides a standardized, automated way to provision and configure new AWS accounts that conform to your organization's compliance requirements.
  This self-service capability helps teams move quickly and maintain governance.

  Account Factory integrates with AWS Service Catalog to create a repeatable process for account creation.
  Administrators can define account baselines and network configurations, and developers and teams can provision compliant accounts without waiting for central IT approval processes.


>  AWS Control Tower helps you set up and govern a secure, multi-account AWS environment.

## AWS Control Tower technical concepts

AWS Control Tower operates across multiple IT domains, including cloud governance, identity management, security, and compliance. Understanding these technical concepts is essential for effectively implementing and managing your AWS Control Tower environment.


- Organizations and organizational units
  Organizations in AWS Control Tower represent the hierarchical structure of your accounts. An organization is the root container for all your AWS accounts, and organizational units (OUs) are logical groupings of accounts within that structure.

  AWS Control Tower creates a recommended OU structure during landing zone setup, including Security, Sandbox, and custom OUs. This structure helps you apply appropriate guardrails and policies to different groups of accounts based on their purpose and compliance requirements.


- Landing zone
  
  A landing zone is a well-architected, multi-account AWS environment that follows best practices for security and compliance.
  It serves as the foundation for your cloud adoption journey.
 
  AWS Control Tower automates the creation of your landing zone, configuring core accounts, networking, security services, and logging.
  This automation reduces the time and specialized knowledge needed to build a secure foundation for your AWS environment.


- Guardrails
  Guardrails are governance rules that help you maintain control over your AWS environment.
   They implement specific governance, compliance, or security requirements across multiple accounts.

  Each guardrail has a specific intent and enforcement level. Mandatory guardrails are automatically enabled and cannot be disabled, and strongly recommended and elective guardrails can be enabled based on your organization's needs.


- Account Factory

  Account Factory is a standardized account-provisioning service that helps you create new AWS accounts that comply with your organization's standards.
  It provides a repeatable blueprint for account creation.

  Account Factory integrates with Service Catalog to offer self-service account provisioning capabilities. Users with appropriate permissions can create accounts through the AWS Control Tower console or programmatically through APIs.


- Drift detection

  Drift occurs when resources in your AWS Control Tower environment are modified outside of the AWS Control Tower governance. Drift detection identifies these changes that might compromise your governance model.

  AWS Control Tower periodically scans your environment for drift and notifies administrators when it's detected. You can then repair the drift to bring your environment back into compliance with your governance model.


- Shared responsibility model
  The AWS Shared Responsibility Model defines the security responsibilities between AWS and customers. AWS secures the infrastructure that runs AWS Control Tower, and you're responsible for how you configure and use the service.

  AWS Control Tower helps you implement your side of the shared responsibility model by providing guardrails and governance capabilities. However, you must still configure these features appropriately for your security and compliance needs.


- Baseline configuration
  Baseline configuration represents the standard settings and services deployed to each account in your AWS Control Tower environment. It establishes a consistent starting point for all accounts.

  The AWS Control Tower baseline includes identity management, logging configurations, and security services. This standardization helps maintain governance and reduces the effort required to configure new accounts.


- Compliance frameworks
  Compliance frameworks are structured sets of guidelines and practices designed to help organizations meet regulatory requirements.
  AWS Control Tower helps implement controls that support compliance with various frameworks.

  Guardrails in AWS Control Tower can be mapped to requirements from framework, such as the following:

  - National Institute of Standards and Technology (NIST)

  - Payment Card Industry Data Security Standard (PCI DSS)

  - Health Insurance Portability and Accountability Act of 1996 (HIPAA)

  This mapping helps you demonstrate compliance and reduces the effort required to prepare for audits.


## AWS Control Tower key features and capabilities

AWS Control Tower offers a comprehensive set of features and capabilities designed to help you establish and maintain governance over your AWS environment. These tools work together to provide security, compliance, and operational excellence at scale.

Review the following to learn more about the key features of AWS Control Tower.


- Centralized dashboard
The AWS Control Tower dashboard provides a unified view of your multi-account environment. It displays the status of your accounts, guardrails, and compliance posture.

The dashboard highlights issues requiring attention, such as guardrail violations or account drift. This visibility helps administrators quickly identify and address governance concerns across the organization.


- Automated account provisioning
AWS Control Tower automates the creation of new AWS accounts through Account Factory. This automation applies standardized configurations and guardrails to each new account.

Account provisioning can be initiated through the AWS Control Tower console or programmatically through APIs. This flexibility supports both human-driven and automated workflows for account creation without compromising governance standards.


- Guardrail library
  AWS Control Tower includes a library of pre-built guardrails that implement common governance, security, and compliance controls. These guardrails can be selectively applied to different organizational units.

  The guardrail library continues to expand with new controls based on customer feedback and evolving best practices. This growing collection helps you implement comprehensive governance without developing custom policies from scratch.

Review the following to learn more about the key capabilities of AWS Control Tower.


- Multi-account management
  
  AWS Control Tower provides tools to organize and manage multiple AWS accounts from a central location. This capability is essential for organizations that need to maintain separate accounts for different teams or workloads.

  The service integrates with AWS Organizations to create a hierarchical structure of accounts and organizational units. This structure helps you apply appropriate policies and guardrails at different levels of your organization.


- Continuous compliance monitoring
  AWS Control Tower continuously monitors your environment for compliance with enabled guardrails. This monitoring helps identify resources or configurations that violate your governance policies.

  When non-compliant resources are detected, AWS Control Tower logs the violation and can notify administrators. This capability helps maintain your compliance posture over time as your environment changes and grows.


- Customizable controls
  With AWS Control Tower, you can customize your governance model to meet specific organizational requirements. You can select which guardrails to enable for different parts of your organization.

  Beyond the built-in guardrails, you can extend AWS Control Tower with custom controls using AWS CloudFormation hooks and AWS Config rules.
  This extensibility helps you address unique governance requirements and maintain the benefits of the managed service.


https://aws.amazon.com/controltower/features/


## AWS Control Tower practical business applications

Review the following practical business applications for AWS Control Tower.

- Accelerating cloud adoption
  Organizations use AWS Control Tower to accelerate their cloud adoption by starting with a well-architected foundation. The service provides a ready-to-use environment that follows AWS best practices for security and operations.
  
  By automating the setup of foundational elements like identity management, logging, and security controls, AWS Control Tower reduces the time to establish a production-ready environment. This acceleration helps businesses quickly realize cloud benefits and maintain appropriate governance.

- Enforcing regulatory compliance
  Financial institutions and healthcare organizations use AWS Control Tower to implement controls required by regulations like General Data Protection Regulation (GDPR), HIPAA, and PCI DSS. The service's guardrails help enforce these requirements across all accounts.

  AWS Control Tower detective guardrails continuously monitor the environment for compliance violations and provide audit trails of resource configurations. This monitoring capability helps organizations demonstrate compliance during audits and quickly address any deviations.

- Managing decentralized IT
Large enterprises with decentralized IT teams use AWS Control Tower to balance central governance with team autonomy. Through this service, central IT sets guardrails that support team innovation within defined boundaries.

Account Factory enables self-service account provisioning that automatically applies organizational standards. This capability reduces bottlenecks in account creation and helps you confirm that all accounts meet security and compliance requirements.

- Supporting mergers and acquisitions
  Companies undergoing mergers or acquisitions use AWS Control Tower to integrate acquired IT assets into their governance framework. The service helps establish consistent controls across previously separate environments.

  The ability of AWS Control Tower to enroll existing accounts helps organizations bring acquired AWS accounts into compliance with corporate standards.
  This capability reduces the security and compliance risks often associated with mergers and acquisitions.

## Check your knowledge

The following section will check your understanding of AWS Control Tower.

1. What is a core function of AWS Control Tower?


- Providing detailed cost analysis for each AWS account


- Automating the deployment of machine learning (ML) models
- Implementing guardrails to enforce governance policies

- Managing DNS routing between AWS Regions  


A core function of AWS Control Tower is implementing guardrails to enforce governance policies across your AWS environment.



2. What is a technical concept related to AWS Control Tower?


- Drift detection that identifies unauthorized changes
- Container orchestration for microservices applications
- Database sharding for horizontal scaling
- Network packet inspection for intrusion detection
 
Drift detection is a technical concept related to AWS Control Tower that identifies when resources are modified outside of the governance of AWS Control Tower.

3. What is a key feature of AWS Control Tower?


- Real-time language translation for global applications

- Automated database query optimization

- Centralized dashboard for multi-account governance

- Edge computing capabilities for Internet of Things (IoT) devices

 
A key feature of AWS Control Tower is the centralized dashboard that provides visibility into your multi-account environment and governance status.


4. What is a practical business application of AWS Control Tower?


- Processing high-volume financial transactions
- Analyzing genomic data for medical research
- Rendering 3D graphics for animation studios
- Enforcing regulatory compliance across accounts

 
A practical business application of AWS Control Tower is enforcing regulatory compliance across accounts through consistent guardrails and monitoring.




# Technical Overview for AWS Control Tower
 

By the end of this lesson, you will be able to do the following:

Identify the elements of the AWS Control Tower service architecture.

Identify the key service integrations for AWS Control Tower.

## AWS Control Tower architecture

AWS Control Tower architecture consists of interconnected AWS services working together to provide governance at scale. 
The service orchestrates these components to create a secure, well-structured environment that serves as the foundation for your AWS Cloud presence.


<img width="1680" height="943" alt="image" src="https://github.com/user-attachments/assets/5d832a81-2827-45d0-a2d4-19daa66f1bdc" />

<img width="903" height="513" alt="image" src="https://github.com/user-attachments/assets/cada73d1-4e0c-43a3-b55f-b98e24c366f9" />



1. AWS Control Tower setup
AWS Control Tower sets up the foundational structure in the management account, which creates the basis for a well-architected multi-account AWS environment.

2. AWS Organizations configuration
AWS Organizations is established to create and manage multiple AWS accounts. It implements hierarchal structures and OUs.

3. Identity management
IAM Identity Center provides centralized access management. It sets up single sign-on capabilities and identity federation for your AWS environment.


4. AWS CloudFormation StackSets deployment
AWS CloudFormation StackSets automatically deploys templates across accounts and AWS Regions to establish consistent configurations and resources.

5. Service integration
Service Catalog connects with AWS Control Tower to provide a curated collection of approved IT services, templates, and configurations.


6. Log archive setup
The log archive account centralizes logging functionality by collecting and storing CloudTrail logs and other audit-related information across the organization.

7. Audit configuration
The audit account implements centralized security tooling and monitoring,
with Amazon Simple Notification Service (Amazon SNS) notifications and AWS Config record resource configurations.

8. Account provisioning
Provisioned accounts receive standardized baselines, including network configurations and AWS Backup policies.
This helps maintain organizational compliance and security standards.


https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html


## AWS Control Tower integrations

AWS Control Tower integrates with numerous AWS services to deliver its governance capabilities. These integrations extend the functionality of AWS Control Tower and helps you build a comprehensive cloud management solution.


- AWS Organizations
  AWS Organizations provides the foundational account structure for AWS Control Tower. AWS Control Tower uses Organizations to create and manage OUs and to apply SCPs.


- AWS Config
  AWS Config provides the configuration monitoring capabilities that power AWS Control Tower detective guardrails.
  It records resource configurations and evaluates them against rules that define your compliance requirements.

  AWS Control Tower automatically sets up AWS Config in each enrolled account and deploys rules that implement detective guardrails. The service also configures AWS Config to deliver logs to your centralized log archive account for comprehensive auditing.


- AWS CloudTrail
  CloudTrail records API activity across your AWS accounts, providing an audit trail of actions taken in your environment. AWS Control Tower automatically configures CloudTrail in each enrolled account.

  CloudTrail logs are centralized in the log archive account created by AWS Control Tower. This centralization helps security teams monitor activity across all accounts from a single location and supports compliance requirements for comprehensive audit logging.


- AWS IAM Identity Center
  AWS IAM Identity Center provides unified access management for your AWS Control Tower environment. It allows you to manage user access to multiple AWS accounts from a central location.

  AWS Control Tower configures IAM Identity Center during landing zone setup, creating default permission sets for common roles. This integration streamlines access management across your multi-account environment and supports the principle of least privilege.


- AWS Service Catalog
  Service Catalog powers the Account Factory capability in AWS Control Tower. It provides the self-service provisioning interface that makes it possible for users to create standardized accounts.

  Account Factory uses Service Catalog products to define the account baseline and configuration options. This integration enables customizable yet compliant account provisioning that meets your organization's requirements.


- Amazon S3
  Amazon Simple Storage Service (Amazon S3) stores logs and other artifacts generated by AWS Control Tower and its integrated services. The service automatically creates S3 buckets in the log archive account to store CloudTrail and AWS Config logs.

  AWS Control Tower configures appropriate bucket policies and encryption settings to protect the sensitive information contained in these logs. This integration provides secure, durable storage for your compliance and audit data.


- AWS Lambda
  Lambda functions perform many of the automated actions in AWS Control Tower. These functions respond to events and make API calls to configure services and implement guardrails.

  AWS Control Tower deploys Lambda functions to detect and respond to drift, implement custom guardrails, and perform other automation tasks.
  This integration extends the capabilities of AWS Control Tower beyond what's possible with built-in service configurations alone.

### Integration considerations

When integrating AWS Control Tower with other services, consider security, scalability, and data management requirements for optimal performance and reliability.


- Security

  Use IAM roles and policies to manage service access to AWS Control Tower, implement encryption for sensitive data, and follow security best practices for authentication. Regularly audit access patterns and permissions to maintain a strong security posture. Consider implementing additional security layers, such as virtual private cloud (VPC) endpoints or private links where applicable to minimize exposure to public networks.
 

- Scalability
  Design integrations with AWS Control Tower to handle varying workloads by implementing proper error handling and retry mechanisms. Monitor service quotas and request increases when needed to accommodate growth.
  Use asynchronous processing patterns where appropriate to decouple components and improve system resilience during peak loads.

- Monitoring
  Set up comprehensive monitoring for AWS Control Tower using CloudWatch metrics and create appropriate alarms to detect potential issues early. Implement logging for troubleshooting and optimization, and consider setting up dashboards to visualize key performance indicators (KPIs).
  Establish automated notification systems to alert teams when predefined thresholds are exceeded.

## Check your knowledge

The following section will check your understanding of AWS Control Tower.

1. What is an element of AWS Control Tower service architecture?


- Content delivery network (CDN) for global distribution

- Quantum computing simulator for algorithm testing

- Blockchain ledger for immutable record keeping

- Log archive account for centralized logging functionality

 
The log archive account is an element of AWS Control Tower service architecture that centralizes audit logs from all accounts in your organization.

2. What is a service that integrates with AWS Control Tower?


- Amazon Mechanical Turk for human task processing

- AWS Organizations for account hierarchy management

- AWS DeepRacer for reinforcement learning

- Amazon Comprehend for natural language processing (NLP)

 
AWS Organizations is a service that integrates with AWS Control Tower to provide the foundational account structure and management capabilities.


# AWS Control Tower Demonstrations
 

By the end of this lesson, you will recognize how to use the AWS Management Console to perform the basic functions of AWS Control Tower.

This lesson contains the following demonstrations:

Setting Up AWS Control Tower Landing Zone

Exploring AWS Control Tower Dashboard and Resources

Creating a New Account Using AWS Control Tower Account Factory

Deleting AWS Control Tower Resources

Performing the following demonstrations in an AWS account can have an associated cost. 
To avoid incurring fees, do not perform these demonstrations in your AWS environment. If you choose to perform the demonstrations in your environment, you will need to clean up any resources you create to avoid incurring additional unwanted fees.

 
## Setting Up AWS Control Tower Landing Zone
In this demonstration, you will learn how to set up AWS Control Tower through the AWS Management Console.

https://youtu.be/25C_DlBYJjc

## Exploring AWS Control Tower Dashboard and Resources

In this demonstration, you will explore the AWS Control Tower dashboard in the AWS Management Console.

https://youtu.be/j5kVRQpVS1Q

## Creating a New Account Using AWS Control Tower Account Factory

In this demonstration, you will learn how to create a new account using AWS Control Tower Account Factory.

https://youtu.be/_bc63T5kqwM

## Deleting AWS Control Tower Resources

In this demonstration, you will learn how to remove the resources you created during this lesson. 
To clean up the AWS environment, you will use the AWS Management Console to delete AWS Control Tower and any related items.

 https://www.youtube.com/watch?v=25C_DlBYJjc


 https://docs.aws.amazon.com/controltower/latest/userguide/manual-cleanup-required.html


 # Learn More
 
### AWS Control Tower user guides

To learn more information about AWS Control Tower, review the following.

[AWS Control Tower Documentation](https://docs.aws.amazon.com/controltower/)

To access documentation for users of AWS Control Tower, choose DOCUMENTATION.

 
[AWS Control Tower User Guide](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)

To access the guidance for AWS Control Tower, choose USER GUIDE.

 
### Use cases and best practices for AWS Control Tower

To learn more about the use cases and best practices for implementing AWS Control Tower, review the following.

[AWS Control Tower blogs](https://aws.amazon.com/blogs/publicsector/category/management-tools/aws-control-tower/)

To learn more about AWS Control Tower, choose AWS BLOG POSTS.
 
[Ask the AWS Control Tower team](https://repost.aws/)

To ask questions about AWS Control Tower, choose AWS RE:POST and tag your questions with AWS Control Tower.

 
[AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)

The AWS Well-Architected Framework helps you understand the pros and cons of decisions you make while building systems on AWS. To learn more, choose FRAMEWORK.

 
### AWS Control Tower pricing

To learn more about pricing for AWS Control Tower, review the following.

[AWS Control Tower pricing](https://aws.amazon.com/controltower/pricing/)

To learn more about AWS Control Tower pricing, choose PRICING.
 
[AWS Pricing Calculator](https://calculator.aws/#/)
To estimate the cost for your architecture solution, choose PRICING CALCULATOR.
