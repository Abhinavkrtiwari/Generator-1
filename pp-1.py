import random
import string

print("Hi,Welcome to Password generator!")

#input the length of password

length=int(input('\nEnter the length of password:'))


lower= string.ascii_lowercase
upper= string.ascii_uppercase
num = string.digits
symbols = string.punctuation


#Now combine the data and store the data.

All= lower + upper + num + symbols

#Now random module is used to generate the password.


temp = random.sample(All,length)




Password = "".join(temp)

print(Password)
      
      
