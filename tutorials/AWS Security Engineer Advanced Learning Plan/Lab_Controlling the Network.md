In this lab, you use public and private subnets, security groups, and ACLs to create a three-security zone network infrastructure. 
You then use VPC flow logs to monitor the traffic that reaches the resources in each zone to verify only the required traffic is allowed.

https://skillbuilder.aws/learn/BQTYG4FDFG/controlling-the-network/

# Controlling the Network


SPL-TF-200-SISBPN-10-EN - Version 1.0.7

© 2025 Amazon Web Services, Inc. or its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited. All trademarks are the property of their owners.

 

## Lab overview
You are a network security engineer at AnyCompany. You are responsible for creating a secure network infrastructure in AWS to prepare for AnyCompany’s upcoming migration to the cloud. AnyCompany currently has a three-tier network security infrastructure on-premises:

The Public Access Zone hosts load balancers that serve as the primary connection point to your web servers.
The Web Server Zone hosts the frontend servers for your website.
The Database Zone hosts the backend database servers that provide data to your website.
You must ensure each zone is securely segmented from each other and only certain types of traffic are allowed to flow between them to support the company’s websites and applications.

In this lab, you use public and private subnets, security groups, and network ACLs to create a three-security zone network infrastructure. You then use VPC flow logs to monitor the traffic that reaches the resources in each zone to verify only the required traffic is allowed.

## Objectives
By the end of this lab, you should be able to do the following:

- Create a three-security zone network infrastructure
- Implement network segmentation using security groups, network ACLs, and public and private subnets
- Monitor network traffic to EC2 instances using VPC flow logs
- Technical knowledge prerequisites

To successfully complete this lab, you should be familiar with navigation of the AWS Management Console and have an understanding of basic networking concepts.

Icon key
Various icons are used throughout this lab to call attention to different types of instructions and notes. The following list explains the purpose for each icon:

 Expected output: A sample output that you can use to verify the output of a command or edited file.
 Note: A hint, tip, or important guidance.
 Learn more: Where to find more information.
 Caution: Information of special interest or importance (not so important to cause problems with the equipment or data if you miss it, but it could result in the need to repeat certain steps).
 Consider: A moment to pause to consider how you might apply a concept in your own environment or to initiate a conversation about the topic at hand.
 Knowledge check: An opportunity to check your knowledge and test what you have learned.
 Hint: A hint to a question or challenge.




## Lab environment
The following diagram shows the basic architecture of the lab environment:

 <img width="1742" height="1122" alt="image" src="https://github.com/user-attachments/assets/69c8b173-7491-4000-939d-0747f9ff8133" />


Image description: The diagram depicts the data flow from an external user to an internet gateway, though a Network Load Balancer in a public subnet, to a web server in a private subnet, to a database server in a separate private subnet.

The following list details the major resources in the diagram:

- A VPC with one public subnet and two private subnets in one Availability Zone, and one public subnet in a second Availability Zone.
- A Network Load Balancer with two nodes, one in each public subnet.
- An EC2 instance acting as a web server is the first private subnet.
- An EC2 instance acting as a database server in the second subnet.
- Two security groups, one for each instance based its purpose.

The network traffic flows from an external user, though an internet gateway to one of the two Network Load Balancer nodes, to the web server. If the URL of the WordPress blog site running on the web server is requested, traffic flows to the database server as well.

## Task 1: Restrict network traffic using security groups


As part of your task of replicating your on-premises network zones in AWS, you must ensure that your hosts are properly secured. You decide to use security groups for each resource type to control the traffic that is allowed to flow between them.

In this task, you create new rules for existing security groups to address your traffic needs.

### Task 1.1: Verify current connectivity state

First, verify that you are unable to access the web server.

<img width="246" height="510" alt="image" src="https://github.com/user-attachments/assets/8a1addcb-2531-4d65-ba66-93b01b0867f3" />

3. Copy the TestSiteUrl value from the list to the left of these instructions. Paste the URL into a new web browser tab and press Enter to navigate to an Apache test page on the web server.

 Expected output: The connection should time out after approximately 1 minute, with an error stating the page could not be reached.

Currently, there are no security group rules that allow traffic to pass from the load balancer to the web server, so the connection times out.

### Task 1.2: Allow HTTPS traffic to the web server


4. Return to your web browser tab with the AWS Management Console.

5. At the top of the AWS Management Console, in the search bar, search for and choose EC2.

In the navigation list at the left of the page, under Network & Security, choose Security Groups.

7. On the Security Groups page, select the Web Server SG security group.

   Caution: Verify Web Server SG is the only item selected.

In the Details pane at the bottom of the page, choose the Inbound rules tab.

At the right side of the Inbound rules section, choose Edit inbound rules.

On the Edit inbound rules page, choose Add rule.

In the row for the new rule:

For Type, select HTTPS.

For Source, select Anywhere-IPv4.

Notice 0.0.0.0/0 is automatically added as the source IP CIDR.
For Description – optional, enter Allow HTTPS traffic from any source.

 Note: The rule you just added allows inbound traffic on port 443 to any resource in the WebServerSg security group from any IPv4 source IP. Because this lab utilizes a Network Load Balancer to pass the traffic directly to the web server, you must allow HTTPS connections from any source to the web server.

At the lower-right of the page, choose Save rules.

### Task 1.3: Verify traffic flow to the web server
Next, verify the rules you added to the security group allows you to access the web server.

Copy the TestSiteUrl value from the list to the left of these instructions. Paste the URL into a new web browser tab and press Enter to navigate to an Apache test page on the web server, or refresh the page if you still have the web browser tab open.

 Note: It can take approximately 15 seconds for the page to load the first time. The web server uses a self-signed SSL certificate. If your web browser warns you of a potential security risk due to a self-signed certificate, choose to continue to the site.

 Caution: On MacOS Catalina and later, some Chromium-based web browsers, such as Google Chrome or Microsoft Edge, might not display a link to continue to the site, with a NET::ERR_CERT_INVALID error message. If you experience this situation, try using an alternative web browser, such as Mozilla Firefox.

 Expected output: An Apache HTTP server test page should load.

<img width="1204" height="422" alt="image" src="https://github.com/user-attachments/assets/bc1d289f-2369-4c35-b75c-9de930f7c734" />

Close the Test page for the Apache HTTP server web browser tab.

Now that you’ve verified you can access the web server over HTTPS, attempt to access the WordPress site.

