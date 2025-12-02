  

 # Lab 6 Monitoring and Alerting with CloudTrail and CloudWatch


 
## Lab overview and objectives

In this lab, you will configure logging and monitoring in an AWS account. You will understand how to create an AWS CloudTrail trail, which will be an audit log of API calls made in the account. You will then create an Amazon Simple Notification Service (Amazon SNS) topic. By subscribing your email to the topic, you will be alerted when particular events occur. Next, you will define an Amazon EventBridge rule. The rule will notice any time that someone modifies a security group and will send you an email alert about the incident. Finally, you will create an Amazon CloudWatch alarm to notice whenever multiple failed login attempts occur for the AWS Management Console.

After completing this lab, you should be able to do the following:

- Analyze event details in the CloudTrail event history.
- Create a CloudTrail trail with CloudWatch logging enabled.
- Create an SNS topic and an email subscription to it.
- Configure an EventBridge rule to monitor changes to resources in an AWS account.
- Create CloudWatch metric filters and CloudWatch alarms.
- Query CloudTrail logs by using CloudWatch Logs Insights.
 

 

## Scenario

The lab starts with an Amazon Elastic Compute Cloud (EC2) instance that is associated with a security group. In one of the lab tasks, you will test whether modifying the security group successfully invokes a rule and sends you an email notification. The lab also starts with a preconfigured CloudTrail trail that writes to CloudWatch Logs. The lab also includes a preconfigured AWS Identity and Access Management (IAM) user, which you will use to test alerting for failed console login attempts.

By the end of task x, you will have created the architecture shown in the following diagram:

<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_security/lab6/end-task-5.png"   />


 <br>

---

## Task 1: Preparing your lab environment with CloudFormation

In this task, you will use a CloudFormation template to create an SNS topic and subscribe your email address to the topic. The topic will be used in later tasks to deliver email alerts to you about important activity that occurs in the AWS account.

1. Visit <a href="console.aws.amazon.com/console/home">https://console.aws.amazon.com/console/home</a>. Then choose *Multi-session enabled* from the dropdown menu in the top right of the screen.

   <img width="500"  src="https://github.com/user-attachments/assets/c0fa4abd-534e-4635-a38f-6c58060e5cfc" />

2. Choose *Sign-in using root user email*. Then follow the instructions to log into your root account.

   <img width="300"  src="https://github.com/user-attachments/assets/af7f9159-26f0-4b60-b84d-5a2ce6db9276" />
 

3. Once logged in, in the search bar at the top of the screen, search for and select *CloudFormation*.
   
   <img width="500"  src="https://github.com/user-attachments/assets/da3a6769-ce22-4e62-8293-a549afa4fcc4" />


4. Right-click the link and download a CloudFormation template to your computer

5. Choose *Create stack \> With new resources (standard)* and configure these settings.

   **Step 1: Specify template**

   - *Template source:* *Upload a template file*
   - *Upload a template file:* Click *Choose file*, then select the downloaded *lab-environment.yaml* file.
     
     <img width="800" src="https://github.com/user-attachments/assets/716e7374-d955-4cbb-9bf7-63399c0fea5d" />

   - Choose *Next*

   **Step 2: Create Stack**

   - *Stack name:* *lab-environment*
   - *SubscriptionEmail*: *\<An email account to receive notifications\>* (e.g., your UST email account)
     
     <img width="800" src="https://github.com/user-attachments/assets/0db16807-5181-411c-b7d1-8d3ff525035c" />

     
   - Choose *Next*

   **Step 3: Configure stack options**
   
   - Scroll down to the bottom and tick the checkbox for *"I acknowledge that AWS CloudFormation might create IAM resources with customised names."*

   <img width="800" src="https://github.com/user-attachments/assets/5e4f3bd7-27a9-4c53-95e6-b4cf1370fed9" />
   
   - Keep all the other settings as default.
   - Choose *Next*. 

   **Step 4: Review lab-network**

   - Choose *Submit*.

   The *template* will now be used by AWS CloudFormation to generate a *stack* of resources in the AWS account.

6. Wait for the status to change to *CREATE_COMPLETE*.

   <img width="300" src="https://github.com/user-attachments/assets/1714a343-8496-4e22-9f0b-836b00afdf7e" />


   Choose *Refresh* every 15 seconds to update the display, if necessary.

