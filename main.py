from sympy import randprime
import random

#A function made to generate a large prime number
def GLP():
  return randprime(10**100, 10**101)

#A function that generates a random number[between 1 through 20]
def GRN():
  return random.randint(1, 20)
  
#Alice I
def Cal_A(g, x, n):
  A = g**x % n
  return A
  
#Alice II
def Cal_K1(B, x, n):
  K1 = B**x % n
  return K1
  
#Bob I
def Cal_B(g, y, n):
  B = g**y % n
  return B

#Bob II
def Cal_K2(A, y, n):
  K2 = A**y % n
  return K2

def Master_C0De():
  a = "the number of step|what A does"
  b = " |\n"
  print("Master C0De: " + a + "|what an evesdropper can see|what B does|")
  print("Order: Step|Alice|Eve|Bob\n")
  One_n = GLP()
  print("1.| " + str(One_n) + " | " + str(One_n) + " | " + str(One_n) + b)
  Two_g = GRN()
  print("2.| " + str(Two_g) + " | " + str(Two_g) + " | " + str(Two_g) + b)
  Three_x = GRN()
  Three_y = GRN()
  print("3.| " + str(Three_x) + " | " + "N/A" + " | " + str(Three_y) + b)
  Four_A = Cal_A(Two_g, Three_x, One_n)
  Four_B = Cal_B(Two_g, Three_y, One_n)
  print("4.| " + str(Four_A) + " | " + "N/A" + " | " + str(Four_B) + b)
  print("5.| " + str(Four_B) + " | " + str(Four_A) + " <-> "+ str(Four_B) + " | " + str(Four_A) + b)
  Six_K1 = Cal_K1(Four_B, Three_x, One_n)
  Six_K2 = Cal_K2(Four_A, Three_y, One_n)
  print("6.| " + str(Six_K1) + " | " + "N/A" + " | " + str(Six_K2) + b)
  Seven_U = str(Six_K1) + " = " + str(Six_K2)
  print("7.| " + Seven_U + " | " + "N/A" + " | " + Seven_U + b)

print("Welcome to D-HKEP")
print("[aka. Diffie-Hellman Key Exchange Protocol]\n")
print("Its a simulation that shows how the Diffie-Hellman Key Exchange Protocol works\n")

print("Start code?")
ANS = input("[y/n]: ")

if ANS == "y":
  print("\nStarting...\n")
  print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--\n")
  print("Key:")
  print("1. Alice and Bob agree on a large prime number, n")
  print("2. Alice and Bob agree on a generator g")
  print("3. Alice and Bob make their own private key x and y [respectfully in that order]")
  print("4. Alice and Bob calculate their public keys A and B [respectfully in that order]")
  print("5. Alice and Bob exchange their public keys A and B [respectfully in that order]")
  print("6. Alice and Bob calculate their shared secret key, K1 and K2 [respectfully in that order]")
  print("7. Key exchange successful\n")
  print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--\n")
  Master_C0De()

elif ANS == "n":
  print("Then why did you run this code?")
  exit(784)
  
else:
  print("Invalid answer")