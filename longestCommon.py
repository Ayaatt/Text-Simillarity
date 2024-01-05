def longest_common_subsequence(X, Y):
    # Find the length of the strings
    m = len(X)
    n = len(Y)

    # Declare the array for storing the dp values
    L = [[0]*(n+1) for i in range(m+1)]

    # Building the matrix in bottom-up way
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # The length of the LCS is the final value in the matrix
    return L[m][n]

# def longest_common_subsequence(X, Y):
#     # Find the length of the strings
#     m = len(X)
#     n = len(Y)

#     # Declare the array for storing the dp values
#     L = [[0]*(n+1) for i in range(m+1)]

#     # Building the matrix in bottom-up way
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if X[i - 1] == Y[j - 1]:
#                 L[i][j] = L[i - 1][j - 1] + 1
#             else:
#                 L[i][j] = max(L[i - 1][j], L[i][j - 1])

#     # Following code is used to print LCS
#     index = L[m][n]

#     # Create a character array to store the lcs string
#     lcs = [""] * (index + 1)
#     lcs[index] = ""

#     # Start from the right-most-bottom-most corner and
#     # one by one store characters in lcs[]
#     i = m
#     j = n
#     while i > 0 and j > 0:

#         # If current character in X[] and Y are same, then
#         # current character is part of LCS
#         if X[i-1] == Y[j-1]:
#             lcs[index-1] = X[i-1]
#             i -= 1
#             j -= 1
#             index -= 1

#         # If not same, then find the larger of two and
#         # go in the direction of larger value
#         elif L[i-1][j] > L[i][j-1]:
#             i -= 1
#         else:
#             j -= 1

#     return "".join(lcs)


# Example usage
# X = "AGGTAB"
# Y = "GXTXAYB"
# lcs = longest_common_subsequence(X, Y)
# print("Longest Common Subsequence:", lcs)
