import jaccard
import cosine
import damerauLevi
import diceCoef
import euclidienDistance
import jaroDistance
import jaroWinkler
import levenshteinD
import manhattan
# import nGram
import smithWaterman
import hammingDistance
import longestCommon
import needlemanWunsch
from datetime import datetime
import time
import numpy as np
import json
import csv
from statistics import mean
import pandas as pd
import csv
from tabulate import tabulate
# from nltk import word_tokenize
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///similarity.db'
# db = SQLAlchemy(app)


# class algoritma(db.Model):
# __tablename__ = 'algoritma'
# ID = db.Column(db.Integer, primary_key=True)
# originalData = db.Column(db.String)
# inputData = db.Column(db.String)
# Jaccard_Corrected_data = db.Column(db.String),
# JaroDistance_Corrected_data = db.Column(db.String),
# Dice_Coefficien_Corrected = db.Column(db.String),
# Cosine_Corrected_data = db.Column(db.String),
# Damerau_Levenshtein_Corrected = db.Column(db.String),
# Euclidien_Distance_Corrected = db.Column(db.String),
# hamming_Distance_Corrected = db.Column(db.String),
# Jaro_Winkler_Corrected = db.Column(db.String),
# Longest_Common_Corrected = db.Column(db.String),
# Levenshtein_Distance_Corrected = db.Column(db.String),
# Manhattan_Corrected = db.Column(db.String),
# Needleman_Corrected = db.Column(db.String),
# N_Gram_Corrected = db.Column(db.String),
# Smith_Waterman_Corrected = db.Column(db.String),
# Jaccard_Time = db.Column(db.Float),
# JaroDistance_Time = db.Column(db.Float),
# Dice_Coefficien_Time = db.Column(db.Float),
# Cosine_Time = db.Column(db.Float),
# Damerau_Levenshtein_Time = db.Column(db.Float),
# Euclidien_Distance_Time = db.Column(db.Float),
# hamming_Distance_Time = db.Column(db.Float),
# Jaro_Winkler_Time = db.Column(db.Float),
# Longest_Common_Time = db.Column(db.Float),
# Levenshtein_Distance_Time = db.Column(db.Float),
# Manhattan_Time = db.Column(db.Float),
# Needleman_Time = db.Column(db.Float),
# N_Gram_Time = db.Column(db.Float),
# Smith_Waterman_Time = db.Column(db.Float),
# Jaccard_Accuracy = db.Column(db.Float),
# JaroDistance_Accuracy = db.Column(db.Float),
# Dice_Coefficien_Accuracy = db.Column(db.Float),
# Cosine_Accuracy = db.Column(db.Float),
# Damerau_Levenshtein_Accuracy = db.Column(db.Float),
# Euclidien_Distance_Accuracy = db.Column(db.Float),
# hamming_Distance_Accuracy = db.Column(db.Float),
# Jaro_Winkler_Accuracy = db.Column(db.Float),
# Longest_Common_Accuracy = db.Column(db.Float),
# Levenshtein_Distance_Accuracy = db.Column(db.Float),
# Manhattan_Accuracy = db.Column(db.Float),
# Needleman_Accuracy = db.Column(db.Float),
# N_Gram_Accuracy = db.Column(db.Float),
# Smith_Waterman_Accuracy = db.Column(db.Float),


# from nltk import word_tokenize
# with app.app_context():
#     try:
#         if not os.path.exists('similarity.db'):
#             db.create_all()
#             print('Database and tables created successfully')
#     except Exception as e:
#         print(f'Error creating database and tables: {e}')


