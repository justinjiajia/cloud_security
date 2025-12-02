  

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


In this task, you will learn how to access event details in the CloudTrail event history and how to create a CloudTrail trail with CloudWatch logging enabled.

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
  
- On the *Choose trail attributes* page, configure the following:
  - *Trail name*: Enter *LabCloudTrail*.
  - *Storage location*: Choose *Create a new S3 bucket*, and accept the default bucket name, which includes *aws-cloudtrail-logs*.
  - *Log file SSE-KMS encryption*: Clear the check box (to disable this option).

    <img width="891" height="552" alt="image" src="https://github.com/user-attachments/assets/f45e3277-364c-47b9-8fdb-1ef5026068f1" />


  - *CloudWatch Logs*: Select *Enabled*.
  - *Log group*: Choose *New*.
  - *Log group name*: **
  - IAM Role: Choose *Existing*.
  - Role name: Choose *CloudTrailRole*.
    
    > This IAM role grants CloudTrail the permissions to deliver the trail's log events to an Amazon CloudWatch Logs log group. It was also created by the stack you submitted in task 1.

    <img width="800" src="https://github.com/user-attachments/assets/49d75efc-5784-4319-81dd-33fad7d072f3" />


  - Keep the other default trail attributes, and choose *Next*.

- On the *Choose log events* page, configure the following:
  - *Event type*: Select *Management events* only.
  - *API activity*: Keep *Read* and *Write* selected.

    <img width="800" alt="image" src="https://github.com/user-attachments/assets/fc54d315-1350-48e7-ba27-21f4e9c546b9" />
   

  - Choose *Next*.

- Scroll down to the bottom of the page, and choose *Create trail*.

  Wait until the trail is successfully created.

  <img width="800" src="https://github.com/user-attachments/assets/bf91e8e3-c2ed-45a6-b9a2-7f526a1d6919" />


This CloudTrail trail, with CloudWatch logging enabled, is an essential component of the monitoring and alerting solutions that you will build in the rest of this lab.
 

<br>

---
 

## Task 3: Creating a CloudWatch alarm based on a metrics filter

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


  
  

