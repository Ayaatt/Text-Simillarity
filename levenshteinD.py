def levenshtein_distance(str1, str2):
    # Membuat matriks ukuran (len(str1)+1) x (len(str2)+1)
    matrix = [[0 for n in range(len(str2) + 1)] for m in range(len(str1) + 1)]
    print(f"matrix : {matrix}")

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

    print(f"matrix : {matrix}")
    return matrix[-1][-1]


# Contoh penggunaan
distance = levenshtein_distance("rat", "cat")
print("Levenshtein Distance:", distance)