7. In the email address you provided earlier, you should receive an email notification titled *AWS Notification - Subscription Confirmation* from *Login Failure Notifications* .

   <img width="500" src="https://github.com/user-attachments/assets/0220c818-9af1-474c-8c9d-447ae6841ad0" />
  
9. Click the *Confirm subscription* link to confirm the subscription of your email address to an SNS Topic created by the stack.

    <img width="500" src="https://github.com/user-attachments/assets/5d875a99-d6e4-4dbb-a2c9-d0f29f157a52" />

    Then, close the tab that displays *Subscription confirmed!* 

   > Amazon SNS is a fully managed messaging service that provides the ability to send messages to users at scale through SMS, mobile push, and email. 



   Now, you've created all the resources needed for this lab. The meaning of the previous steps will become clear after we learn CloudFormation for automation.

<br>

---

## Task 2: Creating a CloudTrail trail with CloudWatch Logs enabled

In this task, you will analyze the type of event information that is available in the CloudTrail event history. You will also create a CloudTrail trail with CloudWatch logging enabled.

 

1. Analyze the information available in the CloudTrail event history.

- In the search bar at the top left of the screen, search for and choose *CloudTrail* to open the CloudTrail console.

  <img width="500" src="https://github.com/user-attachments/assets/c1a3601b-a58a-45fa-ae6a-a1a4e2eca8fb" />

- In the navigation pane, choose *Event history*.

  <img width="800" src="https://github.com/user-attachments/assets/46efde6c-01fe-42db-a413-2726be9b2c73" />


- From the *Read-only* dropdown menu under the Event history section heading, choose *Event source*.

  
  
- In the search box to the right of *Event source*, type *cloudformation.amazonaws.com* and choose it when it appears.

  <img width="800" src="https://github.com/user-attachments/assets/ebbaea05-2a9a-4182-b146-ca4fea6aeb8d" />

  
- The events in the event history are filtered so that only audit trail events where the source of the event was AWS CloudFormation are displayed.

  <img width="800" src="https://github.com/user-attachments/assets/84bff424-54f3-4f89-b192-a5b69012fa70" />

  
- Choose the most recent *CreateStack* event.
  
  <img width="800" src="https://github.com/user-attachments/assets/bec7dad5-7c9b-40fa-a7bb-afcfa575ebfe" />


- The *Event record* from the chosen event displays.
  
  > Note: The Event record, sometimes called the event payload, is the full JSON text of an event. The record contains fields that help you determine the requested action as well as when and where the request was made. 

 
  > Analysis: The CreateStack event occurred when we performed task 1 to create resources in the account. Notice that the record includes details such as the `userIdentity `for the person who made the API call, `eventTime`, and `awsRegion`. Other essential audit record details are also provided.

  > Note: The event history exists by default in each Region. The history shows events from the last 90 days for the Region that you are viewing. This view is limited to management events with create, modify, and delete API calls and account activity. To maintain a record of account activity that extends past 90 days, including all management events with the option to include data events and read-only activity, you need to configure a CloudTrail trail. You will do this in the next step.

 

2. Create a *CloudTrail* trail with *CloudWatch Logs* enabled.

- In the navigation pane, choose *Trails*.

  <img width="800" src="https://github.com/user-attachments/assets/9263adff-5e05-4ae9-be91-45f2f57f3044" />

- Choose *Create trail*.
  
