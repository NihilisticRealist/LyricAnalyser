import matplotlib.pyplot as plt

words = {}

#    EDIT THIS LINE FOR OTHER FILES
with open("inMind.txt", "r") as song:

    for lyric in song:
        for word in lyric.lower().split(" "):
            word = word.strip("\n").strip(",").strip(".").strip(";").strip(":").strip("?").strip("!").strip("'").strip('"')
            if word not in words:
                words[word] = 1

            else:
                words[word] = words[word] + 1

plt.bar(sorted(words, key=words.__getitem__, reverse=True), sorted(words.values(), reverse=True), 1, color='b'); plt.show()