import json
import uuid

from message_queue import send_message


def lambda_handler(event, context):

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

    send_message(order)

    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "Order created",
            "order": order
        })
    }