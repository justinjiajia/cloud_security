
https://skillbuilder.aws/learn/WQEJ1Q7B4N/aws-security-engineer--centralized-account-management


This course focuses on mastering AWS Organizations and AWS Control Tower to implement centralized security governance across multiple AWS accounts within your organization. You will learn how to design effective organizational unit structures, create and manage service control policies, configure delegated administrator access, and properly handle root credential management.

The course develops your skills in automated account provisioning processes, policy enforcement mechanisms, and break-glass procedures for emergency access scenarios. 
This course is part of the AWS Security Engineer Advanced Learning Plan.
If you are preparing for this role please refer to the other courses in the learning plan as needed.


# Course Overview

Centralized account management serves as the foundation for enterprise-wide AWS security governance. In this course, you will master AWS Organizations and AWS Control Tower to create scalable, secure multi-account architectures. You will discover how to design organizational unit (OU) structures that align with business requirements, implement service control policies that enforce security across all accounts, and establish centralized management for critical security services.


This course builds directly on your previous knowledge, transforming theoretical concepts into practical implementation strategies that AWS security engineers use often.

### AWS Organizations
You will learn to deploy and configure AWS Organizations from scratch, including designing effective organizational unit (OU) structures that reflect your organization's hierarchy and security requirements. This includes understanding how to move accounts between OUs, manage account creation workflows, and implement consolidated billing strategies that support security governance.

### Control Tower Implementation
Discover how AWS Control Tower extends Organizations with additional governance capabilities. You will explore the differences between these services, learn to implement Control Tower landing zones, and create custom guardrails that automatically enforce your organization's security policies across all managed accounts.

### Policy Enforcement at Scale
Implement service control policies (SCPs) and resource control policies (RCPs) to create guardrails that prevent security misconfigurations. You will understand how these policies interact with IAM permissions and learn to implement common security use cases like preventing public S3 buckets or restricting EC2 instance types.

### Centralized Security Management
Learn to configure delegated administrator access for AWS security services, enabling specialized teams to manage security tools across the organization without requiring management account access. This includes services like Security Hub, GuardDuty, and Config.

### Root User Security
Implement comprehensive security controls for management account root users, including MFA requirements, access monitoring, and break-glass procedures for emergency access scenarios. This foundational security practice protects your entire AWS organization.

## Lesson summary

You just completed an overview lesson of this course. This course teaches centralized account management using AWS Organizations and AWS Control Tower. You will implement policies, secure root access, and enable organization-wide security governance. 


---

# Deploying and Configuring AWS Organizations

In this lesson, you will learn how to do the following:
- Design an effective organizational unit (OU) structure based on organizational requirements.
- Implement a new AWS Organizations deployment.
- Configure service control policies to enforce governance at scale.

## Understanding AWS Organizations

AWS Organizations provides the foundational service for centrally managing multiple AWS accounts within your organization. Think of it as the organizational chart for your cloud infrastructure—just as a company has departments, divisions, and subsidiaries, AWS Organizations allows you to create a hierarchical structure of accounts that reflects your business units, environments, and security zones. This service enables consolidated billing, centralized account management, and organization-wide policy enforcement, forming the backbone of enterprise AWS governance.

AWS Organizations consists of several components.  


<img width="1416" height="1084" alt="image" src="https://github.com/user-attachments/assets/241d9564-998b-4a61-9cd4-04cada9bb3e9" />

<img width="902" height="642" alt="image" src="https://github.com/user-attachments/assets/d1344878-4349-49ab-b026-fbc0c2efeb3b" />

 1. Management Account
The central account that created the organization and has full administrative control

2. Root Organizational Unit
The top-level container that holds all accounts and other OUs in the organization

3. Organizational Units
Containers that group accounts for policy application and management

4. Member Accounts
Individual AWS accounts that belong to the organization

5. Service Control Policies
Policies attached to OUs that define maximum permissions for accounts

### Designing Your Organizational Unit (OU) Structure

Now that you understand the key components and relationships within an AWS Organizations architecture, it's time to translate this knowledge into a practical design for your specific environment. The following systematic approach will help you create an OU structure that aligns with your organizational goals and operational requirements. To learn more about this approach, choose the arrow buttons to display each of the following four steps.

1. Step 1: Analyze Organizational Requirements

Before creating OUs, analyze your organization's structure, compliance requirements, and operational needs. Consider factors like business units, environments (production, staging, development), regulatory boundaries, and cost allocation requirements. Organizations planning mergers or acquisitions could consider separate OUs to maintain security boundaries during integration processes. Document which accounts need similar security controls and governance policies.

2. Step 2: Plan Your Hierarchy

Design a logical hierarchy that supports both current and future needs. Common patterns include organizing by environment, business unit, or function. Avoid creating deeply nested structures that become difficult to manage. Plan for a maximum of 4-5 levels to maintain simplicity and clarity.

3. Step 3: Map Security Controls to OUs

Identify which security policies and controls apply to each OU. Production environments typically require stricter controls than development environments. Regulatory workloads may need special handling. This mapping will guide your service control policy implementation.

