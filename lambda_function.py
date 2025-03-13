import boto3  

def lambda_handler(event, context):  
    ec2 = boto3.resource('ec2')  
    # Create a new EC2 instance  
    instance = ec2.create_instances(  
        ImageId='ami-08b5b3a93ed654d19',  
        MinCount=1,  
        MaxCount=1,  
        InstanceType='t3.micro'  
    )  
    print(f'New instance created: {instance[0].id}')  
    return {  
        'statusCode': 200,  
        'body': f'Created instance with ID: {instance[0].id}'  
    }