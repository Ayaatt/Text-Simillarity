import jaccard
# import cosine
# import damerauLevi
# import diceCoef
# import euclidienDistance
import jaroDistance
import jaroWinkler
# import levenshteinD
# import manhattan
# import nGram
# import smithWaterman
# import hamstringDistance
# import longestCommon
# import needlemanWunsch
import time
import numpy as np
import json
# from nltk import word_tokenize


def calculate_similarity(algorithm, token1, token2):
    return algorithm(token1, token2)


def tokenize(query):
    return query.lower().split()


def nilai_tertinggi(datalist):
    if not datalist:
        return None  # Kembalikan None jika daftar kosong
    # Mencari elemen dengan nilai tertinggi
    max_value = max(datalist, key=lambda x: x[1])
    return max_value[0]  # Mengembalikan string di samping nilai tertinggi


def koreksi(algorithm):
    dictionary = ["on", "off", "fan", "tv", "television", "PC", "lamp", "turn"]
    user_query = input("Masukkan kalimat : ")

    corrected_tokens = []

    tokens = tokenize(user_query)

    for token in tokens:
        if token in [".", ",", "!", "?", ":", ";", "the"]:
            corrected_tokens.append(token)
            continue
        for benar_kata in dictionary:
            # benar_set = set(benar_kata)
            # if tokens != benar_kata:
            # similarity_jaro = jaroDistance.jaro(str(tokens), str(benar_set))
            similarity = calculate_similarity(algorithm, token, benar_kata)

            print("Hasil kesamaan Jaro antara kalimat input '" + token +
                  "' dan kalimat benar '" + benar_kata + "' adalah " + str(similarity))
            print(f" kata_set : {token}")
            print(f" benar_kata : {benar_kata}")
        best_match = max(dictionary, key=lambda benar_kata: calculate_similarity(
            algorithm, token, benar_kata))
        corrected_tokens.append(best_match)

    kalimatnya = ' '.join(corrected_tokens)
    # print(f" CORRECT  : {kalimatnya}")
    return kalimatnya


start_time = time.time()
# jackar = koreksi(jaccard.jakar)
# jarno = koreksi(jaroDistance.jaro)
# print(f"jaccard : {jackar}")
# print(f"Jaro : {jarno}")
jarWe = koreksi(jaroWinkler.jaro_winkler_similarity)
print(f"JaroWin : {jarWe}")
elapsed_time = time.time() - start_time
print(f"WAKTU YANG DIBUTUHKAN : {elapsed_time}")

# for benar_kata in dictionary:
#     # benar_set = set(benar_kata)
#     # if tokens != benar_kata:
#     similarity_jaro = jaccard.jakar(token, benar_kata)
#     hasil.append((benar_kata, similarity_jaro))

#     # print(f"hasil : {hasil}")

#     # print("Hasil kesamaan Jaro antara kalimat input '" + token +
#     #       "' dan kalimat benar '" + benar_kata + "' adalah " + str(similarity_jaro))
#     # print(f" kata_set : {token}")
#     # print(f" benar_kata : {benar_kata}")
# result = nilai_tertinggi(hasil)
# print(f"hasil : {hasil}")
# print(result)
# corrected_tokens.append(result)

# else:
#     corrected_tokens.append(benar_kata)

# sorting(token, benar_kata, similarity_jaro)
# sorting(similarity_jaro)
# print(sorting(similarity_jaro))
# siapa yang paling tinggi scorenya
# variabel hasil dikosongkan


# hasil_json = json.dumps(hasil)
# print(hasil)
# Memfilter data untuk kata "on"


# result = nilai_tertinggi(hasil)
# print("Nilai tertinggi:", result)
# result = text_correction(token)
# corrected_tokens.append(token)
# elapsed_time = time.time() - start_time
# corrected_sentence = " ".join(corrected_tokens)
# print(f"token akhir : {token}")
# kalimatnya = ' '.join(corrected_tokens)
# print(f"CORECTED_TOKENS: {kalimatnya}")
# print(user_query)
