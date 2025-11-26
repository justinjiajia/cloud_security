https://awsacademy.instructure.com/courses/64690/assignments/615155

<img width="800" src="https://github.com/user-attachments/assets/38cfa19c-9eca-4637-849c-495cf37575c9" />


# Module 10 - Guided Lab: Automating Infrastructure Deployment with AWS CloudFormation
 
## Lab overview and objectives

Deploying infrastructure in a consistent, reliable manner is difficult. It requires people to follow documented procedures without taking any undocumented shortcuts. It can also be difficult to deploy infrastructure out-of-hours when fewer staff are available. AWS CloudFormation changes this situation by defining infrastructure in a template that can be automatically deployed—even on an automated schedule.

In this lab, you will learn how to deploy multiple layers of infrastructure with AWS CloudFormation, update a CloudFormation stack, and delete a stack (while retaining some resources).

After completing this lab, you should be able to:

- Use AWS CloudFormation to deploy a virtual private cloud (VPC) networking layer
- Use AWS CloudFormation to deploy an application layer that references the networking layer
- Explore templates with AWS CloudFormation Designer
- Delete a stack that has a deletion policy

   **Do not change the Region unless specifically instructed to do so**.

## Task 1: Deploying a networking layer

It is a best practice to deploy infrastructure in *layers*. Common layers are:

- Network (Amazon VPC)
- Database
- Application

This way, templates can be reused between systems. For example, you can deploy a common network topology between development, test, and production environments, or deploy a standard database for multiple applications.

In this task, you will deploy an AWS CloudFormation template that creates a *networking layer* by using Amazon VPC.

 




