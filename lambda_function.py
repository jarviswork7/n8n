import json\nimport boto3\n\ndef lambda_handler(event, context):\n    ec2 = boto3.client('ec2')\n    instance_id = event.get('instance_id')\n    response = ec2.describe_instances(\n        InstanceIds=[instance_id]\n    )\n    instance_details = response['Reservations'][0]['Instances'][0]\n    return {\n        'statusCode': 200,\n        'body': json.dumps({\n            'InstanceDetails': instance_details\n        })\n    }\n