from polyglot.text import Text
from polyglot.downloader import downloader
import stanza


class Tokenizer:
    def __init__(self, library=None, lang=None):
        if library == 'stanza':
            self.tokenizer = StanzaTokenizer(lang)
        else:
            self.tokenizer = PolyglotTokenizer(lang)

    def tokenize(self, blob):
        return self.tokenizer.tokenize(blob)


class PolyglotTokenizer:
    def __init__(self, lang=None):
        supported_tasks = downloader.supported_tasks(lang=lang)
        if "pos2" in supported_tasks:
            self.tokenize = self._tokenize_with_pos
        else:
            self.tokenize = self._tokenize_without_pos

    def _tokenize_with_pos(self, blob):
        text = Text(blob)
        return [
            {
                'raw': sentence.raw,
                'start': sentence.start,
                'end': sentence.end,
                'tokens': sentence.tokens,
                'words': sentence.words,
                'pos_tags': sentence.pos_tags,
                'language': sentence.language.code
            } for sentence in text.sentences
        ]

    def _tokenize_without_pos(self, blob):
        text = Text(blob)
        return [
            {
                'raw': sentence.raw,
                'start': sentence.start,
                'end': sentence.end,
                'tokens': sentence.tokens,
                'words': sentence.words,
                'language': sentence.language.code
            } for sentence in text.sentences
        ]


class StanzaTokenizer:
    def __init__(self, lang=None):
        if lang:
            self.nlp = stanza.Pipeline(
                lang=lang
            )
        else:
           self.nlp = stanza.Pipeline() 

    def tokenize(self, blob):
        doc = self.nlp(blob)
        return doc.to_dict()