4. Step 4: Consider Scaling and Growth

Plan for organizational growth and changing requirements. Your OU structure should accommodate new business units, additional environments, and evolving compliance needs. Build flexibility into your design while maintaining security boundaries.


### Implementation Best Practices

With your OU structure designed and security controls mapped, you are ready to move from planning to execution. These implementation best practices will help you successfully deploy and manage your AWS Organizations environment while avoiding common pitfalls that can impact security, governance, and operational efficiency.



- Account Creation Strategy
  Establish standardized procedures for creating new AWS accounts. Use AWS Organizations' account creation APIs to automate account provisioning with consistent naming conventions, billing contact information, and initial security settings. Implement approval workflows that ensure new accounts align with organizational policies before creation.


- Cross-Account Access Patterns
  Design cross-account access patterns early in your implementation. Use AWS IAM roles for cross-account access rather than sharing credentials. Implement centralized identity management through AWS IAM Identity Center (formerly SSO) to provide users with federated access to multiple accounts based on their organizational role.


- Monitoring and Governance
  Enable AWS CloudTrail organization-wide logging to maintain visibility into API activities across all accounts. Implement AWS Config organization-wide to monitor configuration compliance. These services provide the audit trail and compliance monitoring capabilities essential for enterprise environments.


- Migration Considerations
  When migrating existing accounts to AWS Organizations, plan the transition carefully. Understand that existing accounts will inherit policies from their assigned OU. Test policy impacts in development environments first. Consider using AWS Control Tower Account Factory for standardized account vending if migrating to a Control Tower environment.


> AWS Organizations centrally manages multiple AWS accounts with hierarchical structure

## Implementing Service Control Policies for Governance

Service Control Policies (SCPs) act as guardrails that define the maximum permissions available to accounts within your organization. Unlike IAM policies that grant permissions, SCPs set boundaries—they can only restrict or deny actions, never grant additional permissions. This makes them ideal for enforcing organization-wide security requirements, such as preventing the deletion of security-critical resources or restricting deployment to specific AWS regions. When implementing SCPs, start with AWS managed policies for common use cases, then customize based on your specific security requirements. Remember that SCPs affect all users and roles in the target accounts, including account administrators, making careful testing essential before production deployment.


## Test your knowledge

1. Your organization needs to prevent any account from launching EC2 instances outside of us-east-1 and us-west-2 regions while allowing all other services to operate globally. What is the most effective approach using AWS Organizations?


- Create an IAM policy in each account that denies EC2 actions in unauthorized regions
- [x] Attach a Service Control Policy to the Root OU that denies EC2 actions except in approved regions
- Configure AWS Config rules to detect and remediate instances launched in unauthorized regions
- Use AWS CloudFormation StackSets to deploy region restrictions across all accounts

 
Excellent! Service Control Policies provide the centralized, enforceable approach needed for this requirement. An SCP attached to the Root OU will prevent EC2 launches in unauthorized regions across all accounts in the organization, regardless of local IAM permissions.

2. When designing an OU structure for a large enterprise with multiple business units and environments, which approach provides the best balance of security, manageability, and scalability?


- Create a flat structure with all accounts directly under the Root OU to simplify management
- Organize by environment first (Production, Staging, Development) with business units nested underneath
- [x] Organize by business unit first with environment-based OUs nested underneath each business unit
- Create separate organizations for each business unit to maintain complete isolation

 
Correct! Business unit-first organization typically provides the best balance because it aligns with natural organizational boundaries, allows for business-unit-specific compliance requirements, and enables appropriate delegation of administrative responsibilities while maintaining environment-based controls within each unit.

## Lesson summary

You learned that AWS Organizations provides centralized multi-account management through hierarchical OU structures and Service Control Policies. Proper OU design and SCP implementation create scalable governance frameworks for enterprise environments. 


---

# Implementing AWS Control Tower


In this lesson, you will learn how to do the following:
- Describe the difference between the functionality of AWS Organizations and AWS Control Tower
- Implement a new AWS Control Tower deployment
- Describe Control Tower's types of controls to meet organizational security needs

## AWS Control Tower

AWS Organizations provides the foundational multi-account management capabilities including account creation, organizational unit structures, consolidated billing, and basic policy enforcement through Service Control Policies. It offers the essential building blocks for multi-account governance but requires manual configuration of many security and compliance capabilities. Organizations is ideal when you need granular control over every aspect of your multi-account setup or have specific customization requirements that don't align with standardized approaches.


AWS Control Tower builds on AWS Organizations to provide an opinionated, automated approach to multi-account governance. It includes pre-configured security guardrails, automated account provisioning through Account Factory, centralized logging and monitoring setup, and a dashboard for governance oversight. Control Tower is designed for organizations that want to implement AWS best practices quickly with minimal manual configuration, trading some customization flexibility for faster implementation and ongoing automation.

### When to choose AWS Control Tower Over AWS Organizations Alone

