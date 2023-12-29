def jaro_distance(s1, s2):
    # Jika string sama, return 1
    if s1 == s2:
        return 1.0

    # Panjang string dan jarak pencarian
    len_s1, len_s2 = len(s1), len(s2)
    max_distance = int(max(len_s1, len_s2) / 2) - 1
    print(
        f"len_s1 : {len_s1} || len_s2 : {len_s2} || max distance : {max_distance}")

    # Menandai karakter yang sama di kedua string
    match_s1 = [False] * len_s1
    match_s2 = [False] * len_s2

    # Menghitung jumlah match dan transposisi
    matches, transpositions = 0, 0
    for i in range(len_s1):
        start, end = max(0, i - max_distance), min(i +
                                                   max_distance + 1, len_s2)
        for j in range(start, end):
            if match_s2[j]:
                continue
            if s1[i] != s2[j]:
                continue
            matches += 1
            match_s1[i] = True
            match_s2[j] = True
            break

    if matches == 0:
        return 0.0

    k = 0
    for i in range(len_s1):
        if not match_s1[i]:
            continue
        while not match_s2[k]:
            k += 1
        if s1[i] != s2[k]:
            transpositions += 1
        k += 1

    transpositions //= 2

    print(f"match s1 : {match_s1}")
    print(f"match s1 : {match_s2}")
    print(f"transposisi : {transpositions}")

    return (matches / len_s1 + matches / len_s2 + (matches - transpositions) / matches) / 3


# Contoh penggunaan
distance = jaro_distance("MSRTHA", "MARHTA")
print("Jaro Distance:", distance)