Copy the WordPressUrl value from the list to the left of these instructions. Paste the URL into a new web browser tab and press Enter to navigate to the WordPress page.

 Expected output: The connection should time out after approximately 1 minute, with a Gateway Timeout error on the page.

WordPress is configured so that the web page is hosted from one instance and its database is running on a different instance in a separate private subnet. Currently, there are no security group rules that allow traffic to pass from the web server EC2 instance to the database server EC2 instance, so the connection times out.

### Task 1.4: Allow traffic from the web server to the database server

Return to your web browser tab with the EC2 management console.

On the Security Groups page, select the Web Server SG security group.

In the Details pane at the bottom of the page, choose the Outbound rules tab.

At the right side of the Outbound rules section, choose Edit outbound rules.

On the Edit outbound rules page, choose Add rule.

In the row for the new rule:

For Type, select MYSQL/Aurora.

Notice Protocol and Port range are automatically set to TCP and 3306, respectively.
For Destination, select Custom.

In the search box to the right of the Destination parameter, search for and select DatabaseServerSG.

For Description – optional, enter Allow MYSQL database traffic to resources in the DatabaseServerSG security group.

 Note: The rule you just added allows outbound traffic on port 3306 from any resource in the WebServerSg security group to any resource in the DatabaseServerSg security group. For the purposes of this lab, it allows MYSQL traffic to flow from the web server EC2 instance to the database server EC2 instance.

At the lower-right of the page, choose Save rules.
Next, add an ingress (inbound) rule to the database server security group.

On the Security Groups page, select the Database Server SG security group.

 Caution: Verify Database Server SG is the only item selected.

<img width="1299" height="410" alt="image" src="https://github.com/user-attachments/assets/a9bc2cbd-e0db-4c9b-a7f3-66ad9df3b101" />

In the Details pane at the bottom of the page, choose the Inbound rules tab.

At the right side of the Inbound rules section, choose Edit inbound rules.

On the Edit inbound rules page, choose Add rule.

In the row for the new rule:

For Type, select MYSQL/Aurora.

For Source, select Custom.

In the search box to the right of the Source parameter, search for and select WebServerSg.

For Description – optional, enter Allow MYSQL database traffic from resources in the WebServerSg security group.

 Note: The rule you just added allows inbound traffic to any resource in the DatabaseServerSg security group from any resource in the WebServerSg security group. For the purposes of this lab, it allows MYSQL traffic to flow to the database server EC2 instance from the web server EC2 instance.

At the lower-right of the page, choose Save rules.


### Task 1.5: Verify traffic flow to the database server and configure WordPress

Now that you have added security group rules to allow traffic to flow to the database server, you should be able to load the WordPress page.

29. Copy the WordPressUrl value from the list to the left of these instructions. Paste the URL into a new web browser tab and press Enter to navigate to the WordPress page, or refresh the page if you still have the web browser tab open.

 Expected output: The WordPress welcome page should load.

Next, finalize the WordPress configuration. You have decided to use a WordPress blog site as an easy way to replicate and test traffic flow to the application servers you plan to migrate from your on-premises environment. The WordPress server configuration uses a frontend web server in one subnet, with a database server is a separate subnet, similar to how your application servers are configured.

30. In the Information needed section:
- For *Site Title*, enter `AWS Security Best Practices`.
- For Username, enter `wpadmin`.
- For Password, copy and paste the AdministratorPassword value listed to the left of these instructions.
- For Your Email, enter `wpadmin@example.corp`.

31. At the bottom of the page, choose Install WordPress.

<img width="771" height="430" alt="image" src="https://github.com/user-attachments/assets/fc85e574-b4be-4b28-9aee-b12fdd551863" />

32. On the Success! page, choose Log In.

33. On the WordPress login page:

- For Username or Email Address, enter `wpadmin`.
- For Password, copy and paste the AdministratorPassword value listed to the left of these instructions.
Choose Log In.
<img width="387" height="472" alt="image" src="https://github.com/user-attachments/assets/317c6c52-322c-45f0-9151-a4d84e28035d" />

 Note: It can take approximately 1-2 minutes for the WordPress dashboard to load the first time.

You should now see the WordPress dashboard.

35. Close your web browser tab with the WordPress dashboard.

    <img width="1293" height="732" alt="image" src="https://github.com/user-attachments/assets/7e7092e8-826f-42c3-b0e1-1f47714d75b3" />

 
 Task complete: You have successfully added security group rules to allow only the appropriate traffic to connect to the WordPress site hosted in your private subnet.

## Task 2: Restrict traffic to the public subnet


Now that you have secured traffic to and from your instances, you would like to further harden the network security posture.

In this task, you modify the network access control lists (ACLs) for each subnet to allow only the traffic required for access to the website to pass through at the subnet level.

### Task 2.1: Create network ACL rules for the load balancer subnets
Return to your web browser tab with the EC2 management console.

At the top of the page, in the unified search bar, search for and choose VPC.

In the navigation list at the left of the page, under Security, choose Network ACLs.

At the upper-right corner of the Network ACLs page, choose Create network ACL.

On the Create network ACL page:

In the Network ACL settings section, for Name – optional, enter load-balancer-nacl.
For VPC, select Lab VPC.
Choose Create network ACL.

On the Network ACLs page, select load-balancer-nacl.

In the Details pane at the bottom of the page, choose the Inbound rules tab.

 Note: Notice there is only one inbound rule that denies all incoming traffic.

Choose the Outbound rules tab.

 Note: Notice there is only one outbound rule that denies all incoming traffic.

Choose the Subnet associations tab.

Choose Edit subnet associations.

On the Edit subnet associations page:

- Select Load Balancer Subnet 1 (Public).
- Select Load Balancer Subnet 2 (Public).
Choose Save changes.

Copy the TestSiteUrl value from the list to the left of these instructions. Paste the URL into a new web browser tab and press Enter to navigate to an Apache test page on the web server.

 Expected output: The connection should time out after approximately 30 seconds, with an error stating the page could not be reached.

Return to your web browser tab with the VPC management console.

On the Network ACLs page, select load-balancer-nacl.

In the Details pane at the bottom of the page, choose the Inbound rules tab.

Choose Edit inbound rules.

On the Edit inbound rules page, choose Add new rule.

In the row for the new rule:

