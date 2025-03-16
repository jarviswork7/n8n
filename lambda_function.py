import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    buckets = response['Buckets']
    bucket_details = []

    for bucket in buckets:
        # Get creation date in a readable format
        creation_date = bucket['CreationDate'].strftime("%Y-%m-%d %H:%M:%S")
        bucket_details.append({
            'Name': bucket['Name'],
            'CreationDate': creation_date
        })

    return {
        'statusCode': 200,
        'body': json.dumps(bucket_details)
    }