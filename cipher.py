import time
import random
import os
import nltk
nltk.download('words')
ev = set(w.lower() for w in nltk.corpus.words.words())


alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt():
    newstr = ''
    shift = random.randint(0,25)
    print(shift)
    string = input("Please enter your string to encrypt(lowercase only): ")
    print('Encrypting...')
    for char in string:
        if char not in alpha:
            newstr+=char
                    
        else:
            
            idx = alpha.index(char)
            idx += shift
            if idx>25:
                idx = idx - 26
            newstr+=alpha[idx]

    print('Finished Task.')
    print("Your newly encrypted string is: " + newstr)
    print("Thank you for using Caesar Cipher (CC) Version 1.0!")

def decrypt():
    word_count = 0
    dec = input("Enter the string you would like to Decrypt: ")
    keyornah = input("Do you have a key? ")
    if keyornah == 'yes':
        key = int(input("Enter your key(shift): "))
        print("Decrypting...")
        decstring = ''
        for char in dec:
            if char not in alpha:
                
                decstring+=char
            else:
                idx2 = alpha.index(char)
                idx2-=key
                if idx2<0:
                    idx2 = idx2+26
                decstring+=alpha[idx2]
        print("Your decrypted string is: " + decstring)
        exit()
    else:
        print('Without a key, the sentence that will be generated might not be correct. Please look carefully and review all test cases after the task is finshed.')
        
        for key2 in range(25):
            print("Trying test case number " + str(key2))
            brute = ''
            for char in dec:
                if char not in alpha:
                    brute+=char
                else:
                    idx3 = alpha.index(char)
                    idx3-=key2
                    if idx3<0:
                        idx3+=26
                    brute+=alpha[idx3]
            rah = brute.split()
            
            if len(rah) == 1:
                if rah[0] in ev:
                    os.system('cls||clear')
                    print("Message Possibly Cracked: " + brute)
                    ans2 = input("Would you like to continue?: ")
                    if ans2 == 'no':
                        print('Message Cracked: ' + brute)
                        print("Thank you for using Caesar Cipher Version 1.0!")
                        exit()
                    elif ans == 'yes':

                        pass
            else:
                for word in rah:

                    if word in ev:
                        word_count+=1



		          

                if word_count >= len(rah)//3:
                    os.system('cls||clear')
                    print("Message Possibly Cracked: " + brute)
                    ans2 = input("Would you like to continue?: ")
                    if ans2 == 'no':
                        print('Message Cracked: ' + brute)
                        print("Thank you for using Caesar Cipher Version 1.0!")
                        exit()
                    elif ans == 'yes':

                        pass



                
            print("Completed. Finished string is: " + brute)
            time.sleep(0.5)
            
            brute = ''
            
        print("Thank you for using Caesar Cipher Version 1.0!")
        exit()
                       
ans = input("Would you like to Encrypt or Decrypt a String(e/d)?: ")
if ans == 'e':
    encrypt()
elif ans == 'd':
    decrypt()
   
    
    
                   