# @app.route('/add_data', methods=['POST'])
# def add_data():
# data = request.get_json()
# new_data = algoritma(
#     originalData=data['originalData'],
#     inputData=data['inputData'],
#     Jaccard_Corrected_data=data['Jaccard_Corrected_data'],
#     JaroDistance_Corrected_data=data['JaroDistance_Corrected_data'],
#     Dice_Coefficien_Corrected=data['Dice_Coefficien_Corrected'],
#     Cosine_Corrected_data=data['Cosine_Corrected_data'],
#     Damerau_Levenshtein_Corrected=data['Damerau_Levenshtein_Corrected'],
#     Euclidien_Distance_Corrected=data['Euclidien_Distance_Corrected'],
#     hamming_Distance_Corrected=data['hamming_Distance_Corrected'],
#     Jaro_Winkler_Corrected=data['Jaro_Winkler_Corrected'],
#     Longest_Common_Corrected=data['Longest_Common_Corrected'],
#     Levenshtein_Distance_Corrected=data['Levenshtein_Distance_Corrected'],
#     Manhattan_Corrected=data['Manhattan_Corrected'],
#     Needleman_Corrected=data['Needleman_Corrected'],
#     N_Gram_Corrected=data['N_Gram_Corrected'],
#     Smith_Waterman_Corrected=data['Smith_Waterman_Corrected'],
#     Jaccard_Time=data['Jaccard_Time'],
#     JaroDistance_Time=data['JaroDistance_Time'],
#     Dice_Coefficien_Time=data['Dice_Coefficien_Time'],
#     Cosine_Time=data['Cosine_Time'],
#     Damerau_Levenshtein_Time=data['Damerau_Levenshtein_Time'],
#     Euclidien_Distance_Time=data['Euclidien_Distance_Time'],
#     hamming_Distance_Time=data['hamming_Distance_Time'],
#     Jaro_Winkler_Time=data['Jaro_Winkler_Time'],
#     Longest_Common_Time=data['Longest_Common_Time'],
#     Levenshtein_Distance_Time=data['Levenshtein_Distance_Time'],
#     Manhattan_Time=data['Manhattan_Time'],
#     Needleman_Time=data['Needleman_Time'],
#     N_Gram_Time=data['N_Gram_Time'],
#     Smith_Waterman_Time=data['Smith_Waterman_Time'],
#     Jaccard_Accuracy=data['Jaccard_Accuracy'],
#     JaroDistance_Accuracy=data['JaroDistance_Accuracy'],
#     Dice_Coefficien_Accuracy=data['Dice_Coefficien_Accuracy'],
#     Cosine_Accuracy=data['Cosine_Accuracy'],
#     Damerau_Levenshtein_Accuracy=data['Damerau_Levenshtein_Accuracy'],
#     Euclidien_Distance_Accuracy=data['Euclidien_Distance_Accuracy'],
#     hamming_Distance_Accuracy=data['hamming_Distance_Accuracy'],
#     Jaro_Winkler_Accuracy=data['Jaro_Winkler_Accuracy'],
#     Longest_Common_Accuracy=data['Longest_Common_Accuracy'],
#     Levenshtein_Distance_Accuracy=data['Levenshtein_Distance_Accuracy'],
#     Manhattan_Accuracy=data['Manhattan_Accuracy'],
#     Needleman_Accuracy=data['Needleman_Accuracy'],
#     N_Gram_Accuracy=data['N_Gram_Accuracy'],
#     Smith_Waterman_Accuracy=data['Smith_Waterman_Accuracy']
# )

# # Add the new data to the database
# db.session.add(new_data)
# db.session.commit()

# return "Data added successfully", 201


