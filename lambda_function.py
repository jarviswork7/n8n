import boto3

def lambda_handler(event, context):
    client = boto3.client('lambda')

    function_name = 'n8n-myLambdaFunction'

    response = client.create_function(
        FunctionName=function_name,
        Runtime='python3.9',
        Role='arn:aws:iam::123456789012:role/service-role',  # Modify with appropriate IAM role
        Handler='lambda_function.lambda_handler',
        Timeout=30,
        MemorySize=128,
        Architectures=['arm64'],
        PackageType='Zip',
        Tags={
            "createdBy": "Daniel",
            "Name": "n8n"
        }
    )

    return response