Choose AWS Control Tower when you want to implement AWS multi-account best practices quickly with minimal manual configuration. Control Tower excels in environments where standardization is more important than customization, where you need rapid deployment of governance capabilities, or where your team lacks deep AWS expertise for manual configuration. However, if your organization requires highly customized governance models, has existing complex account structures that don't align with Control Tower patterns, or needs granular control over every security configuration, implementing Organizations directly may be more appropriate. Many organizations start with Control Tower for its quick implementation benefits, then gradually add custom configurations as their requirements evolve.


### Implementing AWS Control Tower
 
#### Step 1: Pre-Implementation Assessment
   
<img width="800" src="https://github.com/user-attachments/assets/3734e6a4-3dc7-4de7-a5d5-4ec0b318ac24" />


Evaluate your current AWS account structure and governance needs. Control Tower works best when implemented in new environments or when you can migrate to its standardized patterns. Review existing accounts, organizational units, and policies to understand what changes will be required. Document any custom requirements that might conflict with Control Tower's approach.

#### Step 2: Design and Deploy Landing Zone Architecture
 
<img width="800" src="https://github.com/user-attachments/assets/e11b647d-b535-4e7d-94a1-cd6a5217dca3" />

Plan your Control Tower landing zone including the home region, organizational unit structure, and initial account strategy. The landing zone includes the management account and a security account for centralized logging and auditing. Consider how your business units and environments will map to the Account Factory provisioning templates.

Launch Control Tower in your management account using the AWS Console setup wizard. This process creates foundational OUs (Core and Custom), sets up the security account, enables organization-wide logging, and implements basic guardrails. The initial deployment typically takes 60-90 minutes to complete all automation.


#### Step 3: Configure Account Factory

<img width="800" src="https://github.com/user-attachments/assets/5190424b-7217-4648-8ccf-783fd4c7c963" />

Set up Account Factory templates that define standard configurations for new accounts including network settings, security baselines, and initial access patterns. These templates ensure consistency across all newly provisioned accounts while reducing manual configuration overhead.


>  AWS Organizations provides flexibility; AWS Control Tower offers automated governance and standardized implementation


## Control Tower Controls

With AWS Control Tower deployed and Account Factory configured, you now need to understand the control system that enforces governance across your multi-account environment. Control Tower's controls automatically detect, prevent, and remediate configuration drift while maintaining consistent security and compliance as your infrastructure scales.


- Mandatory Controls
  Mandatory controls cannot be disabled and are automatically enabled to enforce fundamental governance rules across all Control Tower managed accounts in the landing zone. These include restrictions on changing CloudTrail configurations, preventing deletion of security-critical resources, and ensuring proper logging configurations. Understanding these controls helps you plan account architectures that work within Control Tower's governance framework.

- Strongly Recommended Controls
  Strongly recommended controls implement AWS security best practices and can be enabled or disabled as needed. Examples include detecting public S3 buckets, monitoring for unencrypted EBS volumes, and alerting on root user access. These controls help maintain the security of your landing zone and should be reviewed carefully as they address many common security concerns in AWS environments.


- Elective Controls
  Elective controls are optional and can be enabled or disabled to help meet specific compliance requirements. These might include restrictions on specific instance types, requirements for resource tagging, or controls related to specific compliance frameworks. Evaluate these based on your specific regulatory and operational needs.

- Custom Controls and Extensions
  Extend Control Tower's governance using AWS Config rules, Service Control Policies (SCPs), and custom controls through AWS Organizations to address organization-specific requirements not covered by AWS-provided controls. These custom implementations can detect configuration drift, enforce organizational policies, and automatically remediate common issues. Design custom controls to complement, not conflict with, existing Control Tower controls.

### Managing Control Tower at Scale

As your Control Tower implementation grows, focus on automation and standardization to maintain governance effectiveness. Use AWS Service Catalog and Account Factory to standardize account provisioning workflows, ensuring new accounts inherit appropriate security configurations and access patterns. Implement AWS Config organization-wide rules to monitor compliance across all accounts and use AWS Security Hub to aggregate security findings. Regularly review control effectiveness and compliance dashboards to identify trends and areas for improvement. Consider implementing Infrastructure as Code practices for managing custom controls and account configurations, enabling version control and repeatable deployments across your Control Tower environment.

## Test your knowledge

1. Your organization wants to implement automated multi-account governance with minimal custom configuration while ensuring strong security baselines. You also need the ability to add custom compliance rules for industry-specific requirements. Which approach best meets these needs?


- Implement AWS Organizations with manually configured Service Control Policies for all governance requirements
- [x] Deploy AWS Control Tower for foundational governance and add custom guardrails for industry-specific needs
- Use AWS Control Tower exclusively without any customization to ensure full automation
- Create separate AWS accounts for each requirement and manage them independently

 This approach leverages Control Tower's automated implementation of AWS best practices while providing the flexibility to add custom guardrails for specific industry requirements. It balances automation with customization effectively.

2. During Control Tower implementation, you discover that one of the mandatory controls conflicts with a critical business application that requires root user access for specific API operations. What is the most appropriate resolution?


