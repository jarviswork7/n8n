import boto3

def lambda_handler(event, context):
    client = boto3.client('lambda')
    response = client.create_function(
        FunctionName='MyLambdaFunction',
        Runtime='python3.9',
        Role='<ROLE_ARN>',  # Assuming role is provided correctly
        Handler='lambda_function.lambda_handler',
        Code={
            'ZipFile': b"""
            def lambda_handler(event, context):
                return "Hello from Lambda!"
            """
        },
        Description='A simple Lambda function',
        Timeout=30,
        MemorySize=128,
        Tags={
            'createdBy': 'Daniel',
            'Name': 'n8n'
        },
        Architectures=['arm64']
    )
    return response