# Single spaCy document example
import spacy

# Load spacy object that contains tokenizer, tagger, parser, and named entity recognition modules.
nlp = spacy.load('en_core_web_sm')
print(nlp.pipe_names)

text = 'This is a sentence about nothing.'

# Convert the string into a Doc object
doc = nlp(text)
print(doc)