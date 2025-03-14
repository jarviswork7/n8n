import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'lambda-code-n8n'
    
    try:
        # Delete all objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name).get('Contents', [])
        for obj in objects:
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
        
        # Delete the bucket
        s3.delete_bucket(Bucket=bucket_name)
        return {'status': 'Bucket deleted successfully'}
    except Exception as e:
        return {'error': str(e)}