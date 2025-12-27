## AWS SimuLearn: Application Logs
 

https://skillbuilder.aws/learn/ZRJDNF9BWD/aws-simulearn-application-logs



## Simulated business scenario

A web gaming company had a security breach incident and lost significant time trying to find server access logs. 
The new compliance officer wants to find a way to analyze server logs efficiently.



> Wang Xiulan
Hello! Thanks for stopping by. I am the new compliance officer at a web gaming company, and we recently had a security breach on our application server. I was hoping you could help me find a more efficient way to access our server logs.
You
Hello! I am happy to help. Can you tell me more?
Wang Xiulan
During the incident, we lost significant time trying to find the access logs on the application server. We want to find a better way to quickly analyze server logs. Do you know of such a solution?
You
Absolutely! You can install the Amazon Kinesis agent on the application server and configure it to send access log data to an Amazon Data Firehose stream, which can be configured to send the access log data to an Amazon S3 bucket.
Wang Xiulan
I see. What is the benefit of having our log data in an S3 bucket?
You
With the logs in Amazon S3, you can use AWS Glue, a serverless data integration service, to discover properties of the data and prepare it for analytics.
Wang Xiulan
Interesting. How does AWS Glue work?
You
AWS Glue provides all the capabilities needed for data integration, so you can start analyzing your data and putting it to use in minutes instead of months.
You
You can quickly find and access data using the AWS Glue Data Catalog, which is a central repository to store structural and operational metadata for all your data assets.
You
You can configure an AWS Glue crawler to automatically scan Amazon S3, identify data formats and suggest schemas and transformations, and then populate the Data Catalog with this metadata.
Wang Xiulan
That sounds great. How will I be able to access the Data Catalog?
You
That’s where Amazon Athena comes in. Athena is an interactive query service that you can use to analyze data in S3 using standard SQL. Athena works with the Data Catalog to read the schema information and apply it to the log data in S3.
You
You can use Athena to help analyze the access log data stored in S3 by running interactive analytics using SQL queries, without the need to aggregate or load the data into Athena.
Wang Xiulan
Fantastic! This solution will definitely help us proactively investigate security incidents in the future.
