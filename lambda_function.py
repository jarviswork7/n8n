def lambda_handler(event, context):
    """
    A simple AWS Lambda handler function.
    This function is the entry point for AWS Lambda to execute your code.
    """
    return {
        'statusCode': 200,
        'body': 'Lambda function executed successfully with the proper setup.'
    }