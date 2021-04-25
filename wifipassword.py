import os


def Magic(ssidName):
    password = str(os.popen("netsh wlan show profile " + ssidName + " key=clear").readlines())
    if ('[\'Profile "{}" is not found on the system.\\n\']'.format(ssidName)) in password:
        print("Oh Darling Sorry!! But I don't remember you've ever connected to that network", end="")
    else:
        starting = password.find("Key Content            : ") + 25
        ending = password.find("Key Content            : ") + 25 + 64
        for i in range(starting, ending):
            if password[i:i + 12] != "\\n', '\\n', '":
                print(password[i], end="")
            else:
                break
    print('\n')


for x in range(5):
    Magic(str(input("Hi!! You can ask me the password of any saved wifi network : ")))
