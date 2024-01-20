
def make_sentence(stack):

    numberToEnglish = {'1':'One',
               '2':'Two',
               '3':'Three',
               '4':'Four',
               '5':'Five',
               '6':'Six',
               '7':'Seven',
               '8':'Eight',
               '9':'Nine',
               '0':'Zero'
               }
    
    conventions = {2:'double',
               3:'triple',
               4:'quadruple',
               5:'quintuple',
               6:'sextuple',
               7:'septuple',
               8:'octuple',
               9:'nonuple',
               10:'decuple'
               }
    
    count = len(stack)
    digit = stack.pop()
    if count > 1:
        return  " " + conventions[count] + " " + numberToEnglish[digit]
    else:
        return " " + numberToEnglish[digit]

def process_phone_number(phone_number):

    cleanedNumber = ""
    englishSentance = ""
    stack = []

    for index, char in enumerate(phone_number):

        if char.isdigit():
            if len(stack) == 0:
                #Only executes if its a first digit OR more than 1 non digit characters are read
                stack.append(char)
            else:
                if char == stack[-1]:
                    #If char is equal to top of the stack, PUSH char
                    stack.append(char)
                else:
                    # If not then clear the stack and append the new char
                    englishSentance += make_sentence(stack)
                    stack.clear()
                    stack.append(char)

                if  index == (len(phone_number)-1):
                    #Only executes for last character
                    englishSentance += make_sentence(stack)
                    stack.clear()
            
            cleanedNumber+=char
        elif not char.isdigit():
            if len(stack) !=0:
                # Char is non digit and stack is not  empty
                englishSentance += make_sentence(stack)
                stack.clear()

    return cleanedNumber + '\n' + englishSentance

def read_phone_numbers():

    result = ""
    with open('test.txt','r') as inFile:
        lines = inFile.readlines()

    totalPhoneNumbers = int(lines[0].strip())               
    phoneNumbers = [line.strip() for line in lines[1:]]     
    
    for phoneNumber in phoneNumbers:                                    
        result += process_phone_number(phoneNumber) + "\n"
    
    with open('output.txt','w') as outFile:
        lines = outFile.writelines(result)


def main():
    read_phone_numbers()

if __name__=="__main__":
    main()
