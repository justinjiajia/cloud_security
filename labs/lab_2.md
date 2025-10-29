


# Guided Lab: Build your VPC and Run a Web Server



## Lab overview and objectives

In this lab, you will use Amazon Virtual Private Cloud (VPC) to create your own VPC and add additional components to produce a customized network. You will also create a security group. You will then configure and customize an EC2 instance to run a web server and you will launch the EC2 instance to run in a subnet in the VPC.

Amazon Virtual Private Cloud (Amazon VPC) enables you to launch Amazon Web Services (AWS) resources into a virtual network that you defined. This virtual network closely resembles a traditional network that you would operate in your own data center, with the benefits of using the scalable infrastructure of AWS. You can create a VPC that spans multiple Availability Zones.

After completing this lab, you should be able to do the following:

- Create a VPC.

- Create subnets.

- Configure a security group.

- Launch an EC2 instance into a VPC.

  

## Scenario

In this lab you build the following infrastructure:

<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_foundation/L2-architecture.png" alt="Architecture" />

---

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


   ![image-20251030004501629](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030004501629.png)



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

   ![image-20251030005258707](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030005258707.png)

   

The VPC resources are created. The NAT Gateway will take a few minutes to activate. Please wait until all the resources are created before proceeding to the next step.

   

6. Once it is complete, choose *View VPC*



The wizard has provisioned a VPC with a public subnet and a private subnet in one Availability Zone with route tables for each subnet. It also created an Internet Gateway and a NAT Gateway.

To view the settings of these resources, browse through the VPC console links that display the resource details. For example, choose Subnets to view the subnet details and choose Route tables to view the route table details. 

   ![image-20251030010204115](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030010204115.png)

   

   The diagram below summarizes the VPC resources you have just created and how they are configured.<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_foundation/L2-task1.png" alt="Task 1" />

​         

 

## Task 2: Create Additional Subnets


In this task, you will create two additional subnets for the VPC in a second Availability Zone. Having subnets in multiple Availability Zones within a VPC is useful for deploying solutions that provide **High Availability**. 


After creating a VPC as you have already done, you can still configure it further, for example, by adding more subnets. Each subnet you create resides entirely within one Availability Zone. 

 

1. In the left navigation pane, choose *Subnets*.

   ![image-20251030010659550](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030010659550.png)

 

2. Choose *Create subnet* at the top right, then configure:

   - VPC ID:  ***\<your student ID\>-vpc*** (select from the menu).

   - Subnet name:  ***\<your student ID\>-subnet-public2***

   - Availability Zone: Select the second Availability Zone (i.e., *us-east-1b*)

   - IPv4 CIDR block: *10.0.2.0/24*

     - The subnet will have all IP addresses starting with *10.0.2.x*.

       ![image-20251030011307668](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030011307668.png)




3. Choose *Add new subnet*, then configure:

   - Subnet name: ***\<your student ID\>-subnet-private2***

   - Availability Zone: Select the second Availability Zone (i.e., *us-east-1b*)

   - IPv4 CIDR block: *10.0.3.0/24*

     - The subnet will have all IP addresses starting with *10.0.3.x*.

       ![image-20251030011652372](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030011652372.png)

       

 

4. Choose *Create subnet* to create two new subnets as configured



Examining the route table tab in the lower pane reveals that both subnets are associated with a route table that only contains the local route for communication within the VPC. This is the main (default) route table automatically upon the creation of this VPC.  It controls the routing for all subnets that are not explicitly associated with any other route table.

Now, you will first configure the new private subnet to route internet-bound traffic to the NAT Gateway so that resources in the second private subnet are able to connect to the Internet, while still keeping the resources private. In other words, you'll associate the second private subnet with a route table that contains the entry for the NAT Gateway.



5. In the lower pane, choose *Route tables*.

![image-20251030012007929](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030012007929.png)



> Note: If the newly created routes are not visible, choose refresh  button at the top to update the list of routes.



6. Select  the ***\<your student ID\>-subnet-private2*** subnet.

7. In the lower pane, choose the *Route table* tab, then choose *Edit route table association*.

8. Choose ***\<your student ID\>-rtb-private1-us-east-1a*** from the menu for Route table ID, then Choose *Save*

   ![image-20251030013906059](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030013906059.png)

Note that Destination *0.0.0.0/0* is set to Target *nat-xxxxxxxx*. This means that traffic destined for the internet (*0.0.0.0/0*) will be sent to the NAT Gateway. The NAT Gateway will then forward the traffic to the internet.

This route table is therefore being used to route traffic from private subnets. 

Next, you will configure the Route Table that is used by the Public Subnets.



9. Select  the ***\<your student ID\>-subnet-public2*** subnet.

10. In the lower pane, choose the *Route table* tab, then choose *Edit route table association*.
11. Choose ***\<your student ID\>-rtb-public*** from the menu for Route table ID, then Choose *Save*