- Disable the conflicting mandatory control to accommodate the business requirement
- Exclude the account containing the business application from Control Tower management
- Create a custom control that overrides the mandatory control for this specific use case
- [x] Redesign the business application to work within Control Tower's mandatory control constraints

 
Correct! Business applications should be redesigned to work within AWS security best practices rather than compromising fundamental security controls. This often involves using IAM roles and temporary credentials instead of direct root user access.

## Lesson summary

AWS Control Tower builds on AWS Organizations to provide automated multi-account governance with pre-configured controls. Custom controls extend Control Tower's capabilities for organization-specific requirements while maintaining security baselines. 

 
# Implementing Service Control Policies (SCPs) and Resource Control Policies (RCPs)
In this lesson, you will learn how to do the following:

- Describe how SCPs interact with IAM policies
- Implement SCPs to address common security use cases
- Configure RCPs to manage permissions across resources

## Policy Interaction in AWS Organizations

Service Control Policies create a crucial security boundary within your AWS environment, but understanding how they interact with IAM policies is essential for effective implementation. Think of SCPs as security guardrails on a highway, they define where you cannot go, but IAM policies are like your driver's license that determines what you're actually allowed to do within those boundaries. An action is only permitted when both the SCP allows it AND an IAM policy grants it. This intersection model means that SCPs can never grant permissions; they can only restrict or deny actions that would otherwise be permitted by IAM policies. This design ensures that organizational security requirements cannot be bypassed by account-level configurations.


<img width="1416" height="728" alt="image" src="https://github.com/user-attachments/assets/0656759f-55c8-42b5-9fc2-97de715c3491" />

<img width="680" height="485" alt="image" src="https://github.com/user-attachments/assets/b98e3ba5-7d89-47fd-b413-1a74b9004b89" />

1. SCP Boundary
Defines maximum possible permissions at the organizational level.

2. IAM Permissions
Grants specific permissions to users, groups, and roles.

3. Effective Permissions
The intersection where both SCP allows and IAM grants.

4. Denied Actions
Anything outside the SCP boundary is automatically denied.

5. Unused Grants
IAM permissions that exceed SCP boundaries have no effect.


### Common SCP Implementation Patterns

Now that you understand how SCPs and IAM permissions interact, you can explore practical implementation patterns. These common approaches help organizations address specific security and compliance requirements effectively.


#### Regional Restriction Policies
Implement SCPs that restrict AWS service usage to specific geographic regions, supporting data residency requirements and reducing attack surface. Example use cases include preventing accidental resource creation in high-cost regions, ensuring compliance with data sovereignty laws, or limiting service usage to regions where your organization has operational support. Remember to allow global services like IAM, CloudFront, and Route 53 that don't operate within specific regions.


#### Service Restriction Policies
Create SCPs that prevent the use of specific AWS services that don't align with organizational security policies. Common restrictions include preventing the use of services that don't support encryption at rest, blocking services that create internet-accessible resources by default, or restricting access to experimental services that haven't completed security review. These policies help maintain security standards while allowing innovation within approved boundaries.


#### Resource Protection Policies
Implement SCPs that prevent the modification or deletion of security-critical resources such as CloudTrail trails, Config configurations, or security-related IAM roles and policies. These policies ensure that foundational security infrastructure remains intact even if account-level administrators attempt to modify configurations. Include exceptions for authorized security personnel using specific roles or conditions.


#### Cost Control Policies
Use SCPs to implement cost control measures such as preventing the launch of expensive EC2 instance types, restricting the creation of resources that generate high data transfer costs, or limiting the use of on-demand capacity in favor of reserved instances. While cost control isn't primarily a security concern, it supports overall governance objectives and prevents resource exhaustion attacks.


#### Additional AWS Organizations Policy Types
Beyond SCPs, AWS Organizations supports additional policy types for comprehensive governance including backup policies for automated backup management, tag policies for consistent resource tagging, AI services opt-out policies for chat and other AI services, and declarative policies for standardized configurations across accounts.


### SCP Development and Testing Process

Understanding these implementation patterns provides the foundation for SCP deployment. However, successful implementation requires following a structured development and testing process to avoid disrupting legitimate operations. 

#### Step 1: Policy Design and Documentation
Begin by clearly documenting the security requirement or compliance need that the SCP addresses. Define the scope of accounts and resources affected, identify any necessary exceptions, and create test criteria for validating policy effectiveness. Consider SCP limitations including the maximum of 5 SCPs per organizational unit and policy size restrictions when designing your governance strategy. Document the business justification and maintain version control for all policy changes.

#### Step 2: Policy Development in Test Environment
Develop and initially test SCPs in a dedicated test environment that mirrors your production OU structure. Create test scenarios that validate both the intended restrictions and any necessary exceptions. Test with different user roles and permission levels to ensure the policy works as expected across various access patterns.

#### Step 3: Limited Production Deployment
Deploy new SCPs to a limited set of non-critical accounts first, monitoring for any unexpected impacts on legitimate operations. Gather feedback from account owners and monitor CloudTrail logs for denied actions that might indicate necessary policy adjustments. This staged approach prevents organization-wide disruptions.


