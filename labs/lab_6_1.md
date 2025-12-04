  

 # Guided Lab 6.1: Monitoring and Alerting with CloudTrail and CloudWatch


 
## Lab overview and objectives

In this lab, you will configure logging and monitoring in an AWS account. You will understand how to create an AWS CloudTrail trail, which will be an audit log of API calls made in the account. You will then create an Amazon CloudWatch alarm to notice whenever multiple failed login attempts occur for the AWS Management Console.

After completing this lab, you should be able to do the following:

- Analyze event details in the CloudTrail event history.
- Create a CloudTrail trail with CloudWatch logging enabled.
- Create CloudWatch metric filters and CloudWatch alarms.



By the end of this lab, you will have created the architecture shown in the following diagram:

<img src="https://raw.githubusercontent.com/justinjiajia/img/refs/heads/master/aws/cloud_security/lab6/end-task-5.png"   />


 <br>

---

## Task 1: Preparing your lab environment with CloudFormation


In this task, you will provision an SNS (short for Simple Notification Service) topic and subscribe your email address using a CloudFormation template. This topic will be used in subsequent tasks to deliver email alerts to you about important activity that occurs in the AWS account.

1. Visit <a href="console.aws.amazon.com/console/home">https://console.aws.amazon.com/console/home</a>. Then choose *Multi-session enabled* from the dropdown menu in the top right of the screen.

   <img width="500"  src="https://github.com/user-attachments/assets/c0fa4abd-534e-4635-a38f-6c58060e5cfc" />

2. Choose *Sign-in using root user email*. Then follow the instructions to log into your root account.

   <img width="300"  src="https://github.com/user-attachments/assets/af7f9159-26f0-4b60-b84d-5a2ce6db9276" />
 

3. Once logged in, in the search bar at the top of the screen, search for and select *CloudFormation*.
   
   <img width="500"  src="https://github.com/user-attachments/assets/da3a6769-ce22-4e62-8293-a549afa4fcc4" />


