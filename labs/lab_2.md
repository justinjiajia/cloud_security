


# Guided Lab: Build your VPC and Run a Web Server



## Lab overview and objectives

In this guided lab, you will use Amazon Virtual Private Cloud (VPC) to create your own VPC and add additional components to produce a customized network. You will also create a security group. You will then configure and customize an EC2 instance to run a web server and you will launch the EC2 instance to run in a subnet in the VPC.

Amazon Virtual Private Cloud (Amazon VPC) enables you to launch Amazon Web Services (AWS) resources into a virtual network that you defined. This virtual network closely resembles a traditional network that you would operate in your own data center, with the benefits of using the scalable infrastructure of AWS. You can create a VPC that spans multiple Availability Zones.

After completing this lab, you should be able to do the following:

- Create a VPC.

- Create subnets.

- Configure a security group.

- Launch an EC2 instance into a VPC.

- Connect to the EC2 instance and deploy a Web service

  

## Scenario

In this lab you build the following infrastructure:

<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_foundation/L2-architecture.png" alt="Architecture" />



## Task 1: Create Your VPC



In this task, you will use the VPC and more option in the VPC console to create multiple resources, including a VPC, an Internet Gateway, a public subnet and a private subnet in a single Availability Zone, two route tables, and a NAT Gateway.



1. In the search box at the top left of the screen, search for and choose *VPC* to open the VPC console.

   <img width="784" height="140" alt="image" src="https://github.com/user-attachments/assets/2e5083b4-573c-45ae-90ca-1f77e6ec12ed" />


   

2. Begin creating a VPC.

   - In the top right of the screen, verify that N. Virginia (us-east-1) is the region.
   
     <img width="310" height="91" alt="image" src="https://github.com/user-attachments/assets/dfbe62a0-db65-4c8c-abeb-889809af69ed" />
     

   - Next, choose Create VPC.
     
     <img width="271" height="59" alt="image" src="https://github.com/user-attachments/assets/315cd7ff-ed6c-4501-90e2-67398fff83cc" />

     
     

3. Configure the VPC details in the VPC settings panel on the left:

   - Choose *"VPC and more"*.

   - **IMPORTANT FOR GRADING:** Under Name tag auto-generation, keep Auto-generate selected, however change the value from *"project"* to ***\<your student ID\>***.

   - Keep the IPv4 CIDR block set to 10.0.0.0/16

     <img width="371" height="431" alt="image" src="https://github.com/user-attachments/assets/5f66a9c6-2333-4eb9-93e9-91c44844dd34" />


   - For Number of Availability Zones, choose *1*.

   - For Number of public subnets, keep the *1* setting.

   - For Number of private subnets, keep the *1* setting.

   - Expand the Customize subnets CIDR blocks section

     - Change Public subnet CIDR block in us-east-1a to *10.0.0.0/24*
     - Change Private subnet CIDR block in us-east-1a to *10.0.1.0/24*

     <img width="370" height="431" alt="image" src="https://github.com/user-attachments/assets/b7abaaef-1bda-4cb1-b697-30499f210e52" />

       

   - Set NAT gateways to *In 1 AZ*.

   - Set VPC endpoints to *None*.

   - Keep both DNS hostnames and DNS resolution enabled.


   <img width="372" height="360" alt="image" src="https://github.com/user-attachments/assets/c9b6db18-aaa3-46bb-9818-e661aa254bc6" />



4. In the Preview panel on the right, confirm the settings you have configured.

   - VPC: ***\<your student ID\>-vpc***


      - Subnets: us-east-1a
        - Public subnet name: ***\<your student ID\>-subnet-public1-us-east-1a***
        - Private subnet name: ***\<your student ID\>-subnet-private1-us-east-1a***


      - Route tables
        - ***\<your student ID\>-rtb-public***
        - ***\<your student ID\>-rtb-private1-us-east-1a***

   

      - Network connections

        - ***\<your student ID\>-igw***

        - ***\<your student ID\>-nat-public1-us-east-1a***

          


5. At the bottom of the screen, choose *Create VPC*.

