import sys
import math

def letterToNumber(letter):
    """ Convert letter into integer equivalent using ASCII conversion
    """
    asciiChar = ord(letter)
    if str.isupper(letter):
        asciiChar += 32
    number = int(asciiChar - 97)
    return number
    
def numberToLetter(number):
    """ Convert integer into letter equivalent
    """
    ascii = number + 97
    return chr(ascii)

def rotateCaesar(p, k):
    """ Encrypt integer equivalent of letter using Caesar cipher rotation with key k
    """
    c = (p + k) % 26
    return c

def main():
    # Check user entered exactly 1 arg
    if len(sys.argv) != 2:
        sys.exit("You must enter k as the integer key: python3 caesar.py k")
    
    # Check that user input integer is not negative
    k = int(sys.argv[1])
    if k < 0:
        raise Exception("You must enter a non-negative integer.")
        
    # Get plaintext input
    plaintext = input("plaintext: ")
    
    # Encrypt plaintext by iterating over every character of plaintext.
    print("ciphertext: ", end="")
    for i in range(0, len(plaintext)):
        # If character is not a letter, skip encryption and print plaintext.
        if not (str.isalpha(plaintext[i])):
            print(plaintext[i], end="")
        else: # If character is a letter:
            plaintextNumber = letterToNumber(plaintext[i])         # Convert plaintext letter to int equivalent
            encryptedNumber = rotateCaesar(plaintextNumber, k)     # Rotate int-equivalent letter by secret key
            ciphertextChar = numberToLetter(encryptedNumber);      # Convert encrypted number equivalent back to letter
            if str.isupper(plaintext[i]):       # If original character was uppercase, convert encrypted letter to uppercase.
              ciphertextChar = ciphertextChar.upper()
            
            #Print encrypted character.
            print(ciphertextChar, end="")
        
    
    print("")
    
if __name__ == "__main__":
    main()
