from VARIABLES_ import *
import requests
import json

def update_database(word_index, value):
    global counters, total_counteded
    counter = counters[word_index]

    _status_code_a = 0
    while _status_code_a != 200:
        _status_code_a = requests.get(f"{dreamlo_url}/delete/{counter}").status_code

    _status_code_b = 0
    while _status_code_b != 200:
        _status_code_b = requests.get(f"{dreamlo_url}/add/{counter}/{value}").status_code


def get_total_word_counted(word_index):
    global counters
    counter = counters[word_index]

    _gotValue = False
    while not _gotValue:
        _res = requests.get(f"{dreamlo_url}/json")
        if _res.status_code == 200:
            try:
                _total = json.loads(_res.text)
                _gotValue = True
            except:
                print("failed to get value")


    for counteded in _total['dreamlo']['leaderboard']['entry']:
        if counteded['name'] == counter:
            return int(counteded['score'])
    return 0


def check_counted_words_present(message):
    message_list = str(message).split(' ')
    if len(message_list) == 1:
        for i, _list in enumerate(all_words_list):
            if message in _list:
                return i
    else:
        for message_item in message_list:
            for i, _list in enumerate(all_words_list):
                if message_item in _list:
                    return i

    return None


def check_if_asking_price_xD(message):
    for i in bhendi_asking_pharases:
        if message == i:
            return True
    return False
