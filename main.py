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
    current_value = 0

    # Create a temporary list and push all letters with current_value to it,
    #   while also removing them from info_raw. Print a statement with that
    #   list of letters, increment current_value, and repeat until we've
    #   checked all letters.
    while len(info_raw) > 1:
        templist = []
        for value in list(letters):
            if (info_raw[value] == current_value):
                templist.append(value)
                info_raw.pop(value)

        print(output_intro(templist) + output_outro(current_value))
        current_value += 1

    # Check if there were any non-letters, and if so, concatonate and print.
    if (info_raw['not_a_letter']):
        print("\nNon-letter characters '" +
          "', '".join(info_raw['not_a_letter']) + "' detected.")

################################################################################
# OUPUT_INTRO                                                                  #
# Purpose: prevent "The letterS [one letter] ", and to add 'and' if necessary. #
################################################################################
def output_intro(input):
    if (len(input) > 1):
        last_item = input[-1]
        input.pop()
        string = "The letters " + ", ".join(input) +", and " + last_item
    else:
        string = "The letter " + input
    return string

################################################################################
# OUTPUT_OUTRO                                                                 #
# Purpose: prevent "[letters] appeared 1 timeS".                   #
################################################################################
def output_outro(value):
    if (value == 1):
        string = " appeared 1 time."
    else:
        string = " appeared " + str(value) + " times."
    return string

################################################################################
# FUNCTION CALLING                                                             #
################################################################################

# Call the function
record_frequency(string_array)
# Wait for input to close the command line
input(" ")