<img width="728" height="441" alt="image" src="https://github.com/user-attachments/assets/47d7d162-76a9-4d3d-aecd-35ee1c34802f" />

   

The VPC resources are created. The NAT Gateway will take a few minutes to activate. Please wait until all the resources are created before proceeding to the next step.


   

6. Once it is complete, choose *View VPC*



The wizard has provisioned a VPC with a public subnet and a private subnet in one Availability Zone with route tables for each subnet. It also created an Internet Gateway and a NAT Gateway.

To view the settings of these resources, browse through the VPC console links that display the resource details. For example, choose Subnets to view the subnet details and choose Route tables to view the route table details. 

<img width="1228" height="526" alt="image" src="https://github.com/user-attachments/assets/aaf20d45-d175-4718-8f06-d0215924dcd6" />


The diagram below summarizes the VPC resources you have just created and how they are configured.

<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_foundation/L2-task1.png" alt="Task 1" />

​         

 

## Task 2: Create Additional Subnets


In this task, you will create two additional subnets for the VPC in a second Availability Zone. Having subnets in multiple Availability Zones within a VPC is useful for deploying solutions that provide **High Availability**. 


After creating a VPC as you have already done, you can still configure it further, for example, by adding more subnets. Each subnet you create resides entirely within one Availability Zone. 

 

1. In the left navigation pane, choose *Subnets*.

   <img width="151" height="296" alt="image" src="https://github.com/user-attachments/assets/ee88fa36-5532-416f-93d8-1097c719b8b5" />


 

2. Choose *Create subnet* at the top right, then configure:

   - VPC ID:  ***\<your student ID\>-vpc*** (select from the menu).

   - Subnet name:  ***\<your student ID\>-subnet-public2***

   - Availability Zone: Select the second Availability Zone (i.e., *us-east-1b*)

   - IPv4 CIDR block: *10.0.2.0/24*

     > The subnet will have all IP addresses starting with *10.0.2.x*.

     <img width="710" height="596" alt="image" src="https://github.com/user-attachments/assets/8bf9e588-4f17-412c-aa98-9f7a16b4aca7" />





3. Choose *Add new subnet*, then configure:

   - Subnet name: ***\<your student ID\>-subnet-private2***

   - Availability Zone: Select the second Availability Zone (i.e., *us-east-1b*)

   - IPv4 CIDR block: *10.0.3.0/24*

     > The subnet will have all IP addresses starting with *10.0.3.x*.

     <img width="712" height="557" alt="image" src="https://github.com/user-attachments/assets/c2b0591d-27e2-444d-b05c-d30294f567b3" />


       

4. Choose *Create subnet* to create two new subnets as configured



Examining the route table tab in the lower pane reveals that both subnets are associated with a route table that only contains the local route for communication within the VPC. This is the main (default) route table automatically upon the creation of this VPC.  It controls the routing for all subnets that are not explicitly associated with any other route table.

Now, you will first configure the new private subnet to route internet-bound traffic to the NAT Gateway so that resources in the second private subnet are able to connect to the Internet, while still keeping the resources private. In other words, you'll associate the second private subnet with a route table that contains the entry for the NAT Gateway.




5. Select  the ***\<your student ID\>-subnet-private2*** subnet.

6. In the lower pane, choose the *Route table* tab, then choose *Edit route table association*.

7. Choose ***\<your student ID\>-rtb-private1-us-east-1a*** from the menu for Route table ID, then Choose *Save*

   <img width="790" height="358" alt="image" src="https://github.com/user-attachments/assets/8b23f509-dcc8-4736-b6cb-abaf36403bd3" />


Note that Destination *0.0.0.0/0* is set to Target *nat-xxxxxxxx*. This means that traffic destined for the internet (*0.0.0.0/0*) will be sent to the NAT Gateway. The NAT Gateway will then forward the traffic to the internet.

This route table is therefore being used to route traffic from private subnets. 

Next, you will configure the Route Table that is used by the Public Subnets.



8. Select  the ***\<your student ID\>-subnet-public2*** subnet.

9. In the lower pane, choose the *Route table* tab, then choose *Edit route table association*.

