import json
from difflib import get_close_matches

data = json.load(open("data.json", mode="r", encoding="utf-8"))


def word_definition(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) >0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "This word doesn't exist in our dictionary. Please double check the spelling"
        else:
            return "Please enter 'Y' or 'N' the next time to confirm."
    else:
        return "This word doesn't exist in our dictionary. Please double check the spelling."

word = input("Enter a word: ")

output_message = word_definition(word)

if isinstance(output_message, list):
    for i in output_message:
        print(i)
else:
    print(output_message)
