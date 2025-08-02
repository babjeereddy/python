password = "123"
for i in range(1000):
    guess = str(i).zfill(3)
    if guess == password:
        print("Password found:", guess)
        break
    