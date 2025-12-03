 
# Guided Lab 6.2: Automating Infrastructure Deployment with AWS CloudFormation
 
## Lab overview and objectives

Deploying infrastructure in a consistent, reliable manner is difficult. It requires people to follow documented procedures without taking any undocumented shortcuts. It can also be difficult to deploy infrastructure out-of-hours when fewer staff are available. AWS CloudFormation changes this situation by defining infrastructure in a template that can be automatically deployed, even on an automated schedule.

In this lab, you will learn how to deploy multiple layers of infrastructure with AWS CloudFormation, update a CloudFormation stack, and delete a stack (while retaining some resources).

After completing this lab, you should be able to:

- Use AWS CloudFormation to deploy a virtual private cloud (VPC) networking layer
- Use AWS CloudFormation to deploy an EC2 Web server that references the networking layer
- Delete a stack while retaining some resources
- Explore templates with AWS Infrastructure Composer (optional)


<br>

---


## Task 1: Deploying a networking layer

It is a best practice to deploy infrastructure in *layers*. Common layers are:

- Network (Amazon VPC)
- Application (e.g., Web server)
- Database

This way, templates can be reused between systems. For example, you can deploy a common network topology between development, test, and production environments, or deploy a standard database for multiple applications.

In this task, you will deploy an AWS CloudFormation template that creates an Amazon VPC with related resources for a networking layer.

