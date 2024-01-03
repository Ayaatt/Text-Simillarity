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
import numpy as np
import json
import csv
from statistics import mean
import pandas as pd
from io import StringIO
# from nltk import word_tokenize


def calculate_similarity(algorithm, token1, token2):
    return algorithm(token1, token2)


def tokenize(query):
    return query.lower().split()


def best_match_and_score(algorithm, token):
    # if not dictionary:
    #     return None, None  # or some other default value
    dictionary = ["on", "off", "fan", "tv", "television",
                  "PC", "lamp", "turn", "unlock", "lock", "gate", "light", "windows", "back door", "oven", "open", "close", "enable", "disable"]

    best_match, best_similarity = max(
        ((word, algorithm(token, word)) for word in dictionary),
        key=lambda x: x[1],
    )
    return best_match, best_similarity

# Function to process a DataFrame with input tokens, using the provided algorithms and dictionary


def process_input_dataframe(df, algorithms):
    results = []
    start_time_jaccard = time.time()

    for input_token in df['Input']:
        tokens = tokenize(input_token)
        corrected_tokens_jaccard = []
        corrected_tokens_jaro = []
        corrected_tokens_dice = []
        corrected_tokens_cosine = []
        corrected_tokens_dama = []
        corrected_tokens_euc = []
        corrected_tokens_hams = []
        corrected_tokens_jaroWin = []
        corrected_tokens_longes = []
        corrected_tokens_leven = []
        corrected_tokens_manha = []
        corrected_tokens_need = []
        corrected_tokens_ngram = []
        corrected_tokens_smith = []
        similarity_scores_jaccard = []
        similarity_scores_jaro = []
        similarity_scores_dice = []
        similarity_scores_dama = []
        similarity_scores_cosine = []
        similarity_scores_euc = []
        similarity_scores_hams = []
        similarity_scores_jaroWin = []
        similarity_scores_longes = []
        similarity_scores_leven = []
        similarity_scores_manha = []
        similarity_scores_need = []
        similarity_scores_ngram = []
        similarity_scores_smith = []
        times_jaccard = []
        times_jaro = []
        times_dice = []
        times_dama = []
        times_cosine = []
        times_euc = []
        times_hams = []
        times_jaroWin = []
        times_longes = []
        times_leven = []
        times_manha = []
        times_need = []
        times_ngram = []
        times_smith = []

        for token in tokens:
            if token in [".", ",", "!", "?", ":", ";", "the"]:
                corrected_tokens_jaccard.append(token)
                corrected_tokens_jaro.append(token)
                corrected_tokens_dice.append(token)
                corrected_tokens_cosine.append(token)
                corrected_tokens_dama.append(token)
                corrected_tokens_euc.append(token)
                corrected_tokens_hams.append(token)
                corrected_tokens_jaroWin.append(token)
                corrected_tokens_longes.append(token)
                corrected_tokens_leven.append(token)
                corrected_tokens_manha.append(token)
                corrected_tokens_need.append(token)
                corrected_tokens_ngram.append(token)
                corrected_tokens_smith.append(token)
                continue

            # Jaccard correction and similarity calculation
            best_match_jaccard, best_similarity_jaccard = best_match_and_score(
                algorithms[0][1], token)
            times_jaccard.append(time.time() - start_time_jaccard)
            corrected_tokens_jaccard.append(best_match_jaccard)
            similarity_scores_jaccard.append(best_similarity_jaccard)

            # Jaro correction and similarity calculation
            start_time_jaro = time.time()
            best_match_jaro, best_similarity_jaro = best_match_and_score(
                algorithms[1][1], token)
            times_jaro.append(time.time() - start_time_jaro)
            corrected_tokens_jaro.append(best_match_jaro)
            similarity_scores_jaro.append(best_similarity_jaro)

            # Dama correction and similarity calculation
            start_time_dama = time.time()
            best_match_dama, best_similarity_dama = best_match_and_score(
                algorithms[1][1], token)
            times_dama.append(time.time() - start_time_dama)
            corrected_tokens_dama.append(best_match_dama)
            similarity_scores_dama.append(best_similarity_dama)

            # Dice correction and similarity calculation
            start_time_dice = time.time()
            best_match_dice, best_similarity_dice = best_match_and_score(
                algorithms[1][1], token)
            times_dice.append(time.time() - start_time_dice)
            corrected_tokens_dice.append(best_match_dice)
            similarity_scores_dice.append(best_similarity_dice)

            # Cosine correction and similarity calculation
            start_time_cosine = time.time()
            best_match_cosine, best_similarity_cosine = best_match_and_score(
                algorithms[1][1], token)
            times_cosine.append(time.time() - start_time_cosine)
            corrected_tokens_cosine.append(best_match_cosine)
            similarity_scores_cosine.append(best_similarity_cosine)

            # Euclidien Distance correction and similarity calculation
            start_time_euc = time.time()
            best_match_euc, best_similarity_euc = best_match_and_score(
                algorithms[1][1], token)
            times_euc.append(time.time() - start_time_euc)
            corrected_tokens_euc.append(best_match_euc)
            similarity_scores_euc.append(best_similarity_euc)

            # Hamstring correction and similarity calculation
            start_time_hams = time.time()
            best_match_hams, best_similarity_hams = best_match_and_score(
                algorithms[1][1], token)
            times_hams.append(time.time() - start_time_hams)
            corrected_tokens_hams.append(best_match_hams)
            similarity_scores_hams.append(best_similarity_hams)

            # Jaro-Winkler correction and similarity calculation
            start_time_dice = time.time()
            best_match_dice, best_similarity_dice = best_match_and_score(
                algorithms[1][1], token)
            times_dice.append(time.time() - start_time_dice)
            corrected_tokens_dice.append(best_match_dice)
            similarity_scores_dice.append(best_similarity_dice)

            # Longest correction and similarity calculation
            start_time_longes = time.time()
            best_match_longes, best_similarity_longes = best_match_and_score(
                algorithms[1][1], token)
            times_longes.append(time.time() - start_time_longes)
            corrected_tokens_longes.append(best_match_longes)
            similarity_scores_longes.append(best_similarity_longes)

            # Levenshtein correction and similarity calculation
            start_time_leven = time.time()
            best_match_leven, best_similarity_leven = best_match_and_score(
                algorithms[1][1], token)
            times_leven.append(time.time() - start_time_leven)
            corrected_tokens_leven.append(best_match_leven)
            similarity_scores_leven.append(best_similarity_leven)

            # Manhattan correction and similarity calculation
            start_time_manha = time.time()
            best_match_manha, best_similarity_manha = best_match_and_score(
                algorithms[1][1], token)
            times_manha.append(time.time() - start_time_manha)
            corrected_tokens_manha.append(best_match_manha)
            similarity_scores_manha.append(best_similarity_manha)

            # Needleman correction and similarity calculation
            start_time_need = time.time()
            best_match_need, best_similarity_need = best_match_and_score(
                algorithms[1][1], token)
            times_need.append(time.time() - start_time_need)
            corrected_tokens_need.append(best_match_need)
            similarity_scores_need.append(best_similarity_need)

            # N-Gram correction and similarity calculation
            start_time_ngram = time.time()
            best_match_ngram, best_similarity_ngram = best_match_and_score(
                algorithms[1][1], token)
            times_ngram.append(time.time() - start_time_ngram)
            corrected_tokens_ngram.append(best_match_ngram)
            similarity_scores_ngram.append(best_similarity_ngram)

            # Smith correction and similarity calculation
            start_time_smith = time.time()
            best_match_smith, best_similarity_smith = best_match_and_score(
                algorithms[1][1], token)
            times_smith.append(time.time() - start_time_smith)
            corrected_tokens_smith.append(best_match_smith)
            similarity_scores_smith.append(best_similarity_smith)

        # Reconstruct the corrected sentences
        corrected_sentence_jaccard = ' '.join(corrected_tokens_jaccard)
        corrected_sentence_jaro = ' '.join(corrected_tokens_jaro)
        corrected_sentence_dice = ' '.join(corrected_tokens_dice)
        corrected_sentence_cosine = ' '.join(corrected_tokens_cosine)
        corrected_sentence_euc = ' '.join(corrected_tokens_euc)
        corrected_sentence_dama = ' '.join(corrected_tokens_dama)
        corrected_sentence_hams = ' '.join(corrected_tokens_hams)
        corrected_sentence_jaroWin = ' '.join(corrected_tokens_jaroWin)
        corrected_sentence_longes = ' '.join(corrected_tokens_longes)
        corrected_sentence_leven = ' '.join(corrected_tokens_leven)
        corrected_sentence_manha = ' '.join(corrected_tokens_manha)
        corrected_sentence_need = ' '.join(corrected_tokens_need)
        corrected_sentence_ngram = ' '.join(corrected_tokens_ngram)
        corrected_sentence_smith = ' '.join(corrected_tokens_smith)

        # Add the results to the dataframe
        result_row = {
            'Input': input_token,
            'Jaccard Corrected': corrected_sentence_jaccard,
            'JaroDistance Corrected': corrected_sentence_jaro,
            'Dice Coefficien Corrected': corrected_sentence_dice,
            'Cosine Corrected': corrected_sentence_cosine,
            'Damerau-Levenshtein Corrected': corrected_sentence_dama,
            'Euclidien Distance Corrected': corrected_sentence_euc,
            'Hamstring Distance Corrected': corrected_sentence_hams,
            'Jaro-Winkler Corrected': corrected_sentence_jaroWin,
            'Longest Common Corrected': corrected_sentence_longes,
            'Levenshtein Distance Corrected': corrected_sentence_leven,
            'Manhattan Corrected': corrected_sentence_manha,
            'Needleman Corrected': corrected_sentence_need,
            'N-Gram Corrected': corrected_sentence_ngram,
            'Smith Waterman Corrected': corrected_sentence_smith,
            'Jaccard Time': sum(times_jaccard)*100,
            'JaroDistance Time': sum(times_jaro)*100,
            'Dice Coefficien Time': sum(times_dice)*100,
            'Cosine Time': sum(times_cosine)*100,
            'Damerau-Levenshtein Time': sum(times_dama)*100,
            'Euclidien Distance Time': sum(times_euc)*100,
            'Hamstring Distance Time': sum(times_hams)*100,
            'Jaro-Winkler Time': sum(times_jaroWin)*100,
            'Longest Common Time': sum(times_longes)*100,
            'Levenshtein Distance Time': sum(times_leven)*100,
            'Manhattan Time': sum(times_manha)*100,
            'Needleman Time': sum(times_need)*100,
            'N-Gram Time': sum(times_ngram)*100,
            'Smith Waterman Time': sum(times_smith)*100,
            'Jaccard Accuracy': np.mean(similarity_scores_jaccard),
            'JaroDistance Accuracy': np.mean(similarity_scores_jaro),
            'Dice Coefficien Accuracy': np.mean(similarity_scores_dice),
            'Cosine Accuracy': np.mean(similarity_scores_cosine),
            'Damerau-Levenshtein Accuracy': np.mean(similarity_scores_dama),
            'Euclidien Distance Accuracy': np.mean(similarity_scores_euc),
            'Hamstring Distance Accuracy': np.mean(similarity_scores_hams),
            'Jaro-Winkler Accuracy': np.mean(similarity_scores_jaroWin),
            'Longest Common Accuracy': np.mean(similarity_scores_longes),
            'Levenshtein Distance Accuracy': np.mean(similarity_scores_leven),
            'Manhattan Accuracy': np.mean(similarity_scores_manha),
            'Needleman Accuracy': np.mean(similarity_scores_need),
            'N-Gram Accuracy': np.mean(similarity_scores_ngram),
            'Smith Waterman Accuracy': np.mean(similarity_scores_smith),
        }
        results.append(result_row)

    return pd.DataFrame(results)


