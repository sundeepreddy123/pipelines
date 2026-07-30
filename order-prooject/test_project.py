print("TEST SCRIPT STARTED")
import json

from order_lambda import lambda_handler as order_lambda
from order_worker import lambda_handler as worker_lambda
from notification import subscribe


def send_email(order):

    print(
        f"EMAIL: Order {order['order_id']} "
        f"completed for {order['customer_name']}"
    )


def send_sms(order):

    print(
        f"SMS: Your order {order['order_id']} "
        f"is completed"
    )


subscribe(send_email)
subscribe(send_sms)


event = {
    "body": json.dumps({
        "customer_name": "Sundeep",
        "product": "Laptop",
        "quantity": 1
    })
}


print("\n--- STEP 1: Create Order ---")

response = order_lambda(event, None)

print(response)


print("\n--- STEP 2: Process SQS Message ---")

worker_response = worker_lambda({}, None)

print(worker_response)