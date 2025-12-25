https://skillbuilder.aws/learn/YJ5XKSDUNA/aws-security-hub-cspm-getting-started/


# Introduction to AWS Security Hub CSPM
 

By the end of this lesson, you will be able to do the following:

- Identify the core functionality of Security Hub CSPM.
- Identify the technical concepts related to Security Hub CSPM.
- Identify the key features and capabilities of Security Hub CSPM.
- Identify the practical applications of Security Hub CSPM.

CSPM stands for cloud security posture management

## AWS Security Hub CSPM introduction

Security Hub has enhanced its capabilities, evolving from a centralized security findings aggregator and security posture management service to a comprehensive unified cloud security solution. What you previously knew as Security Hub, focused on aggregating security findings, security best practice checks, and compliance monitoring, is now Security Hub CSPM—a core capability within the enhanced Security Hub solution.


Building on this foundation, Security Hub now automatically correlates security signals across multiple capabilities including vulnerability management (Amazon Inspector), threat detection (Amazon GuardDuty), posture management (AWS Security Hub CSPM), and sensitive data discovery (Amazon Macie).

This enhanced correlation helps you identify critical security risks that might be missed when viewing findings in isolation.

## Security Hub CSPM core functionality

Security Hub CSPM delivers core functionality that helps organizations maintain a strong security posture across their AWS environments.
It acts as a central dashboard for security findings, and provides visibility into your security state and compliance status.


- Security findings aggregation

  Security Hub CSPM collects and consolidates findings from integrated AWS services such as Amazon GuardDuty, Amazon Inspector, and Amazon Macie. It normalizes these findings into a standard format, making it easier to understand security issues across different services.

  The service also integrates with third-party security tools, to bring all security findings into a single location. This eliminates the need to switch between multiple dashboards and provides a comprehensive view of your security posture.


- Security standards compliance

  Security Hub CSPM automatically checks your AWS resources against security standards. These standards include the AWS Foundational Security Best Practices and the Center for Internet Security (CIS) AWS Foundations Benchmark. These checks help you identify areas where your security configuration might not meet industry best practices.

  The service continuously monitors your environment and provides compliance scores that show how well your resources align with these standards. This ongoing assessment helps you track improvements in your security posture over time.


- Automated security response

  Security Hub CSPM  supports automated response and remediation through integration with Amazon EventBridge.
  When Security Hub detects a security issue, it can trigger automated workflows to address the problem without manual intervention.

  You can create custom actions in Security Hub that send findings to EventBridge, which then initiates remediation actions using AWS Lambda functions or other AWS services.
  This automation helps organizations respond to security issues quickly and consistently while reducing the manual workload on security teams.

## Security Hub technical concepts

Understanding Security Hub CSPM requires familiarity with several IT domains including cloud security, compliance frameworks, and security operations. These domains provide the foundation for effectively implementing and using Security Hub CSPM in your AWS environment.


- Security findings

  Security findings represent discovered security issues within your AWS environment. Each finding contains details about the security issue, including the affected resource, the severity of the issue, and recommendations for remediation.

  Security Hub CSPM  uses the AWS Security Finding Format (ASFF), a standardized JSON format for security findings. This standardization makes it possible to normalize findings from different sources, to provide a consistent view of security issues across your environment.


- Security standards

  Security standards are collections of security controls that help you assess your security posture against industry best practices.
  Security Hub CSPM  supports several standards, including AWS Foundational Security Best Practices, CIS AWS Foundations Benchmark, and Payment Card Industry Data Security Standard (PCI DSS).

  Each standard contains multiple controls that check specific aspects of your AWS configuration.
  Security Hub CSPM automatically evaluates your resources against these controls and provides a compliance score for each standard, to help you identify areas for improvement.


