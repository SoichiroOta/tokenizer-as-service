import os
import json

import responder

from download import download
from tokenization import Tokenizer


env = os.environ
DEBUG = env['DEBUG'] in ['1', 'True', 'true']
LIBRARY = env.get('LIBRARY')
LANG = env.get('LANG')

api = responder.API(debug=DEBUG)
download(library=LIBRARY, lang=LANG)    
tokenizer = Tokenizer(library=LIBRARY,lang=LANG)


@api.route("/")
async def tokenize(req, resp):
    body = await req.text
    texts = json.loads(body)
    docs = [tokenizer.tokenize(text) for text in texts]
    resp.media = dict(data=docs)


if __name__ == "__main__":
    api.run()