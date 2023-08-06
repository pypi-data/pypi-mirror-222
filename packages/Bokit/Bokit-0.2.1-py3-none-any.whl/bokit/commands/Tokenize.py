class Tokenize:

    '''Tokenization pipeline for Tibetan text'''
    
    def __init__(self):

        from botok import WordTokenizer
        from botok.config import Config
        from pathlib import Path
        
        # initialize the tokenizer
        config = Config(dialect_name="general", base_path=Path.home())
        self._wt = WordTokenizer(config=config)

    def query(self, text):

        '''Takes in Tibetan string and returns list of tokens.
        
        text | str | Tibetan string
        
        '''

        # initialize the list of tokens to be returned
        tokens = []

        # tokenize the input text
        tokenizer_output = self._wt.tokenize(text, split_affixes=False)
        
        # iterate through the tokens and add them to the list
        for token in tokenizer_output:
            tokens.append(token['text_unaffixed'])

        return tokens
   