- Security controls

  Security controls are specific checks that evaluate whether your AWS resources comply with security best practices.
  Each control focuses on a particular security requirement, such as ensuring that Amazon Simple Storage Service (Amazon S3) buckets are not publicly accessible.

  Controls are grouped into categories based on their security focus, such as data protection or infrastructure security.
  Security Hub CSPM runs these controls automatically and provides detailed results that help you understand and address any compliance issues.


- Cross-Region aggregation

  Cross-Region aggregation allows you to designate a home Region that collects and consolidates findings from multiple AWS Regions.
  This feature provides a unified view of your security posture across your global AWS infrastructure.

  When you enable cross-Region aggregation, Security Hub CSPM  automatically replicates findings from linked Regions to your home Region.
  This centralization makes it easier to monitor and manage security across your entire AWS environment.


- Security scores

  Security scores provide a quantitative measure of your security posture.
  Security Hub CSPM calculates scores for each security standard and for your overall environment based on the results of security control checks.

  These scores help you track your security posture over time and identify trends.
  A higher score indicates better alignment with security best practices, and a lower score highlights areas that need attention.


- Custom insights

  Custom insights are queries that group and filter security findings based on criteria that you define. These insights help you focus on specific security issues that are most relevant to your organization.

  You can create custom insights to track particular types of resources, specific vulnerabilities, or findings with certain attributes.
  These insights make it easier to prioritize your security efforts and monitor issues that matter most to your organization.

## Security Hub key features and capabilities

Security Hub CSPM offers a robust set of features and capabilities designed to strengthen your security posture and streamline security management across your AWS environment. These tools help security teams identify, prioritize, and respond to security issues efficiently.

Review the following to learn more about the key features of Security Hub CSPM.


- Consolidated security findings
  Security Hub CSPM aggregates findings from multiple AWS security services and supported third-party products into a standardized format. This consolidation eliminates the need to check multiple dashboards and tools to understand your security status.


- Automated compliance checks
  Security Hub CSPM  automatically checks your AWS resources against industry standards and best practices. It continuously evaluates your environment against frameworks like the CIS AWS Foundations Benchmark, AWS Foundational Security Best Practices, and PCI DSS.

  Each compliance check produces a pass or fail result, along with details about the resources that failed the check and recommendations for remediation. These automated checks help you maintain compliance without manual effort and identify security gaps before they become problems.


- Security score
  Security Hub CSPM calculates security scores that provide a quantitative measure of your security posture. These scores are calculated for each enabled security standard and for your overall environment.

  The scoring system helps you track improvements in your security posture over time and identify areas that need attention. Security scores make it easier to communicate security status to stakeholders and demonstrate the impact of security investments.


- Multi-account management

  Security Hub CSPM integrates with AWS Organizations to provide centralized security management across multiple AWS accounts. The service automatically consolidates security findings from member accounts into a designated administrator account, and provides a unified view of your organization's security posture.

  This centralized approach helps large organizations maintain consistent security practices and monitor security across their entire AWS environment from a single location. The administrator account can enable security standards, view aggregated findings, and track security scores for all member accounts, to enhance the efficiency of security management at scale.

Review the following to learn more about the key capabilities of Security Hub CSPM.


- Cross-Region aggregation

  Cross-Region aggregation in Security Hub CSPM consolidates findings from multiple AWS Regions into a designated home Region. This centralization simplifies security monitoring for global AWS infrastructures. The unified view across all Regions helps organizations maintain consistent security oversight regardless of where their resources are deployed.


- Custom actions and response
  
  Custom actions and automated response capabilities in Security Hub CSPM integrate with EventBridge to enable automated responses to findings.

  Organizations can create custom actions that trigger specific remediation workflows based on their security requirements.

  These automated responses help security teams address issues quickly and consistently, thus reducing the time between detection and remediation of security concerns.

https://aws.amazon.com/security-hub/cspm/features/

## Security Hub CSPM practical business applications

Review the following practical business applications for Security Hub CSPM.

