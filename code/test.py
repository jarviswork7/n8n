import boto3\n\ndef lambda_handler(event, context):\n    s3_client = boto3.client('s3')\n    response = s3_client.list_buckets()\n    bucket_names = [bucket['Name'] for bucket in response['Buckets']]\n    return {\n        'statusCode': 200,\n        'body': bucket_names\n    }\n