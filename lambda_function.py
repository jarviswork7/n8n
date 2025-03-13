import json
import boto3



def lambda_handler(event, context):
    bucket_name = "n8n-tesast-98698798"
    s3 = boto3.client('s3')
    
    try:
        # Delete all objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objects:
            for obj in objects['Contents']:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
            
        # Delete the bucket itself
        s3.delete_bucket(Bucket=bucket_name)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Successfully deleted bucket: {bucket_name}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error deleting bucket: {str(e)}')
        }
