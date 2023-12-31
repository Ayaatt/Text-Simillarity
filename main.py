import jaccard
import cosine
import damerauLevi
import diceCoef
import euclidienDistance
import jaroDistance
import jaroWinkler
import levenshteinD
import manhattan
import nGram
import smithWaterman
import hamstringDistance
import longestCommon
import needlemanWunsch
import time


def tokenize(query):
    set_query_input = set_query_input.lower().split()
    set_query_input = set(query)
    return set_query_input


# jaccard.jekar()
dictionary = ["on", "off", "fan", "tv", "television", "PC", "lamp"]
user_query = input("Masukkan kalimat : ")
user_query = user_query.lower()  # Convert query to lowercase
for kata in user_query:
    tokens = tokenize(user_query)  # Tokenize the user query string
    start_time = time.time()  # Start measuring time
    corrected_tokens = []  # create a new array of text
    for token in tokens:
        if token in [".", ",", "!", "?", ":", ";", "the"]:
            corrected_tokens.append(token)
            continue
# result = text_correction(token)
corrected_tokens.append(token)
elapsed_time = time.time() - start_time
corrected_sentence = " ".join(corrected_tokens)