10. Choose ***\<your student ID\>-rtb-public*** from the menu for Route table ID, then Choose *Save*

    <img width="792" height="373" alt="image" src="https://github.com/user-attachments/assets/4c82675a-3bcb-4a74-bd45-0ceb05af5bf3" />


Note that Destination *0.0.0.0/0* is set to Target *igw-xxxxxxxx*, which is an Internet Gateway. This means that internet-bound traffic will be sent straight to the internet via this Internet Gateway.

Now, the VPC has public and private subnets configured in two Availability Zones. The route tables you created in task 1 have also been updated to route network traffic for the two new subnets.


<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_foundation/L2-task2.png" alt="Task 2" />






## Task 3: Launch a Web Server Instance

In this task, you will launch an Amazon EC2 instance into the new VPC. You will configure the instance to act as a web server.



1. In the search box to the right of  Services, search for and choose EC2 to open the EC2 console.

   <img width="760" height="269" alt="image" src="https://github.com/user-attachments/assets/41ed54cd-6247-44e4-8291-b2c423a27749" />


   

2. From the Launch instance tile choose Launch instance.

   <img width="569" height="142" alt="image" src="https://github.com/user-attachments/assets/5651eeb2-74ed-4988-b8a8-a14e282e2333" />


   

3. Configure the instance:

   - Name: *Web Server 1*

     > When you name your instance, AWS creates a tag and associates it with the instance. A tag is a key value pair. The key for this pair is *Name*, and the value is the name you enter for your EC2 instance.

   - In the list of available Quick Start AMIs, keep the default Amazon Linux selected.

   - Also keep the default Amazon Linux 2023 AMI selected.

     > The type of Amazon Machine Image (AMI) you choose determines the Operating System that will run on the EC2 instance that you launch.

     <img width="820" height="716" alt="image" src="https://github.com/user-attachments/assets/8b917728-8fbf-4765-8093-ae27e66dfc15" />


   - In the Instance type panel, choose *t3.large* from the dropdown menu.

     > The Instance Type defines the hardware resources assigned to the instance. 

   - From the Key pair name menu, select *vockey*.

     > The vockey key pair you selected will allow you to connect to this instance via SSH after it has launched. Although you will not need to do that in this lab, it is still required to identify an existing key pair, or create a new one, or choose to proceed without a key pair, when you launch an instance.

   <img width="813" height="305" alt="image" src="https://github.com/user-attachments/assets/6692d961-1d30-4d47-a22c-298a4ae409d8" />


 

4. Configure the Network settings:


   - Next to Network settings, choose *Edit*, then configure:

     - VPC:  ***\<your student ID\>-vpc***
     - Subnet:  ***\<your student ID\>-subnet-public2*** (not Private!)
     - Auto-assign public IP: *Enable*

     <img width="813" height="233" alt="image" src="https://github.com/user-attachments/assets/b00267d2-426c-452f-8ab3-194077ddedfb" />


     

   - Next, you will configure the instance to use a VPC security group, which acts as a virtual firewall.  You can add rules to the security group to allow traffic to or from its associated instances.

     - Under Firewall (security groups), choose *Create security group*, then configure:

       - Security group name: *Web Server Security Group*

       - Description: *Enable HTTP access*

         

         <img width="812" height="200" alt="image" src="https://github.com/user-attachments/assets/2d1a8617-792c-4a1a-ba9b-d7a5332d109c" />


         

     - Choose *Add security group rule*, then configure the following settings:

       - Type: *HTTP*

       - Source: *Anywhere-IPv4*

       - Description: *Permit web requests*

       <img width="797" height="277" alt="image" src="https://github.com/user-attachments/assets/c2a67c8a-177c-45be-ac61-1131c1eb695b" />




5. In the *Configure storage* section, keep the default settings.

   > Note: The default settings specify that the root volume of the instance, which will host the Amazon Linux operating system that you specified earlier, will run on a general purpose SSD (gp3) hard drive that is 8 GiB in size. You could add more storage volumes, however that is not needed in this lab.

 

