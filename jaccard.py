import math


# def cocok(perKata):
#     array_of_words = (list(kata) for kata in perKata)
#     for hasil in array_of_words:
#         return hasil

def cocok(words):
    return set(words)


# def jakar(a, b):
#     intersection = len(list(set(a).intersection(b)))
#     union = (len(a) + len(b)) - intersection
#     print(type(intersection))
#     print(type(union))
#     return intersection / union

def jakar(set_a, set_b):
    # Assume jakar() is a function that calculates Jaccard Similarity
    intersection = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    return intersection / union if union != 0 else 0.0


benar = ["tolong", "matikan", "lampu"]
kalimat = input("Masukkan kalimat : ")
berkata = kalimat.split()
similarity_threshold = 0.5
kalimat_benar = []

# berkata_sets = [set(word) for word in berkata]
# benar_sets = [set(word) for word in benar]

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
        # print(f" HASILNYA : {kalimat_benar}")
# for i, berkata_set in enumerate(berkata_sets):
#     for j, benar_set in enumerate(benar_sets):
#         similarity = jakar(berkata_set, benar_set)
#         print(
#             f"Jaccard similarity between '{berkata[i]}' and '{benar[j]}' is {similarity}")
kalimatnya = ' '.join(kalimat_benar)
print(f" HASILNYA : {kalimatnya}")
print(berkata)
# print(f" kata_set : {kata_set}")
# print(f" benar_kata : {benar_kata}")

# set_berkata = cocok(berkata)
# set_benar = cocok(benar)

# x = 0  # Initialize x to 0
# x += 1  # Increment x

# if kalimat and x < len(benar):
#     similarity = jakar(benar.index[x], berkata)
#     distance = 1 - similarity
#     print("Jaccard Similarity:", similarity)
#     print("Jaccard Distance:", distance)

# if kalimat and x < len(benar):
#     similarity = jakar(set_benar, set_berkata)
#     distance = 1 - similarity
#     print("Jaccard Similarity:", similarity)
#     print("Jaccard Distance:", distance)
# else:
#     print("Invalid index or empty input")
