def jaro_distance(s1, s2):
    if not s1 or not s2:
        return 0.0

    len_s1, len_s2 = len(s1), len(s2)
    match_distance = (max(len_s1, len_s2) // 2) - 1

    s1_matches = [False] * len_s1
    s2_matches = [False] * len_s2

    matches, transpositions = 0, 0
    for i in range(len_s1):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, len_s2)

        for j in range(start, end):
            if s2_matches[j]:
                continue
            if s1[i] != s2[j]:
                continue
            s1_matches[i] = s2_matches[j] = True
            matches += 1
            break

    if matches == 0:
        return 0.0

    j = 0
    for i in range(len_s1):
        if not s1_matches[i]:
            continue
        while not s2_matches[j]:
            j += 1
        if s1[i] != s2[j]:
            transpositions += 1
        j += 1

    transpositions /= 2

    return (matches / len_s1 + matches / len_s2 + (matches - transpositions) / matches) / 3


def jaro_winkler_similarity(s1, s2, prefix_scale=0.1):
    jaro_sim = jaro_distance(s1, s2)

    # Up to the first 4 characters, count how many are same in both strings
    common_prefix = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            break
        common_prefix += 1
    common_prefix = min(4, common_prefix)

    return jaro_sim + (common_prefix * prefix_scale * (1 - jaro_sim))


# Example usage
string1 = "MARTHA"
string2 = "MARHTA"
similarity = jaro_winkler_similarity(string1, string2)
print("Jaro-Winkler Similarity:", similarity)
