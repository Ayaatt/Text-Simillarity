def smith_waterman(seq1, seq2, match_score=3, gap_cost=2):
    # Initialize the scoring matrix
    m, n = len(seq1), len(seq2)
    score_matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    max_score = 0

    # Calculate scores for each position in the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                # If the characters match
                diagonal_score = score_matrix[i - 1][j - 1] + match_score
            else:
                # If the characters don't match
                diagonal_score = score_matrix[i - 1][j - 1] - gap_cost

            # Calculate the possible scores for a given position
            up_score = score_matrix[i - 1][j] - gap_cost
            left_score = score_matrix[i][j - 1] - gap_cost

            # Take the maximum
            score_matrix[i][j] = max(0, diagonal_score, up_score, left_score)

            # Update the max score found so far
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]

    return max_score


# Example usage
seq1 = "AGCACACA"
seq2 = "ACACACTA"
alignment_score = smith_waterman(seq1, seq2)
print("Smith-Waterman Alignment Score:", alignment_score)
