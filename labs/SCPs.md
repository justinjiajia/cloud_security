
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
        // Key Pairs (The lab uses an existing key pair "vockey")
        "ec2:DescribeKeyPairs",
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
