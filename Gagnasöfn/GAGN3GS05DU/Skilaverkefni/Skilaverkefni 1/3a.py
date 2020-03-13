oll_ord = {}
print("Sláðu inn streng\n---> ", end="")
inntöku_strengur = input()

for word in inntöku_strengur.split(" "):
    word = word.lower()
    try: oll_ord[word] += 1
    except KeyError: oll_ord[word] = 1

sorted_dict = {k: v for k, v in sorted(oll_ord.items(), key=lambda item: item[1], reverse=True)}

for word in sorted_dict:
    print(word+":", sorted_dict[word])