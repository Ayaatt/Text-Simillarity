import math


def cocok(words):
    return set(words)


def jakar(set_a, set_b):
    intersection = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    return intersection / union if union != 0 else 0.0


benar = ["tolong", "matikan", "lampu", "cook", "antique"]
kalimat = input("Masukkan kalimat : ")
berkata = kalimat.split()
# similarity_threshold = 0.5
kalimat_benar = []

print(type(berkata))

for kata in berkata:
    # kata_set = set(kata)
    kondisi = False
    kata_set = set(kata)
    highest_similarity = 0.0
    most_similar_word = kata  # Default to the original word
    for benar_kata in benar:
        benar_set = set(benar_kata)
        similarity = jakar(kata_set, benar_set)
        # if similarity >= similarity_threshold:

        if similarity > highest_similarity:
            kondisi = True
            highest_similarity = similarity
            most_similar_word = benar_kata
            print("Hasil kesamaan Jaccard antara kalimat input '" + kata +
                  "' dan kalimat benar '" + most_similar_word + "' adalah " + str(similarity))
            print(f" kata_set : {kata_set}")
            print(f" benar_kata : {benar_kata}")

    kalimat_benar.append(most_similar_word)

    if not kondisi:
        kalimat_benar.append(kata)

kalimatnya = ' '.join(kalimat_benar)
print(f" HASILNYA : {kalimatnya}")
print(berkata)
