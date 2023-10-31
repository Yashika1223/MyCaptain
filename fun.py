def most_frequent(in_string):
    #initialize an empty dictionary
    letter_count = {}

    #convert the input string to lowercase
    in_string = in_string.replace(" ", "").lower()

    #count the frequency of each letter in the string
    for letter in in_string:
        if letter.isalpha(): 
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    #sort the dictionary by the values in decreasing order
    sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

    #print the letters and their frequencies
    for letter, count in sorted_letter_count:
        print(f"{letter} = {count:02d}", end=" ")


in_string = "Mississippi"
most_frequent(in_string)
