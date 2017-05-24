'''
Our main function opens the encrypted password
file passwords.txt and reads the contents of each line in the password file. For
each line, it splits out the username and the hashed password. For each individual
hashed password, the main function calls the testPass() function that
tests passwords against a dictionary file.
'''

import passlib.hash, crypt
import hashlib
from passlib import *

def testPassword(passWord):
	print "passWord received to test is: {}".format(passWord)
	
	if len(passWord) < 2: #If like *
		return

	ctype = passWord[1]
	#print "ctype is: {}".format(ctype)
	salt = passWord[3:11]
	#print "salt is: {}".format(salt)

	with open("dictionary.txt") as f:
		plainTextPasswords = f.readlines()

		for plainTextPassword in plainTextPasswords:
			plainTextPassword = plainTextPassword.strip('\n')

			#print "plainTextPassword is: {}".format(plainTextPassword)
			value = passlib.hash.sha512_crypt.encrypt(plainTextPassword, salt=salt, rounds=5000)
			if value == passWord:
				print "Match!"
				print "plaintext password for: {} is: {}".format(passWord, plainTextPassword)
				#print "original passWord: {}".format(passWord)
				#print "value we got for the plaintext: {}".format(value)
				break
			else:
				print "No Match"
		return


def getPasswords():
	with open("passwords.txt") as f:
		passwords = f.readlines()
		
		for fullString in passwords:
			if ":" in fullString:
				userName = fullString.split(":")[0]
				passWord = fullString.split(":")[1]
				print "\n======Testing passwords for user: {}".format(userName)
				print "fullString in password file is: {}".format(fullString)
				testPassword(passWord)

if __name__ == "__main__":
	getPasswords()
