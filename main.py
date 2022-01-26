################################################################################
# VARIABLES                                                                    #
################################################################################

string_array = ["found", "array", "sting", "young", "pr0xy"]


################################################################################
# RECORD_FREQUENCY                                                             #
# Purpose: Intake an array of strings, record frequency of letters             #
################################################################################

def record_frequency(intake_string_array):
    # Reset letter frequency variables
    letter_frequency = {'a' : 0, 'b' : 0, 'c' : 0,
                        'd' : 0, 'e' : 0, 'f' : 0,
                        'g' : 0, 'h' : 0, 'i' : 0,
                        'j' : 0, 'k' : 0, 'l' : 0,
                        'm' : 0, 'n' : 0, 'o' : 0,
                        'p' : 0, 'q' : 0, 'r' : 0,
                        's' : 0, 't' : 0, 'u' : 0,
                        'v' : 0, 'w' : 0, 'x' : 0,
                        'y' : 0, 'z' : 0, 'not_a_letter' : []}

    # Iterate through the array and increment letter frequency variables
    #   by letter appearance.
    for word in intake_string_array:
        for letter in word:
            if (letter in letter_frequency.keys()):
                letter_frequency[letter] += 1
            else:
                letter_frequency['not_a_letter'].append(letter)

    # Send raw info to the output handler function.
    output_handler(letter_frequency)


################################################################################
# OUTPUT_HANDLER                                                               #
# Purpose: Intake raw values of letter appearances, output semantic summary.   #
################################################################################

def output_handler(info_raw):
    letters = info_raw.keys()
    letters_not_present = []

    # Iterate through the raw output.
    for letter in letters:
        # Check if the letter has a value attached (excludes 'not_a_letter').
        if (isinstance(info_raw[letter], int)):
            # Print a statement if the letter appeared at least once.
            if (info_raw[letter] > 0):
                print("The letter " + letter + " appeared " + str(info_raw[letter]) + " times.")
            # Add all letters that did not appear to the empty list.
            else:
                letters_not_present.append(letter)

    # Print the list of letters that did not appear, concatonated as a string.
    print("The letters " + ", ".join(letters_not_present) + " did not appear.")

    # Check if there were any non-letters, and if so, concatonate and print.
    if (info_raw['not_a_letter']):
        print("Characters " + ", ".join(info_raw['not_a_letter']) + " detected.")


################################################################################
# FUNCTION CALLING                                                             #
################################################################################

# Call the function
record_frequency(string_array)
# Wait for input to close the command line
input(" ")
