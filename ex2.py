def caesar_cipher(text,key):
    translated = ''
    for s in text:
        if s.isalpha():
            num = ord(s)
            num += key
            
            if s.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)

        else:
            translated += symbol
            
    print(translated)


caesar_cipher("xvillage",3)