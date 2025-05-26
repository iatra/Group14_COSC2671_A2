"""
COSC2671 Social Media and Network Analytics
@author Jeffrey Chan, RMIT University, 2023

"""

import re
from nltk.stem import WordNetLemmatizer 
import string

class RedditProcessing:
    """
    This class is used to pre-process Reddit posts.  This centralises the processing to one location.  Feel free to add or edit.
    """

    def __init__(self, tokeniser, lStopwords, lemmatizer=None, filter_out_terms=None):
        """
        Initialise the tokeniser and set of stopwords to use.

        @param tokeniser:
        @param lStopwords:
        """

        self.tokeniser = tokeniser
        self.lStopwords = lStopwords
        self.lemmatizer = lemmatizer
        self.filter_out_terms = filter_out_terms or set()



    def process(self, text):
        """
        Perform the processing.
        @param text: the text (tweet) to process

        @returns: list of (valid) tokens in text
        """

        text = text.lower()
        tokens = self.tokeniser.tokenize(text)
        tokensStripped = [tok.strip() for tok in tokens]

        # Lemmatization if provided
        if self.lemmatizer:
            tokensLemmatized = [self.lemmatizer.lemmatize(tok) for tok in tokensStripped]
        else:
            tokensLemmatized = tokensStripped

        # pattern for digits
        # the list comprehension in return statement essentially remove all strings of digits or fractions, e.g., 6.15
        regexDigit = re.compile("^\d+\s|\s\d+\s|\s\d+$")
        # regex pattern for http
        regexHttp = re.compile("^http")

        return [tok for tok in tokensLemmatized 
                if tok not in self.lStopwords 
                and tok not in self.filter_out_terms
                and regexDigit.match(tok) == None
                and regexHttp.match(tok) == None]