# @app.route('/show_all_data_html')
# def show_all_data_html():
# users = algoritma.query.all()
# users_data = []
# for user in users:
#     user_data = {
#         'Original': user.originalData,
#         'Input': user.input_data,
#         'Jaccard Corrected': user.Jaccard_Corrected_data,
#         'JaroDistance Corrected': user.JaroDistance_Corrected_data,
#         'Dice Coefficien Corrected': user.Dice_Coefficien_Corrected,
#         'Cosine Corrected': user.Cosine_Corrected_data,
#         'Damerau-Levenshtein Corrected': user.Damerau_Levenshtein_Corrected,
#         'Euclidien Distance Corrected': user.Euclidien_Distance_Corrected,
#         'hamming Distance Corrected': user.hamming_Distance_Corrected,
#         'Jaro-Winkler Corrected': user.Jaro_Winkler_Corrected,
#         'Longest Common Corrected': user.Longest_Common_Corrected,
#         'Levenshtein Distance Corrected': user.Levenshtein_Distance_Corrected,
#         'Manhattan Corrected': user.Manhattan_Corrected,
#         'Needleman Corrected': user.Needleman_Corrected,
#         'N-Gram Corrected': user.N_Gram_Corrected,
#         'Smith Waterman Corrected': user.Smith_Waterman_Corrected,
#         'Jaccard Time': user.Jaccard_Time,
#         'JaroDistance Time': user.JaroDistance_Time,
#         'Dice Coefficien Time': user.Dice_Coefficien_Time,
#         'Cosine Time': user.Cosine_Time,
#         'Damerau-Levenshtein Time': user.Damerau_Levenshtein_Time,
#         'Euclidien Distance Time': user.Euclidien_Distance_Time,
#         'hamming Distance Time': user.hamming_Distance_Time,
#         'Jaro-Winkler Time': user.Jaro_Winkler_Time,
#         'Longest Common Time': user.Longest_Common_Time,
#         'Levenshtein Distance Time': user.Levenshtein_Distance_Time,
#         'Manhattan Time': user.Manhattan_Time,
#         'Needleman Time': user.Needleman_Time,
#         'N-Gram Time': user.N_Gram_Time,
#         'Smith Waterman Time': user.Smith_Waterman_Corrected,
#         'Jaccard Accuracy': user.Jaccard_Accuracy,
#         'JaroDistance Accuracy': user.JaroDistance_Accuracy,
#         'Dice Coefficien Accuracy': user.Dice_Coefficien_Accuracy,
#         'Cosine Accuracy': user.Cosine_Accuracy,
#         'Damerau-Levenshtein Accuracy': user.Damerau_Levenshtein_Accuracy,
#         'Euclidien Distance Accuracy': user.Euclidien_Distance_Accuracy,
#         'hamming Distance Accuracy': user.hamming_Distance_Accuracy,
#         'Jaro-Winkler Accuracy': user.Jaro_Winkler_Accuracy,
#         'Longest Common Accuracy': user.Longest_Common_Accuracy,
#         'Levenshtein Distance Accuracy': user.Levenshtein_Distance_Accuracy,
#         'Manhattan Accuracy': user.Manhattan_Accuracy,
#         'Needleman Accuracy': user.Needleman_Accuracy,
#         'N-Gram Accuracy': user.N_Gram_Accuracy,
#         'Smith Waterman Accuracy': user.Smith_Waterman_Accuracy,
#     }
#     users_data.append(user_data)

