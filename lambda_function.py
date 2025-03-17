import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'n8n-daniel'
    try:
        # Delete all objects in the bucket before deleting the bucket
        response = s3.list_object_versions(Bucket=bucket_name)
        versions = response.get('Versions', []) + response.get('DeleteMarkers', [])
        for version in versions:
            s3.delete_object(Bucket=bucket_name, Key=version['Key'], VersionId=version['VersionId'])
        
        # Delete the bucket
        s3.delete_bucket(Bucket=bucket_name)
        return {'status': 'Bucket deleted successfully'}
    except Exception as e:
        return {'error': str(e)}