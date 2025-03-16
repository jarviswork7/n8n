def lambda_handler(event, context):
    # Main entry point for AWS Lambda
    return {
        'statusCode': 200,
        'body': 'Lambda function executed successfully.'
    }