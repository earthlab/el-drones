This is a workflow for syncing local storage with AWS S3 bucket storage. This is useful for UAV data so that you can save your UAV images in the cloud instead of storing them on your local dekstop, and can download them to access locally when needed. 

1. Open AWS-CLI   
    - Microsoft Menu > Amazon Web Services > Windows Powershell for AWS  
2. Configure AWS Earth Lab credentials (only done first time)  
    - Type `aws configure`  
        - Enter Access Key for your AWS account 
        - Enter Secret Access Key for your AWS account  
        - Enter Home Region: `us-west-2`  
        - Enter Output: `s3`
3. View Earth Lab s3 buckets
    - Type `aws s3 ls`
4. View objects in your desired bucket
    - Type `aws s3 ls <bucket_name>`
    - e.g., `aws s3 ls wogwogrep4` 
5. Sync data from S3 bucket to your local drive
    - Type `aws s3 sync <source_path> <target_path>` 
    - e.g., `aws s3 sync s3://wogwogrep4 D:\`
    - Data download!