1. Copy the following YAML code and paste it into a plain text file called *lab-network.txt*.
   
   ```yaml
   AWSTemplateFormatVersion: 2010-09-09
   Description: Sample template that creates a VPC with DNS and public IPs enabled.
   
   # What follows # is a comment
   # This template creates:
   #   VPC
   #   Internet Gateway
   #   Public Route Table
   #   Public Subnet
   
   
   ######################
   # Resources section
   ######################
   
   Resources:       # A required section; Declares the AWS resources to provision 
   
     ## VPC
   
     VPC:                          # Specify the logical name of a resource
       Type: AWS::EC2::VPC         # A mandatory attribute defines the kind of AWS resource it is. The `Type` attribute has the format AWS::ServiceName::ResourceType.
       Properties:                 # Defines configuration details for the specific resource type; Some properties are required, while others are optional
         EnableDnsSupport: true    # E.g., set the property `EnableDnsSupport` to true 
         EnableDnsHostnames: true
         CidrBlock: 10.0.0.0/16
         
     ## Internet Gateway
   
     InternetGateway:
       Type: AWS::EC2::InternetGateway
     
     VPCGatewayAttachment:
       Type: AWS::EC2::VPCGatewayAttachment
       Properties:
         VpcId: !Ref VPC    
         InternetGatewayId: !Ref InternetGateway   
         # The `Ref` function, when used with a resource (referred to by the logical name in the same template) , returns its identifier 
         # Short form: !Ref logicalName` 
         # Long form: `Ref: logicalName`
     
     ## Public Route Table
   
     PublicRouteTable:
       Type: AWS::EC2::RouteTable
       Properties:
         VpcId: !Ref VPC
     
     PublicRoute:
       Type: AWS::EC2::Route
       DependsOn: VPCGatewayAttachment     # The `DependsOn` attribute enforces creation order by specifying prerequisite resources
       Properties:
         RouteTableId: !Ref PublicRouteTable
         DestinationCidrBlock: 0.0.0.0/0
         GatewayId: !Ref InternetGateway
     
     ## Public Subnet
     
     PublicSubnet:
       Type: AWS::EC2::Subnet
       Properties:
         VpcId: !Ref VPC
         CidrBlock: 10.0.0.0/24
         AvailabilityZone: !Select [0, Fn::GetAZs: !Ref AWS::Region]   
         
         # The Fn::Select function returns a specific item from a list by index
         # Short form: `!Select [index, list]` 
         # Long form: `Fn::Select: [index, list]`
         # The Fn::GetAZs function returns available Availability Zones for a region
         # Short form: `!GetAZs region`
         # Long form: `Fn::GetAZs: region`
         # `AWS::Region` is a built-in parameter for the current region
         # E.g., `!Ref AWS::Region` returns "us-east-1" if the stack is created in Region us-east-1
         # Mixed syntax is required when nesting functions; Consecutive short-form functions cannot be directly chained 
     
     PublicSubnetRouteTableAssociation:
       Type: AWS::EC2::SubnetRouteTableAssociation
       Properties:
         SubnetId: !Ref PublicSubnet
         RouteTableId: !Ref PublicRouteTable
     
     PublicSubnetNetworkAclAssociation:
       Type: AWS::EC2::SubnetNetworkAclAssociation
       Properties:
         SubnetId: !Ref PublicSubnet  
         NetworkAclId: !GetAtt VPC.DefaultNetworkAcl  
         
         # The `Fn::GetAtt` function returns the value of an attribute from a resource in the template
         # What follows the dot is the name of a predefined attribute to retrieve
     
   ######################
   # Outputs section
   ######################
   
   Outputs:
     
     PublicSubnet:                                 # Logical name of the current output; unique within the template.
       Description: The subnet ID to use for public web servers
       Value: !Ref PublicSubnet                    # The value of the output
       Export:                                     # Export output values into other stacks 
         Name: !Sub '${AWS::StackName}-SubnetID'   # The name of the output when used for a cross-stack reference.
         
         # The `Fn::Sub` function replaces variables in strings with values; Functions similarly to Python's f-strings
   
     VPC:
       Description: VPC ID
       Value: !Ref VPC
       Export:                                  
         Name: !Sub '${AWS::StackName}-VPCID'
   ```

   Templates can be written in JavaScript Object Notation (JSON) or YAML Ain't Markup Language (YAML). YAML is a markup language that is similar to JSON, but it is easier to read and edit.

2. In the **AWS Management Console**, from the **Services** menu, choose **CloudFormation**.

3. Choose **Create stack \> With new resources (standard)**  and configure these settings.

   **Step 1: Specify template**

   - **Template source:** **Upload a template file**
   - **Upload a template file:** Click **Choose file** then select the *lab-network.yaml* file that you created.
     
     <img width="800" src="https://github.com/user-attachments/assets/f44e84f7-1fd0-463c-971f-28ce778c9984" />

   - Choose **Next**

   **Step 2: Create Stack**

   - **Stack name:** *lab-network*
     
     <img width="800" src="https://github.com/user-attachments/assets/cb8b38e6-951a-4ef1-84bd-7e8d29c4046f" />
     
   - Choose **Next**

   **Step 3: Configure stack options**

   - In the **Tags** section, enter these values.
     - **Key:** *application*
     - **Value:** *test*

     <img width="800" src="https://github.com/user-attachments/assets/7183b9d2-93b5-4f63-b133-5f725c06cba7" />
  
   - Keep all the other settings as default.
   - Choose **Next**.

   **Step 4: Review lab-network**

   - Choose **Submit**.

   The *template* will now be used by AWS CloudFormation to generate a *stack* of resources in the AWS account.

   The specified *tags* are automatically propagated to the resources that are created, which makes it easier to identify resources that are used by particular applications.

4. Choose the **Stack info** tab.

   
   <img width="300" src="https://github.com/user-attachments/assets/53be5c3d-f22e-473a-a0a6-4b6c71238527" />


5. Wait for the status to change to *CREATE_COMPLETE*.

   <img width="300" src="https://github.com/user-attachments/assets/39c311b9-b564-4559-a46e-a3eeea5cbea1" />

   Choose **Refresh** every 15 seconds to update the display, if necessary.

   You can now examine the resources that were created.

6. Choose the **Resources** tab.

   You will see a list of the resources that were created by the template.

   <img width="800" src="https://github.com/user-attachments/assets/9da69728-0972-424a-aa1b-10eeb7c2c5ed" />


   If the list is empty, update the list by choosing **Refresh** .

7. Choose the **Events** tab and scroll through the events log.

   The events log shows (from more recent to less recent) the activities that were performed by AWS CloudFormation. Example events include starting to create a resource and then completing the resource creation. Any errors that were encountered during the creation of the stack will be listed in this tab.

8. Choose the **Outputs** tab.

   A CloudFormation stack can provide *output information*, such as the ID of specific resources and links to resources.

   Two outputs are listed.

   - **PublicSubnet:** The ID of the public subnet that was created (for example: *subnet-08aafd57f745035f1*)
   - **VPC:** The ID of the VPC that was created (for example: *vpc-08e2b7d1272ee9fb4*)

   <img width="800" src="https://github.com/user-attachments/assets/b19d11a1-a7a9-44c7-ab43-64864df0fa0c" />



   Outputs can also be used to provide values to other stacks. This is shown in the **Export name** column. In this case, the VPC and subnet IDs are given export names so that other stacks can retrieve the values. These other stacks can then build resources inside the VPC and subnet that were just created. You will use these values in the next task.



## Task 2: Deploying a Web server

Now that you deployed the *network layer*, you will deploy an *application layer* that contains an Amazon Elastic Compute Cloud (Amazon EC2) instance and a security group.

The AWS CloudFormation template will *import* the VPC and subnet IDs from the *Outputs* of the existing CloudFormation stack. It will then use this information to create the security group in the VPC and the EC2 instance in the subnet.

1. Copy the following YAML code and paste it into a plain text file called *lab-instance.txt*.

   ```yaml
   AWSTemplateFormatVersion: 2010-09-09
   Description: Sample template that creates an EC2 and places it in the VPC created by the previous stack.
   
   Parameters:            # This section declares parameters for the template
     
     NetworkStackName:              # Parameter logic name
       Description: >-              # YAML syntax for introducing multi-line strings
         Name of an active CloudFormation stack that contains the networking
         resources, such as the VPC and subnet that will be used in this stack.
       Type: String
       Default: lab-network         # Default value for the parameter
   
     KeyName:
       Type: AWS::EC2::KeyPair::KeyName
       Description: Name of an existing EC2 KeyPair
       Default: <the name of the key pair you just created>
   
   Resources:
   
     Ec2Instance:
       Type: AWS::EC2::Instance
       Properties:
         ImageId: ami-0fa3fe0fa7920f68e
         InstanceType: t2.micro
         KeyName: !Ref KeyName
   
         NetworkInterfaces:                          # Defines network interfaces for EC2 instance
           - GroupSet: [!Ref InstanceSecurityGroup]  # `GroupSet` is a list of security group IDs
             AssociatePublicIpAddress: true          # Assigns a public IP address to the network interface
             DeviceIndex: 0                          # Primary network interface (eth0)
             DeleteOnTermination: true               # Auto-deletes the network interface when the instance terminates
             SubnetId: 
               Fn::ImportValue: !Sub '${NetworkStackName}-SubnetID'  
               # The `Fn::ImportValue` function imports the value of the specified name exported by another stack
         
         UserData:
           Fn::Base64: |    # `|` is the YAML syntax for introducing multi-line strings; This text preserves line breaks exactly as written.
             #!/bin/bash
             dnf install -y httpd
             systemctl enable httpd
             systemctl start httpd
             echo '<html><img src="https://raw.githubusercontent.com/justinjiajia/cloud_security/refs/heads/main/labs/resources/AWS_logo_RGB.png" /><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
         
           # The `Fn::Base64` function returns the Base64 representation of the input string. 
           # This function is typically used to pass encoded data to Amazon EC2 instances by way of the UserData property.
   
     DiskVolume:
       Type: AWS::EC2::Volume
       Properties:
         Size: 1                          # Smallest possible - 1 GiB
         VolumeType: gp3                  # Recommended default type
         AvailabilityZone: !GetAtt Ec2Instance.AvailabilityZone
   
     DiskMountPoint:
       Type: AWS::EC2::VolumeAttachment
       Properties:
         InstanceId: !Ref Ec2Instance
         VolumeId: !Ref DiskVolume
         Device: /dev/sdh
   
     InstanceSecurityGroup:                   # Specifies a security group.
       Type: AWS::EC2::SecurityGroup                  
       Properties:
         GroupDescription: Enable SSH access via port 22
         VpcId: 
           Fn::ImportValue: !Sub '${NetworkStackName}-VPCID'
         SecurityGroupIngress:                # Inbound rules for the security group
           - IpProtocol: tcp
             FromPort: 80
             ToPort: 80
             CidrIp: 0.0.0.0/0
   
   Outputs:
   
     EC2Instance:
       Description: Instance ID
       Value: !Ref Ec2Instance
       Export:
         Name: !Sub '${AWS::StackName}-InstanceID'
   
     URL:
       Description: URL of the sample website
       Value: !Sub 'http://${Ec2Instance.PublicDnsName}'
   ```


3. In the left navigation pane, choose **Stacks**.

4. Select **Create stack > With new resources (standard)**, and then configure these settings.

   **Step 1: Specify template**

   - **Template source:** **Upload a template file**
   - **Upload a template file:** Click **Choose file** then select the *lab-instance.txt* file that you created.
     <img width="800" src="https://github.com/user-attachments/assets/440144ce-4ea3-4d38-9b63-c86d5a1782e4" />

   - Choose **Next**

   **Step 2: Create Stack**

   - **Stack name:** `lab-instance`
   - **NetworkStackName:** `lab-network`
      
     <img width="800" src="https://github.com/user-attachments/assets/e2e1cab7-b991-4c3a-a11f-48ba0592c932" />


   - Choose **Next**


    The *Network Stack Name* parameter tells the template the name of the first stack that you created (*lab-network*), so it can retrieve values from the *Outputs*.

   **Step 3: Configure stack options**

   - In the **Tags** section, enter these values.
     - **Key:** `application`
     - **Value:** `test`

     
   - Choose **Next**

   **Step 4: Review lab-instance**

   - Choose **Create stack**

   While the stack is being created, examine the details in the **Events** tab and the **Resources** tab. You can monitor the progress of the resource-creation process and the resource status.

5. Wait for the **Status** to change to CREATE_COMPLETE.


6. Choose the **Outputs** tab.
   
   <img width="800" src="https://github.com/user-attachments/assets/2975f4b6-74aa-4b20-bf0d-e1e78de6d841" />



8. Copy the **URL** that is displayed, open a new web browser tab, paste the URL, and press ENTER.

   The browser tab will open the application, which is running on the web server that this new CloudFormation stack created.


   A CloudFormation stack can use reference values from another CloudFormation stack. For example, this portion of the *lab-instance* template references the *lab-network* template:

   ```yaml
   WebServerSecurityGroup:
     Type: AWS::EC2::SecurityGroup
     Properties:
       GroupDescription: Enable HTTP ingress
       VpcId:
         Fn::ImportValue: !Sub ${NetworkStackName}-VPCID
   ```

   The last line uses the *network stack name* that you provided (*lab-network*) when the stack was created. It imports the value of *lab-network-VPCID* from the *Outputs* of the first stack. It then inserts the value into the VPC ID field of the security group definition. The result is that the security group is created in the VPC that was created by the first stack.

   Here is another example, which is in the CloudFormation template that you just used to create the application stack. This template code places the EC2 instance into the subnet that was created by the network stack:

   ```yaml
   SubnetId:
     Fn::ImportValue:
     !Sub ${NetworkStackName}-SubnetID
   ```

   It takes the *subnet ID* from the *lab-network* stack and uses it in the *lab-instance* stack to launch the instance into the public subnet, which was created by the 1st stack.

## Task 3: Updating a Stack

AWS CloudFormation can also *update* a stack that has been deployed. When you update a stack, AWS CloudFormation will only modify or replace the resources that are being changed. Any resources that are not being changed will be left as-is.

In this task, you will update the *lab-application* stack to modify a setting in the security group.

First, you will examine the current settings for the security group.

1. In the **AWS Management Console**, from the **Services** menu, choose **EC2**.

2. In the left navigation pane, choose **Security Groups**.

3. Select the check box for *lab-instance-InstanceSecurityGroup-xxx*.

   <img width="800" src="https://github.com/user-attachments/assets/f3fc4d9a-d88d-4392-9221-5c030277514c" />


4. Choose the **Inbound rules** tab.

   Currently, only one rule is in the security group. The rule permits *HTTP* traffic.

   You will now return to AWS CloudFormation to update the stack.

6. From the **Services** menu, choose **CloudFormation**.

7. Right-click the following link and download the updated template to your computer:

   This template has an additional configuration to permit inbound Secure Shell (SSH) traffic on port 22:

   ```yaml
   - IpProtocol: tcp
     FromPort: 22
     ToPort: 22
     CidrIp: 0.0.0.0/0
   ```

9. In the **Stacks** list of the **AWS CloudFormation console**, select **lab-instance**.

10. Choose **Update stack \> Make a direct update** and configure these settings.

   - Select **Replace current template**
   - **Template source:** **Upload a template file**
   - **Upload a template file:** Click **Choose file** then select the *lab-instance-2.txt* file that you downloaded.

   <img width="800" src="https://github.com/user-attachments/assets/ba29939e-7574-40c1-9115-d672d82a2544" />



11. Choose **Next** in each of the next *three* screens to advance to the **Review lab-application** page.

   In the **Change set preview** section at the bottom of the page, AWS CloudFormation displays the resources that will be updated:

   <img width="800" src="https://github.com/user-attachments/assets/00609294-cbfd-42d6-89b3-f5b7073b6d98" />



   This change set preview indicates that AWS CloudFormation will ***Modify*** the *InstanceSecurityGroup* without needing to replace it (*Replacement = False*). This change set means that the security group will have a minor change applied to it, and no references to the security group will need to change.

11. Choose **Submit**

12. Wait for the status to change to *UPDATE_COMPLETE*.

     Update the status by choosing **Refresh** every 15 seconds, if necessary.

    You can now verify the change.

13. Return to the **Amazon EC2 console** and from the left navigation pane, choose **Security Groups**.

14. In the **Security Groups** list, select *lab-instance-InstanceSecurityGroup-xxx*.

    The **Inbound rules** tab should display an additional rule that allows *SSH* traffic over *TCP port 22*.

    <img width="800" src="https://github.com/user-attachments/assets/38cb0faa-ecac-4ad6-a559-315d5c3a3c74" />



    This subtask demonstrates how changes can be deployed in a repeatable, documented process. 

## Task 4: Exploring templates with AWS CloudFormation Designer

*AWS CloudFormation Designer* is a graphic tool for creating, viewing, and modifying AWS CloudFormation templates. With Designer, you can diagram your template resources by using a drag-and-drop interface, and then edit their details through the integrated JSON and YAML editor.

Whether you are a new to AWS CloudFormation or an experienced AWS CloudFormation user, Designer can help you quickly see the interrelationship between a template's resources. It also enables you to easily modify templates.



In this task, you will gain some hands-on experience with Designer.

1. From the **Services** menu, choose **CloudFormation**.

2. In the left navigation pane, choose **Infrastructure Composer**.

   **Tip:** You might need to expand the left navigation pane by choosing the menu icon.

3. Choose the **File** menu, select **Open > Template file**, and select the **lab-application2.yaml** template that you downloaded previously.

   <img width="300" alt="image" src="https://github.com/user-attachments/assets/9efa076c-1308-497d-b2f7-872bcfe096c7" />


   **Infrastructure Composer** will display a graphical representation of the template:

   <img width="1000" alt="image" src="https://github.com/user-attachments/assets/8cb429ca-5479-4e86-b96c-aa61a2228eae" />


   ![CloudFormation Designer](img/designer.png)

   Instead of drawing a typical architecture diagram, Designer is a visual editor for AWS CloudFormation templates. It draws the resources that are defined in a template and their relationship to each other.

5. Experiment with the features of the Designer. Some things to try are:

   - Click the displayed resources and choose Details. The right pane will then display the portion of the template that defines the resources.


     <img width="1000" alt="image" src="https://github.com/user-attachments/assets/0aed4ffa-2912-4d22-8b44-bdc76703d24b" />

   - Try dragging a new resource—from the **Resource types** pane on the left—into the design area. The definition of the resource will be automatically inserted into the template.
   - Try dragging the resource connector circles to create relationships between resources.
   - Open the **lab-network.yaml** template that you downloaded earlier in the lab and also explore its resources in Designer.

## Task 5: Deleting the stack

When resources are no longer required, AWS CloudFormation can delete the resources built for the stack.

A *deletion policy* can also be specified against resources. It can preserve or (in some cases) back up a resource when its stack is deleted. This feature is useful for retaining databases, disk volumes, or any resource that might be needed after the stack is deleted.

The *lab-application* stack was configured to take a snapshot of an Amazon Elastic Block Store (Amazon EBS) disk volume before it is deleted. The code in the template that accomplishes that configuration is:

```
  DiskVolume:
    Type: AWS::EC2::Volume
    Properties:
      Size: 100
      AvailabilityZone: !GetAtt WebServerInstance.AvailabilityZone
      Tags:
        - Key: Name
          Value: Web Data
    DeletionPolicy: Snapshot