- On the Choose trail attributes page, configure the following:
  - *Trail name*: Enter *LabCloudTrail*.
  - *Storage location*: Choose *Create a new S3 bucket*, and accept the default bucket name, which includes *aws-cloudtrail-logs*.
  - *Log file SSE-KMS encryption*: Clear the check box (to disable this option).

    <img width="891" height="552" alt="image" src="https://github.com/user-attachments/assets/f45e3277-364c-47b9-8fdb-1ef5026068f1" />


  - *CloudWatch Logs*: Select Enabled.
  - Log group: Choose New, and accept the default log group name.
  - IAM Role: Choose Existing.
  - Role name: Choose `LabCloudTrailRole`.

    <img width="800" alt="image" src="https://github.com/user-attachments/assets/7d038bef-7b1b-48f6-8f53-eb7a84d4a9f2" />


    <img width="800" alt="image" src="https://github.com/user-attachments/assets/8728b9ec-ed6f-4864-a7f8-df45f2a3e4f5" />

    <details><summary>Inline permission policy named <strong><i>CloudTrailPolicy</i></strong> attached to the <strong><i>LabCloudTrailRole</i></strong></summary>
    <pre lang="json"><code>    
    {
        "Statement": [
            {
                "Action": [
                    "logs:*"
                ],
                "Resource": "*",
                "Effect": "Allow"
            }
        ]
    }    
    </code></pre></details>

    <details><summary>IAM role trust policy for <strong><i>LabCloudTrailRole</i></strong></summary>
    <pre lang="json"><code>    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "cloudtrail.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }
    </code></pre></details>


  - Keep the other default trail attributes, and choose Next.

- On the Choose log events page, configure the following:
  - Event type: Keep Management events selected, and don't select Data events or Insights events.
  - API activity: Keep Read and Write selected.

    <img width="800" alt="image" src="https://github.com/user-attachments/assets/fc54d315-1350-48e7-ba27-21f4e9c546b9" />


Choose Next.

Scroll down to the bottom of the page.

 Important: This is where you would complete the process to create the trail. However, the user that you are logged in as does not have the necessary permissions to create a CloudTrail with CloudWatch Logs enabled. This is because of the security restrictions placed on AWS accounts that are used for labs.

Instead, choose Cancel.

Analyze the existing CloudTrail trail.

Notice that a trail named LabCloudTrail already exists. It is configured with the same settings that you chose in the previous step, except for minor differences such as the Amazon Simple Storage Service (Amazon S3) bucket name and log group name.

This CloudTrail trail, with CloudWatch logging enabled, is an essential component of the monitoring and alerting solutions that you will build in the rest of this lab.

Congratulations! In this task, you learned how to access event details in the CloudTrail event history and how to create a CloudTrail trail.

 

## Task 2: Creating an SNS topic and subscribing to it

Amazon SNS is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication. The A2P functionality provides the ability to send messages to users at scale through SMS, mobile push, and email.

In this task, you will create an SNS topic and subscribe your email address to the topic. The topic will be used in later tasks to deliver email alerts to you about important activity that occurs in the AWS account.

6. Create an SNS topic.

In the search box to the right of  Services, search for and choose Simple Notification Service to open the Amazon SNS console.

To open the navigation pane, choose the  menu icon in the upper-left corner.

In the navigation pane, choose Topics.

Choose Create topic, and configure the following:

Type: Choose Standard.

Name: Enter MySNSTopic

<img width="800" alt="image" src="https://github.com/user-attachments/assets/d4ce80a6-810d-4bce-a42e-08f8d3c39937" />



Expand the Access policy - optional section.

Specify who can publish messages to the topic: Choose Everyone.

Specify who can subscribe to this topic: Choose Everyone.
<img width="1130" alt="image" src="https://github.com/user-attachments/assets/85406932-3e90-4dc0-b15e-36202e889875" />


```json
{
  "Version": "2008-10-17",
  "Id": "__default_policy_ID",
  "Statement": [
    {
      "Sid": "__default_statement_ID",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": [
        "SNS:Publish",
        "SNS:RemovePermission",
        "SNS:SetTopicAttributes",
        "SNS:DeleteTopic",
        "SNS:ListSubscriptionsByTopic",
        "SNS:GetTopicAttributes",
        "SNS:AddPermission",
        "SNS:Subscribe"
      ],
      "Resource": "arn:aws:sns:us-east-1:776520358045:MySNSTopic",
      "Condition": {
        "StringEquals": {
          "AWS:SourceOwner": "776520358045"
        }
      }
    },
    {
      "Sid": "__console_pub_0",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "SNS:Publish",
      "Resource": "arn:aws:sns:us-east-1:776520358045:MySNSTopic"
    },
    {
      "Sid": "__console_sub_0",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": [
        "SNS:Subscribe"
      ],
      "Resource": "arn:aws:sns:us-east-1:776520358045:MySNSTopic"
    }
  ]
}
```

