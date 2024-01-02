import math


def jakar(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    # Menghitung irisan dan gabungan karakter
    intersection = set1.intersection(set2)
    union = set1.union(set2)

    # Menghitung skor Jaccard
    if not union:
        return 0
    return len(intersection) / len(union)


# benar = ["tv", "on", "lamp", "turn"]
# kalimat = input("Masukkan kalimat : ")
# berkata = kalimat.split()
# similarity_threshold = 0.5
# kalimat_benar = []

# print(type(berkata))


def jaccard_similarity(user, dicti, similarity_threshold=0.2):
    tokens = user.lower().split()
    kalimat_benar = []
    for kata in tokens:
        # kata_set = set(kata)
        # kondisi = False
        if kata in [".", ",", "!", "?", ":", ";", "the"]:
            kalimat_benar.append(kata)
            continue
        best_match = max(
            dicti, key=lambda dict_word: jakar(kata, dict_word))
        kalimat_benar.append(best_match)

    # Menggabungkan token yang telah dikoreksi
    return ' '.join(kalimat_benar)


# dictionary = ["on", "off", "fan", "tv", "television", "pc", "lamp", "turn"]
# original_query = "trun no the lamb"
# corrected_query = jaccard_similarity(original_query, dictionary)
# print(f"Corrected Query: {corrected_query}")
#     for benar_kata in dicti:
#         benar_set = set(benar_kata)
#         similarity = jakar(kata_set, benar_set)
#         if similarity > similarity_threshold:
#             kalimat_benar.append(benar_kata)
#             kondisi = True
#             print("Hasil kesamaan Jaccard antara kalimat input '" + kata +
#                   "' dan kalimat benar '" + benar_kata + "' adalah " + str(similarity))
#             print(f" kata_set : {kata}")
#             print(f" benar_kata : {benar_kata}")

#     if not kondisi:
#         kalimat_benar.append(kata)

# kalimatnya = ' '.join(kalimat_benar)
# print(f" CORRECT JACCARD : {kalimatnya}")


# jaccard_similarity(berkata, benar)
