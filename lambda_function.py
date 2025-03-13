import json
import boto3


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'n8n-test-98698798'
    
    try:
        # Delete all objects in the bucket first
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])

        # Now delete the bucket
        s3.delete_bucket(Bucket=bucket_name)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Bucket deleted successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }