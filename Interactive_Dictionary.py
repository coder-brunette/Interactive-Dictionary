import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
	w = w.lower()
	if w in data:
		return data[w]
	elif len(get_close_matches(w, data.keys()))>0:
		inp = input("Did you mean %s instead? Press Y for Yes or N for No: " %get_close_matches(w, data.keys())[0])
		if inp == "Y":
			return data(get_close_matches(w, data.keys())[0])
		elif inp == "N":
			return "The word doesn't exist. Please double check it!"
		else:
			return "We didn't understand your entry."
	else:
		return "The word doesnt exist. Please double check it!"

word = input("Enter word: ")
print(translate(word))