6. Configure a script to run on the instance when it launches: 

   - Expand the *Advanced details* panel.

   - Scroll to the bottom of the page and then copy and paste the code shown below into the User data box:

     ```shell
     #!/bin/bash
     dnf install -y httpd
     systemctl enable httpd
     systemctl start httpd
     echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
     ```

     <img width="818" height="374" alt="image" src="https://github.com/user-attachments/assets/6e941701-43f5-4132-b616-9e5de4f43275" />
  
     Remember that your instance is running Amazon Linux 2023. The shell script above will run with root user permissions when the instance launches for the first time. The script will:

     - Install an Apache web server (`httpd`);
     - Configure the web server to automatically start on boot;
     - Run the Web server once it has finished installing;
     - Create a simple Web page.



7. At the bottom of the Summary panel on the right side of the screen choose Launch instance. You will see a Success message.

8. Choose *View all instances*

9. Wait until *Web Server 1* shows 3/3 checks passed in the Status check column.



This may take a few minutes. Choose the refresh  icon at the top of the page every 30 seconds or so to more quickly become aware of the latest status of the instance.



You will now connect to the web server running on the EC2 instance.

 

10. Select  *Web Server 1*.

    

<img width="1070" height="655" alt="image" src="https://github.com/user-attachments/assets/cf9dc19e-2607-479d-8d63-f976d4b169dc" />




11. Copy the Public IPv4 DNS value or the Public IPv4 address value shown in the Details tab at the bottom of the page.

 

12. Open a new web browser tab, paste the Public DNS value or the Public IPv4 address value and press Enter. You should see a test page displaying the AWS logo and your instance's metadata.
    **Keep this tab open for later steps.**

<img width="1159" height="412" alt="image" src="https://github.com/user-attachments/assets/4e4e4d4e-23df-475b-9ee6-548c7d408f36" />


The complete architecture you deployed is:


<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_foundation/L2-end-architecture.png" alt="Architecture" />


# Task 4: Connect to and Manage Your Amazon EC2 Instance

 In this task, you will establish a secure connection to your EC2 instance using the browser-based *EC2 Instance Connect*. Once connected, you will use the Linux command line to verify, stop, and restart the Apache web service.



1. Select the instance we just created
   
2. Click the *Connect* button at the top of the console.

   <img width="1014" height="233" alt="image" src="https://github.com/user-attachments/assets/e55f6f89-ffe1-47e5-aadb-0862f07631f0" />


3. On the *EC2 Instance Connect* tab, leave all the settings as their defaults, then choose *Connect*.

   <img width="1636" height="614" alt="image" src="https://github.com/user-attachments/assets/54622489-d72c-4f43-9665-bf144c5f66bd" />


A new browser tab will open with a terminal session, presenting a command prompt (`$`). You are now securely connected to your EC2 instance.

<img width="507" height="158" alt="image" src="https://github.com/user-attachments/assets/ea038428-76b7-4623-a260-6dda7157214a" />

Now that you have a terminal session, you will interact with the Apache web server (also known as `httpd`).

4. Run the following command to confirm that the Apache web server is active and listening for connections.

   ```shell
   sudo systemctl status httpd
   ```

<img width="1029" height="390" alt="image" src="https://github.com/user-attachments/assets/5fb3e3ae-ca40-455d-8a26-fd26ef7336f7" />


5. Stop the HTTP Web service. Now, you will stop the web server to simulate taking it offline and verify the service has stopped.

   ```shell
   sudo systemctl stop httpd
   sudo systemctl status httpd
   ```
 The output should now show ***inactive (dead)***.  Switch to the browser tab displaying your Web page and refresh the page. The page should now be inaccessible

 6. Restart the web server to bring it back online.
   ```shell
   sudo systemctl start httpd
   sudo systemctl status httpd
   ```

Now, refresh the tab, and the Web page should now be accessible again.


# Task 5: Terminate your EC2 instances

Remember to terminate all running EC2 instances in your console to avoid unnecessary charges and clean up resources.

<img width="1006" height="494" alt="image" src="https://github.com/user-attachments/assets/6f714399-4947-4986-8991-f0e572c24cf9" />


