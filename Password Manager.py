from cryptography.fernet import Fernet
master_pwd = input("Enter your master password")


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if data and "|" in data:
                user, password = data.split("|")
                print("User: ", user, ", Password: ", password)


def new():
    name = input('Account Name')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (new/view)?, press q to quit").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "new":
        new()
    else:
        print("Invalid mode.")
        continue

