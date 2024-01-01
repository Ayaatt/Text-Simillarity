import jaccard
# import cosine
# import damerauLevi
# import diceCoef
# import euclidienDistance
# import jaroDistance
# import jaroWinkler
# import levenshteinD
# import manhattan
# import nGram
# import smithWaterman
# import hamstringDistance
# import longestCommon
# import needlemanWunsch
import time


def tokenize(query):
    return set(query.lower().split())


# jaccard.jekar()
dictionary = ["on", "off", "fan", "tv", "television", "PC", "lamp"]
user_query = input("Masukkan kalimat : ")
# user_query = user_query.lower()  # Convert query to lowercase

corrected_tokens = []  # create a new array of text


for kata in user_query:
    tokens = tokenize(user_query)  # Tokenize the user query string
    start_time = time.time()  # Start measuring time
    for token in tokens:
        if token in [".", ",", "!", "?", ":", ";", "the"]:
            corrected_tokens.append(token)
            for benar_kata in dictionary:
                benar_set = tokenize(benar_kata)
                jaccard.jekar(tokens, benar_set)
                # similarity = jaccard.jakar(tokens, benar_set)
                # corrected_tokens.append(benar_kata)
                # print("Hasil kesamaan Jaccard antara kalimat input '" + kata +
                #       "' dan kalimat benar '" + benar_kata + "' adalah " + str(similarity))
                # print(f" kata_set : {tokens}")
                # print(f" benar_kata : {benar_kata}")
                break


# result = text_correction(token)
# corrected_tokens.append(token)
# elapsed_time = time.time() - start_time
# corrected_sentence = " ".join(corrected_tokens)

# kalimatnya = ' '.join(corrected_tokens)
# print(f" HASILNYA : {kalimatnya}")
# print(user_query)