At the bottom of the page, choose Create topic.




 

7. To create an email subscription to the SNS topic, choose Create subscription, and configure the following:

Topic ARN: Notice that the Amazon Resource Number (ARN) of the topic that you just created is already filled in.

Protocol: Choose Email.

Endpoint: Enter an email address where you can receive emails during this lab.

<img width="1128" alt="image" src="https://github.com/user-attachments/assets/96b51854-5f31-427a-991f-9a375a800f71" />


Scroll to the bottom of the page, and choose Create subscription.

 

Check your email and confirm the subscription.

Check your email for a message from AWS Notifications.

In the email body, choose the Confirm subscription link.

A webpage opens and displays a message that the subscription was successfully confirmed.

 

In this task, you successfully created an SNS topic and an email subscription to the topic. You will use this configuration in the next tasks.

 

## Task 3: Creating an EventBridge rule to monitor security groups


In this task, you will create an EventBridge rule. The rule will notice whenever inbound rule changes are made to a new or existing security group in the same Region in your AWS account. Whenever the rule conditions are met, the rule will publish a message to the SNS topic that you created.

 

9. Create a rule to monitor changes to EC2 security groups.

- In the console, in the search box to the right of  Services, search for and choose Amazon EventBridge to open the EventBridge console.
- Choose Create rule.
- In the Define rule detail screen, enter the following details:
  - Name:  MonitorSecurityGroups
  - Event bus: default
  - Rule type: Rule with an event pattern.

    <img width="627" alt="image" src="https://github.com/user-attachments/assets/f3aff451-0567-4f1d-b77c-5ff38f7db496" />

- Choose Next

- In the Build event pattern screen, enter the following details:
  - Event source: AWS events or EventBridge partner events
  - Leave the Sample event - optional default settings
  - Under Event pattern, choose **Custom patterns (JSON editor)**

    > Choose **Custom patterns (JSON editor)** automatically selects **Other** in the above section:
    > <img width="628" alt="image" src="https://github.com/user-attachments/assets/a459066c-64d3-4c40-a25d-32f418fa7c10" />


  - Copy and paste the following code into the Enter the event JSON field

    ```json
    {
      "source": ["aws.ec2"],
      "detail-type": ["AWS API Call via CloudTrail"],
      "detail": {
        "eventSource": ["ec2.amazonaws.com"],
        "eventName": ["AuthorizeSecurityGroupIngress", "ModifyNetworkInterfaceAttribute"]
      }
    }
    ```
  - Choose Next.
    > Important: To record events with a detail-type value of AWS API Call via CloudTrail, a CloudTrail trail with logging enabled is required. The trail that was created for you fulfills this necessary condition.

  - In the Select targets section, configure the following for Target 1:
    - Target types: AWS service
    - Select a target: Choose SNS topic.
    - Topic: Choose MySNSTopic.
    - Permissions:  UnCheck  Use execution role (recommended)
    
      <img width="600" alt="image" src="https://github.com/user-attachments/assets/21f93c22-2a1a-49fe-b9e4-b757d00a548e" />

    - Expand  Additional settings
    - For Configure target input, choose Input transformer.
      <img width="600" alt="image" src="https://github.com/user-attachments/assets/b603b118-23ce-4800-8097-1321874191ae" />

    - Choose Configure input transformer.
    - Scroll down to the ***Target input transformer*** section.
    - In the ***Input path*** field (first box), copy and paste the following code:

      ```json
      {"name":"$.detail.requestParameters.groupId","source":"$.detail.eventName","time":"$.time","value":"$.detail"}
      ```

      <img width="600" alt="image" src="https://github.com/user-attachments/assets/a1d5247c-2c4b-4a83-8afe-720c7d3bdb6a" />
    - In the Template field (second box), copy and paste the following text:    

      ```
      "The <source> API call was made against the <name> security group on <time> with the following details:"
      " <value> "
      ```
 
      > **Analysis**: The Input path you are setting defines four variables: `name`, `source`, `time`, and `value`. For each variable, a value is set by referencing data contained in the JSON structure of CloudTrail events that match the event pattern that you also defined. The Input template that you are setting defined the information that will be passed to the target, which in this case is an SNS topic. Notice that the template includes the names of the four variables defined in the Input path.

  - Choose Confirm then choose Next.
  - In the Configure tags screen choose Next.
  - At the Review and create screen, scroll to the botton and choose Create rule.

    <img width="600" alt="image" src="https://github.com/user-attachments/assets/88946cb7-5cef-43f7-b405-155f013012c6" />

    <img width="600" alt="image" src="https://github.com/user-attachments/assets/e58e55be-e01f-439a-adf2-e84711550bfa" />

 