# template = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Data Display</title>
#     <style>
#         table {
#             width: 100%;
#             border-collapse: collapse;
#         }
#         th, td {
#             border: 1px solid black;
#             padding: 15px;
#             text-align: left;
#         }
#         th {
#             background-color: #4CAF50;
#             color: white;
#         }
#     </style>
# </head>
# <body>
#     <h1>Users</h1>
#     <table>
#         <tr>
#             <td>Original</td>
#             <td>Input</td>
#             <td>Jaccard Corrected</td>
#             <td>JaroDistance Corrected</td>
#             <td>Dice Coefficien Corrected</td>
#             <td>Cosine Corrected</td>
#             <td>Damerau-Levenshtein Corrected</td>
#             <td>Euclidien Distance Corrected</td>
#             <td>hamming Distance Corrected</td>
#             <td>Jaro-Winkler Corrected</td>
#             <td>Longest Common Corrected</td>
#             <td>Levenshtein Distance Corrected</td>
#             <td>Manhattan Corrected</td>
#             <td>Needleman Corrected</td>
#             <td>N-Gram Corrected</td>
#             <td>Smith Waterman Corrected</td>
#             <td>Jaccard Time</td>
#             <td>JaroDistance Time</td>
#             <td>Dice Coefficien Time</td>
#             <td>Cosine Time</td>
#             <td>Damerau-Levenshtein Time</td>
#             <td>Euclidien Distance Time</td>
#             <td>hamming Distance Time</td>
#             <td>Jaro-Winkler Time</td>
#             <td>Longest Common Time</td>
#             <td>Levenshtein Distance Time</td>
#             <td>Manhattan Time</td>
#             <td>Needleman Time</td>
#             <td>N-Gram Time</td>
#             <td>Smith Waterman Time</td>
#             <td>Jaccard Accuracy</td>
#             <td>JaroDistance Accuracy</td>
#             <td>Dice Coefficien Accuracy</td>
#             <td>Cosine Accuracy</td>
#             <td>Damerau-Levenshtein Accuracy</td>
#             <td>Euclidien Distance Accuracy</td>
#             <td>hamming Distance Accuracy</td>
#             <td>Jaro-Winkler Accuracy</td>
#             <td>Longest Common Accuracy</td>
#             <td>Levenshtein Distance Accuracy</td>
#             <td>Manhattan Accuracy</td>
#             <td>Needleman Accuracy</td>
#             <td>N-Gram Accuracy</td>
#             <td>Smith Waterman Accuracy</td>
#         </tr>
#         {% for user in users %}
#         <tr>
#             <td>{{ user.originalData }}</td>
#             <td>{{ user.input_data }}</td>
#             <td>{{ user.Jaccard_Corrected_data }}</td>
#             <td>{{ user.JaroDistance_Corrected_data }}</td>
#             <td>{{ user.Dice_Coefficien_Corrected }}</td>
#             <td>{{ user.Cosine_Corrected_data }}</td>
#             <td>{{ user.Damerau_Levenshtein_Corrected }}</td>
#             <td>{{ user.Euclidien_Distance_Corrected }}</td>
#             <td>{{ user.hamming_Distance_Corrected }}</td>
#             <td>{{ user.Jaro_Winkler_Corrected }}</td>
#             <td>{{ user.Longest_Common_Corrected }}</td>
#             <td>{{ user.Levenshtein_Distance_Corrected }}</td>
#             <td>{{ user.Manhattan_Corrected }}</td>
#             <td>{{ user.Needleman_Corrected }}</td>
#             <td>{{ user.N_Gram_Corrected }}</td>
#             <td>{{ user.Smith_Waterman_Corrected }}</td>
#             <td>{{ user.Jaccard_Time }}</td>
#             <td>{{ user.JaroDistance_Time }}</td>
#             <td>{{ user.Dice_Coefficien_Time }}</td>
#             <td>{{ user.Cosine_Time }}</td>
#             <td>{{ user.Damerau_Levenshtein_Time }}</td>
#             <td>{{ user.Euclidien_Distance_Time }}</td>
#             <td>{{ user.hamming_Distance_Time }}</td>
#             <td>{{ user.Jaro_Winkler_Time }}</td>
#             <td>{{ user.Longest_Common_Time }}</td>
#             <td>{{ user.Levenshtein_Distance_Time }}</td>
#             <td>{{ user.Manhattan_Time }}</td>
#             <td>{{ user.Needleman_Time }}</td>
#             <td>{{ user.N_Gram_Time }}</td>
#             <td>{{ user.Smith_Waterman_Corrected }}</td>
#             <td>{{ user.Jaccard_Accuracy }}</td>
#             <td>{{ user.JaroDistance_Accuracy }}</td>
#             <td>{{ user.Dice_Coefficien_Accuracy }}</td>
#             <td>{{ user.Cosine_Accuracy }}</td>
#             <td>{{ user.Damerau_Levenshtein_Accuracy }}</td>
#             <td>{{ user.Euclidien_Distance_Accuracy }}</td>
#             <td>{{ user.hamming_Distance_Accuracy }}</td>
#             <td>{{ user.Jaro_Winkler_Accuracy }}</td>
#             <td>{{ user.Longest_Common_Accuracy }}</td>
#             <td>{{ user.Levenshtein_Distance_Accuracy }}</td>
#             <td>{{ user.Manhattan_Accuracy }}</td>
#             <td>{{ user.Needleman_Accuracy }}</td>
#             <td>{{ user.N_Gram_Accuracy }}</td>
#             <td>{{ user.Smith_Waterman_Accuracy }}</td>
#         </tr>
#         {% endfor %}
#     </table>
#     </table>
# </body></html>
# """

# return render_template_string(template, users=users_data)


# def send_data(url, data):
#     headers = {'Content-Type': 'application/json'}
#     response = requests.post(url, data=json.dumps(data), headers=headers)
#     return response


