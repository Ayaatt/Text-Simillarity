import math
from collections import Counter


def text_to_vector(text):
    words = text.split()
    return Counter(words)


def cosine_similarity(vektor1, vektor2):
    # Menghitung dot product antara dua vektor

    vec1 = text_to_vector(vektor1)
    vec2 = text_to_vector(vektor2)

    intersection = set(vec1.keys()) & set(vec2.keys())
    dot_product = sum([vec1[x] * vec2[x] for x in intersection])
    # print(f"intersection : {intersection}")
    # print(f"dot product : {dot_product}")

    # Menghitung magnitude masing-masing vektor
    magnitude1 = math.sqrt(sum([val**2 for val in vec1.values()]))
    magnitude2 = math.sqrt(sum([val**2 for val in vec2.values()]))
    # print(f"Magnitude 1 : {magnitude1}")
    # print(f"Magnitude 2 : {magnitude2}")

    # Menghitung dan mengembalikan kesamaan kosinus
    if not magnitude1 or not magnitude2:
        return 0
    else:
        return dot_product / (magnitude1 * magnitude2)


# # # Contoh penggunaan
# text1 = "intelligence"
# text2 = "imtekligemce"

# # vector1 = text_to_vector(text1)
# # vector2 = text_to_vector(text2)
# # print(f"Vektor 1 : {vector1}")
# # print(f"Vektor 1 : {vector2}")


# similarity = cosine_similarity(text1, text2)
# print("Cosine Similarity:", similarity)