10. To test the EventBridge rule, modify a security group that is associated with an EC2 instance.

- In the search box to the right of  Services, search for and choose EC2 to open the Amazon EC2 console.
- In the navigation pane, choose Instances.
- Select the check box for LabInstance
  This instance was created for you when you started the lab.

- In the lower pane, choose the Security tab.
- Under Security groups, choose the link for the security group name that contains LabSecurityGroup.
  Details for this security group display.

- On the Inbound rules tab, choose Edit inbound rules.

- Choose Add rule, and configure the following:
  - Type: Choose SSH.
  - Source: Choose Anywhere-IPv4.
  - Choose Save rules.

 

11. Check the CloudTrail event history.
- Navigate to the CloudTrail console.
- In the navigation pane, choose Event history.
  Notice the most recent entries that appear. One event should look similar to the one in the following screenshot.

  <img width="800" alt="CloudTrail event history recent entry" src="https://github.com/user-attachments/assets/96d2cbc6-897e-49a8-a2e9-c2910e7fda82" />

  > Note: If an AuthorizeSecurityGroupIngress event has not appeared yet, you might need to wait a minute or two and then refresh the history. To refresh the history, choose the  refresh icon.

- Choose the AuthorizeSecurityGroupIngress link. In the Event record make sure the fromPort and toPort show 22 and not 80

  <img width="800" alt="image" src="https://github.com/user-attachments/assets/34035edc-2a32-4108-bcd3-522fc022d99a" />

  In the Event record section, notice that details of this event match some of the details that you set in the EventBridge rule that you created a moment ago. 


```json
{
    "eventVersion": "1.10",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROA3JTBYLCOTP5TT67MV:user289515=Jia_Jia",
        "arn": "arn:aws:sts::776520358045:assumed-role/voclabs/user289515=Jia_Jia",
        "accountId": "776520358045",
        "accessKeyId": "ASIA3JTBYLCOV3DU7KQR",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROA3JTBYLCOTP5TT67MV",
                "arn": "arn:aws:iam::776520358045:role/voclabs",
                "accountId": "776520358045",
                "userName": "voclabs"
            },
            "attributes": {
                "creationDate": "2025-06-15T09:52:04Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2025-06-15T10:51:12Z",
    "eventSource": "ec2.amazonaws.com",
    "eventName": "AuthorizeSecurityGroupIngress",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "112.119.155.35",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "requestParameters": {
        "groupId": "sg-0632fa4ee8a8468a4",
        "ipPermissions": {
            "items": [
                {
                    "ipProtocol": "tcp",
                    "fromPort": 22,
                    "toPort": 22,
                    "groups": {},
                    "ipRanges": {
                        "items": [
                            {
                                "cidrIp": "0.0.0.0/0"
                            }
                        ]
                    },
                    "ipv6Ranges": {},
                    "prefixListIds": {}
                }
            ]
        }
    },
    "responseElements": {
        "requestId": "1007f69c-2ccf-4240-a0ed-0d15ea353e94",
        "_return": true,
        "securityGroupRuleSet": {
            "items": [
                {
                    "groupOwnerId": "776520358045",
                    "groupId": "sg-0632fa4ee8a8468a4",
                    "securityGroupRuleId": "sgr-09be5c962afdc06ed",
                    "isEgress": false,
                    "ipProtocol": "tcp",
                    "fromPort": 22,
                    "toPort": 22,
                    "cidrIpv4": "0.0.0.0/0",
                    "securityGroupRuleArn": "arn:aws:ec2:us-east-1:776520358045:security-group-rule/sgr-09be5c962afdc06ed"
                }
            ]
        }
    },
    "requestID": "1007f69c-2ccf-4240-a0ed-0d15ea353e94",
    "eventID": "2aae5c69-4eaf-490d-b022-fd622c12a717",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "776520358045",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "ec2.us-east-1.amazonaws.com"
    },
    "sessionCredentialFromConsole": "true"
}
```

