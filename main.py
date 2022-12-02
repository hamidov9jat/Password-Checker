import hashlib
import sys

import requests


def request_api_data(query_char: str):
    """
    Return data from the api when possible
    :param query_char:
    :return: result from the api or raises runtime error
    """
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching the data set: {res.status_code}, check the api format!')

    return res


def get_password_leaks_count(hashes: str, hash_suffix_to_check: str):
    hashes_info = (line.split(':') for line in hashes.splitlines())

    for suffix, count in hashes_info:
        if suffix == hash_suffix_to_check:
            return int(count)
    return 0


def pwned_api_check(password: str) -> int:
    """
     Check if the password exists in api response
    :param password:
    :return: prevalence count for the given password
    """
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chars, suffix = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_chars)
    return get_password_leaks_count(response.text, suffix)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count > 0:
            print(f'{password} was found {count} times... you should probably change your password!')
        else:
            print(f'You have strong password!{password} was NOT previously exposed in data breaches.')

    # Simple message to assert that everything went fine
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
