import os

from polyglot.downloader import downloader
import stanza


env = os.environ
LIBRARY = env.get('LIBRARY')
LANG = env.get('LANG')


def download(library=None, lang=None):
    if lang is None:
        language = 'en'
    else:
        language = lang

    if library == 'stanza':
        stanza.download(language)
        return

    downloader.download("embeddings2." + language)
    supported_tasks = downloader.supported_tasks(lang=language)  
    if "pos2" in supported_tasks:
        downloader.download("pos2." + language)
    return


if __name__ == '__main__':
    download(library=LIBRARY, lang=LANG)