Specifically, the `"eventSource": "ec2.amazonaws.com"` and `"eventName": "AuthorizeSecurityGroupIngress"` name-value pairs in the event match the event pattern that you defined in the rule. Therefore, this event should result in a message being published to the SNS topic that you created.

 

Check the inbox of the email address that you subscribed to the SNS topic.

```
The AuthorizeSecurityGroupIngress API call was made against the sg-0632fa4ee8a8468a4 security group on 2025-06-15T10:51:12Z with the following details:"
" {eventVersion:1.10,userIdentity:{type:AssumedRole,principalId:AROA3JTBYLCOTP5TT67MV:user289515=Jia_Jia,arn:arn:aws:sts::776520358045:assumed-role/voclabs/user289515=Jia_Jia,accountId:776520358045,accessKeyId:ASIA3JTBYLCOV3DU7KQR,sessionContext:{sessionIssuer:{type:Role,principalId:AROA3JTBYLCOTP5TT67MV,arn:arn:aws:iam::776520358045:role/voclabs,accountId:776520358045,userName:voclabs},attributes:{creationDate:2025-06-15T09:52:04Z,mfaAuthenticated:false}}},eventTime:2025-06-15T10:51:12Z,eventSource:ec2.amazonaws.com,eventName:AuthorizeSecurityGroupIngress,awsRegion:us-east-1,sourceIPAddress:112.119.155.35,userAgent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36,requestParameters:{groupId:sg-0632fa4ee8a8468a4,ipPermissions:{items:[{ipProtocol:tcp,fromPort:22,toPort:22,groups:{},ipRanges:{items:[{cidrIp:0.0.0.0/0}]},ipv6Ranges:{},prefixListIds:{}}]}},responseElements:{requestId:1007f69c-2ccf-4240-a0ed-0d15ea353e94,_return:true,securityGroupRuleSet:{items:[{groupOwnerId:776520358045,groupId:sg-0632fa4ee8a8468a4,securityGroupRuleId:sgr-09be5c962afdc06ed,isEgress:false,ipProtocol:tcp,fromPort:22,toPort:22,cidrIpv4:0.0.0.0/0,securityGroupRuleArn:arn:aws:ec2:us-east-1:776520358045:security-group-rule/sgr-09be5c962afdc06ed}]}},requestID:1007f69c-2ccf-4240-a0ed-0d15ea353e94,eventID:2aae5c69-4eaf-490d-b022-fd622c12a717,readOnly:false,eventType:AwsApiCall,managementEvent:true,recipientAccountId:776520358045,eventCategory:Management,tlsDetails:{tlsVersion:TLSv1.3,cipherSuite:TLS_AES_128_GCM_SHA256,clientProvidedHostHeader:ec2.us-east-1.amazonaws.com},sessionCredentialFromConsole:true} "
```

You should have received a message from AWS Notifications indicating that an AuthorizeSecurityGroupIngress API call was made. The API call occurred when you modified the security group.

> Note: Recall that you subscribed your email address to the SNS topic, which is why you received the email.

 

In this task, you successfully created an EventBridge rule to monitor changes to Amazon EC2 security groups in the Region. You also tested that modifying a security group invokes the rule, which then publishes a message to the SNS topic. Finally, you verified that you received an email with details about the event, because you previously subscribed your email to the topic.

 

 

## Task 4: Creating a CloudWatch alarm based on a metrics filter

So far in this lab, you have used **CloudTrail** and **EventBridge** to alert you whenever someone modifies the inbound rules for a security group in one of the Regions in your account. In this task, you will use a different service, CloudWatch, to notify you when a user fails to log in to the AWS Management Console a specific number of times.

 

Create a CloudWatch metric filter.

In the search box to the right of  Services, search for and choose CloudWatch to open the CloudWatch console.

In the navigation pane, expand  Logs, and then choose Log groups.

Select the check box for CloudTrailLogGroup.

