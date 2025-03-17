import boto3
import json

# Define the Lambda handler
def lambda_handler(event, context):
    client = boto3.client('lambda', region_name='us-east-1')

    # Attempt to create a new Lambda function
    try:
        response = client.create_function(
            FunctionName='n8n-daniel',
            Runtime='python3.9',
            Role='arn:aws:iam::145023133524:role/service-role/n8n-operations-manager-role-77x7ibol',
            Handler='lambda_function.lambda_handler',
            Code={
                'ZipFile': b"""def lambda_handler(event, context):\n    return 'Hello from Lambda!'""",
            },
            Timeout=30,
            MemorySize=120,
            Architectures=['arm64'],
            Tags={
                'createdBy': 'Daniel',
                'Name': 'n8n'
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Lambda function created successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error creating Lambda function: ' + str(e))
        }