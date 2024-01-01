import math


def jakar(set_a, set_b):
    # Assume jakar() is a function that calculates Jaccard Similarity
    intersection = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    return intersection / union if union != 0 else 0.0


# benar = ["tv", "on", "lamp"]
# kalimat = input("Masukkan kalimat : ")
# berkata = kalimat.split()
# # similarity_threshold = 0.5
# # kalimat_benar = []

# print(type(berkata))


def jekar(user, dict):
    similarity_threshold = 0.0
    kalimat_benar = []
    for kata in user:
        kata_set = set(kata)
        kondisi = False
        for benar_kata in dict:
            benar_set = set(benar_kata)
            similarity = jakar(kata_set, benar_set)
            if similarity > similarity_threshold:
                kalimat_benar.append(benar_kata)
                kondisi = True
                print("Hasil kesamaan Jaccard antara kalimat input '" + kata +
                      "' dan kalimat benar '" + benar_kata + "' adalah " + str(similarity))
                print(f" kata_set : {kata_set}")
                print(f" benar_kata : {benar_kata}")
                break

        if not kondisi:
            kalimat_benar.append(kata)


# jekar(berkata, benar)