For Rule number, enter 100.
For Type, select HTTPS.
Notice the Protocol (TCP) and Port range (443) fields are filled automatically.
For Source, enter 0.0.0.0/0.
For Allow/Deny, select Allow.
Create a second rule with the following configuration:
For Rule number, enter 101.

For Type, select Custom TCP.

For Port range, enter 1024-65535.

For Source, enter 10.10.0.0/16.

For Allow/Deny, select Allow.

 Learn more: The rule you just created allows inbound connections on ephemeral ports from any resource within the lab VPC. Devices temporarily use ephemeral ports to initiate a connection with one another. After the initial connection is made, traffic is then allowed to propagate on the required port, such as HTTPS (port 443). For more information about, refer to Ephemeral ports in the Additional resources section.

Choose Save changes.

On the Network ACLs page, select load-balancer-nacl if it is not already selected.

In the Details pane at the bottom of the page, choose the Outbound rules tab.

Choose Edit outbound rules.

On the Edit outbound rules page, choose Add new rule.

63. In the row for the new rule:

- For Rule number, enter 100.
- For Type, select HTTPS.
- For Destination, enter the value of WebServerSubnet listed to the left of these instructions.
- For Allow/Deny, select Allow.

64. Create a second rule with the following configuration:

- For Rule number, enter `101`.
- For Type, select `Custom TCP`.
- For Port range, enter `1024-65535`.
- For Destination, enter `0.0.0.0/0`.
- For Allow/Deny, select `Allow`.

 Learn more: For more information about the recommended traffic rules for a load balancer, refer to Network ACLs for load balancers in a VPC in the Additional resources section at the end of this lab.

64. Choose Save changes.


### Task 2.2: Create network ACL rules for the web server subnet

- Knowledge check: Based on the steps you just followed, create a new network ACL for the web server subnet with the following configuration:

  - Name: web-server-nacl.

  - VPC: Lab VPC

  - Inbound rules:
    - Allow HTTPS (port 443) traffic from any source, 0.0.0.0/0.
    - Allow TCP traffic on ports 1024-65535 from the entire VPC subnet, 10.10.0.0/16.

  - Outbound rules:

    - Allow TCP traffic on ports 1024-65535 to any destination, 0.0.0.0/0.
    - Allow MYSQL/Aurora (port 3306) traffic to the database server subnet, which is listed to the left of these instructions as DatabaseServerSubnet.

  - Subnet associations: Web Server Subnet (Private)

 Hint: If you get stuck, refer to Task 2.2 solution in the Answer key section at the end of this lab.


### Task 2.3: Verify traffic flow to the web server
Next, verify the network ACL rules you added allow you to access the web server.


65. Copy the TestSiteUrl value from the list to the left of these instructions. Paste the URL into a new web browser tab and press Enter to navigate to an Apache test page on the web server, or refresh the page if you still have the web browser tab open.

 Expected output: An Apache HTTP server test page should load.

Close the Test page for the Apache HTTP server web browser tab.

### Task 2.4: Create network ACL rules for the database server subnet

Finally, create network ACL rules to allow only the required traffic to the database server subnet.

- Knowledge check: Based on the steps you just followed, create a new network ACL for the web server subnet with the following configuration:
  - Name: database-server-nacl.
  - VPC: Lab VPC
  - Inbound rules:
    - Allow MYSQL/Aurora (port 3306) traffic from the web server subnet, which is listed to the left of these instructions as WebServerSubnet.
    - Allow TCP traffic on ports 1024-65535 from the entire VPC subnet, `10.10.0.0/16`.

  - Outbound rules:
    - Allow TCP traffic on ports 1024-65535 to the entire VPC subnet, `10.10.0.0/16`.

  - Subnet associations: Database Server Subnet (Private)

 Hint: If you get stuck, refer to Task 2.4 solution in the Answer key section at the end of this lab.


### Task 2.5: Verify traffic flow to the database server

Next, verify the network ACL rules you added allow you to access the WordPress blog site.

Copy the WordPressUrl value from the list to the left of these instructions. Paste the URL into a new web browser tab and press Enter to navigate to the WordPress blog site, or refresh the page if you still have the web browser tab open.

 Expected output: The WordPress blog page should load.

Close the WordPress blog web browser tab.

 Task complete: You have successfully created network ACL rules to limit inbound and outbound traffic to only what is required to successfully access your blog site.


---

<br>


## Task 3: Inspect network traffic with VPC flow logs


You have now configured security groups and network ACLs to limit allowed network traffic to only what is absolutely necessary for your blog site to function properly. Next, you would like to verify that non-essential traffic is being denied successfully.

In this task, you create VPC flow logs to send network traffic data to Amazon CloudWatch. You then analyze the logs to confirm which types of traffic are allowed, and which are rejected.

### Task 3.1: Create the CloudWatch log group

First, you must create the CloudWatch log group to send the VPC flow logs to.

69. At the top of the page, in the unified search bar, search for and choose CloudWatch.
70. In the navigation pane at the left of the page, in the Logs section, choose Log groups.
71. At the upper-right of the Log groups page, choose Create log group.
72. On the Create log group page:

- In the Log group details section, for Log group name, enter blog-access-logs.
- For Retention setting, choose `1 day`.

 Note: For the purposes of this lab, you don’t need to retain the logs beyond the duration of the lab. However, in a production environment, select the retention time based on your organization’s policy or regulation requirements.

Choose Create.


### Task 3.2: Create a VPC flow log

Now that you have the CloudWatch log group, you can create and configure a VPC flow log to record traffic flow within the VPC.

74. At the top of the page, in the unified search bar, search for and choose VPC.
75. In the navigation pane at the left of the page, in the Virtual private cloud section, choose Your VPCs.

On the Your VPCs page, select Lab VPC.

In the Details pane at the bottom of the page, choose the Flow logs tab.

At the right of the Flow logs section, choose Create flow log.

79. On the Create flow log page:

- In the Flow log settings section, for Name, enter vpc-flow-logs-for-blog.
- For Filter, select All.
- For Maximum aggregation interval, select 1 minute.
  - Learn more: You select 1 minute in this lab to shorten the time before you can see the resulting logs. For more information, refer to Aggregation interval in the Additional resources section at the end of this lab.