# Define the list of input tokens
input_tokens = [
    "turn on the tea.",
    "turn off the flight.",
    "look the door.",
    "unluck the door.",
    "turn on the lump.",
    "look the windows.",
    "unluck the windows.",
    "turn on the van.",
    "turn off the van.",
    "turn on the hater.",
    "unable the hater.",
    "disassemble the back door.",
    "unluck the back door.",
    "look the gate.",
    "unluck the gate.",
    "turn on the over.",
    "turn off the over.",
    "oven the gate.",
    "clause the gate."
]

# Create a DataFrame from the list of input tokens
df_input = pd.DataFrame(input_tokens, columns=['Input'])

# Define the algorithms to use
algorithms_to_use = [
    ('jaccard', jaccard.jakar),
    ('jaro', jaroDistance.jaro),
    ('cosine', cosine.cosine_similarity),
    ('damerau-levenshtein', damerauLevi.damerau_levenshtein_distance),
    ('euclidien', euclidienDistance.euclidean_distance),
    ('hamstring', hamstringDistance.hamming_distance),
    ('jaro-winkler', jaroWinkler.jaro_winkler_similarity),
    ('levenshtein', levenshteinD.levenshtein_distance),
    ('longest', longestCommon.longest_common_subsequence),
    ('manhattan', manhattan.manhattan_distance),
    ('needleman', needlemanWunsch.needleman_wunsch),
    ('ngram', nGram.ngrams),
    ('smith', smithWaterman.smith_waterman)
]

