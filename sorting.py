
def tokenize(query):
    return query.lower().split()


# user_query = input("Masukkan Kalimat : ")

input_tokens = [
    "turn on the tea",
    "turn off the flight",
    "look the door",
    "unluck the door",
    "turn on the lump",
    "look the windows",
    "unluck the windows",
    "turn on the van",
    "turn off the van",
    "turn on the hater",
    "unable the hater",
    "disassemble the back door",
    "unluck the back door",
    "look the gate",
    "unluck the gate",
    "turn on the over",
    "turn off the over",
    "oven the gate",
    "clause the gate"
]

ground_truth_sentences = [
    "turn on the tv",
    "turn off the light",
    "lock the door",
    "unlock the door",
    "turn on the lamp",
    "lock the windows",
    "unlock the windows",
    "turn on the fan",
    "turn off the fan",
    "turn on the heater",
    "enable the heater",
    "disable the back door",
    "unlock the back door",
    "lock the gate",
    "unlock the gate",
    "turn on the oven",
    "turn off the oven",
    "open the gate",
    "close the gate"
]

tokens_benar = tokenize(input_tokens)
tokens_banding = tokenize(ground_truth_sentences)
print(tokens_banding)
terbaru = []

for token in tokens_banding:
    # print(f"token : {token}")
    if token in [".", ",", "!", "?", ":", ";", "the"]:
        terbaru.append(token)
        continue
        # print(f"listnya : {lst}")
    for benar_kata in tokens_benar:
        # benar_set = set(benar_kata)
        # if token != benar_kata:
        #     break
        terbaru.append(benar_kata)
print(f"terbaru : {terbaru}")
