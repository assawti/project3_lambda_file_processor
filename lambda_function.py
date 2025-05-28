
import json

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))
    return {"statusCode": 200, "body": "File processed."}
