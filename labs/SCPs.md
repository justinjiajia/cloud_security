
## Lab 2

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        // VPC & Networking (Create VPC, subnets, route tables, Internet Gateway, etc.)
        "ec2:CreateVpc",
        "ec2:CreateSubnet",
        "ec2:CreateRouteTable",
        "ec2:CreateRoute",
        "ec2:CreateInternetGateway",
        "ec2:AttachInternetGateway",
        "ec2:AssociateRouteTable",
        "ec2:ModifyVpcAttribute",
        // NAT Gateway (Create, describe, delete)
        "ec2:CreateNatGateway",
        "ec2:DescribeNatGateways",
        "ec2:DeleteNatGateway",
        "ec2:AllocateAddress",
        "ec2:AssociateAddress",
        // Security Groups
        "ec2:CreateSecurityGroup",
        "ec2:AuthorizeSecurityGroupIngress",
        "ec2:AuthorizeSecurityGroupEgress",
        "ec2:DescribeSecurityGroups",
        // EC2 Instance (Launch, describe, terminate)
        "ec2:RunInstances",
        "ec2:DescribeInstances",
        "ec2:TerminateInstances",
        // Key Pairs
        "ec2:DescribeKeyPairs",
        // Allow for EC2 Instance Connect"
        "ec2-instance-connect:SendSSHPublicKey",
        // Describe actions needed for the console to function properly
        "ec2:DescribeAvailabilityZones",
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets",
        "ec2:DescribeRouteTables",
        "ec2:DescribeInternetGateways",
        "ec2:DescribeImages",
        "ec2:DescribeInstanceTypes",
        "ec2:DescribeTags"
      ],
      "Resource": "*"
    }
  ]
}
```


A SCP that restricts member accounts to only the us-east-1 region;
This policy uses NotAction to exempt crucial global services (like IAM and Route 53)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyAllOutsideUSEast1",
      "Effect": "Deny",
      "NotAction": [
        "a4b:*",
        "acm:*",
        "aws-marketplace:*",
        "aws-portal:*",
        "budgets:*",
        "cloudfront:*",
        "config:*",
        "ec2:DescribeRegions",
        "globalaccelerator:*",
        "health:*",
        "iam:*",
        "organizations:*",
        "pricing:*",
        "route53:*",
        "route53domains:*",
        "s3:GetAccountPublic*",
        "s3:ListAllMyBuckets",
        "s3:ListMultiRegionAccessPoints",
        "s3:PutAccountPublic*",
        "shield:*",
        "sts:*",
        "support:*",
        "trustedadvisor:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": "us-east-1"
        }
      }
    }
  ]
}
```
