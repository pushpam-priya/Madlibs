# with open("story.txt", "r") as f:
#     story = f.read()
story = input("Write a story: ")
# print(story)

words = set()
startOfWord = -1

targetStart = "<"
targetEnd = ">"

for i, char  in enumerate(story):
    if char == targetStart:
        startOfWord = i

    if char == targetEnd and targetStart != -1:
        word = story[startOfWord: i + 1]
        words.add(word)
        startOfWord = -1

# print(words)

answers = {}
for word in words:
    answer = input("Enter a word for " + word + ":")
    answers[word] = answer

# print(answers)

for word in words:
    story = story.replace(word, answers[word])
print(story)