# Define the dictionary of correct words

# Process the DataFrame with the provided input tokens
df_results = process_input_dataframe(
    df_input, algorithms_to_use)

# Save the processed data to a CSV file
output_csv_path_full = 'corrections.csv'
df_results.to_csv(output_csv_path_full, index=False)

# The path to the CSV file can be used to download or further process the file
print(f"Results saved to {output_csv_path_full}")

# def calculate_accuracy(best_similarity):
#     return mean(best_similarity)


# def koreksi(algorithms, original_tokens):
#     dictionary = ["on", "off", "fan", "tv", "television", "PC", "lamp", "turn"]
#     # user_query = input("Masukkan kalimat : ")

#     results = []

#     # tokens = tokenize(user_query)

#     for algorithm in algorithms:
#         start_time = time.time()
#         corrected_tokens = []
#         similarity_scores = []
#         for token in original_tokens:
#             if token in [".", ",", "!", "?", ":", ";", "the"]:
#                 corrected_tokens.append(token)
#                 continue
#             best_match, best_similarity = max((benar_kata, calculate_similarity(
#                 algorithm, token, benar_kata))for benar_kata in dictionary)

#             # best_match = max(dictionary, key=lambda benar_kata: calculate_similarity(
#             #     algorithm, token, benar_kata))
#             corrected_tokens.append(best_match)
#             similarity_scores.append(best_similarity)

