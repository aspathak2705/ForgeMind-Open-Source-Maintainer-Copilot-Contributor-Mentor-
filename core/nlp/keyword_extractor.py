import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class KeywordExtractor:

    def __init__(self):

        self.stop_words = set(
            stopwords.words("english")
        )

        self.lemmatizer = (
            WordNetLemmatizer()
        )

    def extract(
        self,
        text: str,
    ):

        tokens = word_tokenize(
            text.lower()
        )

        keywords = []

        for token in tokens:

            if not token.isalnum():
                continue

            if token in self.stop_words:
                continue

            keyword = (
                self.lemmatizer
                .lemmatize(token)
            )

            keywords.append(
                keyword
            )

        return list(
            set(keywords)
        )