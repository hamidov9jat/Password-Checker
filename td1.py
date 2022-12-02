import hashlib

import requests


def request_api_data(query_char):
    """
    Return data from the api when possible
    :param query_char:
    :return: result from the api or raises runtime error
    """
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching the data: {res.status_code}, check the api format!')

    return res
    # print(res.content)


def pwned_api_check(password):
    """
     Check if the password exists in api response
    :param password:
    :return:
    """
    # sha1password = hashlib.sha1(password.encode('utf-8'))
    print(password.encode('utf-8'))

# request_api_data('123')
