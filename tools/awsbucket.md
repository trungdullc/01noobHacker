# AWS S3 Bucket
```
Description: Try and dump an AWS bucket 
--no-sign-request avoids need for credentials
--recursive grabs everything possible

aws s3 cp --recursive --no-sign-request s3://<bucket_name> .
i. e. `aws s3 cp --recursive --no-sign-request s3://tamuctf .`
```

## Back to README.md
[BACK](../README.md)