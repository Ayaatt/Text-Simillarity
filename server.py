from flask import Flask, request, render_template_string, jsonify, abort
from datetime import datetime
import os
import time
import requests
import main

app = Flask(__name__)

dictionary = ["on", "off", "fan", "tv", "television",
              "PC", "lamp", "turn", "unlock", "lock", "gate", "light", "windows", "back door", "oven", "open", "close", "enable", "disable"]


@app.route('/corrected_string/<algorithm>', methods=['POST'])
def user(algorithm):
    start_time = time.time()
    fungsi_algoritma = main.find_algorithm(algorithm)
    # print(fungsi_algoritma)
    body = request.get_json()
    tokens = main.tokenize(body['input'])
    print(tokens)
    corrected_tokens = []
    for token in tokens:
        similarity_scores = []
        if token in [".", ",", "!", "?", ":", ";", "the"]:
            corrected_tokens.append(token)
            continue

        if algorithm in ["jaro", "damerau-levenshtein", "levenshtein", "jaro-winkler", "manhattan", "euclidien"]:
            isDistance = True
        else:
            isDistance = False

        best_match, best_similarity = main.best_match_and_score(
            fungsi_algoritma, token, dictionary, is_distance_metric=isDistance)
        print(
            f"token : {token} || dict : {dictionary} || best_match : {best_match} || best_similarity : {best_similarity}")
        # print(token, "  ", best_match)
        similarity_scores.append(best_similarity)
        corrected_tokens.append(best_match)
        # similarity_scores.append(best_similarity)

    corrected_sentence = ' '.join(corrected_tokens)

    total_time = (time.time() - start_time)
    return jsonify({"output": corrected_sentence, "time": total_time, "score": main.np.mean(similarity_scores)}), 200


@app.route('/get_supported_algorithm', methods=['GET'])
def get_supported_algorithm():
    algorithm_used = [
        'jaccard',
        'jaro',
        'cosine',
        'damerau-levenshtein',
        'dice',
        'euclidien',
        'hamming',
        'jaro-winkler',
        'levenshtein',
        'longest',
        'manhattan',
        'needleman',
        'smith'
    ]
    data = main.json.dumps(algorithm_used)
    return data


if __name__ == '__main__':
    app.run(port=1000)
