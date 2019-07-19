import json, os
from requests_oauthlib import OAuth1Session
from GenerateText import GenerateText


def markovbot():
    keyfile = open('keys.json')
    keys = json.load(keyfile)
    oath = create_oath_session(keys)

    generator = GenerateText(1)

    tweetmarkovstring(oath, generator)


def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
        oath_key_dict[os.environ("consumer_key")],
        oath_key_dict[os.environ("consumer_secret")],
        oath_key_dict[os.environ("access_token")],
        oath_key_dict[os.environ("access_token_secret")]
    )
    return oath


def tweetmarkovstring(oath, generator):
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    markovstring = generator.generate()
    params = {'status': markovstring}
    req = oath.post(url, params)

    if req.status_code == 200:
        print('tweet Success!')
    else:
        print('tweet Failed...')


if __name__ == '__main__':
    markovbot()
