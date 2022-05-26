# Hamza Zahid
# 22-11157
import rsa
import pandas
publicKey, privateKey = rsa.newkeys(512)# generate public and private keys with rsa.newkeys method,this method accepts
string = input("Enter a Message to encrypt: ")# Program is getting input from user to encrypt
#---------------------------- HERE IS THE ENCRYPTION PART ---------------------------
ENCRYPTEDSTRING = rsa.encrypt(string.encode(),publicKey) # Encrypting Message using correct RSA Algorithm
print("original string: ", string)# This is the original message which user entered
#------------------- Showing Encrypted Message -----------------
print("encrypted string: ", ENCRYPTEDSTRING)#Showing encrypted message
#----------------------------------------------------------------------
#--------------------------- HERE IS THE DECRYPTION PART ------------------
encrypted_message_to_decrypt=ENCRYPTEDSTRING # giving encrypted message to program for decryption
DECRYPTEDSTRING = rsa.decrypt(encrypted_message_to_decrypt, privateKey).decode()# Decrypting Message using correct RSA Algorithm
print("decrypted string: ", DECRYPTEDSTRING)# Here it is the decrypted message
