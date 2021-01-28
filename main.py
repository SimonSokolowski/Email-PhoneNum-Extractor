import re

textToSearch = input("Please enter a text with phone numbers (in any format) and I will "
                     "find the numbers for you.\nType 'sample' for a sample to be entered for you. \n")

beginSearch = input("Press any key when ready\n")

if textToSearch == "sample":
    textToSearch = "This is the sample text, which includes a range of formats: \n" \
                   "Call me tomorrow morning on my number (44) 75034 052223, or on my home \n" \
                   "number +4407302-041656. Also try my wife's number, 07363 136412. \n"

    print(textToSearch)

phoneNumRegex = re.compile(r"\+?\S?\S?\d{5}\D?\D\D?\d{6}\S?|\S?\+?\D?\d{2}\D?\D\D?\d{5}\D?\D\D?\d{6}\S?")
matchObject = phoneNumRegex.findall(textToSearch)

print("The numbers I managed to find are: " + str(matchObject))