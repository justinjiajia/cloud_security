


## Simulated business scenario
 
A startup company requires rapid deployment of its IT resources for application development. 
The company's compliance officer has a big challenge, tracking and managing any changes to AWS resource configurations.




> Paulo Santos
Hello! Thanks for stopping by. I have a compliance problem that I hope you can help with.
You
Hi! I will if I can. What is the problem?
Paulo Santos
I am the compliance officer for a new startup company. Because we’re a startup, we need to be agile and move fast. But changes can be made to the IT environment that are not tracked and are often in violation of our agreed standards.
Paulo Santos
Is there anything we can do to help automate the compliance of IT resources?
You
Yes there is! I would start by using infrastructure as code with AWS CloudFormation. That change alone will help standardize your creation and change process.
Paulo Santos
Infrastructure as code? I know what IT infrastructure is, but I don’t understand how it can be accomplished with code?
You
With infrastructure as code, you create a template that describes all the AWS resources that you want to include in your infrastructure, such as Amazon EC2 instances and AWS Lambda functions.
You
CloudFormation can then provision and configure those resources for you. You can treat your new template like any other code by saving it in a repository and performing a code review on it before deployment.
Paulo Santos
Awesome! But how can that help with compliance?
You
You can ensure that standards are followed during the code review process. But even as you manage your resources through CloudFormation, users can change those resources outside of CloudFormation.
You
What’s great is that CloudFormation has drift detection. That’s the ability to detect if resources no longer match the template used to deploy them.
Paulo Santos
That is fantastic. So, by using CloudFormation and drift detection, I can tell when something has been changed in our environment. Now if we could just automatically reverse the changes.
You
You can! In AWS Lambda, you can create a function that monitors for drift and remediates any drift that is detected.
Paulo Santos
That sounds really cool, and it would make my work much easier.


### Solution Request
Use an AWS Lambda function, invoked by an Amazon EventBridge schedule, to detect and remediate changes to an environment that was built by using AWS CloudFormation.


####  Step 1
In this solution, a template stored in an Amazon Simple Storage Service (Amazon S3)  bucket is used by AWS CloudFormation to deploy and manage a stack. 
A stack is a collection of AWS resources that you can manage as a single unit. Any changes manually made to that stack are detected and remediated by an AWS Lambda function.


<img width="642" height="470" alt="image" src="https://github.com/user-attachments/assets/7cb4c134-44ba-4486-88e2-bd413eeac0a3" />

### Step 2

<img width="647" height="477" alt="image" src="https://github.com/user-attachments/assets/86ad9508-50a2-4523-aed4-c68f56099467" />

 
A template is used to describe resources within a stack. That template can be uploaded from local storage or obtained from an S3 bucket.
