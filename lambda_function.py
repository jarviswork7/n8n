import boto3

# Function to invoke the Lambda function

def lambda_invoke(event, context):
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName='YourLambdaFunctionName',  # Replace with your Lambda function name
        InvocationType='RequestResponse'
    )
    
    # Read the response
    response_payload = response['Payload'].read().decode('utf-8')
    return response_payload
