import math
from collections import Counter


def text_to_vector(text):
    # Mengonversi teks menjadi vektor frekuensi kata
    word_counts = Counter(text.split())
    print(f"word counter : {word_counts}")
    return word_counts


def euclidean_distance(vec1, vec2):
    # Gabungkan semua kata dari kedua vektor
    all_words = set(vec1.keys()) | set(vec2.keys())
    print(f"all words : {all_words}")

    # Hitung jarak Euclidean
    return math.sqrt(sum((vec1.get(word, 0) - vec2.get(word, 0)) ** 2 for word in all_words))


# Contoh penggunaan
text1 = "I enjoy reading about artificial intelligence"
text2 = "I enjoy listening about artificial intelligence"

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)
print(f"Vektor 1 : {vector1}")
print(f"Vektor 1 : {vector2}")

distance = euclidean_distance(vector1, vector2)
print("Euclidean Distance:", distance)