1. Right click the [link](https://canvas.ust.hk/files/11454418/download?download_frd=1&verifier=yusE1GLODhGpbS5ZGd3dMAlkSh7ILSkWzoonQ1eM) and download a template file called *lab-network.yaml* onto your laptop. This file contains the following YAML code:
   
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

   > Note: Templates can be written in JavaScript Object Notation (JSON) or YAML Ain't Markup Language (YAML). YAML is a markup language that is similar to JSON, but it is easier to read and edit.

2. In the *AWS Management Console*, from the search bar at the top of the screen, search for and select *CloudFormation*.
   
   <img width="500"  src="https://github.com/user-attachments/assets/da3a6769-ce22-4e62-8293-a549afa4fcc4" />
   
3. Choose *Create stack \> With new resources (standard)* and configure these settings:

   **Step 1: Specify template**

   - *Template source:* *Upload a template file*
   - *Upload a template file:* Click *Choose file*, then select the *lab-network.yaml* file that you created.
     
     <img width="800" src="https://github.com/user-attachments/assets/050904f4-dc04-4e11-b038-f964d771fde8" />


   - Choose *Next*

   **Step 2: Create Stack**

   - *Stack name:* *lab-network*
     
     <img width="800" src="https://github.com/user-attachments/assets/cb8b38e6-951a-4ef1-84bd-7e8d29c4046f" />
     
   - Choose *Next*

   **Step 3: Configure stack options**

   - In the *Tags* section, enter these values.
     - *Key:* *application*
     - *Value:* *test*

     <img width="800" src="https://github.com/user-attachments/assets/7183b9d2-93b5-4f63-b133-5f725c06cba7" />
  
   - Keep all the other settings as default.
   - Choose *Next*.

   **Step 4: Review lab-network**

   - Choose *Submit*.

   The *template* will now be used by AWS CloudFormation to generate a *stack* of resources in the AWS account.

   The specified *tags* are automatically propagated to the resources that are created, which makes it easier to identify resources that are used by particular applications.

4. Choose the *Stack info* tab.

   
   <img width="300" src="https://github.com/user-attachments/assets/53be5c3d-f22e-473a-a0a6-4b6c71238527" />


5. Wait for the status to change to *CREATE_COMPLETE*.

   <img width="300" src="https://github.com/user-attachments/assets/39c311b9-b564-4559-a46e-a3eeea5cbea1" />

   Choose *Refresh* every 15 seconds to update the display, if necessary.

   You can now examine the resources that were created.

6. Choose the **Resources** tab.

   You will see a list of the resources that were created by the template.

   <img width="800" src="https://github.com/user-attachments/assets/9da69728-0972-424a-aa1b-10eeb7c2c5ed" />


   If the list is empty, update the list by choosing *Refresh* .

7. Choose the *Events* tab and scroll through the events log.

   The events log shows (from more recent to less recent) the activities that were performed by AWS CloudFormation. Example events include starting to create a resource and then completing the resource creation. Any errors that were encountered during the creation of the stack will be listed in this tab.

8. Choose the *Outputs* tab.

   A CloudFormation stack can provide *output information*, such as the ID of specific resources and links to resources.

   Two outputs are listed.

   - **PublicSubnet:** The ID of the public subnet that was created (for example: *subnet-08aafd57f745035f1*)
   - **VPC:** The ID of the VPC that was created (for example: *vpc-08e2b7d1272ee9fb4*)

   <img width="800" src="https://github.com/user-attachments/assets/b19d11a1-a7a9-44c7-ab43-64864df0fa0c" />



   Outputs can also be used to provide values to other stacks. This is shown in the **Export name** column. In this case, the VPC and subnet IDs are given export names so that other stacks can retrieve the values. These other stacks can then build resources inside the VPC and subnet that were just created. You will use these values in the next task.



<br>

---

## Task 2: Deploying a Web server

Now that you deployed the network layer, you will deploy an Amazon Elastic Compute Cloud (Amazon EC2) instance and a security group.

The AWS CloudFormation template will import the VPC and subnet IDs from the ***Outputs*** of the existing CloudFormation stack. It will then use this information to create the security group in the VPC and the EC2 instance in the subnet.

EC2 Instances require key pairs for secure access. However, cloudFormation cannot securely deliver private keys in a key pair to users. So, before we draft the CloudFormation template, we need to create the key pair to use manually, and then use it as a parameter of the template.

EC2 instances require key pairs for SSH access. Because CloudFormation does not deliver the private key in a pair, you are recommended to manually create the key pair first, and then reference it as a parameter in your template.

1. Go to the EC2 console, choose *Key pairs* in the left navigation pane, and choose *Create key pairs*
   
2. Provide a name in the format: *ust-\<your ITSC account string\>* (replace with your actual ITSC account)

   <img width="800"  src="https://github.com/user-attachments/assets/e81f641f-795f-4a32-81c3-a779c3371cbc" />

   Keep the remaining settings at their defaults. Select *Create key pair*

   > Note: The private key file will be automatically downloaded. If you plan to use only the EC2 Instance Connect feature for accessing your instance later, you don't need to retain this private key file.

3. Copy the following YAML code, and paste it into a plain text file. Replace the placeholder *\<the name of the key pair you just created\>* with what is expected. Save the template as *lab-instance.yaml*.

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
       DeletionPolicy: Snapshot
   
     DiskMountPoint:
       Type: AWS::EC2::VolumeAttachment
       Properties:
         InstanceId: !Ref Ec2Instance
         VolumeId: !Ref DiskVolume
         Device: /dev/xvdh
   
     InstanceSecurityGroup:                 # Specifies a security group.
       Type: AWS::EC2::SecurityGroup                  
       Properties:
         GroupDescription: Enable HTTP request
         VpcId: 
           Fn::ImportValue: !Sub '${NetworkStackName}-VPCID'
         SecurityGroupIngress:              # Inbound rules for the security group
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


4. In the left navigation pane, choose **Stacks**.

5. Select **Create stack > With new resources (standard)**, and then configure these settings.

   **Step 1: Specify template**

   - **Template source:** **Upload a template file**
   - **Upload a template file:** Click *Choose file* then select the *lab-instance.yaml* file that you created. <br>
     
     <img width="800" src="https://github.com/user-attachments/assets/23b3054f-e0a0-4a48-ac7f-59d133383167" />


   - Choose *Next*

   **Step 2: Create Stack**

   - *Stack name:* `lab-instance`
   - *KeyName:* `ust-<your ITSC account string>`
   - *NetworkStackName:* `lab-network`
      
     <img width="800" src="https://github.com/user-attachments/assets/e2e1cab7-b991-4c3a-a11f-48ba0592c932" />


   - Choose *Next*
     
     The *KeyName* parameters tells the template the key pair to use, while the *Network Stack Name* parameter tells it the first stack you created (i.e., *lab-network*) so as to retrieve values from its *Outputs*.

   **Step 3: Configure stack options**

   - In the *Tags* section, enter these values.
     - *Key:* `application`
     - *Value:* `test`

     
   - Choose *Next*.

   **Step 4: Review lab-instance**

   - Choose *Create stack*.

   While the stack is being created, examine the details in the **Events** tab and the **Resources** tab. You can monitor the progress of the resource-creation process and the resource status.

6. Wait for the *Status* to change to *CREATE_COMPLETE*.


7. Choose the *Outputs* tab.
   
   <img width="800" src="https://github.com/user-attachments/assets/2975f4b6-74aa-4b20-bf0d-e1e78de6d841" />

8. Copy the *URL* that is displayed, open a new web browser tab, paste the URL, and press ENTER.

   The browser tab will open the webpage, which is running on the web server that this new CloudFormation stack created.


   A CloudFormation stack can use reference values from another CloudFormation stack. For example, this portion of the *lab-instance* template references the *lab-network* template:

   ```yaml
   InstanceSecurityGroup:
     Type: AWS::EC2::SecurityGroup                  
     Properties:
       GroupDescription: Enable HTTP request
       VpcId: 
         Fn::ImportValue: !Sub '${NetworkStackName}-VPCID'
   ```

   The last line uses the *network stack name* that you provided (*lab-network*) when the stack was created. It imports the value of *lab-network-VPCID* from the *Outputs* of the first stack. It then inserts the value into the VPC ID field of the security group definition. The result is that the security group is created in the VPC that was created by the first stack.

   Here is another example. This template code places the EC2 instance into the subnet that was created by the network stack:

   ```yaml
   SubnetId:
     Fn::ImportValue: !Sub ${NetworkStackName}-SubnetID
   ```

   It takes the *subnet ID* from the *lab-network* stack and uses it in the *lab-instance* stack to launch the instance into the public subnet, which was created by the first stack.

<br>

---

## Task 3: Updating a Stack

AWS CloudFormation can also *update* a stack that has been deployed. When you update a stack, AWS CloudFormation will only modify or replace the resources that are being changed. Any resources that are not being changed will be left as-is. 

In this task, you will update the *lab-instance* stack to modify a setting in the security group. This demonstrates how changes can be deployed in a repeatable, documented process. 

First, you will examine the current settings for the security group.

1. Navigate to the *EC2* console.

2. In the left navigation pane, choose *Security Groups*.

3. Select the check box for *lab-instance-InstanceSecurityGroup-xxx*.

   <img width="800" src="https://github.com/user-attachments/assets/f3fc4d9a-d88d-4392-9221-5c030277514c" />


4. Choose the *Inbound rules* tab.

   Currently, only one rule is in the security group. The rule permits inbound HTTP traffic.

   You will now return to AWS CloudFormation to update the stack.



5. Right-click the [link](https://canvas.ust.hk/files/11457839/download?download_frd=1&verifier=rAHEESKLyWrSuRnlzkII52zw7PfihWeKOzKA5mCc) and download the updated template to your computer:

   This template has an additional configuration to permit inbound Secure Shell (SSH) traffic on port 22:

   ```yaml
   - IpProtocol: tcp
     FromPort: 22
     ToPort: 22
     CidrIp: 0.0.0.0/0
   ```

6. Navigate back to the *CloudFormation* console.
   
7. In the *Stacks* list, select *lab-instance*.

8. Choose *Update stack \> Make a direct update* and configure the following settings:

   - Select *Replace existing template*
   - *Template source:* *Upload a template file*
   - Click *Choose file* then select the *lab-instance-2.yaml* file that you downloaded. <br>

  
   <img width="800" src="https://github.com/user-attachments/assets/b01786aa-8f5d-4e66-8c2c-3c8e7e5e983b" />

   - Choose *Next*.

9. In *Step 2: Specify stack details*, make sure you change the *KeyName* field to the name of your key pair. Choose *Next*

10. Advance to the *Review lab-instance* page. In the *Changeset preview* section at the bottom of the page, AWS CloudFormation displays the resources that will be updated:

   <img width="800" src="https://github.com/user-attachments/assets/00609294-cbfd-42d6-89b3-f5b7073b6d98" />


   This changeset preview indicates that AWS CloudFormation will ***Modify*** the *InstanceSecurityGroup* without needing to replace it (*Replacement = False*). This change set means that the security group will have a minor change applied to it, and no references to the security group will need to change.
   
   Choose *Submit*.

11. Wait for the status to change to *UPDATE_COMPLETE*. Update the status by choosing *Refresh* every 15 seconds, if necessary.

You can now verify the change.

12. Return to the *EC2* console and from the left navigation pane, choose *Security Groups*.

13. In the *Security Groups* list, select *lab-instance-InstanceSecurityGroup-xxx*.

    The *Inbound rules* tab should display an additional rule that allows *SSH* traffic over *TCP port 22*.

    <img width="800" src="https://github.com/user-attachments/assets/38cb0faa-ecac-4ad6-a559-315d5c3a3c74" />

(Optional) Next, let's ssh into the launched instance, and explore the Amazon EBS disk volume mounted to it.

14. Select *Instances* in the left navigation pane, choose the launched instance from the *Instances* list, and then choose *Connect* at the top right of the list. It opens the *Connect* pane. Choose *Connect*.

    <img width="800" src="https://github.com/user-attachments/assets/108df803-7a0e-4d42-b4ae-61f3c4f96de3" />

15. In the opened tab that displays the SSH terminal, type the following commands line by line:

    ```shell
    # lists all available block devices and their filesystems, labels, and mount points.
    sudo lsblk -f
    # create an EXT4 filesystem on the EBS disk volume
    sudo mkfs -t ext4 /dev/xvdh
    # creates a directory /data to serve as the mount point
    sudo mkdir /data
    # mount /dev/xvdh (now with an ext4 filesystem) to the /data directory.
    sudo mount /dev/sdh /data
    # lists block devices again to verify changes; the mounted EBS disk volume is now ready for use.
    sudo lsblk -f
    ```

    <img width="700" src="https://github.com/user-attachments/assets/5b93e135-3bb0-42bb-a881-3aa0b3ba4e51" />

    
<br>

---


## Task 4: Deleting the stack

When resources are no longer required, AWS CloudFormation can delete the resources built for the stack.

A *deletion policy* can also specified against resources in a template. It can preserve or (in some cases) back up a resource when its stack is deleted. This feature is useful for retaining databases, disk volumes, or any resource that might be needed after the stack is deleted.

The *lab-instance* stack was configured to take a snapshot of the Amazon Elastic Block Store (Amazon EBS) disk volume before it is deleted. The code in the template that accomplishes that configuration is:

```yaml
DiskVolume:
  Type: AWS::EC2::Volume
  Properties:
    Size: 1
    AvailabilityZone: !GetAtt WebServerInstance.AvailabilityZone
  DeletionPolicy: Snapshot
```

The *DeletionPolicy* in the final line directs AWS CloudFormation to create a snapshot of the disk volume before it is deleted.

You will now delete the *lab-instance* stack and see the results of this deletion policy.

1. Return to the *AWS CloudFormation* console*.

2. In the list of stacks, choose the *lab-instance* link.

3. Choose *Delete* at the top right corner of the *Stacks* list. Choose *Delete* to confirm deletion in the popup window.

   You can monitor the deletion process in the *Events* tab and update the screen by choosing *Refresh* occasionally. You might also see an events log entry that indicates that the EBS snapshot is being created.

4. Wait for the stack to be deleted. It will disappear from the *Stacks* list.

   > Note: The instance stack was removed, but the network stack remained untouched. This reinforces the idea that different teams (for example, the network team or the web application team) could manage their own stacks.

You will now verify that a snapshot of the EBS volume was created before the EBS volume was deleted.


5. Navigate to the *EC2* console, and in the left navigation pane, choose *Snapshots*.

   You should see a snapshot with a **Started** time in the last few minutes.

   <img width="800" src="https://github.com/user-attachments/assets/61b6511a-0939-41b7-ae58-6da7c921e58c" />


6. Now you can manually delete this snapshot if you don't need the data stored in it anymore.

   <img width="800" src="https://github.com/user-attachments/assets/9d2eec20-a7ff-4d6d-afe9-9e4c6efb0147" />

 
<br>

---

## Challenge Task

Copy the provided YAML template into a plain text file and save it with a *.yaml* extension.
To complete the template, fill in the blanks to meet the following requirements:

- Create an IAM group named *Developers*;
- Create an IAM user and assign it to the *Developers* group (the user name is provided via the `IAMUserName` parameter);
- Create an S3 bucket (the bucket name is provided via the `S3BucketName` parameter).
- Create an IAM policy named *DevelopersS3Access* that grants permission to list all account buckets and perform all actions on the bucket created by this template. Attach this policy to the *Developers* group.

After filling in the blanks, append an *Outputs* section to export the values shown in the screenshot below.


<img width="800" src="https://github.com/user-attachments/assets/835804f1-a115-43be-b25c-1e626cf66269" />


  
  
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Creates an IAM Group with S3 privileges, an IAM User, and a named S3 bucket.

Parameters:

  S3BucketName:
    Description: 'The globally unique name for the new S3 bucket.'
    Type: String
    AllowedPattern: '^[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$'
    ConstraintDescription: 'Bucket name must be 3-63 chars, lowercase, and can include dots/hyphens.'

  IAMUserName:
    Description: 'The name of the IAM user to be created.'
    Type: String  

  IAMUserPassword:
    Description: 'Initial password for the IAM user. Must be at least 8 characters.'
    Type: String
    NoEcho: true
    MinLength: 8

Resources:
  # 1. IAM Group for Developers
  DevelopersGroup:
    Type: AWS::IAM::Group
    Properties:
      GroupName: _____________

  # 2. Customer-Managed Policy for S3 Privileges
  DevelopersS3Policy:
    Type: AWS::IAM::Policy
    Properties:
      PolicyName: _____________
      Groups: [_____________]
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          # Allows listing all buckets in the account
          - Effect: 'Allow'
            Action:
              - 's3:ListAllMyBuckets'
            Resource: '*'
          # Allows all actions on the specific bucket created by this template
          - Effect: 'Allow'
            Action: _____________
            Resource:
              - !Sub 'arn:aws:s3:::${S3BucketName}'
              - !Sub '_____________'

  # 3. IAM User
  DeveloperOne:
    Type: AWS::IAM::User
    Properties:
      UserName: _____________
      Groups: [_____________]
      LoginProfile:
        Password: !Ref IAMUserPassword
        PasswordResetRequired: false

  # 4. S3 Bucket
  ProjectBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: _____________
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: 'AES256'

```


After editing and saving your template file, proceed to create a CloudFormation stack to provision all the resources.

Note: In *Step 2: Specify stack details*, configure the settings as follows:

- **Stack name**: *lab-iam-s3*
- **IAMUserUser**: *\<your ITSC account string\>-dev*
- **IAMUserPassword**: *isom5140_lab3*
- **S3BucketName**: *ust-\<your ITSC account string\>-project-bucket*

Once you choose *Submit*, wait for the stack status to change to *CREATE_COMPLETE*. You can view the *BucketArn* you defined in the *Outputs* tab.

Then, log in as the new IAM user (*\<your ITSC account string\>-dev*), navigate to the Amazon S3 console, and verify the S3 permissions:

- You should see the *General purpose buckets* list. This confirms the `s3:ListAllMyBuckets` permission is working.
- Find the bucket named *ust-\<your-ITSC\>-project-bucket*. You should be able to open it, upload, and delete objects, confirming full bucket permissions.


### Tips:

For detailed guidance on the CloudFormation resource syntax used in this chanllege task, consult the official AWS documentation:

- [AWS::IAM::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html) for specifying the *PolicyDocument* and *Groups* properties of the *DevelopersS3Policy* resource;

- [AWS::IAM::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html) for specifying the *Groups* property of the *DeveloperOne* resource.
- [CloudFormation built-in functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference.html)

Additionally, note that the arn of a resource can be retrieved via its `Arn` attribute (`GetAtt`). 


<br>

---

## Task 5: Exploring and editing templates with AWS Infrastructure Composer (Optional)

*AWS Infrastructure Composer* is a graphic tool for creating, viewing, and modifying AWS CloudFormation templates. With it, you can diagram your template resources by using a drag-and-drop interface, and then edit their details through the integrated JSON and YAML editor.

Whether you are a new to AWS CloudFormation or an experienced AWS CloudFormation user, Infrastructure Composer can help you quickly see the interrelationship between a template's resources. It also enables you to easily modify templates.


In this task, you will gain some hands-on experience with Designer.

1. Navigate back to the *AWS CloudFormation* console.

2. In the left navigation pane, choose *Infrastructure Composer*.

3. Choose  *Menu > Open > Template file*, and select the *lab-application-2.yaml* template that you downloaded previously.

   <img width="300" alt="image" src="https://github.com/user-attachments/assets/9efa076c-1308-497d-b2f7-872bcfe096c7" />


   *Infrastructure Composer* will display a graphical representation of the template:

   
   <img width="800" src="https://github.com/user-attachments/assets/2d612c47-56b2-49d8-844e-93c332eddd91" />


   *Infrastructure Composer* is a visual editor for AWS CloudFormation templates. It draws the resources that are defined in a template and their relationship to each other.

Next, let's experiment with the features of the *Infrastructure Composer*. For example, click the displayed resources and choose *Details* to display the portion of the template that defines the resources. You'll also try dragging a new resource from the **Resource types** pane on the left into the *Canvas* area.

4. Choose the *Resources* tab in the left pane, and type *iam::role* in the search bar. Drag the resource *AWS::IAM:Role* into the *Canvas* area.

   <img width="200"  src="https://github.com/user-attachments/assets/09c7f8c2-3360-429e-8ca1-8d845be71358" />
   
5. Repeat the previous step to add *AWS::IAM:InstanceProfile* into the *Canvas* area.

   <img width="200" src="https://github.com/user-attachments/assets/fab79f76-17ac-4eb4-9693-c25faee656af" />
   
6. Switch to the *Template* view. You'll see the definitions of the resources have been automatically inserted into the template.

   <img width="800" src="https://github.com/user-attachments/assets/7ae45049-2865-439d-8a35-32274e6d4a23" />

7. Switch back to the *Canvas* view. Click on the *Role* resource, and then select *Details* in the floating bar. It displays the *Resource properties* editor on the right.
   
   <img width="200"   src="https://github.com/user-attachments/assets/47b0054d-efe5-4d49-ad2d-ce69bc715914" />
   
8. Change the value in the *Logical ID* field from *Role* to *EC2InstanceRole*. Then copy and past the following code into the *Resource configuration* field.

   ```yaml
   AssumeRolePolicyDocument:
     Version: '2012-10-17'
     Statement:
       - Effect: Allow
         Principal:
           Service: ec2.amazonaws.com
         Action: 'sts:AssumeRole'
   Policies:
     - PolicyName: S3ReadAccessPolicy
       PolicyDocument:
         Version: '2012-10-17'
         Statement:
           - Effect: Allow
             Action:
               - 's3:GetObject'
               - 's3:ListBucket'
               - 's3:ListAllMyBuckets'
             Resource: '*'
   ```

   <img width="300"   src="https://github.com/user-attachments/assets/f0164326-5474-4570-93c1-acc92c0c89e5" />

9. Click *Save* to save the change.
    
10. Click on the *InstanceProfile* resource, and then select *Details* in the floating bar. It displays the *Resource properties* editor for this resource on the right.

    <img width="200"  src="https://github.com/user-attachments/assets/084f2f96-a05f-4822-8cc7-af2ce5f458b5" />

11. Change the value in the *Logical ID* field from *InstanceProfile* to *EC2InstanceProfile*. Then copy and past the following code into the *Resource configuration* field.

    ```yaml
    InstanceProfileName: !Sub '${AWS::StackName}-InstanceProfile'
    Roles: [!Ref EC2InstanceRole]
    ```

    <img width="300" src="https://github.com/user-attachments/assets/3c13890c-f132-484c-905e-1d3b1289b62e" />

12. Click *Save* to save the change.

    You will see the *EC2InstanceRole* now nested within the *EC2InstanceProfile*. In AWS, an Instance Profile acts as a container specifically for an IAM role, allowing it to be attached to an EC2 instance.


    <img width="200" src="https://github.com/user-attachments/assets/c1ad93eb-f763-45ef-bd2c-ac04f2d449b4" />

Next, you'll need to attach the *EC2InstanceProfile* to the EC2 instance as one of its properties.

13. Click on the *EC2Instance* resource, and then select *Details* in the floating bar. It displays *Resource properties* panel on the right for this resource.

14. Insert the following line between the *InstanceType* line and the *KeyName* line:
    
    ```yaml
    IamInstanceProfile: !Ref EC2InstanceProfile
    ```

15. Click *Save* to save the change. Visually, the *EC2InstanceProfile* will now be encapsulated in the *EC2Instance* in the diagram, reflecting the attachment.

16. Switch to the *Template* view to inspect the YAML code. You'll see all the changes have been applied in the corresponding sections.
    
17. Scroll down to the bottom, and append the following code to the *Outputs* section to define two more pieces of output information.

    ```yaml
      RoleArn:
        Description: 'The ARN of the created IAM Role'
        Value: !GetAtt EC2InstanceRole.Arn
      
      InstanceProfileName:
        Description: 'The name of the Instance Profile attached to the EC2 instance'
        Value: !Ref EC2InstanceProfile
    ```  
 

18. After finishing editing the template, click on *Validate* to validate the new version of the template.

    <img width="800" src="https://github.com/user-attachments/assets/1f3fd69c-a5d8-4354-a609-e049d8ccaeb0" />

19. If everything goes smoothly without errors, click on *Create template*.

    You'll be prompted to save this new template in an S3 bucket.

20. Choose *Use a different bucket* and type *ust-cftemplate-\<your ITSC account string\>-usa-east-1* in the *Transfer bucket name* filed.

    <img width="450" src="https://github.com/user-attachments/assets/6a4ab449-691e-45cf-9539-bd33f31f2ec3" />

    Choose *Confirm and continue to CloudFormation*. This leads you to the first step of the *Create stack* wizard.

21. Click *Next* in *Step 1:Create stack*.
    
    <img width="800" src="https://github.com/user-attachments/assets/55296da5-99ed-4b8a-a769-dd7f22a44fa5" />
    


22. Type *lab-instance* and choose *Next* in the *Step 2: Specify stack details*.

    <img width="800" alt="image" src="https://github.com/user-attachments/assets/4ab11d72-802a-4a42-ab19-41dece4a2895" />

     

 
23. In *Step 3: Configure stack options*, scroll down to the bottom and tick the checkbox for *"I acknowledge that AWS CloudFormation might create IAM resources with customised names."*

   <img width="800" src="https://github.com/user-attachments/assets/5e4f3bd7-27a9-4c53-95e6-b4cf1370fed9" />

24. Click *Submit* to provision the EC2 instance and all the related resources specified in the template.

25. SSH into the EC2 instance when it's ready for use. Then issue the following commands to interact with S3 from within the instance:

    ```shell
    aws s3 ls
    aws s3 ls s3://<the name of one of your s3 buckets>
    aws s3 cp s3://<the name of one of your s3 buckets>/<the name of a file> downloaded_file
    ```

<br>

---

## After-class task: Clean up all lab resources

To avoid incurring charges for unused resources, please follow the steps below to delete all components created during this lab.

### Step 1: Delete CloudFormation Stacks

In the AWS Management Console, navigate to the CloudFormation service. On the *Stacks* page, select and delete all listed stacks in the reverse order of their creation.

### Step 2: Delete EBS Snapshots

Go to the EC2 console, select *Snapshots* from the left navigation pane, and manually delete all snapshots created for this lab.





    