- Centralized security monitoring
  Security Hub CSPM helps large enterprises with complex AWS environments maintain visibility across their entire cloud infrastructure. By aggregating security findings from multiple accounts and Regions, security teams can monitor their organization's security posture from a single dashboard.

  Organizations with distributed teams benefit from having a central location to view and manage security issues.
  This centralization reduces the risk of security gaps that might occur when monitoring is fragmented across different teams or tools.

- Compliance management and reporting

  Financial services organizations use Security Hub CSPM to demonstrate compliance with industry regulations such as PCI DSS.
  Security Hub CSPM automated compliance checks provide continuous assessment against regulatory requirements and security standards.

  Security Hub CSPM generates compliance reports that can be shared with auditors and regulators, which reduces the manual effort required for compliance documentation.
  These reports show compliance status across the organization and track improvements over time.

- Third-party security tool integration

  Organizations with existing security tools use Security Hub CSPM to integrate these tools with their AWS environment.
  The service supports integrations with popular third-party security products, and brings findings from these tools into the same dashboard as AWS security findings.

  This integration capability helps organizations maintain their security investments while gaining the benefits of centralized security management.
  Security teams can continue using familiar tools while getting a comprehensive view of their security posture across all systems.

## Check your knowledge

The following section will check your understanding of Security Hub.

1. What is a core function of AWS Security Hub CSPM?


- Managing AWS Identity and Access Management (IAM) user permissions

- Providing virtual private cloud networking capabilities

- Security findings aggregation from multiple AWS services
 

- Deploying code to AWS Lambda functions

 
A core function of Security Hub CSPM  is security findings aggregation from multiple AWS services, which consolidates security alerts into a standardized format.

2. What is a technical concept related to AWS Security Hub CSPM ?


- Container orchestration clusters
- Security controls that evaluate AWS resource compliance

- Database sharding techniques
- Machine learning model training

  
Security controls that evaluate AWS resource compliance is a technical concept related to Security Hub CSPM. These controls check whether resources meet security best practices.

3. What is a key feature of AWS Security Hub CSPM?


- Creating and managing AWS infrastructure as code

- Processing big data workloads

- Hosting static websites

- Automated compliance checks against industry standards

 
A key feature of Security Hub CSPM is automated compliance checks against industry standards, which continuously evaluate your environment against security frameworks.

4. What is a practical business application of AWS Security Hub CSPM ?


- Centralized security monitoring across AWS accounts
- Processing customer payments
- Developing mobile applications
- Managing employee payroll systems

 
A practical business application of Security Hub CSPM is centralized security monitoring across AWS accounts, 
which helps organizations maintain visibility across their entire cloud infrastructure.  

---

# Technical Overview for AWS Security Hub CSPM


Lesson objectives

By the end of this lesson, you will be able to do the following:

Identify the elements of the Security Hub CSPM architecture.

Identify the key integrations for Security Hub CSPM.



## Security Hub CSPM architecture

Security Hub CSPM architecture is designed to collect, process, and analyze security findings from multiple sources across your AWS environment. 
The service ingests data from integrated AWS services and third-party tools, normalizes this data into a standard format, and provides tools for analysis and response.



<img width="1098" height="841" alt="image" src="https://github.com/user-attachments/assets/52992206-badf-4edc-8952-5ef9c8b56f57" />
<img width="682" height="529" alt="image" src="https://github.com/user-attachments/assets/bb4099a1-216e-4c7b-9878-40dc1575e82e" />

1. Finding providers

Finding providers are AWS services and third-party products that generate security findings and send them to Security Hub CSPM. These include various AWS security services and supported third-party security tools.

2. AWS Security Finding Format
   
ASFF is the standardized JSON format that Security Hub CSPM uses to normalize findings from different sources.
This standardization ensures consistent processing and display of security information regardless of its origin.

3. Security standards processor

The security standards processor runs automated compliance checks against your AWS resources based on enabled security standards.
It evaluates your resources against security controls and generates findings for any non-compliant resources.

