import json
import threading
import time

from order_lambda import lambda_handler as order_lambda
from queue_consumer import process_messages

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


# Register SNS subscribers
subscribe(send_email)
subscribe(send_sms)


# Start SQS consumer in background
consumer_thread = threading.Thread(
    target=process_messages,
    daemon=True
)

consumer_thread.start()


# Give consumer time to start
time.sleep(1)


# Create order
event = {

    "body": json.dumps({

        "customer_name": "Sundeep",

        "product": "Laptop",

        "quantity": 1

    })

}


print("\n--- Sending Order ---")


response = order_lambda(event, None)


print("\nOrder Lambda Response:")

print(response)


# Keep application running
while True:

    time.sleep(5)