#### Step 4: Full Deployment and Monitoring
Once validated, deploy the SCP to all target accounts and establish ongoing monitoring for policy effectiveness. Create alerts for repeated denied actions that might indicate either policy issues or potential security incidents. Regularly review and update policies as organizational requirements evolve.


>  Compliance frameworks provide blueprints for implementing AWS security and regulatory standards

## Resource Control Policies (RCPs) for Resource-Level Governance

Resource Control Policies represent the next evolution in AWS Organizations governance capabilities, providing fine-grained control over resource management actions. While SCPs operate at the API action level, RCPs enable policy enforcement based on resource attributes, tags, and conditions. This allows you to implement sophisticated governance scenarios such as preventing the deletion of resources with specific tags, restricting resource modifications based on cost center assignments, or enforcing naming conventions across resources. Note that RCPs are currently supported by only a limited number of AWS services, so verify service compatibility before implementing RCP-based governance strategies. RCPs work alongside SCPs to create comprehensive governance frameworks that address both action-level and resource-level policy requirements, enabling more nuanced control over how your organization's cloud resources are managed.

## Test your knowledge

1. A development team reports they cannot launch EC2 instances in us-west-2, despite having full EC2 permissions in their IAM policies. Your organization has an SCP that allows EC2 actions only in us-east-1 and eu-west-1. The team needs access to us-west-2 for a customer-facing application. What is the appropriate solution?

- Grant the development team additional IAM permissions that override the SCP restriction
- Temporarily disable the regional restriction SCP for all accounts
- [x] Update the SCP to include us-west-2 in the allowed regions list after appropriate approval
- Create a separate AWS account outside the organization for the us-west-2 deployment

 
Correct
Correct! Updating the SCP through proper change management processes addresses the legitimate business need while maintaining centralized governance control. This ensures the change is reviewed, approved, and documented appropriately.

2. You need to implement an SCP that prevents the deletion of CloudTrail trails across all accounts while allowing security administrators to manage these trails through a specific role. Which policy element is most important for this requirement?


- [x] Use a Deny statement with a condition that excludes the security administrator role
- Use an Allow statement that grants CloudTrail permissions only to the security administrator role

- Create separate SCPs for security administrators and regular users

- Implement the restriction through IAM policies instead of SCPs

 
Correct! A Deny statement with a condition exception for the security administrator role provides the precise control needed. This prevents all accounts from deleting CloudTrail trails except when performed through the authorized role.


## Lesson Summary

In this lesson you have learned that SCPs define maximum permissions by restricting IAM policy effectiveness, requiring both SCP allowance and IAM grants. RCPs enable resource-level governance beyond API action controls. 


# Centralized Security Service Management


In this lesson, you will learn how to do the following:
- Configure delegated administrator access for AWS security services

## The Challenge of Multi-Account Security Management

Managing security services across dozens or hundreds of AWS accounts creates significant operational challenges without proper centralization. Each account typically requires individual configuration of services like AWS Security Hub, Amazon GuardDuty, AWS Config, and Amazon Inspector, leading to inconsistent security postures, duplicated effort, and potential security gaps. Additionally, security teams need visibility across all accounts to effectively monitor threats and compliance status, but accessing multiple accounts individually is inefficient and error-prone. AWS Organizations addresses these challenges through delegated administrator capabilities, allowing specialized security accounts to manage organization-wide security services while maintaining the principle of least privilege and clear separation of duties.

The following are some of the AWS security services supporting delegated administration.


#### AWS Security Hub

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/24ea7a79-ba8d-4719-a45f-1a0e31dc5d07" />

Centralized security findings aggregation and compliance monitoring across all organizational accounts with automated security standards assessment.


#### Amazon GuardDuty

<img width="221" height="190" alt="image" src="https://github.com/user-attachments/assets/856f4bd3-d47a-453e-a8ba-4dab6365d710" />

Intelligent threat detection service providing organization-wide monitoring for malicious activity and unauthorized behavior.


#### AWS Config

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/19c02b82-9e1b-4c33-aa1b-17c77fe6de96" />

Configuration compliance monitoring and automated remediation across all accounts with organization-wide rules and conformance packs.


####  Amazon Inspector

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/f39c803a-0880-4696-bae9-458fbf33971e" />

Automated vulnerability assessment for applications and infrastructure with centralized findings management and reporting.


#### Amazon Macie

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/01fa16c8-79da-4ea5-aa53-8aff48cbf280" />

Data security and privacy service that discovers and protects sensitive data across S3 buckets organization-wide.


#### AWS CloudFormation StackSets

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/07135a89-e9d5-4338-b295-e1d360d49c3c" />

Deploy and manage AWS resources across multiple accounts and regions with centralized template management and updates.

https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/foundational-ous.html


### Implementing Delegated Administrator Access

Now that you understand which security services support delegated administration, discover how to implement this approach. The following interactive process guides you through four essential implementation phases. Each step builds toward comprehensive centralized security management across your AWS organization. 

### Step 1: Establish Dedicated Security Account

<img width="1680" height="1494" alt="image" src="https://github.com/user-attachments/assets/61af990a-f52c-446c-bcc9-693810fd9d1e" />