4. Security Hub CSPM core
   
The core component of Security Hub CSPM processes findings from all sources, to enable centralized security monitoring and management.
It serves as the central point for security finding aggregation, analysis, and distribution.

5. Cross-Region aggregator

The cross-Region aggregator replicates findings from linked Regions to a designated home Region.
This component provides a unified view of security findings across your global AWS infrastructure.

6. Cross-account aggregator
   
The cross-account aggregator collects findings from member accounts in an AWS Organizations structure and consolidates them in the administrator account.
This component enables centralized security management across multiple AWS accounts.

7. Insights engine

The insights engine analyzes security findings to identify patterns and group related findings.
It powers both built-in and custom insights that help you focus on specific security issues or trends.

https://aws.amazon.com/security-hub/getting-started/


## Security Hub CSPM integrations

Security Hub CSPM integrates with numerous AWS services and third-party security tools to provide a comprehensive security management solution. These integrations enable Security Hub CSPM to collect findings from various sources, automate security responses, and extend its capabilities beyond its core functionality.


- Amazon GuardDuty

  Amazon GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior. Security Hub CSPM ingests GuardDuty findings and displays them alongside other security information.


- Amazon Inspector

  Amazon Inspector is a vulnerability management service that automatically assesses applications for vulnerabilities and deviations from best practices. It scans Amazon Elastic Compute Cloud (Amazon EC2) instances, container images, and AWS Lambda functions for software vulnerabilities and network exposure.

  Security Hub CSPM displays Amazon Inspector findings in the consolidated dashboard, to help you see vulnerability information alongside other security findings. This integration helps you prioritize vulnerability remediation based on the overall security context.


- Amazon Macie

  Amazon Macie is a data security service that discovers sensitive data using machine learning and pattern matching. It helps identify and protect personally identifiable information (PII), financial data, and other sensitive information stored in Amazon S3 buckets.

  When Macie is integrated with Security Hub CSPM, its findings about sensitive data exposures appear in your security dashboard. This integration helps you address data protection issues as part of your overall security management process.


- AWS Config

  AWS Config provides a detailed inventory of your AWS resources and their configuration. It records configuration changes and evaluates resources against desired configurations using Config Rules.

  Security Hub CSPM uses AWS Config as the data source for many of its security standard checks. This integration allows Security Hub CSPM to evaluate your resource configurations against security best practices without duplicating the configuration assessment functionality.


- AWS Firewall Manager

  AWS Firewall Manager simplifies your AWS WAF, AWS Shield Advanced, and Amazon Virtual Private Cloud (Amazon VPC) security groups administration across multiple accounts and resources. It provides centralized configuration of firewall rules.

  Security Hub CSPM receives findings from Firewall Manager about resources that don't comply with your security policies. This integration helps you identify and address network security issues as part of your overall security management.


- Third-party integrations

  Security Hub CSPM integrates with various third-party security tools and services to provide comprehensive security monitoring and management. These integrations include the following:

  - Security Information and Event Management (SIEM) systems for long-term storage and correlation with other security data

  - Vulnerability management tools that scan your AWS environment and send findings to Security Hub

  - Endpoint protection platforms that provide visibility into endpoint-level security issues

  - Additional third-party security products that enhance security monitoring capabilities

  This integration capability allows organizations to do the following:

  - Maintain existing security tool investments while centralizing security findings in Security Hub CSPM

  - Combine findings from multiple security tools in a standardized format

  - View all security findings in a single dashboard

  - Enable automated responses to security issues across integrated tools
 
## Integration considerations

When integrating Security Hub CSPM with other services, consider security findings aggregation, compliance automation, 
and remediation workflows to establish a comprehensive security posture management system.


