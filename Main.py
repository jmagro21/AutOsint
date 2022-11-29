import os



print("h - help")
print("do - tout faire sur le future DNS donné ")
Souhait = input("Que  souhaitez vous faire ? : ")

if Souhait == "h" :
    print("Voici ce que vous pouvez faire avec ce script")
    os.system("theHarvester")
elif Souhait == "do" : 
    DNS = input("veuillez saisir l'adresse DNS à Scanner ")
    os.system("theHarvester -d "+DNS+" -b all")
else : 
    print("Vous n'avez rien saisi.")


