import math
from collections import Counter


def text_to_vector(text):
    # Mengonversi teks menjadi vektor frekuensi kata
    word_counts = Counter(text.split())
    print(f"word counter : {word_counts}")
    return word_counts


def manhattan_distance(vec1, vec2):
    # Gabungkan semua kata dari kedua vektor
    all_words = set(vec1.keys()) | set(vec2.keys())
    print(f"all words : {all_words}")

    # Hitung jarak Euclidean
    return sum(abs(vec1.get(word, 0) - vec2.get(word, 0)) for word in all_words)


# # Contoh penggunaan
# text1 = "aku adalah pengangguran akut"
# text2 = "aku ini pengangguran akut"

# vector1 = text_to_vector(text1)
# vector2 = text_to_vector(text2)
# print(f"Vektor 1 : {vector1}")
# print(f"Vektor 1 : {vector2}")

# distance = manhattan_distance(vector1, vector2)
# print("Manhattan Distance:", distance)