- Security findings aggregation

  Configure Security Hub CSPM to aggregate security findings from multiple AWS security services and third-party tools.
  Implement custom insights to identify patterns across findings that might indicate sophisticated threats. Use finding aggregation rules to reduce noise and prioritize critical issues. Consider implementing custom actions to route specific findings to appropriate response teams based on severity, resource type, or compliance impact.

 
- Compliance automation

  Use Security Hub CSPM security standards to automatically assess your environment against industry frameworks and regulatory requirements.
  Implement custom security standards for organization-specific policies. Use automated security checks to continuously validate compliance posture.
  Consider implementing custom controls to address gaps in standard compliance frameworks and maintain a comprehensive view of your security and compliance status.

- Remediation workflows

  Design automated remediation workflows triggered by Security Hub CSPM findings using EventBridge and Lambda.
  Implement tiered response procedures based on finding severity and resource criticality. Use Automation, a capability of AWS Systems Manager, documents for standardized remediation actions.
  Consider implementing approval workflows for high-impact remediation actions to balance automated response with appropriate governance controls.


## Check your knowledge
 
1. What is an element of AWS Security Hub CSPM service architecture?


- Cross-Region aggregator
- Database migration service
- Virtual machine hypervisor
- Content delivery network

 
The Cross-Region aggregator is an element of Security Hub CSPM service architecture that replicates findings from linked Regions to a designated home Region.

2. Which service integrates with AWS Security Hub CSPM?


- AWS Elastic Beanstalk
- Amazon Kinesis Video Streams
- Amazon GuardDuty
- Amazon Mechanical Turk

 
GuardDuty integrates with Security Hub CSPM by sending threat detection findings that Security Hub normalizes and displays alongside other security information.


# AWS Security Hub CSPM Demonstrations
 

By the end of this lesson, you will recognize how to use the AWS Management Console to enable, configure, and manage AWS Security Hub Cloud Security Posture Management (CSPM).

New service options note: When accessing Security Hub from the AWS Management Console, you will have two service options:

- Security Hub: The comprehensive security management service. AWS Security Hub prioritizes your critical security issues and helps you respond at scale to protect your environment. It detects critical issues by correlating and enriching signals into actionable insights, enabling streamlined response.

- Security Hub CSPM: A streamlined experience focused on Cloud Security Posture Management.

Note: Performing the following demonstrations in an AWS account can have an associated cost. 
To avoid incurring fees, do not perform these demonstrations in your AWS environment. If you choose to perform the demonstrations in your environment, you will need to clean up any resources you create to avoid incurring additional unwanted fees.


This lesson contains the following demonstrations:

- Enabling and Configuring AWS Security Hub CSPM

  https://www.youtube.com/watch?v=fbMQROz8RRI

- Reviewing and Managing Security Findings in AWS Security Hub CSPM

  https://www.youtube.com/watch?v=T1ZKdteBvFw

- Cleaning Up Resources

  https://www.youtube.com/watch?v=IiTHOTzuo54

## AWS Security Hub user CSPM guide
 

[AWS Security Hub CSPM Documentation](https://docs.aws.amazon.com/securityhub/)

 
[AWS Security Hub CSPM User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)

 
## Use cases and best practices for AWS Security Hub CSPM

 
[AWS Security Hub CSPM Blogs](https://aws.amazon.com/blogs/security/tag/aws-security-hub/)

 
[Ask the AWS Security Hub Team](https://repost.aws/)

To ask questions about AWS Security Hub CSPM, choose AWS RE:POST and tag your questions with AWS Security Hub.

 
[AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)

The AWS Well-Architected Framework helps you understand the pros and cons of decisions you make while building systems on AWS. To learn more, choose FRAMEWORK.

 
## AWS Security Hub CSPM pricing

 
[AWS Security Hub CSPM Pricing](https://aws.amazon.com/security-hub/pricing/)

 
[AWS Pricing Calculator](https://calculator.aws/#/)
To estimate the cost for your architecture solution, choose PRICING CALCULATOR.
