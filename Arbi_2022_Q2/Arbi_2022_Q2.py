

def  encode_message(inputMessage):

    capitalLetters = [
        ['A','B','C','D','E'],
        ['F','G','H','I','J'],
        ['K','L','M','N','O'],
        ['P','Q','R','S','T'],
        ['U','V','W','X','Y'],
        ['Z']
    ]
    currCol = 0
    currRow = 0
    newCol = 0
    newRow = 0
    resultStr = ""

    for char in inputMessage:

        if (ord(char) >= 65 and
            ord(char) <= 90):
            # To check if its an alphabet

            for rowIndex, row in enumerate(capitalLetters):
                # Finding the character in the matrix
                if char in row:
                    newCol = capitalLetters[rowIndex].index(char)
                    newRow = rowIndex
                    break   
        else:
            # Ignoring spaces and punctuations
            continue

        currToNewRowDiff =  newRow - currRow
        currToNewColDiff =  newCol - currCol

        verticalMoveMent = horizantalMove = ""
        colMove = rowMove = 0

        # Finding the vertical position of the new char
        if currToNewRowDiff == 0:
            # New character is in the same row
            verticalMoveMent = ""
            rowMove = 0
        elif currToNewRowDiff > 0:
            # New character is downward from out current location
            verticalMoveMent = "d"
            rowMove = abs(currToNewRowDiff)
        else:
            # New character is upward from out current location
            verticalMoveMent = "u"
            rowMove = abs(currToNewRowDiff)

        # Finding the horizantal position of the new char
        if currToNewColDiff == 0:
            # New character is in the same column
            horizantalMove = ""
            colMove = 0
        elif currToNewColDiff > 0:
            # New character is on right side from out current location
            horizantalMove = "r"
            colMove = abs(currToNewColDiff)
        else:
            # New character is on left side from out current location
            horizantalMove = "l"
            colMove = abs(currToNewColDiff)

        resultStr += verticalMoveMent*rowMove
        resultStr += horizantalMove*colMove
        resultStr += "#"
        currRow = newRow
        currCol = newCol

    return resultStr 


def main():
    
    inputMessage = ""

    while True:
        
        inputMessage = input("Please enter message to encode or simply enter E to exit program:")

        if (len(inputMessage) == 1 and
            inputMessage[0].upper() == 'E'):
            # If user wants to exit the program
            print("Exiting")
            break
        else:
            # Send the message for encoding
            result = encode_message(inputMessage.upper())
            print(result)


if __name__=="__main__":
    main()

