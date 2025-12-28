

## How to set up your AWS CLI credential

The credentials and config file are updated when you run the command `aws configure`. 
The config file is located at *~/.aws/config* on Linux or macOS, or at *C:\Users\USERNAME\.aws\config* on Windows.


 https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

```shell
rm ~/.aws/config
aws configure
```


## How to create AWS member accounts in batches


https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html

After you sign in to the organization's management account, you can create member accounts that are part of your organization.


```shell
aws organizations create-account --email "justinjiajia@gmail.com" --account-name "ISOM5140_identity"
```

Organizations automatically creates the IAM role `OrganizationAccountAccessRole` for the member account


Member accounts in an organization can only be created in the root of an organization. 

To get the ID of the root:

```shell
aws organizations list-roots | grep "Id"
```

After you create a member account root of an organization, you can move it between OUs.

https://docs.aws.amazon.com/organizations/latest/userguide/orgs_view_ou.html

To get the IDs of existing organizational units:

```shell
aws organizations list-children --parent-id r-mdvy --child-type ORGANIZATIONAL_UNIT
{
    "Children": [
        {
            "Id": "ou-mdvy-d9xaqunq",
            "Type": "ORGANIZATIONAL_UNIT"
        }
    ]
}
```
https://docs.aws.amazon.com/organizations/latest/userguide/move_account_to_ou.html

The following example moves an AWS account from the root to an OU. Note that you must specify the IDs of both the source and destination containers.

```shell
aws organizations move-account --account-id 066712929430 --source-parent-id r-mdvy --destination-parent-id ou-mdvy-d9xaqunq
```


List all member accounts in an organizational unit:

```shell
aws organizations list-accounts-for-parent --parent-id ou-mdvy-d9xaqunq
```
`:q` to quit



## Close a member account

https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-closing.html

 https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_close.html



## Leave an organization

To leave an organization, you must have the following permissions:

organizations:DescribeOrganization – required only when using the Organizations console.

organizations:LeaveOrganization – Note that the organization administrator can apply a policy to your account that removes this permission, preventing you from removing your account from the organization.

If you sign in as an IAM user and the account is missing payment information, 
the user must have either aws-portal:ModifyBilling and aws-portal:ModifyPaymentMethods permissions (if the account has not yet migrated to fine-grained permissions) 
OR payments:CreatePaymentInstrument and payments:UpdatePaymentPreferences permissions (if the account has migrated to fine-grained permissions). 
Also, the member account must have IAM user access to billing enabled.


Service control policies (SCPs) for member accounts to leave an organization

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:List*",
        "s3:GetObject*",
        "s3:GetBucket*",
        "s3:DeleteBucket",
        "s3:DeleteObject*",
        "s3:*BucketPolicy",
        "sns:ListTopics",
        "sns:Unsubscribe",
        "sns:DeleteTopic",
        "sns:SetTopicAttributes",
        "sns:GetTopicAttributes",
        "cloudtrail:DeleteTrail",
        "cloudtrail:StopLogging",
        "cloudtrail:ListTrails",
        "cloudtrail:DescribeTrails",
        "cloudwatch:DeleteAlarms",
        "ec2:TerminateInstances",
        "ec2:Describe*",
        "ec2:DeleteVpc",
        "ec2:DeleteSubnet",
        "ec2:DeleteSecurityGroup",
        "ec2:DetachInternetGateway",
        "ec2:DeleteInternetGateway",
        "ec2:DisassociateRouteTable",
        "ec2:DeleteRouteTable",
        "ec2:DeleteRoute",
        "iam:DeleteRole",
        "iam:DetachRolePolicy",
        "iam:DeleteRolePolicy",
        "iam:RemoveRoleFromInstanceProfile",
        "iam:ListRoles",
        "lambda:DeleteFunction",
        "lambda:RemovePermission",
        "lambda:ListFunctions",
        "config:StopConfigurationRecorder",
        "config:ListConfigurationRecorders",
        "config:Describe*",
        "config:DeleteConfigRule",
        "organizations:DescribeOrganization",
        "organizations:LeaveOrganization",
        "cloudformation:ListStacks",
        "cloudformation:DescribeStacks",
        "cloudformation:DeleteStack",
        "cloudformation:DescribeStackEvents",
        "cloudformation:ListStackResources",
        "logs:DescribeLogGroups",
        "logs:DeleteLogGroup",
        "aws-portal:ModifyBilling",
        "aws-portal:ModifyPaymentMethods",
        "payments:CreatePaymentInstrument",
        "payments:UpdatePaymentPreferences"
      ],
      "Resource": "*"
    }
  ]
}
```


##  Give an admin user billing access

1. Activate IAM Access (Root User): Sign in as the root user, go to the Account page, find "IAM user and role access to Billing information," and select Edit > Activate IAM access, then Update.

2. Assign Permissions (IAM Admin): Create an IAM policy with AWSBillingReadOnlyAccess for viewing or Billing for full control (payments, methods).
Attach this policy to the specific user or a group they belong to. 
