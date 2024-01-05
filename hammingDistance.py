def hamming_distance(str1, str2):
    # Menghitung Hamming Distance antara dua string
    if len(str1) != len(str2):
        distance = 0

    distance = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            distance += 1
    return distance


# # Contoh penggunaan
# distance = hamming_distance("karat", "karetnya")
# print("Hamming Distance:", distance)
