import math
import speech_recognition as sr
import pyttsx3
import time
import nltk
from os import path

# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "aud.wav")
audio_file_path = "new_indo.wav"
bicara = sr.Recognizer()

with sr.AudioFile(audio_file_path) as source:
    audio = bicara.record(source, duration=6)  # read the entire audio file
    teks = bicara.recognize_google(audio, language="id").lower()
    print(f"HASILNYA : {teks}")


# def cocok(perKata):
#     array_of_words = (list(kata) for kata in perKata)
#     for hasil in array_of_words:
#         return hasil

def cocok(words):
    return set(words)


# def jakar(a, b):
#     intersection = len(list(set(a).intersection(b)))
#     union = (len(a) + len(b)) - intersection
#     print(type(intersection))
#     print(type(union))
#     return intersection / union

def jakar(set_a, set_b):
    # Assume jakar() is a function that calculates Jaccard Similarity
    intersection = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    return intersection / union if union != 0 else 0.0


benar = ["tolong", "matikan", "lampu"]
# kalimat = input("Masukkan kalimat : ")
# teks.lower()
berkata = teks.split()
similarity_threshold = 0.5
kalimat_benar = []

# berkata_sets = [set(word) for word in berkata]
# benar_sets = [set(word) for word in benar]

print(type(berkata))

for kata in berkata:
    kata_set = set(kata)
    kondisi = False
    for benar_kata in benar:
        benar_set = set(benar_kata)
        similarity = jakar(kata_set, benar_set)
        if similarity > similarity_threshold:
            kalimat_benar.append(benar_kata)
            kondisi = True
            print("Hasil kesamaan Jaccard antara kalimat input '" + kata +
                  "' dan kalimat benar '" + benar_kata + "' adalah " + str(similarity))
            print(f" kata_set : {kata_set}")
            print(f" benar_kata : {benar_kata}")
            break

    if not kondisi:
        kalimat_benar.append(kata)
        # print(f" HASILNYA : {kalimat_benar}")
# for i, berkata_set in enumerate(berkata_sets):
#     for j, benar_set in enumerate(benar_sets):
#         similarity = jakar(berkata_set, benar_set)
#         print(
#             f"Jaccard similarity between '{berkata[i]}' and '{benar[j]}' is {similarity}")
kalimatnya = ' '.join(kalimat_benar)
print(f" HASILNYA : {kalimatnya}")
print(berkata)

# while True:
#     try:
#         with sr.Microphone() as mic:
#             bicara.adjust_for_ambient_noise(mic, duration=0.2)
#             audio = bicara.listen(mic)
#             teks = bicara.recognize_google(audio)

#             print(f"HASILNYA : {teks}")

#     except:
#         bicara = sr.Recognizer()
#         continue
