import math


def cocok(words):
    return set(words)


def jakar(set_a, set_b):
    intersection = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    return intersection / union if union != 0 else 0.0


benar = ["tolong", "matikan", "lampu"]
kalimat = input("Masukkan kalimat : ")
berkata = kalimat.split()
similarity_threshold = 0.5
kalimat_benar = []

print(type(berkata))

for kata in berkata:
    kata_set = set(kata)
    kondisi = False
    for benar_kata in benar:
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

kalimatnya = ' '.join(kalimat_benar)
print(f" HASILNYA : {kalimatnya}")
print(berkata)
