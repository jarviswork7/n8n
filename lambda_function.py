import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    # Retrieve the list of S3 buckets
    response = s3.list_buckets()
    buckets = response['Buckets']
    
    # List to hold bucket details
    bucket_details = []
    
    # Get details for each bucket
    for bucket in buckets:
        bucket_name = bucket['Name']
        creation_date = bucket['CreationDate'].strftime("%Y-%m-%d %H:%M:%S")
        
        bucket_details.append({
            "Bucket Name": bucket_name,
            "Creation Date": creation_date
        })
    
    return {
        'statusCode': 200,
        'body': json.dumps(bucket_details)
    }