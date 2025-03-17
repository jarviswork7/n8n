import boto3

lambda_client = boto3.client('lambda', region_name='us-east-1')


def lambda_handler(event, context):
    function_name = 'n8n-daniel'
    try:
        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.9',
            Role='<ROLE_ARN>',  # Provide the necessary IAM role ARN here
            Handler='lambda_function.lambda_handler',
            Code={
                'ZipFile': b'''
                def lambda_handler(event, context):
                    return "Hello from Lambda!"
                '''
            },
            Description='Lambda function created for Daniel',
            Timeout=30,
            MemorySize=128,
            Publish=True,
            PackageType='Zip',
            Architectures=['arm64'],
            Tags={
                'createdBy': 'Daniel',
                'Name': 'n8n'
            }
        )
        return {'statusCode': 200, 'body': f'Lambda function {function_name} created successfully.', 'response': response}
    except Exception as e:
        return {'statusCode': 500, 'body': str(e)}