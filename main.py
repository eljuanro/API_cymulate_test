import logging
import requests

def main():
    res = requests.get('https://scotch.io')
    logging.info('Hola')
    logging.warning('Not working')
    print(res.headers)
    print("Hola")

main()