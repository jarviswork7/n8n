import boto3

def lambda_handler(event, context):
    # Create a session using the default profile
    session = boto3.Session(region_name='us-east-1')
    
    # Create an RDS client
    rds_client = session.client('rds')
    
    # Call the describe_db_instances API
    response = rds_client.describe_db_instances()
    
    # Extract the RDS instances details
    db_instances = response['DBInstances']
    
    # Print the DB instances information
    for db_instance in db_instances:
        print(f"DBInstanceIdentifier: {db_instance['DBInstanceIdentifier']}")
        print(f"DBInstanceClass: {db_instance['DBInstanceClass']}")
        print(f"Engine: {db_instance['Engine']}")
        print(f"DBInstanceStatus: {db_instance['DBInstanceStatus']}")
        print("---------------------------------------------")
    
    return db_instances
