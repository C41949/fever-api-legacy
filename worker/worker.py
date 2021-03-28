import time

import requests


def run():
    while True:
        requests.post('http://fever-api-nginx/temperature')
        time.sleep(1)


if __name__ == '__main__':
    run()
