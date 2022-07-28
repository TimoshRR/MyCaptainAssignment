#Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.
def most_frequent(string):
    dictio = dict()
    for key in string:
        if key not in dictio:
            dictio[key] = 1
        else:
            dictio[key] += 1
    return dictio

string = input("Please enter a string: ")
print(most_frequent(string))