<img width="800" alt="image" src="https://github.com/user-attachments/assets/43cbc8bd-3b0c-46d9-a444-695369cab230" />


> Note: Recall that when you created the CloudTrail trail, you configured it to create this log group.

Choose Actions > Create metric filter, and then configure the following:

Filter pattern: Copy and paste the following code:

```
{ ($.eventName = ConsoleLogin) && ($.errorMessage = "Failed authentication") }
```

<img width="600" alt="image" src="https://github.com/user-attachments/assets/227a6a55-8b3b-4626-b5f9-d4c8800d224b" />

Choose Next.

Filter name: Enter ***ConsoleLoginErrors***

Metric namespace: Enter ***CloudTrailMetrics***

Metric name: Enter ***ConsoleLoginFailureCount***

Metric value: Enter `1`

<img width="600" alt="image" src="https://github.com/user-attachments/assets/95fc1e5b-7749-415a-b965-b48b3bf47502" />

At the bottom of the page, choose Next.

Choose Create metric filter.

 

14. Create a CloudWatch alarm based on the metric filter.

    - On the Metric filters tab, select the check box to the right of the ConsoleLoginErrors metric filter that you just created.
      
      <img width="800" alt="image" src="https://github.com/user-attachments/assets/ca25d350-9994-4412-a391-a86974a8e732" />

 

    - Choose Create alarm. A new browser tab opens.
    - On the Specify metric and conditions page, in the Conditions section, configuring the following alarm details:
       - Whenever ConsoleLoginFailureCount is: Choose Greater/Equal.
       - than...: Enter 3
         <img width="800" alt="image" src="https://github.com/user-attachments/assets/90c812ba-7525-4988-91c8-4458ecd5d989" />

         <img width="800" alt="image" src="https://github.com/user-attachments/assets/74ef35cc-7c3f-4bd5-a178-793a8e88640d" />

         Observe the settings. This alarm will be invoked whenever the sum of the ConsoleLoginFailureCount metric that you defined is greater than or equal to 3 within any 5-minute period.

       - Choose Next.

    - On the Configure actions page, configure the following:

Select an SNS topic: Choose Select an existing topic.

Send a notification to...: Choose **MySNSTopic**.

<img width="872" alt="image" src="https://github.com/user-attachments/assets/ecf22ef6-a2e5-402c-851a-85a1bb532382" />


Choose Next.

On the Add name and description page, configure the following:

Alarm name: Enter FailedLogins

Choose Next.

Scroll to the bottom of the page, and choose Create alarm.

Test the CloudWatch alarm by attempting to log in to the console with incorrect credentials at least three times.

In the search box to the right of  Services, search for and choose IAM to open the IAM console.

In the navigation pane, choose Users.
<img width="800" alt="image" src="https://github.com/user-attachments/assets/547b221e-cb42-40db-a593-13d6ff594bb4" />


Choose the link for the test user name.

Choose the Security credentials tab, and then copy the Console sign-in link.

<img width="800" alt="image" src="https://github.com/user-attachments/assets/3f749882-d95a-4d24-8aea-63a0ffa76a0a" />

Paste the copied link into a new browser tab to load the console sign-in page.

Enter credentials, including an incorrect password, and attempt to sign in. Repeat this at least three times:

IAM user name: Enter test

Password: test

Choose Sign in.

 Note: Each time that you attempt to log in, you will see a message indicating that your authentication information is incorrect. This is expected!

 

Re-establish your access to the AWS account.

Close all browser tabs where you have the AWS Management Console open.

On the lab instructions page, choose the AWS  link above these instructions to log in again as the voclabs user.

 Important: Your attempts to log in to the console as the test user cleared the previous authentication information from your browser's cache. Therefore, you need to re-authenticate to gain access to the console.

 

Graph the metric that you created.

Navigate to the CloudWatch console.

In the navigation pane, expand  Metrics, and then choose All metrics.

In the Metrics section, under Custom namespaces, choose CloudTrailMetrics.

<img width="1171" alt="image" src="https://github.com/user-attachments/assets/24f47217-9924-48dd-a4ed-2b00a33e25e2" />

> Note: If CloudTrailMetrics does not yet appear, wait until the SNS notification is received.

