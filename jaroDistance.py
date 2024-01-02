def jaro(s, t):
    s_len = len(s)
    t_len = len(t)
    # print(f"type s_len : {type(t_len)}")
    # print(f"type t_len : {type(t_len)}")

    if s_len == 0 and t_len == 0:
        return 1.0

    match_distance = max(s_len, t_len) // 2 - 1
    s_matches = [False] * s_len
    t_matches = [False] * t_len
    matches = 0
    transpositions = 0
    # print(f"s_len : {s_len}")
    # print(f"t_len : {t_len}")

    # print(f"s_matches : {s_matches}")
    # print(f"t_matches : {t_matches}")

    for i in range(s_len):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, t_len)

        for j in range(start, end):
            if t_matches[j]:
                continue
            if s[i] != t[j]:
                continue
            s_matches[i] = True
            t_matches[j] = True
            matches += 1
            break

    if matches == 0:
        return 0.0

    k = 0
    for i in range(s_len):
        if not s_matches[i]:
            continue
        while not t_matches[k]:
            k += 1
        if s[i] != t[k]:
            transpositions += 1
        k += 1

    return ((matches / s_len) +
            (matches / t_len) +
            ((matches - transpositions // 2) / matches)) / 3


# benar = ["tv", "on", "lamp", "turn"]
# kalimat = input("Masukkan kalimat : ")
# berkata = kalimat.split()


def jaro_distance(user, dicti, similarity_threshold=0.2):
    kalimat_benar = []
    for kata in user:
        kata_set = set(kata)
        kondisi = False
        if kata in [".", ",", "!", "?", ":", ";", "the"]:
            kalimat_benar.append(kata)
            continue
        for benar_kata in dicti:
            benar_set = set(benar_kata)
            similarity = jaro(str(kata_set), str(benar_set))
            if similarity > similarity_threshold:
                kalimat_benar.append(benar_kata)
                kondisi = True
                print("Hasil kesamaan Jaccard antara kalimat input '" + kata +
                      "' dan kalimat benar '" + benar_kata + "' adalah " + str(similarity))
                print(f" kata_set : {kata}")
                print(f" benar_kata : {benar_kata}")

        if not kondisi:
            kalimat_benar.append(kata)

    # kalimatnya = ' '.join(kalimat_benar)
    # print(f" CORRECT JACCARD : {kalimatnya}")


# jaro_distance(berkata, benar)

# # Contoh penggunaan
# benar = ["tv", "on", "lamp", "turn"]
# kalimat = input("Masukkan kalimat : ")
# berkata = kalimat.split()
# similarity_threshold = 0.5
# kalimat_benar = []

# # print(type(berkata))
# distance = jaro_distance(berkata, )
# print("Jaro Distance:", distance)