- For Destination, select Send to CloudWatch Logs.
- For Destination log group, select blog-access-logs.
- For Service role, select VpcFlowLogsRole.
- For Log record format, select Custom format.
- On the Log format drop-down menu, select the following options in this order:
  - account-id
  - interface-id
  - srcaddr
  - srcport
  - dstaddr
  - dstport
  - subnet-id
  - flow-direction
  - action


 Expected output: The Format preview box should look like this:

```
${account-id} ${interface-id} ${srcaddr} ${srcport} ${dstaddr} ${dstport} ${subnet-id} ${flow-direction} ${action}
```

Choose Create flow log.

 Learn more: The VpcFlowLogsRole IAM role that you selected while configuring the flow logs contains the following policy:


```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams"
      ],
      "Resource": "*",
      "Effect": "Allow"
    }
  ]
}
```

The policy allows the VPC Flow Logs service to create CloudWatch log groups and log streams, and write events to the log streams.

 Learn more: For more information about VPC Flow Logs, refer to Logging IP traffic with VPC Flow Logs and Publish flow logs to CloudWatch Logs in the Additional resources section at the end of this lab.

### Task 3.3: Generate traffic to the blog

Next, visit the WordPress blog site to generate traffic to the web and database servers.

81. Copy the WordPressUrl value from the list to the left of these instructions. Paste the URL into a new web browser tab and press Enter to navigate to the WordPress blog site, or refresh the page if you still have the web browser tab open.
82. Refresh the page three times to generate additional traffic.
83. Update the URL to `HTTP://` and then attempt to access the blog site again.

Because you have only allowed HTTPS traffic from the load balancer to the web server, the request should time out. When you view the flow logs, you should find rejection messages for traffic on port 80.

 Caution: If your web browser has HTTPS-Only Mode turned on, you might need to turn it off to successfully attempt to visit the site using HTTP.

Return to your web browser tab with the VPC management console.

At the top of the page, in the unified search bar, search for and choose CloudWatch.

In the navigation pane at the left of the page, in the Logs section, choose Log groups.

On the Log groups page, select the link for blog-access-logs.

On the blog-access-logs details page, in the Log streams section, choose Search all log streams.

 Note: The Search all option allows you to search through all of the log streams that are in the log group, rather than searching through them individually.

Review several of the log entries to determine what types of traffic were allowed and which were rejected. Use the right arrow  to expand each item to view the full message

If you followed the log format listed in task 3.1, the log messages should appear similar to this:

|Account number |	Interface ID	| Source IP address |	Source port|	Destination IP address|		Destination port|		Subnet ID	|	Traffic direction	|	Action|	
|---|---|---|---|---|---|---|---|---|
|111122223333	|eni-0cf0d60e2c2a9f674	|10.10.1.52	|2197	|10.10.10.10	|443|	subnet-0f2a1fafd992c336e	|ingress	|ACCEPT|
|111122223333|	eni-0cf0d60e2c2a9f674|	205.251.233.176	|29803	|10.10.1.52	|80	|subnet-0f2a1fafd992c336e|	ingress|	REJECT|
 
 
 What types of traffic do you notice are accepted? Which are rejected? What do you think could be the cause of the traffic on ports other than 80, 443, or 3306?

 Task complete: You have successfully created VPC Flow Logs to monitor the network traffic within your VPC.

## Conclusion
You successfully did the following:

- Created a three-security zone network infrastructure
- Implemented network segmentation using security groups, network ACLs, and public and private subnets
- Monitored network traffic to EC2 instances using VPC flow logs
 
## Additional resources

