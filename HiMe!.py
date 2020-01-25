while True:
    print("Please enter password.")
    password = input()
    if password != "123":
        print("Invalid password!")
        continue
    print("Access granted.")
    break
while True:
    print("Who is this?")
    ident = input()
    if ident != "JP":
        continue
    else:
        break
print("Hello JP!")
    