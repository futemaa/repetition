while True: 
    usuario = input("Digite seu Usuário: ")
    senha = input("Digite sua senha: ")
    if usuario == senha:
        print("A senha não pode ser igual ao nome de usuário!")
    else:
        print("Login bem-sucedido!")    
        break

