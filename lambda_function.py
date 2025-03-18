import boto3
import openpyxl
from openpyxl import Workbook

# Function to create an EC2 instance
def create_ec2_instance():
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    instance = ec2.create_instances(
        ImageId='ami-08b5b3a93ed654d19',
        InstanceType='t3.micro',
        MinCount=1,
        MaxCount=1
    )
    return instance[0].id

# Function to add the instance ID to Excel sheet
def add_instance_id_to_excel(instance_id):
    # Load the workbook and select the active worksheet
    workbook = openpyxl.load_workbook('AWS-Resources.xlsx')
    sheet = workbook.active 
    # Append the instance ID to the sheet
    sheet.append(['EC2 Instance ID', instance_id])
    # Save the workbook
    workbook.save('AWS-Resources.xlsx')

# Lambda handler function
def lambda_handler(event, context):
    instance_id = create_ec2_instance()
    add_instance_id_to_excel(instance_id)
    return {
        'statusCode': 200,
        'body': f'EC2 Instance created with ID: {instance_id} and added to Excel'
    }