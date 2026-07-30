import time

from message_queue import receive_message
from order_worker import lambda_handler as worker_lambda


def process_messages():

    print("SQS consumer started...")

    while True:

        message = receive_message()

        if message is None:

            print("No messages in queue. Waiting...")

            time.sleep(2)

            continue

        print(
            f"Message received from queue: "
            f"{message['order_id']}"
        )

        response = worker_lambda(message, None)

        print(response)