Create or designate a specific AWS account to serve as the security administration hub for your organization. This account should be separate from the management account to implement proper separation of duties and reduce the security blast radius. Configure this account with appropriate IAM roles, cross-account access permissions, and security tooling necessary for organization-wide security management.


### Step 2: Register Delegated Administrator
 <img width="1508" height="2214" alt="image" src="https://github.com/user-attachments/assets/36b6e4b8-b18b-49b9-b77f-94275ddcc837" />


Use the AWS Organizations console or API to register your security account as a delegated administrator for each required security service. This process grants the security account the necessary permissions to manage the specified service across all accounts in the organization. Each service requires separate registration, and permissions are scoped to only the actions necessary for that specific service.


### Step 3: Configure Organization-Wide Service Settings

<img width="1680" height="1427" alt="image" src="https://github.com/user-attachments/assets/2d44bcea-2be8-4d99-b7f5-91b7ca193edd" />


From the delegated administrator account, configure security services with organization-wide settings including member account auto-enrollment, standardized configurations, and centralized findings aggregation. Implement consistent security standards, enable automatic remediation where appropriate, and configure alerting and reporting mechanisms that provide visibility across all accounts.


### Step 4:  Implement Governance and Monitoring

Establish processes for ongoing governance of centralized security services including regular configuration reviews, permission audits, and effectiveness assessments. Monitor delegated administrator activities through CloudTrail logging, implement automated compliance checking, and maintain documentation of security service configurations and operational procedures.

### Service-Specific Implementation Guidance

The four-step process establishes your foundation for delegated administrator implementation across AWS accounts. Each security service requires tailored configuration approaches to maximize effectiveness and integration capabilities. Explore the following tabs to access detailed implementation guidance for specific service configurations.

#### Security Hub Centralization
Configure Security Hub with organization-wide member account management, enabling automated enrollment of new accounts and consistent security standards across all environments. Implement custom insights to track security postures specific to your organizational requirements and integrate with AWS Config for automated compliance monitoring. Set up cross-region aggregation if your organization operates in multiple AWS regions to maintain centralized visibility.


#### GuardDuty Organization Setup

Deploy GuardDuty with organization-wide threat detection capabilities, configuring automatic enablement for new accounts and standardized threat detection settings. Implement threat intelligence feeds specific to your industry or threat landscape, configure automated response actions for high-severity findings, and establish integration with security incident response workflows to ensure rapid response to detected threats.


#### Config Organization Rules
Implement AWS Config organization-wide rules and conformance packs that automatically assess configuration compliance across all accounts. Deploy standardized remediation actions that automatically correct common misconfigurations, establish exception handling processes for legitimate configuration variations, and create compliance reporting that aggregates results across the entire organization for management visibility.

#### Cross-Service Integration

Design integration patterns between centralized security services to create comprehensive security monitoring and response capabilities. Configure Security Hub to aggregate findings from GuardDuty, Config, Inspector, and Macie into a unified dashboard. Implement automated workflows that correlate findings across services and trigger appropriate response actions based on combined risk assessments.


### Operational Considerations for Centralized Security Management

Successfully operating centralized security services require careful attention to several operational factors beyond initial implementation. Consider the cost implications of enabling security services across numerous accounts, as costs can scale significantly with organization size. Implement appropriate cost controls and monitoring to ensure security investments align with organizational budgets. Plan for service limits and quotas that may require AWS support engagement for large organizations. Develop runbooks and procedures for common operational tasks such as onboarding new accounts, investigating security findings, and responding to service issues. Establish clear responsibilities between the centralized security team and individual account owners, ensuring that security governance doesn't impede legitimate business operations while maintaining appropriate oversight and control.

## Test your knowledge

1. Your organization has 50 AWS accounts and wants to implement centralized GuardDuty management. The security team should manage GuardDuty across all accounts, but the management account should not be used for day-to-day security operations. What is the recommended approach?


- Configure GuardDuty in the management account and use cross-account roles for centralized management


- Enable GuardDuty individually in each account and aggregate findings manually
- [x] Create a dedicated security account and register it as a delegated administrator for GuardDuty

- Use AWS Control Tower to automatically enable GuardDuty across all accounts

Correct! A dedicated security account with delegated administrator permissions provides the appropriate separation of duties, centralized management capabilities, and operational efficiency needed for organization-wide GuardDuty management.


2. After implementing delegated administrator access for AWS Config across your organization, account owners report that they cannot modify certain Config rules that conflict with their specific application requirements. How should this situation be addressed?


- Remove delegated administrator permissions and allow each account to manage Config independently


- Provide account owners with permissions to override organization-wide Config rules


- Disable Config rules that cause operational conflicts to avoid impeding business operations
- [x] Establish a governance process for reviewing and approving rule exceptions based on legitimate business needs


Correct! A governance process that evaluates exception requests ensures that legitimate business needs are accommodated while maintaining organizational security and compliance objectives. This balances operational flexibility with centralized control.


## Lesson Summary

Delegated administrator access enables centralized security service management without compromising the management account. Proper implementation requires dedicated security accounts and governance processes for exceptions. 


