import boto3
import uuid

def lambda_handler(event, context):
    # Create an S3 client
    s3_client = boto3.client('s3', region_name='us-east-1')
    
    # Generate a random bucket name
    bucket_name = f'random-bucket-{uuid.uuid4()}'
    
    try:
        # Create the S3 bucket
        s3_client.create_bucket(Bucket=bucket_name)
        
        return {
            'statusCode': 200,
            'body': f'S3 bucket {bucket_name} created successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error creating bucket: {str(e)}'
        }
}