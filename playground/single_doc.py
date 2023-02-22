"""
Single spaCy document example
"""
import spacy

# Load spacy nlp pipeline object.
nlp = spacy.load('en_core_web_sm')
print(f'Type of `nlp`: {type(nlp)}')
print(f'Pipeline components included out-of-the-box from spacy.load: {nlp.pipe_names}')

# String example as our single document
text = 'This is a sentence about nothing.'

# Convert the string into a Doc object
doc = nlp(text)
print(f'Result from feeding in text into nlp pipe: {doc}')
print(f'doc type: {type(doc)}')

# Return a list of the text corresponding to each token
print(f'Returning a list of tokens from the `doc` object: {[token.text for token in doc]}')