def calculate_similarity(algorithm, token1, token2):
    return algorithm(token1, token2)


def tokenize(query):
    return query.lower().split()


def rata(data):
    return mean(data)


def best_match_and_score(algorithm, token, dictionary, is_distance_metric=False):
    if not dictionary:
        return None, None  # or some other default value

    # best_match, best_similarity = max(
    #     ((word, algorithm(token, word)) for word in dictionary),
    #     key=lambda x: x[1],
    # )
    best_match = None
    if is_distance_metric:
        # For distance metrics, initialize with positive infinity
        best_similarity = float('inf')
    else:
        best_similarity = -1  # For similarity metrics, initialize with a low value

    for word in dictionary:
        score = algorithm(token, word)
        if (is_distance_metric and score < best_similarity) or (not is_distance_metric and score > best_similarity):
            best_similarity = score
            best_match = word

    return best_match, best_similarity

# Function to process a DataFrame with input tokens, using the provided algorithms and dictionary


def find_algorithm(name):
    for algorithm_name, algorithm_function in algorithms_to_use:
        if algorithm_name == name:
            return algorithm_function
    return None


def process_input_dataframe(df, dictionary):
    results = []
    start_time_jaccard = time.time()
    start_time_jaro = time.time()
    start_time_dama = time.time()
    start_time_dice = time.time()
    start_time_cosine = time.time()
    start_time_euc = time.time()
    start_time_hams = time.time()
    start_time_jaroWin = time.time()
    start_time_longes = time.time()
    start_time_leven = time.time()
    start_time_manha = time.time()
    start_time_need = time.time()
    start_time_smith = time.time()

    for input_token, ground_truth in zip(df['Input'], dictionary['Original']):
        print(f"{df['Input']}")
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
            # for ground in dictionary['Original']:
            #     truth = tokenize(ground)
                # print(f"{dictionary['Original']}")
            # Jaccard correction and similarity calculation
            best_match_jaccard, best_similarity_jaccard = best_match_and_score(
                find_algorithm("jaccard"), token, tokenize(ground_truth))
            corrected_tokens_jaccard.append(best_match_jaccard)
            similarity_scores_jaccard.append(best_similarity_jaccard)
            times_jaccard.append(time.time() - start_time_jaccard)

            # Jaro correction and similarity calculation
            best_match_jaro, best_similarity_jaro = best_match_and_score(
                find_algorithm("jaro"), token, tokenize(ground_truth), is_distance_metric=True)
            corrected_tokens_jaro.append(best_match_jaro)
            similarity_scores_jaro.append(best_similarity_jaro)
            times_jaro.append(time.time() - start_time_jaro)

            # Dama correction and similarity calculation
            best_match_dama, best_similarity_dama = best_match_and_score(
                find_algorithm("damerau-levenshtein"), token, tokenize(ground_truth), is_distance_metric=True)
            corrected_tokens_dama.append(best_match_dama)
            similarity_scores_dama.append(best_similarity_dama)
            times_dama.append(time.time() - start_time_dama)

            # Dice correction and similarity calculation
            best_match_dice, best_similarity_dice = best_match_and_score(
                find_algorithm("dice"), token, tokenize(ground_truth))
            corrected_tokens_dice.append(best_match_dice)
            similarity_scores_dice.append(best_similarity_dice)
            times_dice.append(time.time() - start_time_dice)

            # Cosine correction and similarity calculation
            best_match_cosine, best_similarity_cosine = best_match_and_score(
                find_algorithm("cosine"), token, tokenize(ground_truth))
            corrected_tokens_cosine.append(best_match_cosine)
            similarity_scores_cosine.append(best_similarity_cosine)
            times_cosine.append(time.time() - start_time_cosine)

            # Euclidien Distance correction and similarity calculation
            best_match_euc, best_similarity_euc = best_match_and_score(
                find_algorithm("euclidien"), token, tokenize(ground_truth), is_distance_metric=True)
            corrected_tokens_euc.append(best_match_euc)
            similarity_scores_euc.append(best_similarity_euc)
            times_euc.append(time.time() - start_time_euc)

            # hamming correction and similarity calculation
            best_match_hams, best_similarity_hams = best_match_and_score(
                find_algorithm("hamming"), token, tokenize(ground_truth), is_distance_metric=True)
            corrected_tokens_hams.append(best_match_hams)
            similarity_scores_hams.append(best_similarity_hams)
            times_hams.append(time.time() - start_time_hams)

            # Jaro-Winkler correction and similarity calculation
            best_match_jaroWin, best_similarity_jaroWin = best_match_and_score(
                find_algorithm("jaro-winkler"), token, tokenize(ground_truth), is_distance_metric=True)
            corrected_tokens_jaroWin.append(best_match_jaroWin)
            similarity_scores_jaroWin.append(best_similarity_jaroWin)
            times_jaroWin.append(time.time() - start_time_jaroWin)

            # Longest correction and similarity calculation
            best_match_longes, best_similarity_longes = best_match_and_score(
                find_algorithm("longest"), token, tokenize(ground_truth), is_distance_metric=True)
            corrected_tokens_longes.append(best_match_longes)
            similarity_scores_longes.append(best_similarity_longes)
            times_longes.append(time.time() - start_time_longes)

            # Levenshtein correction and similarity calculation
            best_match_leven, best_similarity_leven = best_match_and_score(
                find_algorithm("levenshtein"), token, tokenize(ground_truth), is_distance_metric=True)
            corrected_tokens_leven.append(best_match_leven)
            similarity_scores_leven.append(best_similarity_leven)
            times_leven.append(time.time() - start_time_leven)

            # Manhattan correction and similarity calculation
            best_match_manha, best_similarity_manha = best_match_and_score(
                find_algorithm("manhattan"), token, tokenize(ground_truth), is_distance_metric=True)
            corrected_tokens_manha.append(best_match_manha)
            similarity_scores_manha.append(best_similarity_manha)
            times_manha.append(time.time() - start_time_manha)

            # Needleman correction and similarity calculation
            best_match_need, best_similarity_need = best_match_and_score(
                find_algorithm("needleman"), token, tokenize(ground_truth))
            corrected_tokens_need.append(best_match_need)
            similarity_scores_need.append(best_similarity_need)
            times_need.append(time.time() - start_time_need)

            # Smith correction and similarity calculation
            best_match_smith, best_similarity_smith = best_match_and_score(
                find_algorithm("smith"), token, tokenize(ground_truth))
            corrected_tokens_smith.append(best_match_smith)
            similarity_scores_smith.append(best_similarity_smith)
            times_smith.append(time.time() - start_time_smith)

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
            'Original': ground_truth,
            'Input': input_token,
            'Jaccard Corrected': corrected_sentence_jaccard,
            'JaroDistance Corrected': corrected_sentence_jaro,
            'Dice Coefficien Corrected': corrected_sentence_dice,
            'Cosine Corrected': corrected_sentence_cosine,
            'Damerau-Levenshtein Corrected': corrected_sentence_dama,
            'Euclidien Distance Corrected': corrected_sentence_euc,
            'hamming Distance Corrected': corrected_sentence_hams,
            'Jaro-Winkler Corrected': corrected_sentence_jaroWin,
            'Longest Common Corrected': corrected_sentence_longes,
            'Levenshtein Distance Corrected': corrected_sentence_leven,
            'Manhattan Corrected': corrected_sentence_manha,
            'Needleman Corrected': corrected_sentence_need,
            'Smith Waterman Corrected': corrected_sentence_smith,
            'Jaccard Time': sum(times_jaccard),
            'JaroDistance Time': sum(times_jaro),
            'Dice Coefficien Time': sum(times_dice),
            'Cosine Time': sum(times_cosine),
            'Damerau-Levenshtein Time': sum(times_dama),
            'Euclidien Distance Time': sum(times_euc),
            'hamming Distance Time': sum(times_hams),
            'Jaro-Winkler Time': sum(times_jaroWin),
            'Longest Common Time': sum(times_longes),
            'Levenshtein Distance Time': sum(times_leven),
            'Manhattan Time': sum(times_manha),
            'Needleman Time': sum(times_need),
            'Smith Waterman Time': sum(times_smith),
            'Jaccard Accuracy': np.mean(similarity_scores_jaccard),
            'JaroDistance Accuracy': np.mean(similarity_scores_jaro),
            'Dice Coefficien Accuracy': np.mean(similarity_scores_dice),
            'Cosine Accuracy': np.mean(similarity_scores_cosine),
            'Damerau-Levenshtein Accuracy': np.mean(similarity_scores_dama),
            'Euclidien Distance Accuracy': np.mean(similarity_scores_euc),
            'hamming Distance Accuracy': np.mean(similarity_scores_hams),
            'Jaro-Winkler Accuracy': np.mean(similarity_scores_jaroWin),
            'Longest Common Accuracy': np.mean(similarity_scores_longes),
            'Levenshtein Distance Accuracy': np.mean(similarity_scores_leven),
            'Manhattan Accuracy': np.mean(similarity_scores_manha),
            'Needleman Accuracy': np.mean(similarity_scores_need),
            'Smith Waterman Accuracy': np.mean(similarity_scores_smith),
        }
        results.append(result_row)
    hasil = json.dumps(results)
    print(hasil)
    return pd.DataFrame(results)


