subscribers = []


def subscribe(subscriber):

    subscribers.append(subscriber)


def publish_notification(order):

    print("Publishing message to SNS topic")

    for subscriber in subscribers:

        subscriber(order)