#         elapsed_time = time.time() - start_time
#         accuracy = calculate_accuracy(similarity_scores)

#         results.append(
#             (original_tokens, corrected_tokens, elapsed_time, accuracy))

#     return results


# # Add more algorithms as needed
# algorithms = [jaccard.jakar, jaroDistance.jaro]
# original_tokens = tokenize(input("Masukkan kalimat : "))
# corrections_results = koreksi(algorithms, original_tokens)

# with open('corrections.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)

#     writer.writerow(["Original Token",
#                      "Input Token",
#                      "Corrected Tokens Jaccard",
#                      "Corrected Tokens Jaro-Distance",
#                      "Jaccard Time",
#                      "Jaro-Distance Time",
#                      "Accuracy Jaccard",
#                      "Accuracy Jaro-Distance"])

#     for result in corrections_results:
#         # Modify this line according to your actual result
#         writer.writerow(result)
# start_time = time.time()
# # jackar = koreksi(jaccard.jakar)
# # jarno = koreksi(jaroDistance.jaro)
# # print(f"jaccard : {jackar}")
# # print(f"Jaro : {jarno}")
# jarWe = koreksi(jaroWinkler.jaro_winkler_similarity)
# print(f"JaroWin : {jarWe}")
# elapsed_time = time.time() - start_time
# print(f"WAKTU YANG DIBUTUHKAN : {elapsed_time}")

# def nilai_tertinggi(datalist):
#     if not datalist:
#         return None  # Kembalikan None jika daftar kosong
#     # Mencari elemen dengan nilai tertinggi
#     max_value = max(datalist, key=lambda x: x[1])
#     return max_value[0]  # Mengembalikan string di samping nilai tertinggi
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
