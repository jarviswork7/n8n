import boto3

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return {
        'statusCode': 200,
        'body': buckets
    }