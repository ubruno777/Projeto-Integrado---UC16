import bcrypt

def criptografia(senha):

    salt = bcrypt.gensalt()

    criptosenha = bcrypt.hashpw(senha.encode('utf-8'),salt)
    return criptosenha.decode('utf-8')