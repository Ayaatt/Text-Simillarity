def dice_coefficient(a, b):
    """Calculate the Dice Coefficient between two strings."""
    if not a or not b:
        return 0.0

    # Convert strings to sets of characters
    a_bigrams = set(a)
    b_bigrams = set(b)
    print(f"a_diagram : {a_bigrams}")
    print(f"b_diagram : {b_bigrams}")

    # Find the intersection of the two sets
    overlap = len(a_bigrams & b_bigrams)
    print(f"overlap : {overlap}")

    # Calculate Dice's Coefficient
    return 2.0 * overlap / (len(a_bigrams) + len(b_bigrams))


# Example usage
string1 = "night"
string2 = "nigkt"

coefficient = dice_coefficient(string1, string2)
print("Dice's Coefficient:", coefficient)
