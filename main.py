import pyperclip, re

textToSearch = input("Please enter a text with phone numbers and/or emails (in any format) and I will "
                     "find them for you.\nType 'sample' for a sample to be entered for you. \n")
if textToSearch == "sample":
    textToSearch = "This is the sample text, which includes a range of formats: \n" \
                   "Call me tomorrow morning on my number +(44) 7503 452223, or on my home \n" \
                   "number +447302-041656. Also try my wife's number, 07363 136412. \n" \
                   "Here are some emails: cliffordchi@domain.com, example1234@yahoo.ac.uk\n"

    print(textToSearch)

else:
    textToSearch = str(pyperclip.paste())

phoneNumRegex = re.compile(r'''(
    (\S?\+?\D?)                       #seperator
    (\d{2})?                          #country code
    (\D?\D?\D?)                       #seperator
    (\d{5} | \d{4})                   #or first 4 digits
    (\D?\D\D?)                        #seperator
    (\d{6})                           #last 6 digits
    (\S?)                             #seperator
    )''', re.VERBOSE)
findPhoneNumResult = phoneNumRegex.findall(textToSearch)

emailRegex = re.compile(r'''(
    [0-9a-zA-Z.]+                     #username
    @
    [a-zA-Z]+                         #domain name
    \.
    ([a-zA-Z.]{2,5})                  #.com/.co.uk etc
    )''', re.VERBOSE)
findEmailResult = emailRegex.findall(textToSearch)

matchedEmailsOrPhoneNums = []

for groups in findPhoneNumResult:
    if groups[2] != "":
        phoneNum = "+" + groups[2] + " " + "-".join([groups[4], groups[6]])
    else:
        phoneNum = "    " + "-".join([groups[4], groups[6]])
    matchedEmailsOrPhoneNums.append(phoneNum)

for groups in findEmailResult:
    matchedEmailsOrPhoneNums.append(groups[0])

if len(matchedEmailsOrPhoneNums) > 0:
    pyperclip.copy("\n".join(matchedEmailsOrPhoneNums))
    print("Copied to clipboard:")
    print("\n".join(matchedEmailsOrPhoneNums))
else:
    print("No phone numbers or email addresses found.")