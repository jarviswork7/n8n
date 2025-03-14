import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    instance_id = 'i-0dd5489415c629706'
    
    # Describe the instance to get storage details
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get('Reservations', [])
    
    storage_details = []
    for reservation in reservations:
        for instance in reservation.get('Instances', []):
            block_mappings = instance.get('BlockDeviceMappings', [])
            for block in block_mappings:
                volume_id = block.get('Ebs', {}).get('VolumeId')
                if volume_id:
                    volume = ec2_client.describe_volumes(VolumeIds=[volume_id]).get('Volumes', [])[0]
                    storage_details.append({
                        'VolumeId': volume_id,
                        'Size': volume.get('Size'),
                        'Type': volume.get('VolumeType'),
                    })
    return storage_details