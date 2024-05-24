subjects = ["I","YOU"]
verbs = ["Play","Love"]
objects = ["Cricket","Ludo"]

#FUNCTION TO GENERATE SENTENCE
def generate_sentences():
    sentences = []
    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                sentence = f"{subject}{verb}{obj}."
                sentences.append(sentence)
    return sentences

#GENERATE AND PRINT SENTENCES
all_sentences = generate_sentences()
for sentence in all_sentences:
    print(sentence)
