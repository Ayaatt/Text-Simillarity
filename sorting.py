
def tokenize(query):
    return set(query.lower().split())


user_query = input("Masukkan Kalimat : ")

benar = ["satu", "dua", "tiga", "empat", "lima"]
# banding = ["enam", "tujuh", "delapan", "empat", "lima"]
tokens = tokenize(user_query)
print(tokens)
terbaru = []

for token in tokens:
    # print(f"token : {token}")
    if token in [".", ",", "!", "?", ":", ";", "the"]:
        terbaru.append(token)
        continue
        # print(f"listnya : {lst}")
    for benar_kata in benar:
        # benar_set = set(benar_kata)
        if token != benar_kata:
            break
        terbaru.append(benar_kata)
print(f"terbaru : {terbaru}")
