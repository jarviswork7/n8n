import boto3

client = boto3.client('lambda', region_name='us-east-1')

def lambda_handler(event, context):
    try:
        response = client.create_function(
            FunctionName='n8n-ExampleFunction',
            Runtime='python3.9',
            Role='<ROLE_ARN>',
            Handler='lambda_function.lambda_handler',
            Code={
                'ZipFile': b'def lambda_handler(event, context): return "Hello from Lambda!"'
            },
            Timeout=30,
            MemorySize=128,
            Publish=True,
            Architecture='arm64',
            Tags={
                'createdBy': 'Daniel',
                'Name': 'n8n'
            }
        )
        return response
    except Exception as e:
        return str(e)