# Managing Root User Credentials
In this lesson, you will learn how to do the following:

- Implement security controls to protect management account root user credentials and centrally manage member account access
- Design break-glass access procedures for emergency scenarios


## Understanding Root Access Requirements

Root access should be reserved exclusively for tasks requiring this level of privilege. All routine operations should use appropriately scoped IAM roles instead.

Understanding which tasks require root access helps you determine when centralized management or break-glass procedures are necessary.  

- Account Management
  You need root access to change account settings, close AWS accounts, or enable Multi-Factor Authentication (MFA) delete on S3 buckets. Billing operations like changing payment methods also require root user privileges.

- Emergency Scenarios
  Root access serves as your ultimate break-glass mechanism when IAM configurations fail or security incidents require bypassing normal access controls.

### Centralized Root Access Management

AWS Organizations allows management accounts to control root access across all member accounts. This eliminates the need to secure individual root credentials for each member account. The following process demonstrates how to centrally manage root access for member accounts.

#### Step 1: Enable Centralized Access

 <img width="1020" height="1617" alt="image" src="https://github.com/user-attachments/assets/dcd49ec4-a0e2-4670-b8e1-54dd355a5fd4" />


When you enable AWS Organizations, you combine all your AWS accounts into an organization for central management. Centralizing root access lets you remove root user credentials.

1. Open the IAM console
2. Choose Root access management from the navigation pane and select enable
3. In the Capabilities to enable section choose which features to enable

Full guidance can be found in the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html)


#### Step 2: Perform a privileged task
Some tasks can only be performed when you sign in as the root user of an account. Some of these Tasks that require root user credentials can be performed by the management account or delegated administrator for IAM.

Full guidance can be found in the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user-privileged-task.html)

#### Step 3: Enable account recovery of the root user
If you need to recover root user credentials for a member account, the Organizations management account or delegated administrator can perform the Allow password recovery privileged task. The person with access to the root user email inbox for the member account can reset the root user password to recover root user credentials. Amazon recommends deleting root user credentials once you complete the task that requires access to the root user.

Full guidance can be found in the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/reset-root-password.html)


### Break-Glass Access Procedures

Security controls alone aren't enough; you also need well-designed break-glass procedures for emergencies.

Break-glass procedures provide emergency access when normal methods fail but must prevent abuse while ensuring availability. Define clear triggers like widespread IAM failures or security incidents requiring immediate response.

- Access Approval Process - Establish emergency procedures requiring documentation and approval for direct root access. Create templates including justification, planned activities, and duration requirements for bypass scenarios.

- Emergency Scenarios - Document when direct root access bypassing Organizations management is acceptable. Include complete service outages, Organizations service disruptions, or management account compromise scenarios.

Advanced security measures can further strengthen your root user protection strategy.


- Conditional Access
  Implement IP address restrictions limiting root login to corporate networks. Configure device-based restrictions requiring managed corporate devices. Use CloudTrail to verify access patterns align with policies.

- Automated Response
  Integrate root user monitoring with incident response systems for immediate security team notification. Configure automated workflows that enhance monitoring during root user sessions.

- Regular Assessments
  Conduct regular assessments of credential strength, MFA functionality, and monitoring effectiveness. Review procedures to ensure emergency access processes remain current and effective.

## Lesson Summary

You must implement comprehensive security controls for root user credentials including MFA, centralized credential management, and monitoring. Break-glass procedures enable emergency access while maintaining security governance across all member accounts. 


# Knowledge check


1. A multinational company operates 35 AWS accounts managed independently by regional teams. A recent compliance audit revealed inconsistent security policies and monitoring gaps. Different teams use varying access controls and encryption standards. What primary benefit does centralized governance provide?


- Eliminates need for individual account security configurations

- [x] Ensures consistent security policies and compliance across all accounts
- Reduces operational costs through automated resource management
- Allows complete autonomy while maintaining security standards

 
Correct! Centralized governance ensures uniform security policies, compliance monitoring, and reduces security gaps across the organization.
  

2. Your enterprise has Finance, Marketing, and Engineering business units. Each requires production, staging, and development environments with distinct compliance needs. Finance needs strict regulatory controls while Engineering requires development flexibility. Which OU structure provides optimal governance?


- Organize by environment first with business units nested underneath
- Create separate AWS Organizations for each business unit
- [x] Organize by business unit first, then nest environment-based OUs underneath
- Create flat structure with all accounts directly under Root OU

Correct! Business-unit-first structure enables specific compliance controls while maintaining environment governance within each unit.

3. You must deploy AWS Organizations to manage six existing standalone accounts. The designated management account has administrative privileges and consolidated billing. You need to establish an organizational hierarchy and invite existing accounts. What is the foundational first step?


- [x] Create the organization from the designated management account
- Send invitations to all existing accounts immediately
- Enable Service Control Policies across target accounts
- Create organizational units for account categorization

Correct! Creating the organization from the management account is the essential first step enabling all other Organizations features.


4. Your organization requires regional restrictions for compliance purposes. Development accounts must operate only in us-east-1 and eu-west-1. Production accounts need global access for disaster recovery capabilities. You need organization-wide enforcement of these requirements. Which approach effectively implements these different regional policies?