4. Right-click the [link](https://canvas.ust.hk/files/11453703/download?download_frd=1&verifier=jzVegIZJlGirL0D8Q7YsBfHUatj8xbEimEZQf3Uz) and download a CloudFormation template to your computer

5. Choose *Create stack \> With new resources (standard)* and configure these settings.

   **Step 1: Specify template**

   - *Template source:* *Upload a template file*
   - *Upload a template file:* Click *Choose file*, then select the downloaded *lab-environment.yaml* file.
     
     <img width="800" src="https://github.com/user-attachments/assets/716e7374-d955-4cbb-9bf7-63399c0fea5d" />

   - Choose *Next*

   **Step 2: Create Stack**

   - *Stack name:* *lab-environment*
   - *SubscriptionEmail*: *\<An email address to receive notifications\>* (e.g., your UST email)
     
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


You have now used your first AWS CloudFormation template to provision the lab environment, including an SNS topic and an IAM role. The purpose of the IAM role will become clear in task 2. We will take a deep dive into automating infrastructure deployment with CloudFormation in the later part of today's class.

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
  - *Log group name*: *CloudTrailLogGroup*
  - IAM Role: Choose *Existing*.
  - Role name: Choose *CloudTrailRole*.
    
    > This IAM role grants CloudTrail the permissions to deliver the trail's log events to an Amazon CloudWatch Logs log group. This role was also created by the stack you submitted in task 1.

    <img width="800" src="https://github.com/user-attachments/assets/49d75efc-5784-4319-81dd-33fad7d072f3" />

    > This step configures this new trail to send events to *CloudWatch Logs*, in addition to archiving them in S3. The main reason to do so is to unlock real-time operational monitoring and security alerting. Later, you'll see how CloudWatch Logs allows you to set up alarms and get notified via SNS when specific events occur.


  - Keep the other default trail attributes, and choose *Next*.

- On the *Choose log events* page, configure the following:
  - *Event type*: Select *Management events* only.
  - *API activity*: Keep *Read* and *Write* selected.
 
    <img width="800" src="https://github.com/user-attachments/assets/5ee364ac-d31d-4792-8f6f-90376565bf96" />
 
   

  - Choose *Next*.

- Scroll down to the bottom of the page, and choose *Create trail*.

  Wait until the trail is successfully created.

  <img width="800" src="https://github.com/user-attachments/assets/bf91e8e3-c2ed-45a6-b9a2-7f526a1d6919" />


By enabling CloudWatch Logs for this CloudTrail trail, we create a pipeline that streams API audit logs consolidated by this trail to CloudWatch. This allows us to use CloudWatch's alarm system to build real-time monitoring and alerting on specific API activities.
 

<br>

---
 

## Task 3: Creating a CloudWatch alarm based on a metrics filter


In this task, you will use CloudWatch to notify you when a user fails to log in to the AWS Management Console a specific number of times.

The core workflow is to: 

- Create metric filters on a CloudWatch Logs log group to detect specific API patterns. 
- Create CloudWatch Alarms based on those metrics to send alerts (e.g., via SNS).

 

### Task 3.1 Create a CloudWatch metric filter


1. In the search box at the top left corner of your screen, search for and choose *CloudWatch* to open the CloudWatch console.

   <img width="500" src="https://github.com/user-attachments/assets/ad5ee00e-f5b7-4426-8696-d8fd99059f4c" />


2. In the navigation pane, expand Logs, and then choose *Log groups*.

   <img width="800" src="https://github.com/user-attachments/assets/f0b4f9a3-93fa-4ebb-b2f7-57d5b95160cd" />


3. Select the check box for *CloudTrailLogGroup*.

   > Note: Recall that when you created the CloudTrail trail, you configured it to create this log group.

4. Choose *Actions > Create metric filter*.

   <img width="800" src="https://github.com/user-attachments/assets/0cddd773-270c-44a4-b432-2258c23372df" />

5. In the *Create metric filter* wizard, configure the following:
     

   - Filter pattern: Copy and paste the following code:

     ```regex
     { ($.eventName = ConsoleLogin) && ($.errorMessage = "Failed authentication") }
     ```

     <img width="800" src="https://github.com/user-attachments/assets/39a9032d-7982-40a6-bf5c-5a61356ddeea" />

     
     > Written in the CloudWatch Logs [filter pattern syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html), the filter pattern identifies and counts `ConsoleLogin` events where the `errorMessage` displays `"Failed authentication"`.
     
   - Choose *Next*.

6. In *Step 2: Assign metric*, configure the following:

   - *Filter name*: Enter *ConsoleLoginErrors*
   - *Metric namespace*: Enter *CloudTrailMetrics*
   - *Metric name*: Enter *ConsoleLoginFailureCounts*
   - *Metric value*: Enter `1`
  
   <img width="682" height="548" alt="image" src="https://github.com/user-attachments/assets/b3289a6f-1469-4e25-b3c9-ae82de0463da" />

   At the bottom of the page, choose *Next*.

7. In *Step 3: Review and create*, Choose *Create metric filter*.

Now, you've created a metric resulting from filtering `ConsoleLogin` events.  Next, you will set a CloudWatch alarm on the new metric to trigger an SNS email notification when a threshold (e.g., 3 failed logins in 5 minutes) is breached.

<br>

### Task 3.2 Create a CloudWatch alarm based on the metric filter

1. On the *Metric filters* tab, select the check box to the right of the *ConsoleLoginErrors* metric filter that you just created.
      
  <img width="800" src="https://github.com/user-attachments/assets/4ae13519-a27b-4d10-af49-3d1bac8abe2f" />

 

2. Choose *Create alarm*. A new browser tab opens.

3. On the *Specify metric and conditions* page, in the *Conditions* section, configuring the following alarm details:

   - *Whenever ConsoleLoginFailureCounts is...*: Choose *Greater/Equal*.
   - *than...*: Enter `3`

     <img width="800" src="https://github.com/user-attachments/assets/895fabbf-0552-4dda-af34-4395df2fd06e" />

         

   - Keep the other settings as default.
  
     <img width="800" src="https://github.com/user-attachments/assets/9bbd6fd9-ac57-45b3-9775-88787e9cd0f8" />


     This means the alarm will be invoked whenever the sum of the *ConsoleLoginFailureCounts* metric that you defined is greater than or equal to 3 within any 5-minute period.

   - Choose Next.

4. On the *Configure actions* page, configure the following:

   - *Select an SNS topic*: Choose *Select an existing topic*.
   - *Send a notification to...*: Choose *LoginFailureSNSTopic*.

     <img width="800" src="https://github.com/user-attachments/assets/6563f1ff-54eb-4381-9a76-dc9603317738" />

   - Choose *Next*.

5. On the *Add name and description* page, configure the following:
   - *Alarm name*: Enter *FailedLogins*
   - Choose *Next*.

6. On the *Preview and create* page, scroll to the bottom of the page, and choose *Create alarm*.

You have created a CloudWatch alarm. Next, you will test the CloudWatch alarm by attempting to log in to the console with incorrect credentials at least 3 times.

<br>

### Task 3.3 Test the CloudWatch alarm with 3 failed logins

1. Navigate to the IAM console, and in the navigation pane, choose *Users*.

2. Choose the link for the *admin* user you created during the last lab.

3. Choose the *Security credentials* tab, and then copy the *Console sign-in link*.

   <img width="800" src="https://github.com/user-attachments/assets/5cd8f074-9caa-4c86-8be0-5e9d8d53051c" />


4. Paste the copied link into a new browser tab to load the console sign-in page. You need to choose *Sign into new session* if multi-session support has been enabled.

   <img width="800" src="https://github.com/user-attachments/assets/e7cc219c-6cc8-444a-96d6-484401d103b1" />


5. Enter the IAM username *admin* and an **incorrect** password, and attempt to sign in. Repeat this at least 3 times:

   Note: Each time that you attempt to log in, you will see a message indicating that your authentication information is incorrect. This is expected!

   A notification message will be sent to your subscribed email address in a couple of minutes, with the content similar to the following:

   <img width="500" src="https://github.com/user-attachments/assets/317d956d-fbec-4901-983a-8a10b431e84e" />


Under the hood, the login failutres flow through your custom CloudTrail -> your CloudWatch Logs log group -> your metric filter -> the `ConsoleLoginFailureCounts` metric to trigger the alarm and send the notification.

<br>
 

### Task 3.4 Graph the metric (Optional)

1. Navigate to the CloudWatch console. In the navigation pane, expand *Metrics*, and then choose *All metrics*.

2. In the *Metrics* section, under *Custom namespaces*, choose *CloudTrailMetrics*.


3. Choose *Metrics with no dimensions*.

4. Choose *ConsoleLoginFailureCounts*.

   <img width="800" src="https://github.com/user-attachments/assets/404cd6b9-eb20-4121-86bf-09cf306211f3" />

   In the graph area in the upper portion of the page, a small blue dot should appear. The dot indicates that a login failure was detected.

<br>


### Task 3.5 Check the alarm status and details in the CloudWatch console (Optional)

1. In the navigation pane, expand *Alarms*, and then choose *All alarms*.

2. The *State* for the *FailedLogins* alarm should be *In alarm*.
   
   > Note: If the alarm doesn't show this state, wait a minute or two. To refresh the page, choose the  refresh icon.
 

3. To find out if the alarm was invoked recently, choose the link for the *FailedLogins* alarm name, and then choose the *History* tab.

   <img width="800" src="https://github.com/user-attachments/assets/91cda314-549d-4b45-90cf-60c524f44dfe" />


<br>

---

## After-class task: Clean up all lab resources

To conclude this lab and ensure you are not charged for resources you no longer need, perform the following steps to systematically remove all created components.

### Step 1: Delete the metric filter

1. In the CloudWatch console, select *Log groups* from the navigation pane.

2. Choose the *CloudTrailLogGroup* log group from the list to open its details.

3. Navigate to the *Metric filters* tab. Select the checkbox next to *ConsoleLoginErrors* metric filter.

4. Choose *Delete*, then confirm the deletion in the popup window.
 
   <img width="800" src="https://github.com/user-attachments/assets/13a96527-eb97-486e-8c00-2766882884cf" />


### Step 2: Delete the CloudWatch alarm

1. From the CloudWatch navigation pane, select *All alarms*.

2. Locate and select the *FailedLogins* alarm from the list.

3. Choose *Action \> Delete*, and confirm the deletion when prompted.
 
   <img width="800" src="https://github.com/user-attachments/assets/a979eb19-eacb-4ca8-a78b-12e39a85a708" />

### Step 3: Delete the CloudWatch Logs log group

1. Return to *Log groups* in the CloudWatch navigation pane.

2. Select the checkbox for *CloudTrailLogGroup*.

3. Choose *Action \> Delete log group(s)*, and confirm the deletion in the popup window.
 

   <img width="800" src="https://github.com/user-attachments/assets/be30e405-458e-4912-8532-0f2edcbda6df" />


### Step 4: Delete the CloudTrail Trail

1. Navigate to the CloudTrail console.

2. Select *Trails* from the left navigation pane.

3. In the list of trails, select *LabCloudTrail*, then choose *Delete*. Confirm the deletion in the popup window.

   <img width="800" src="https://github.com/user-attachments/assets/b23de50d-d7c5-45fc-9141-8ca06371a7ec" />
 
### Step 5: Delete the CloudFormation stack

1. Open the CloudFormation console.
2. From the left navigation pane, choose *Stacks*.
3. Select the *lab-environment* stack, then choose *Delete*. Confirm the deletion in the popup window to remove all remaining resources.
 
   <img width="800" src="https://github.com/user-attachments/assets/06939716-f5a1-4aa8-8c97-954568acfe9a" />
