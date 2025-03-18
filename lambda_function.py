import boto3
import openpyxl

# Initialize the EC2 client
client = boto3.client('ec2', region_name='us-east-1')

# Lambda handler
def lambda_handler(event, context):
    # Create EC2 instance
    instance = client.run_instances(
        ImageId='ami-08b5b3a93ed654d19',
        InstanceType='t3.micro',
        MaxCount=1,
        MinCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'createdBy', 'Value': 'Daniel'},
                    {'Key': 'Name', 'Value': 'n8n'}
                ]
            }
        ]
    )

    instance_id = instance['Instances'][0]['InstanceId']

    # Load the excel
    path = '/tmp/AWS-Resources.xlsx'
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active
    
    # Add instance ID to Excel
    sheet.append([instance_id])

    workbook.save(path)
    
    return {'InstanceId': instance_id}
