def validaRut(rut):
    caracteres=".-"
    for x in range(len(caracteres)):
        rut=rut.replace(caracteres[x],"")

    rutsindigito=rut[:len(rut)-1]
    rutinvertido=rutsindigito[::-1]

    multi=2
    sum=0

    for i in range(0,len(rutinvertido)):
        if multi>7:
            multi=2
        sum+=int(rutinvertido[i])*multi
        multi+=1

    dv=11-(sum%11)
    dvu=rut[-1:]

    if dv==11:
        dv=0
    if dv==10:
        dv="K"

    if str(dv)==dvu:
        return True
    else:
        return False
    

def validaEmail(email):
   
    validador = "xxx.xx"
    mail = email.split("@")[-1].split(".")[0] #gmail
    mail2 = email.split("@")[-1].split(".")[1] #com
    val = validador.split(".")[-1] #xx
    val2 = validador.split(".")[-2] #xxx
    
    # print(mail, mail2, val, val2)

    if len(mail) > len(val2) and len(mail2) >= len(val):
        return True
    else:
        return False