# Define the list of input tokens
input_tokens = [
    "turn on the tea",
    "turn off the flight",
    "look the door",
    "unluck the door",
    "turn on the lump",
    "look the windows",
    "unluck the windows",
    "turn on the van",
    "turn off the van",
    "turn on the hater",
    "unable the hater",
    "disassemble the back door",
    "unluck the back door",
    "look the gate",
    "unluck the gate",
    "turn on the over",
    "turn off the over",
    "oven the gate",
    "clause the gate"
]

ground_truth_sentences = [
    "turn on the tv",
    "turn off the light",
    "lock the door",
    "unlock the door",
    "turn on the lamp",
    "lock the windows",
    "unlock the windows",
    "turn on the fan",
    "turn off the fan",
    "turn on the heater",
    "enable the heater",
    "disable the back door",
    "unlock the back door",
    "lock the gate",
    "unlock the gate",
    "turn on the oven",
    "turn off the oven",
    "open the gate",
    "close the gate"
]

# Define the algorithms to use
algorithms_to_use = [
    ('jaccard', jaccard.jakar),
    ('jaro', jaroDistance.jaro),
    ('cosine', cosine.cosine_similarity),
    ('damerau-levenshtein', damerauLevi.damerau_levenshtein_distance),
    ('dice', diceCoef.dice_coefficient),
    ('euclidien', euclidienDistance.euclidean_distance),
    ('hamming', hammingDistance.hamming_distance),
    ('jaro-winkler', jaroWinkler.jaro_winkler_similarity),
    ('levenshtein', levenshteinD.levenshtein_distance),
    ('longest', longestCommon.longest_common_subsequence),
    ('manhattan', manhattan.manhattan_distance),
    ('needleman', needlemanWunsch.needleman_wunsch),
    ('smith', smithWaterman.smith_waterman)
]


def exampleCode():

    # Create a DataFrame from the list of input tokens
    df_input = pd.DataFrame(input_tokens, columns=['Input'])
    df_output = pd.DataFrame(ground_truth_sentences, columns=['Original'])

    # Define the dictionary of correct words
    # dictionary = ["on", "off", "fan", "tv", "television",
    #               "PC", "lamp", "turn", "unlock", "lock", "gate", "light", "windows", "back door", "oven", "open", "close", "enable", "disable"]

    # Process the DataFrame with the provided input tokens
    df_results = process_input_dataframe(
        df_input, df_output)

    tabel = tabulate(df_results, headers='keys', tablefmt='grid')

    # Save the processed data to a CSV file
    output_csv_path_full = 'corrections.csv'
    df_results.to_csv(output_csv_path_full, index=False, header=True)
    df_results.to_excel('output.xlsx', index=False)
    # df_results.to_excel("koreksi.xlsx", index=None, header=True)
    # The path to the CSV file can be used to download or further process the file
    print(f"Results saved to {output_csv_path_full}")


# run example code
# exampleCode()


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