![image-20251030014405563](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030014405563.png)

Note that Destination *0.0.0.0/0* is set to Target *igw-xxxxxxxx*, which is an Internet Gateway. This means that internet-bound traffic will be sent straight to the internet via this Internet Gateway.

Now, the VPC has public and private subnets configured in two Availability Zones. The route tables you created in task 1 have also been updated to route network traffic for the two new subnets.


<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_foundation/L2-task2.png" alt="Task 2" />



 

## Task 3: Launch a Web Server Instance

In this task, you will launch an Amazon EC2 instance into the new VPC. You will configure the instance to act as a web server.



1. In the search box to the right of  Services, search for and choose EC2 to open the EC2 console.

   ![image-20251030014812836](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030014812836.png)

   

2. From the Launch instance tile choose Launch instance.

   ![image-20251030014937286](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030014937286.png)

   

3. Configure the instance:

   - Name: *Web Server 1*
     When you name your instance, AWS creates a tag and associates it with the instance. A tag is a key value pair. The key for this pair is *Name*, and the value is the name you enter for your EC2 instance.

   - In the list of available Quick Start AMIs, keep the default Amazon Linux selected.

   - Also keep the default Amazon Linux 2023 AMI selected.

     > The type of Amazon Machine Image (AMI) you choose determines the Operating System that will run on the EC2 instance that you launch.

    ![image-20251030015435353](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030015435353.png)

   - In the Instance type panel, choose *t3.large* from the dropdown menu.

     > The Instance Type defines the hardware resources assigned to the instance. 

   - From the Key pair name menu, select *vockey*.

     > The vockey key pair you selected will allow you to connect to this instance via SSH after it has launched. Although you will not need to do that in this lab, it is still required to identify an existing key pair, or create a new one, or choose to proceed without a key pair, when you launch an instance.

   ![image-20251030015527328](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030015527328.png)

 

4. Configure the Network settings:


   - Next to Network settings, choose *Edit*, then configure:

     - VPC:  ***\<your student ID\>-vpc***
     - Subnet:  ***\<your student ID\>-subnet-public2*** (not Private!)
     - Auto-assign public IP: *Enable*

     ![image-20251030015801737](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030015801737.png)

     

   - Next, you will configure the instance to use a VPC security group, which acts as a virtual firewall.  You can add rules to the security group to allow traffic to or from its associated instances.

     - Under Firewall (security groups), choose *Create security group*, then configure:

       - Security group name: *Web Server Security Group*

       - Description: *Enable HTTP access*

         

         ![image-20251030020513542](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030020513542.png)

         

     - Choose *Add security group rule*, then configure the following settings:

       - Type: *HTTP*

       - Source: *Anywhere-IPv4*

       - Description: *Permit web requests*

       ![image-20251030020613311](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030020613311.png)





5. In the *Configure storage* section, keep the default settings.

   > Note: The default settings specify that the root volume of the instance, which will host the Amazon Linux guest operating system that you specified earlier, will run on a general purpose SSD (gp3) hard drive that is 8 GiB in size. You could add more storage volumes, however that is not needed in this lab.

 

6. Configure a script to run on the instance when it launches: 

   - Expand the *Advanced details* panel.

   - Scroll to the bottom of the page and then copy and paste the code shown below into the User data box:

     ```shell
     #!/bin/bash
     # Install Apache Web Server and PHP
     dnf install -y httpd wget php mariadb105-server
     # Download Lab files
     wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-ACCLFO-2/2-lab2-vpc/s3/lab-app.zip
     unzip lab-app.zip -d /var/www/html/
     # Turn on web server
     chkconfig httpd on
     service httpd start
     ```

     ![image-20251030021037045](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030021037045.png)

     

     > This script will run with root user permissions on the guest OS of the instance. It will run automatically when the instance launches for the first time. The script installs a web server, a database, and PHP libraries, and then it downloads and installs a PHP web application on the web server.



7. At the bottom of the Summary panel on the right side of the screen choose Launch instance. You will see a Success message.

8. Choose *View all instances*

9. Wait until *Web Server 1* shows 3/3 checks passed in the Status check column.



This may take a few minutes. Choose the refresh  icon at the top of the page every 30 seconds or so to more quickly become aware of the latest status of the instance.



You will now connect to the web server running on the EC2 instance.

 

10. Select  *Web Server 1*.

    

![image-20251030021355694](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030021355694.png)



11. Copy the Public IPv4 DNS value or the Public IPv4 address value shown in the Details tab at the bottom of the page.

 

12. Open a new web browser tab, paste the Public DNS value or the Public IPv4 address value and press Enter. You should see a web page displaying the AWS logo and instance meta-data values.

![image-20251030021737839](C:\Users\justi\AppData\Roaming\Typora\typora-user-images\image-20251030021737839.png)

The complete architecture you deployed is:


<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_foundation/L2-end-architecture.png" alt="Architecture" />
