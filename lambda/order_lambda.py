import json
import os
import uuid
import boto3


sqs = boto3.client("sqs")

QUEUE_URL = os.environ["QUEUE_URL"]


def lambda_handler(event, context):

    print("Received event:")
    print(json.dumps(event))

    body = json.loads(event["body"])

    if "customer_name" not in body:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "customer_name is required"
            })
        }

    if "product" not in body:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "product is required"
            })
        }

    order = {
        "order_id": str(uuid.uuid4()),
        "customer_name": body["customer_name"],
        "product": body["product"],
        "quantity": body.get("quantity", 1),
        "status": "CREATED"
    }

    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(order)
    )

    print(f"Order sent to SQS: {order['order_id']}")

    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "Order created",
            "order": order
        })
    }