- Deploy AWS Config rules to monitor regional compliance
- Create IAM policies with regional restrictions in each account
- Use CloudFormation StackSets to manage regional permissions
- [x] Apply different SCPs to development and production OUs based on requirements

Correct! SCPs attached to different OUs enable tailored regional restrictions based on account types and business requirements.


5. Your startup needs multi-account governance with minimal setup complexity. The team has limited AWS expertise for manual configuration. You require automated security guardrails and standardized account provisioning following AWS best practices. Which service best meets these requirements?


- AWS Organizations with manual Service Control Policy configuration
- [x] AWS Control Tower for automated governance with best practices
-  AWS Organizations for maximum customization and control
- Neither service provides sufficient automation for these needs

Correct! Control Tower provides automated governance, pre-configured guardrails, and Account Factory with minimal manual configuration.


6. Your Control Tower environment must detect unencrypted EBS volumes automatically. AWS-provided controls don't address this specific organizational compliance requirement. You need automated detection with immediate alerting capabilities. What implementation approach should you use?


- [x] Create custom controls using AWS Config rules integrated with Control Tower
- Use only AWS-provided strongly recommended controls
- Implement the requirement through enhanced IAM policies
- Disable Control Tower and implement through AWS Organizations

Correct! Custom controls using Config rules extend Control Tower capabilities for organization-specific compliance requirements.


7. A developer has full EC2 permissions through their IAM role. Their account resides in an OU with SCP denying EC2 actions outside us-east-1. The developer attempts launching an instance in ap-southeast-1 region. What occurs when they execute this action?


- Action succeeds because IAM policies override SCP restrictions
- [x] Action is denied because SCPs define maximum permission boundaries
- Action succeeds but triggers automated compliance alerts
- Action fails due to insufficient IAM policy permissions

Correct! SCPs create permission boundaries requiring both SCP allowance AND IAM grant for action success.


8. Your organization must prevent CloudTrail trail deletion across all accounts. Security administrators using "SecurityTeam" role need management capabilities. All other users and roles require deletion restrictions. You need organization-wide enforcement without impacting authorized operations. Which SCP implementation is most effective?



- Create separate SCPs for different user types

- Implement restrictions through account-level IAM policies

- Use Allow statements granting CloudTrail permissions to SecurityTeam
- [x] Use Deny statement with condition excluding SecurityTeam role

Correct! Deny statements with role-based conditions prevent unauthorized deletions while preserving administrative access.


9. Your organization needs preventing deletion of resources tagged "Environment:Production" across all services and accounts. Traditional SCPs operate at API action level but you require resource-attribute-based control. Tag-based governance must work regardless of service type. What Organizations feature addresses this requirement?


- Enhanced Service Control Policies with advanced conditions
- [x] Resource Control Policies for resource-attribute-based governance
- AWS Config organization-wide rules for resource protection
- CloudFormation StackSets with deletion protection parameters

Correct! RCPs enable governance based on resource attributes like tags, providing nuanced control beyond API actions.


10. Your organization manages 50 AWS accounts requiring centralized GuardDuty administration. Security team needs organization-wide GuardDuty management capabilities. Management account should not be used for daily security operations. You need proper separation of duties. What configuration approach is recommended?


- Enable GuardDuty in management account for centralized control
- Configure GuardDuty individually with cross-account access roles
- [x] Create dedicated security account and register as delegated administrator
- Use AWS Control Tower for automatic GuardDuty management

Correct! Dedicated security account as delegated administrator provides centralized management with proper separation.

11. Your management account root user requires enhanced security protection. Current setup uses software-based MFA and individual password storage. New security requirements mandate hardware authentication and enterprise credential management. IP restrictions from corporate networks are also needed. Which control should be prioritized first?


- [x] Implement IP address restrictions for root user access

- Create backup root user accounts for redundancy
- Enable hardware-based MFA and centralized credential management
- Disable root user access completely to prevent security risks

Correct! IP restrictions provide immediate network-level protection and should be implemented first for quick security enhancement.


12. A sophisticated attack has compromised IAM infrastructure across multiple member accounts. Incident response team needs emergency access for investigation and remediation. Normal authentication methods are unavailable or potentially compromised. What break-glass procedure element is most critical for effective response?


- Automatic root access activation across all organizational accounts


- [x] Documented evaluation process to determine where root access is needed
- Immediate password rotation across all potentially affected accounts
- Temporary suspension of security monitoring during incident response

Correct! Evaluation processes ensure root access is granted only where specifically needed, balancing security with response effectiveness.

# Recap and Resources
 

You have successfully completed Centralized Account Management. The following resources have been curated to help you apply your new knowledge. To learn more about the material covered in this course, choose from the following links.

[AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
 
 
[AWS Control Tower User Guide](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
 
[Service Control Policies (SCPs) Reference](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

 
[Delegated Administrator Access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html)
 
[AWS Control Tower Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)
 
[Organizing Your AWS Environment](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html)
 
[AWS IAM Root User Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management)
 
