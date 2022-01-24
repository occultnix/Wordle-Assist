string_array = ["found", "array", "sting", "young", "proxy"]

# intake array of strings, record frequency of letters
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
    #   by letter appearance
    for word in intake_string_array:
        for letter in word:
            if (letter in letter_frequency.keys()):
                letter_frequency[letter] += 1
            else:
                letter_frequency['not_a_letter'].append(letter)

    # Send raw info to the output handler function
    output_handler(letter_frequency)

def output_handler(info_raw):
    # Print statements to semantically communicate letter appearances
    print("The letter A appeared " + str(info_raw['a']) + " times")
    print("The letter B appeared " + str(info_raw['b']) + " times")
    print("The letter C appeared " + str(info_raw['c']) + " times")
    print("The letter D appeared " + str(info_raw['d']) + " times")
    print("The letter E appeared " + str(info_raw['e']) + " times")
    print("The letter F appeared " + str(info_raw['f']) + " times")
    print("The letter G appeared " + str(info_raw['g']) + " times")
    print("The letter H appeared " + str(info_raw['h']) + " times")
    print("The letter I appeared " + str(info_raw['i']) + " times")
    print("The letter J appeared " + str(info_raw['j']) + " times")
    print("The letter K appeared " + str(info_raw['k']) + " times")
    print("The letter L appeared " + str(info_raw['l']) + " times")
    print("The letter M appeared " + str(info_raw['m']) + " times")
    print("The letter N appeared " + str(info_raw['n']) + " times")
    print("The letter O appeared " + str(info_raw['o']) + " times")
    print("The letter P appeared " + str(info_raw['p']) + " times")
    print("The letter Q appeared " + str(info_raw['q']) + " times")
    print("The letter R appeared " + str(info_raw['r']) + " times")
    print("The letter S appeared " + str(info_raw['s']) + " times")
    print("The letter T appeared " + str(info_raw['t']) + " times")
    print("The letter U appeared " + str(info_raw['u']) + " times")
    print("The letter V appeared " + str(info_raw['v']) + " times")
    print("The letter W appeared " + str(info_raw['w']) + " times")
    print("The letter X appeared " + str(info_raw['x']) + " times")
    print("The letter Y appeared " + str(info_raw['y']) + " times")
    print("The letter Z appeared " + str(info_raw['z']) + " times")
    print("The characters that were not letters were " + str(info_raw['not_a_letter']) + ".")

# Call the function
record_frequency(string_array)
# Wait for input to close the command line
input(" ")
