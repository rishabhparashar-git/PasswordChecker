import os


def magic(ssidName):
    finalPassword = ""
    password = str(os.popen("netsh wlan show profile " + ssidName + " key=clear").readlines())
    if ('[\'Profile "{}" is not found on the system.\\n\']'.format(ssidName)) in password:
        return "Oh Darling Sorry!! But I don't remember you've ever connected to that network"
    else:
        starting = password.find("Key Content            : ") + 25
        ending = password.find("Key Content            : ") + 25 + 64
        for i in range(starting, ending):
            if password[i:i + 12] != "\\n', '\\n', '":
                finalPassword = finalPassword + password[i]
            else:
                break
        return str(finalPassword)
