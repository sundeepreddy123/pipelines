from message_queue import receive_message
from notification import publish_notification


def lambda_handler(event, context):

    order = receive_message()

    if order is None:
        print("No messages available")

        return {
            "statusCode": 200,
            "body": "No messages"
        }

    print(f"Processing order: {order['order_id']}")

    order["status"] = "COMPLETED"

    publish_notification(order)

    print("Order processing completed")

    return {
        "statusCode": 200,
        "body": "Order processed successfully"
    }