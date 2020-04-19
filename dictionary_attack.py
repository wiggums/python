dictionary_file = open("github-words.txt", "r")
#print(dictionary_file)

for word in dictionary_file.readlines():
    print(word)