```

The *DeletionPolicy* in the final line directs AWS CloudFormation to create a snapshot of the disk volume before it is deleted.

You will now delete the *lab-instance* stack and see the results of this deletion policy.

1. Return to the main **AWS CloudFormation console** by choosing the Close link at the top of the Designer page (choose **Leave page** if prompted).

2. In the list of stacks, choose the **lab-application** link.

   <img width="1000" alt="image" src="https://github.com/user-attachments/assets/3f99ea7c-c15d-4976-b2ef-893ad9acc99e" />


4. Choose **Delete**

5. Choose **Delete stack**

   You can monitor the deletion process in the **Events** tab and update the screen by choosing **Refresh** occasionally. You might also see an events log entry that indicates that the EBS snapshot is being created.

6. Wait for the stack to be deleted. It will disappear from the stacks list.

   The application stack __ removed, but the network stack remained untouched. This scenario reinforces the idea that different teams (for example, the network team or the application team) could manage their own stacks.

   You will now verify that a snapshot of the EBS volume was created before the EBS volume was deleted.

   <img width="800" alt="image" src="https://github.com/user-attachments/assets/813962e7-bd49-4ae6-a025-12647e50e15d" />


8. From the **Services** menu, choose **EC2**.

9. In the left navigation pane, choose **Snapshots**.

   You should see a snapshot with a **Started** time in the last few minutes.

   <img width="800" alt="image" src="https://github.com/user-attachments/assets/e2b1bff7-612c-46bd-bed0-ed83416b2823" />


    

