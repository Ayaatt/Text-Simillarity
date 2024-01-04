def levenshtein(str1, str2):
    # Membuat matriks ukuran (len(str1)+1) x (len(str2)+1)
    matrix = [[0 for n in range(len(str2) + 1)] for m in range(len(str1) + 1)]
    # print(f"matrix : {matrix}")

    # Menginisialisasi matriks
    for i in range(len(str1) + 1):
        matrix[i][0] = i
    for j in range(len(str2) + 1):
        matrix[0][j] = j

    # Mengisi matriks
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,      # Deletion
                               matrix[i][j - 1] + 1,      # Insertion
                               matrix[i - 1][j - 1] + cost)  # Substitution

    print(f"matrix : {matrix[-1][-1]}")
    return matrix[-1][-1]


def tokenize(query):
    return query.lower().split()


benar = ["turn", "on", "tv"]
kalimat = input("Masukkan kalimat : ")
berkata = tokenize(kalimat)
similarity_threshold = 0.5


def levenshtein_distance(user, dicti):
    kalimat_benar = []
    skor = []
    for kata in user:
        # kata_set = set(kata)
        # kondisi = False
        if kata in [".", ",", "!", "?", ":", ";", "the"]:
            kalimat_benar.append(kata)
            continue
        for d in dicti:
            sim = levenshtein(kata, d)
            print(sim)
        # best_match = max(
        #     dicti, key=lambda dict_word: levenshtein(kata, dict_word))
        # kalimat_benar.append(best_match)
        kalimat_benar.append(d)
        skor.append(sim)

    sentence = ' '.join(kalimat_benar)
    # Menggabungkan token yang telah dikoreksi
    print(sentence)
    print(skor)
    return ' '.join(kalimat_benar)


levenshtein_distance(berkata, benar)

# # Contoh penggunaan
# distance = levenshtein("on", "on")
# print("Levenshtein Distance:", distance)