Choose Metrics with no dimensions.

Choose ConsoleLoginFailureCount.

In the graph area at the top of the page, a small blue dot should appear. The dot indicates that a login failure was detected.

 

Check the alarm status and details in the CloudWatch console.

In the navigation pane, expand  Alarms, and then choose All alarms.

The State for the FailedLogins alarm should be In alarm.


<img width="800" alt="image" src="https://github.com/user-attachments/assets/9416ce0d-9f32-4bcb-9e52-b06dd3b592a0" />

> Note: If the alarm doesn't show this state, wait a minute or two. To refresh the page, choose the  refresh icon.

 Tip: To find out if the alarm was invoked recently, choose the link for the FailedLogins alarm name, and then choose the History tab.

 <img width="800" alt="image" src="https://github.com/user-attachments/assets/526da2b6-241d-4161-88fd-00a4b345d5a8" />


Check the inbox of the email address that you subscribed to the SNS topic.

You should have received a message about multiple failed login attempts, with content that is similar to the following:
 

```
You are receiving this email because your Amazon CloudWatch Alarm "FailedLogins" in the US East (N. Virginia) region has entered the ALARM state, because "Threshold Crossed: 1 out of the last 1 datapoints [3.0 (15/06/25 12:02:00)] was greater than or equal to the threshold (3.0) (minimum 1 datapoint for OK -> ALARM transition)." at "Sunday 15 June, 2025 12:07:17 UTC".

View this alarm in the AWS Management Console:
https://us-east-1.console.aws.amazon.com/cloudwatch/deeplink.js?region=us-east-1#alarmsV2:alarm/FailedLogins

Alarm Details:
- Name:                       FailedLogins
- Description:               
- State Change:               INSUFFICIENT_DATA -> ALARM
- Reason for State Change:    Threshold Crossed: 1 out of the last 1 datapoints [3.0 (15/06/25 12:02:00)] was greater than or equal to the threshold (3.0) (minimum 1 datapoint for OK -> ALARM transition).
- Timestamp:                  Sunday 15 June, 2025 12:07:17 UTC
- AWS Account:                776520358045
- Alarm Arn:                  arn:aws:cloudwatch:us-east-1:776520358045:alarm:FailedLogins

Threshold:
- The alarm is in the ALARM state when the metric is GreaterThanOrEqualToThreshold 3.0 for at least 1 of the last 1 period(s) of 300 seconds.

Monitored Metric:
- MetricNamespace:                     CloudTrailMetrics
- MetricName:                          ConsoleLoginFailureCount
- Dimensions:                         
- Period:                              300 seconds
- Statistic:                           Sum
- Unit:                                not specified
- TreatMissingData:                    missing


State Change Actions:
- OK:
- ALARM: [arn:aws:sns:us-east-1:776520358045:MySNSTopic]
- INSUFFICIENT_DATA:
```
 

 

## Task 5: Querying CloudTrail logs by using CloudWatch Logs Insights

In this final task in the lab, you will use CloudWatch Logs Insights to query CloudTrail logs.

CloudWatch Logs Insights enables you to interactively search and analyze your log data in Amazon CloudWatch Logs. You can perform queries to help you more efficiently and effectively respond to operational issues.

 

Run a CloudWatch Logs Insights query.

In the CloudWatch console, in the navigation pane, choose Logs Insights.

From the Selection criteria dropdown menu under the Logs Insights section heading, select CloudTrailLogGroup.

Delete the existing content from the query field, and then copy and paste the following code into the query field:
```
filter eventSource="signin.amazonaws.com" and eventName="ConsoleLogin" and responseElements.ConsoleLogin="Failure"
| stats count(*) as Total_Count by sourceIPAddress as Source_IP, errorMessage as Reason, awsRegion as AWS_Region, userIdentity.arn as IAM_Arn

```

<img width="800" alt="image" src="https://github.com/user-attachments/assets/d157fef6-f7c3-49f6-947d-da10ca52ae53" />

Choose Run query.

The output should look similar to the following graph:

<img width="800" alt="image" src="https://github.com/user-attachments/assets/2e1821aa-d2a2-4f54-bc8a-6db2299b683b" />


  
  

