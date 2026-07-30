import queue


order_queue = queue.Queue()


def send_message(message):

    order_queue.put(message)

    print("Message sent to SQS queue")


def receive_message():

    if order_queue.empty():

        return None

    return order_queue.get()