from key import token
import requests
from time import sleep

common_url = f'https://api.telegram.org/bot{token}/'


def get_updates():
    url = common_url + 'getupdates'
    response = requests.get(url=url)
    response = response.json()
    return response


def get_message(data):
    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    update_id = data['result'][-1]['update_id']
    message = {
        'chat_id': chat_id,
        'text': message_text,
        'update_id': update_id
    }
    return message


def send_message(chat_id, text):
    url = common_url + f'sendmessage?chat_id={chat_id}&text={text}'
    response = requests.get(url=url)
    response = response.json()
    return response


def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    response = requests.get(url).json()
    price = response['ticker']['last']
    return str(round(price, 2)) + ' USD'


def main():
    last_update_id = 0

    while True:
        updates = get_updates()
        answer = get_message(updates)
        if last_update_id != answer['update_id']:
            last_update_id = answer['update_id']
            if answer['text'] == '/btc':
                send_message(answer['chat_id'], get_btc())
        sleep(2)


if __name__ == '__main__':
    main()
