def needleman_wunsch(seq1, seq2, match_score=1, gap_cost=-1, mismatch_cost=-1):
    # Initialize the matrix with zeros
    m, n = len(seq1), len(seq2)
    score_matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        score_matrix[i][0] = i * gap_cost
    for j in range(n + 1):
        score_matrix[0][j] = j * gap_cost

    # Fill in the score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                match = score_matrix[i - 1][j - 1] + match_score
            else:
                match = score_matrix[i - 1][j - 1] + mismatch_cost

            delete = score_matrix[i - 1][j] + gap_cost
            insert = score_matrix[i][j - 1] + gap_cost

            score_matrix[i][j] = max(match, delete, insert)

    return score_matrix[-1][-1]  # Return the final score


# Test the function
seq1 = "mau"
seq2 = "mia"
alignment_score = needleman_wunsch(seq1, seq2)
print("Alignment Score:", alignment_score)
