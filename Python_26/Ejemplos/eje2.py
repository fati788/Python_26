def mayorEdad(edad):
    if edad > 18: 
        return "Eres menor de edad"
    elif (edad >= 18) and (edad <65):
        return "Eres adulto"
    else:
        return "Eres mayor"
    
print(mayorEdad(20))    
    