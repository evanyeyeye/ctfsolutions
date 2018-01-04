import zipfile

passwords = open("common.txt").read().splitlines()

filename = "evanshi.zip"

while True:    

    try:
        file = zipfile.ZipFile(filename)
    except:
        print("Flag: {}".format(open(filename).read()))    
        break

    for password in passwords:        
        try:    
            file.extractall(pwd=password.encode())
            # print("Password Found: {}".format(password))        
            break
        except:
            pass

    filename = file.namelist()[0]