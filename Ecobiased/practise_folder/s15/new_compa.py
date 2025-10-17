import requests
import json
from datetime import datetime


# Process user orders
def process(input_data):
    if not input_data:
        return "data should not be empty"
    results = []
    disc = 0
    for row in input_data:
        if 'type' in input_data and row['type'] == 'premium':
            disc = 0.2
        elif 'type' in input_data and row['type'] == 'regular':
            disc = 0.1

        total = 0


        fetch_item(row, disc, total)
        results.append({'order_id': order_id, 'total': total, 'user': d['user_id']})

    return results


def fetch_item(row, disc, total=0):
    """

    :param item:
    :return:
    """
    if row and 'items' in row:
        for item in row['items']:
            total = total + item['price'] * item['qty']

        total = total - (total * disc)

        if total > 100:
            total = total - 10

        # add tax
        total = total * 1.08


        insert_records(row, total)

    body_message = f'Your order total is ${total}'
    send_email("https://api.email.com/send", row['email'], 'Order Confirmed', body_message)

def insert_records(row, total):
    """
    save to db
    :param row:
    :param total:
    :return:
    """

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO orders (user_id, total, date) VALUES ({row['user_id']}, {total}, '{datetime.now()}')")
        conn.commit()
        order_id = cursor.lastrowid

        for item in row['items']:
            cursor.execute(
                f"INSERT INTO order_items (order_id, item_id, qty, price) VALUES ({order_id}, {item['id']}, {item['qty']}, {item['price']})")

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
        return None


def send_email(url, to, subject, body_message):
    """
    responsible to send email
    :param url:
    :param to:
    :param subject:
    :param body_message:
    :return:
    """
    requests.post(url,
                  data={'to': to,
                        'subject': subject,
                        'body': body_message})


def check_inventory(row):
    """
    responsible to check inventory
    :return:
    """
    if 'items' in row:
        for item in row['items']:
            r = requests.get(f"https://api.inventory.com/check/{item['id']}")
            inv = json.loads(r.text)

            if inv['stock'] < item['qty']:
                print(f"Not enough stock for {item['id']}")
                return None



def get_db_connection():
    # dummy function
    pass