[Elastic Load Balancing product comparisons](https://aws.amazon.com/elasticloadbalancing/features/?nc=sn&loc=2&dn=1)

[Ephemeral ports](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#nacl-ephemeral-ports)

[Network ACLs for load balancers in a VPC](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html#elb-vpc-nacl)

[Aggregation interval](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-logs-aggregration-interval)

[Logging IP traffic with VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

[Publish flow logs to CloudWatch Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-cwl.html)



## Answer key

### Task 2.2 solution
Return to your web browser tab with the EC2 management console.

At the top of the page, in the unified search bar, search for and choose VPC.

In the navigation list at the left of the page, under SECURITY, choose Network ACLs.

At the upper-right corner of the Network ACLs page, choose Create network ACL.

On the Create network ACL page:

In the Network ACL settings section, for Name – optional, enter web-server-nacl.
For VPC, select Lab VPC.
Choose Create network ACL.

On the Network ACLs page, select web-server-nacl.

In the Details pane at the bottom of the page, choose the Subnet associations tab.

Choose Edit subnet associations.

On the Edit subnet associations page:

Select Web Server Subnet (Private).
Choose Save changes.

Copy the TestSiteUrl value from the list to the left of these instructions. Paste the URL into a new web browser tab and press Enter to navigate to an Apache test page on the web server.

 Expected output: The connection should time out after approximately 10-20 seconds, with an error stating the gateway timed out.

Return to your web browser tab with the VPC management console.

On the Network ACLs page, select web-server-nacl.

In the Details pane at the bottom of the page, choose the Inbound rules tab.

Choose Edit inbound rules.

On the Edit inbound rules page, choose Add new rule.

In the row for the new rule:

For Rule number, enter 100.
For Type, select HTTPS.
For Source, enter 0.0.0.0/0.
For Allow/Deny, select Allow.
Create a second rule with the following configuration:
For Rule number, enter 101.
For Type, select Custom TCP.
For Port range, enter 1024-65535.
For Source, enter 10.10.0.0/16.
For Allow/Deny, select Allow.
Choose Save changes.

On the Network ACLs page, select web-server-nacl if it is not already selected.

In the Details pane at the bottom of the page, choose the Outbound rules tab.

Choose Edit outbound rules.

On the Edit outbound rules page, choose Add new rule.

In the row for the new rule:

For Rule number, enter 100.
For Type, select MYSQL/Aurora.
For Destination, enter the value of DatabaseServerSubnet listed to the left of these instructions.
For Allow/Deny, select Allow.
Create a second rule with the following configuration:
For Rule number, enter 101.
For Type, select Custom TCP.
For Port range, enter 1024-65535.
For Destination, enter 0.0.0.0/0.
For Allow/Deny, select Allow.
Choose Save changes.
Return to Task 2.3


### Task 2.4 solution
Return to your web browser tab with the EC2 management console.

At the top of the page, in the unified search bar, search for and choose VPC.

In the navigation list at the left of the page, under SECURITY, choose Network ACLs.

At the upper-right corner of the Network ACLs page, choose Create network ACL.

On the Create network ACL page:

In the Network ACL settings section, for Name – optional, enter database-server-nacl.

For VPC, select Lab VPC.

Choose Create network ACL.

On the Network ACLs page, select database-server-nacl.

In the Details pane at the bottom of the page, choose the Subnet associations tab.

Choose Edit subnet associations.

On the Edit subnet associations page:

Select Database Server Subnet (Private).
Choose Save changes.

Copy the WordPressUrl value from the list to the left of these instructions. Paste the URL into a new web browser tab and press Enter to navigate to an Apache test page on the web server.

 Expected output: The connection should time out after approximately 10-20 seconds, with an error stating the gateway timed out.

Return to your web browser tab with the VPC management console.

On the Network ACLs page, select database-server-nacl.

In the Details pane at the bottom of the page, choose the Inbound rules tab.

Choose Edit inbound rules.

On the Edit inbound rules page, choose Add new rule.

In the row for the new rule:

For Rule number, enter 100.
For Type, select MYSQL/Aurora.
For Source, enter the value of WebServerSubnet listed to the left of these instructions.
For Allow/Deny, select Allow.
Create a second rule with the following configuration:
For Rule number, enter 101.
For Type, select Custom TCP.
For Port range, enter 1024-65535.
For Source, enter 10.10.0.0/16.
For Allow/Deny, select Allow.
Choose Save changes.

On the Network ACLs page, select database-server-nacl if it is not already selected.

In the Details pane at the bottom of the page, choose the Outbound rules tab.

Choose Edit outbound rules.

On the Edit outbound rules page, choose Add new rule.

In the row for the new rule:

For Rule number, enter 100.
For Type, select Custom TCP.
For Port range, enter 1024-65535.
For Destination, enter 10.10.0.0/16.
For Allow/Deny, select Allow.
Choose Save changes.
Return to Task 2.5

For more information about AWS Training and Certification, see https://aws.amazon.com/training/.



## CloudFormation Templates

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
      Tags:
        - Key: labs:permission-scope
          Value: protected
```

Template 2:

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

Template 3:

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: 'Template for Security Best Practices - Lab 1 - Controlling the network. Creates 1 VPC, 2 public subnets, 2 private subnets, 1 Internet gateway, 1 NAT gateway, 2 EC2 instances (1 in each private subnet), an application load balancer, and an S3 bucket.'

Parameters:
  LabVpcCidr:
    Type: String
    Default: 10.10.0.0/16
    AllowedPattern: ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(/(1[6-9]|2[0-8]))$

  LoadBalancerSubnet1Cidr:
    Type: String
    Default: 10.10.1.0/24
    AllowedPattern: ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(/(1[6-9]|2[0-8]))$

  LoadBalancerSubnet2Cidr:
    Type: String
    Default: 10.10.2.0/24
    AllowedPattern: ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(/(1[6-9]|2[0-8]))$

  WebServerSubnetCidr:
    Type: String
    Default: 10.10.10.0/24
    AllowedPattern: ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(/(1[6-9]|2[0-8]))$

  DatabaseServerSubnetCidr:
    Type: String
    Default: 10.10.20.0/24
    AllowedPattern: ^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(/(1[6-9]|2[0-8]))$

  WebServerPrivateIp:
    Type: String
    Default: 10.10.10.10

  DatabaseServerPrivateIp:
    Type: String
    Default: 10.10.20.20

  LatestAL2AmiId: # Locate latest Amazon Linux 2 AMI from public parameter store
    Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    Default: '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'

  AdministratorPassword:
    Type: String
    NoEcho: true

#-----Create mappings for the Elastic Load Balancing service account number to use in NetworkLbLogsBucketPolicy-----#
Mappings:
  ElbRegionMap:
    us-east-1:
      ElbAcctId: 127311923021
    us-east-2:
      ElbAcctId: 033677994240
    us-west-1:
      ElbAcctId: 027434742980
    us-west-2:
      ElbAcctId: 797873946194
    af-south-1:
      ElbAcctId: 098369216593
    ca-central-1:
      ElbAcctId: 985666609251
    eu-central-1:
      ElbAcctId: 054676820928
    eu-west-1:
      ElbAcctId: 156460612806
    eu-west-2:
      ElbAcctId: 652711504416
    eu-south-1:
      ElbAcctId: 635631232127
    eu-west-3:
      ElbAcctId: 009996457667
    eu-north-1:
      ElbAcctId: 897822967062
    ap-east-1:
      ElbAcctId: 754344448648
    ap-northeast-1:
      ElbAcctId: 582318560864
    ap-northeast-2:
      ElbAcctId: 600734575887
    ap-northeast-3:
      ElbAcctId: 383597477331

Resources:
#-----Start - Create lab networking resources-----#
  LabVpc:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: !Ref LabVpcCidr
      EnableDnsSupport: true
      EnableDnsHostnames: true
      InstanceTenancy: default
      Tags:
        - Key: Name
          Value: Lab VPC

#-----Load Balancer subnet 1 resources-----#
  LoadBalancerSubnet1:
    Type: AWS::EC2::Subnet
    DependsOn: AttachInternetGateway
    Properties:
      CidrBlock: !Ref LoadBalancerSubnet1Cidr
      VpcId: !Ref LabVpc
      MapPublicIpOnLaunch: true
      AvailabilityZone: !Select
        - '0'
        - !GetAZs ''
      Tags:
        - Key: Name
          Value: Load Balancer Subnet 1 (Public)

  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: Internet Gateway

  AttachInternetGateway:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref LabVpc
      InternetGatewayId: !Ref InternetGateway

  PublicRouteTable:
    Type: AWS::EC2::RouteTable
    DependsOn:
      - LoadBalancerSubnet1
      - LoadBalancerSubnet2
    Properties:
      VpcId: !Ref LabVpc

  PublicRoute:
    Type: AWS::EC2::Route
    Properties:
      RouteTableId: !Ref PublicRouteTable
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway

  LoadBalancerSubnet1RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    DependsOn: PublicRoute
    Properties:
      SubnetId: !Ref LoadBalancerSubnet1
      RouteTableId: !Ref PublicRouteTable

#-----Load Balancer subnet 2 resources-----#
  LoadBalancerSubnet2:
    Type: AWS::EC2::Subnet
    DependsOn: AttachInternetGateway
    Properties:
      CidrBlock: !Ref LoadBalancerSubnet2Cidr
      VpcId: !Ref LabVpc
      MapPublicIpOnLaunch: true
      AvailabilityZone: !Select
        - '1'
        - !GetAZs ''
      Tags:
        - Key: Name
          Value: Load Balancer Subnet 2 (Public)

  LoadBalancerSubnet2RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    DependsOn: PublicRoute
    Properties:
      SubnetId: !Ref LoadBalancerSubnet2
      RouteTableId: !Ref PublicRouteTable

#-----Private subnet 1 resources-----#
  WebServerSubnet:
    Type: AWS::EC2::Subnet
    DependsOn: AttachInternetGateway
    Properties:
      CidrBlock: !Ref WebServerSubnetCidr
      VpcId: !Ref LabVpc
      MapPublicIpOnLaunch: false
      AvailabilityZone: !Select
        - '0'
        - !GetAZs ''
      Tags:
        - Key: Name
          Value: Web Server Subnet (Private)

  NatGateway:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId: !GetAtt ElasticIpForNatGateway.AllocationId
      SubnetId: !Ref LoadBalancerSubnet1
      Tags:
        - Key: Name
          Value: NAT Gateway

  ElasticIpForNatGateway:
    Type: AWS::EC2::EIP
    Properties:
      Domain: vpc

  PrivateRouteTable:
    Type: AWS::EC2::RouteTable
    DependsOn:
      - WebServerSubnet
      - DatabaseServerSubnet
    Properties:
      VpcId: !Ref LabVpc

  PrivateRoute:
    Type: AWS::EC2::Route
    DependsOn: AttachInternetGateway
    Properties:
      RouteTableId: !Ref PrivateRouteTable
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId: !Ref NatGateway

  WebServerSubnetRouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    DependsOn: PrivateRoute
    Properties:
      SubnetId: !Ref WebServerSubnet
      RouteTableId: !Ref PrivateRouteTable

#-----Private subnet 2 resources-----#
  DatabaseServerSubnet:
    Type: AWS::EC2::Subnet
    DependsOn: AttachInternetGateway
    Properties:
      CidrBlock: !Ref DatabaseServerSubnetCidr
      VpcId: !Ref LabVpc
      MapPublicIpOnLaunch: false
      AvailabilityZone: !Select
        - '0'
        - !GetAZs ''
      Tags:
        - Key: Name
          Value: Database Server Subnet (Private)

  DatabaseServerSubnetRouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    DependsOn: PrivateRoute
    Properties:
      SubnetId: !Ref DatabaseServerSubnet
      RouteTableId: !Ref PrivateRouteTable
#-----End - Create lab networking resources-----#

#-----Start - create EC2 instance profile to allow the WebServer instance to access required services to build the lab-----#
  WebServerProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      InstanceProfileName: WebServerProfile
      Roles:
        - !Ref WebServerIamRole

  WebServerIamRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: WebServerIamRole
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Action:
              - sts:AssumeRole
            Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore # Allows SSM connections to the instance.

  WebServerBuildPolicy: # Permissions required to build the lab environment
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: WebServerBuildPolicy
      Roles:
        - !Ref WebServerIamRole
      PolicyDocument: # Permissions to modify the SSM connection settings and to delete this policy at the end of the build
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Action:
              - iam:DeleteRolePolicy
              - s3:GetObject
              - s3:List*
            Resource: '*'
          - Effect: Allow
            Action:
              - ssm:UpdateDocument*
              - ssm:CreateDocument*
              - ssm:DeleteDocument*
            Resource: !Sub arn:aws:ssm:${AWS::Region}:${AWS::AccountId}:document/SSM-SessionManagerRunShell
#-----End - create EC2 instance profile to allow the WebServer instance to access required services to build the lab-----#

#-----Start - Create security group for WebServer-----#
  WebServerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: WebServerSG
      GroupDescription: Network access rules for the Web Server instance
      VpcId: !Ref LabVpc
      Tags:
        - Key: Name
          Value: Web Server SG
      SecurityGroupEgress:
        - IpProtocol: TCP
          FromPort: 443
          ToPort: 443
          CidrIp: 0.0.0.0/0
        - IpProtocol: TCP
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0

#-----Start - Create Web Server EC2 instance-----#
  WebServer:
    Type: AWS::EC2::Instance
    DependsOn:
      - WebServerSubnetRouteTableAssociation
    Properties:
      ImageId: !Ref LatestAL2AmiId
      InstanceType: t3.micro
      IamInstanceProfile: !Ref WebServerProfile
      BlockDeviceMappings:
        - DeviceName: /dev/xvda
          Ebs:
            VolumeSize: 8
            DeleteOnTermination: true
            VolumeType: gp2
      NetworkInterfaces:
        - AssociatePublicIpAddress: false
          PrivateIpAddress: !Ref WebServerPrivateIp
          DeviceIndex: '0'
          GroupSet:
            - !Ref WebServerSecurityGroup
          SubnetId: !Ref WebServerSubnet
      Tags:
        - Key: Name
          Value: Web Server
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash
          yum update -y aws-cfn-bootstrap
          /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource WebServer --configsets InstallTools,InstallWebServer,EnableTls,InstallWordpress,ConfigureSsm,RemoveBuildPolicy --region ${AWS::Region}
          /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServer --region ${AWS::Region}
    Metadata:
      AWS::CloudFormation::Init:
        configSets:
          InstallTools:
            - "install-tools"
          InstallWebServer:
            - "install-web-server"
          EnableTls:
            - "enable-tls"
          InstallWordpress:
            - "install-wordpress"
          ConfigureSsm:
            - "configure-ssm"
          RemoveBuildPolicy:
            - "remove-lab-build-policy"

        install-tools:
          commands:
            a-update-yum:
              command: yum update -y
            b-install-python3:
              command: yum install -y python3
            c-remove-aws-cli-v1:
              command: rm -rf /usr/bin/aws
            d-download-aws-cli-v2:
              command: curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
            e-unzip-package:
              command: unzip awscliv2.zip
            f-install-aws-cli-v2:
              command: ./aws/install -b
        install-web-server:  # https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.html
          commands:
            a-amazon-linux-extras:
              command: amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
            b-install-apache-mariadb-php:
              command: yum install -y httpd
            c-start-apache:
              command: systemctl start httpd
            d-start-apache-at-boot:
              command: systemctl enable httpd
            e-add-user-to-apache-group:
              command: usermod -a -G apache ec2-user
            f-change-www-directory-ownership:
              command: chown -R ec2-user:apache /var/www
            g-add-group-write-permissions:
              command: chmod 2775 /var/www && find /var/www -type d -exec sudo chmod 2775 {} \;
            h-add-group-permissions-recursively:
              command: find /var/www -type f -exec sudo chmod 0664 {} \;

        enable-tls: # https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SSL-on-amazon-linux-2.html#ssl_enable
          commands:
            a-install-mod-ssl:
              command: yum install -y mod_ssl
            b-generate-cert:
              command: /etc/pki/tls/certs/make-dummy-cert /etc/pki/tls/certs/localhost.crt
            c-modify-ssl-conf-file:
              command: sed -i 's/SSLCertificateKeyFile/#SSLCertificateKeyFile/' /etc/httpd/conf.d/ssl.conf
            d-restart-httpd-service:
              command: systemctl restart httpd

        install-wordpress: # https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hosting-wordpress.html
          commands:
            a-download-wordpress:
              command: wget https://wordpress.org/latest.tar.gz && tar -xzf latest.tar.gz
            b-create-wp-config-file:
              command: cp wordpress/wp-config-sample.php wordpress/wp-config.php
            c-update-wp-config-file:
              command: !Sub sed -i 's/database_name_here/wordpress_db/; s/username_here/wordpress_user/; s/password_here/${AdministratorPassword}/; s/'\''DB_HOST'\'', '\''localhost'\''/'\''DB_HOST'\'', '\''${DatabaseServerPrivateIp}'\''/' wordpress/wp-config.php
            d-copy-wp-files-to-www:
              command: mkdir /var/www/html/blog && cp -r wordpress/* /var/www/html/blog/

        configure-ssm: # Set Systems Manager Session Manager connection time out 60 minutes, sets the default user for connects to "ec2-user", and changes to the home directory at login.
          files:
            /temp/ssm-settings.yaml:
              content: |
                inputs:
                  s3BucketName: ""
                  s3KeyPrefix: ""
                  s3EncryptionEnabled: true
                  cloudWatchLogGroupName: ""
                  cloudWatchEncryptionEnabled: true
                  idleSessionTimeout: "60"
                  cloudWatchStreamingEnabled: true
                  kmsKeyId: ""
                  runAsEnabled: true
                  runAsDefaultUser: ec2-user
                  shellProfile:
                    linux: cd $HOME; pwd
                schemaVersion: "1.0"
                description: Document to modify Session Manager idle timeout and runas user.
                sessionType: Standard_Stream
          commands:
            a-create-ssm-document:
              command: aws ssm create-document --name "SSM-SessionManagerRunShell" --content "file:///temp/ssm-settings.yaml" --document-format YAML --document-type Session
              ignoreErrors: true
            b-configure-ssm:
              command: aws ssm update-document --name "SSM-SessionManagerRunShell" --content "file:///temp/ssm-settings.yaml" --document-format YAML --document-version '$LATEST'
              ignoreErrors: true

        remove-lab-build-policy: # Removes the WebServerBuildPolicy IAM policy from the WebServerIamRole IAM role, as those permissions are needed at build time, but the student should not have access to them.
          commands:
            remove-lab-build-policy:
              command: !Sub aws iam delete-role-policy --role-name ${WebServerIamRole} --policy-name WebServerBuildPolicy

    CreationPolicy:
      ResourceSignal:
        Timeout: PT4M
#-----End - Create Web Server EC2 instance-----#

#-----Start - create EC2 instance profile to allow the DatabaseServer instance to access required services to build the lab-----#
  DatabaseServerProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      InstanceProfileName: DatabaseServerProfile
      Roles:
        - !Ref DatabaseServerIamRole

  DatabaseServerIamRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: DatabaseServerIamRole
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Action:
              - sts:AssumeRole
            Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore # Allows SSM connections to the instance.

  RevokeSecurityGroupRulesPolicy:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: RevokeSecurityGroupRulesPolicy
      Roles:
        - !Ref DatabaseServerIamRole
      PolicyDocument: # Permissions to remove security group rules that are no longer needed after the build process
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Action:
              - ec2:RevokeSecurityGroupEgress
              - ec2:RevokeSecurityGroupIngress
            Resource: !Sub arn:aws:ec2:${AWS::Region}:${AWS::AccountId}:security-group/*
#-----End - create EC2 instance profile to allow the DatabaseServer instance to access required services to build the lab-----#

#-----Start - Create security group for DatabaseServer-----#
  DatabaseServerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: DatabaseServerSG
      GroupDescription: Network access rules for the Database Server instance
      VpcId: !Ref LabVpc
      Tags:
        - Key: Name
          Value: Database Server SG
      SecurityGroupEgress:
        - IpProtocol: TCP
          FromPort: 443
          ToPort: 443
          CidrIp: 0.0.0.0/0
        - IpProtocol: TCP
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
#-----End - Create security group for DatabaseServer-----#

#-----Start - Create Database Server EC2 instance-----#
  DatabaseServer:
    Type: AWS::EC2::Instance
    DependsOn:
      - DatabaseServerSubnetRouteTableAssociation
      - WebServer
      - NetworkLb
    Properties:
      ImageId: !Ref LatestAL2AmiId
      InstanceType: t3.micro
      IamInstanceProfile: !Ref DatabaseServerProfile
      BlockDeviceMappings:
        - DeviceName: /dev/xvda
          Ebs:
            VolumeSize: 8
            DeleteOnTermination: true
            VolumeType: gp2
      NetworkInterfaces:
        - AssociatePublicIpAddress: false
          PrivateIpAddress: !Ref DatabaseServerPrivateIp
          DeviceIndex: '0'
          GroupSet:
            - !Ref DatabaseServerSecurityGroup
          SubnetId: !Ref DatabaseServerSubnet
      Tags:
        - Key: Name
          Value: Database Server
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash
          yum update -y aws-cfn-bootstrap
          /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource DatabaseServer --configsets InstallTools,InstallConfigureDb,RemoveEgressRules --region ${AWS::Region}
          /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource DatabaseServer --region ${AWS::Region}
    Metadata:
      AWS::CloudFormation::Init:
        configSets:
          InstallTools:
            - "install-tools"
          InstallConfigureDb:
            - "install-and-configure-mariadb"
          RemoveEgressRules:
            - "remove-egress-rules"

        install-tools:
          commands:
            a-update-yum:
              command: yum update -y
            b-install-python3:
              command: yum install -y python3
            c-remove-aws-cli-v1:
              command: rm -rf /usr/bin/aws
            d-download-aws-cli-v2:
              command: curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
            e-unzip-package:
              command: unzip awscliv2.zip
            f-install-aws-cli-v2:
              command: ./aws/install -b

        install-and-configure-mariadb:
          commands:
            a-install-mariadb:
              command: amazon-linux-extras install -y mariadb10.5
            b-mariadb-allow-remote-connections:
              command: sed -i 's/#bind-address/bind-address/' /etc/my.cnf.d/mariadb-server.cnf
            c-enable-and-start-mariadb-service:
              command: systemctl enable mariadb && systemctl start mariadb
            d-set-mariadb-root-password:
              command: !Sub mysqladmin --user=root password "${AdministratorPassword}"
            e-mariadb-drop-anonymous-users1:
              command: mysql -e "DROP USER IF EXISTS ''@'localhost'"
            f-mariadb-drop-test-db:
              command: mysql -e "DROP DATABASE IF EXISTS test"
            g-mariadb-create-wp-db:
              command: mysql -e "CREATE DATABASE IF NOT EXISTS wordpress_db"
            h-mariadb-create-wp-user:
              command: !Sub mysql -e "CREATE USER IF NOT EXISTS 'wordpress_user'@'${WebServerPrivateIp}' IDENTIFIED BY '${AdministratorPassword}'"
            i-mariadb-grant-wp-user-rights:
              command: !Sub mysql -e "GRANT ALL PRIVILEGES ON wordpress_db.* to 'wordpress_user'@'${WebServerPrivateIp}'"
            j-mariadb-flush-privileges:
              command: mysql -e "FLUSH PRIVILEGES"

        remove-egress-rules: # Remove egress rules for ports 80 and 443 from the web and database server security groups. They are needed at build time, but should not be there for the lab.
          commands:
            a-remove-web-server-egress-http:
              command: !Sub aws ec2 revoke-security-group-egress --group-id ${WebServerSecurityGroup.GroupId} --ip-permissions IpProtocol=tcp,FromPort=80,ToPort=80,IpRanges=[{CidrIp=0.0.0.0/0}]
            b-remove-web-server-egress-https:
              command: !Sub aws ec2 revoke-security-group-egress --group-id ${WebServerSecurityGroup.GroupId} --ip-permissions IpProtocol=tcp,FromPort=443,ToPort=443,IpRanges=[{CidrIp=0.0.0.0/0}]
            c-remove-database-server-egress-http:
              command: !Sub aws ec2 revoke-security-group-egress --group-id ${DatabaseServerSecurityGroup.GroupId} --ip-permissions IpProtocol=tcp,FromPort=80,ToPort=80,IpRanges=[{CidrIp=0.0.0.0/0}]

    CreationPolicy:
      ResourceSignal:
        Timeout: PT3M
#-----End - Create Database Server EC2 instance-----#

#-----Start - Create network load balancer-----#

#-----network load balancer (Elastic Load Balancer v2)-----#
  NetworkLb:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    DependsOn:
      - LoadBalancerSubnet1RouteTableAssociation
      - LoadBalancerSubnet2RouteTableAssociation
    Properties:
      IpAddressType: ipv4
      Name: Web-LB
      Scheme: internet-facing
      Subnets:
        - !Ref LoadBalancerSubnet1
        - !Ref LoadBalancerSubnet2
      Type: network

  NetworkLbTargetGroup:
    Type: AWS::ElasticLoadBalancingV2::TargetGroup
    Properties:
      Name: NetworkLb-WebServer-TargetGroup
      Protocol: TCP
      Port: 443
      TargetType: instance
      Targets:
        - Id: !Ref WebServer
      VpcId: !Ref LabVpc

  NetworkLbListener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    Properties:
      DefaultActions:
        - Type: forward
          ForwardConfig:
            TargetGroups:
              - TargetGroupArn: !Ref NetworkLbTargetGroup
      Protocol: TCP
      Port: 443
      LoadBalancerArn: !Ref NetworkLb
#-----End - Create application load balancer-----#

#-----Start - Create IAM role to allow EC2 to send VPC flow logs to CloudWatch-----#
  VpcFlowLogsRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: VpcFlowLogsRole
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action: sts:AssumeRole
          - Effect: Allow
            Principal:
              Service:
                - vpc-flow-logs.amazonaws.com
            Action: sts:AssumeRole
      Path: /
      Policies:
        - PolicyName: VpcFlowLogsPolicy
          PolicyDocument:
            Version: 2012-10-17
            Statement:
              - Effect: Allow
                Action:
                  - logs:CreateLogGroup
                  - logs:CreateLogStream
                  - logs:PutLogEvents
                  - logs:DescribeLogGroups
                  - logs:DescribeLogStreams
                Resource: 'arn:aws:logs:*:*:log-group:blog-access-logs:log-stream:*'
#-----End - Create IAM role to allow EC2 to send VPC flow logs to CloudWatch-----#

Outputs:
  AwsRegion:
    Description: AWS Region the lab is running in.
    Value: !Ref AWS::Region

  TestSiteUrl:
    Description: URL to access the web server Apache test page through the application load balancer.
    Value: !Sub https://${NetworkLb.DNSName}

  WordPressUrl:
    Description: URL to access the Wordpress page on the web server through the application load balancer.
    Value: !Sub https://${NetworkLb.DNSName}/blog

  LoadBalancerSubnet1:
    Description: Subnet CIDR for the first load balancer subnet.
    Value: !Ref LoadBalancerSubnet1Cidr

  LoadBalancerSubnet2:
    Description: Subnet CIDR for the second load balancer subnet.
    Value: !Ref LoadBalancerSubnet2Cidr

  WebServerSubnet:
    Description: Subnet CIDR for the web server subnet.
    Value: !Ref WebServerSubnetCidr

  DatabaseServerSubnet:
    Description: Subnet CIDR for the database server subnet.
    Value: !Ref DatabaseServerSubnetCidr
```

The last template cannot be loaded:

<img width="1022" height="532" alt="image" src="https://github.com/user-attachments/assets/074828b8-7dae-4385-8f10-14c7dcffe65b" />
