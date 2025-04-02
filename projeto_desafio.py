# Funcao para adicionar contatos na agenda
def adicionar_contato(contato_agenda, nome, telefone, email):
    contato_agenda = {"contato": nome, "telefone": telefone, "email": email, "favorito": False}
    agenda_telefonica.append(contato_agenda)
    print(f"\nContato Adicionado com Sucesso!")
    return

# Funcao para visualizar contatos na agenda
def visualizar_contato(agenda_telefonica):
    print("\nAgenda de Contatos")
    for indice,agenda_telefonica in enumerate(agenda_telefonica, start=1):
        favoritos = "★" if agenda_telefonica["favorito"] else "☆"
        nome_contato = agenda_telefonica["contato"]
        telefone_contato = agenda_telefonica["telefone"]
        email_contato = agenda_telefonica["email"]
        print(f"{indice}. {favoritos} {nome_contato} Telefone:{telefone_contato} E-mail:{email_contato}")

# Funcao para atualizar contatos na agenda
def atualizar_contato(agenda_telefonica, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_contato_ajustado = indice_contato - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda_telefonica):
        agenda_telefonica[indice_contato_ajustado]["contato"] = novo_nome
        agenda_telefonica[indice_contato_ajustado]["telefone"] = novo_telefone
        agenda_telefonica[indice_contato_ajustado]["email"] = novo_email
        print(f"Contato Atualizado com Sucesso!")
    else:
        print("\nIndice de Contato Invalido.")
    return

# Funcao para adicionar/remover contatos na agenda
def adicionar_remover_favorito(agenda_telefonica, indice_contato):
    indice_contato_ajustado = indice_contato - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda_telefonica):
        if agenda_telefonica[indice_contato_ajustado]["favorito"] == False:
            agenda_telefonica[indice_contato_ajustado]["favorito"] = True
            contato = agenda_telefonica[indice_contato_ajustado]["contato"]
            print(f"\n{contato} foi Adicionado a sua Lista de Favoritos!")
        else:
            agenda_telefonica[indice_contato_ajustado]["favorito"] = False
            print(f"\n{contato} foi Removido da sua Lista de Favoritos!")
    else:
        print("\nIndice de Contato Invalido.")
    return

def visualizar_favoritos(agenda_telefonica):
    for indice,agenda_telefonica in enumerate(agenda_telefonica, start=1):
        if agenda_telefonica["favorito"]:
            nome_contato = agenda_telefonica["contato"]
            telefone_contato = agenda_telefonica["telefone"]
            email_contato = agenda_telefonica["email"]
            print(f"\n{indice}. ★ {nome_contato} Telefone:{telefone_contato} E-mail:{email_contato}")
        else:
            print("\nNenhum Usuário foi Encontrado na Sua Lista de Favoritos")
    return

def deletar_contato(agenda_telefonica, indice_contato):
    indice_contato_ajustado = indice_contato - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(agenda_telefonica):
        agenda_telefonica.remove(agenda_telefonica[indice_contato_ajustado])
        print(f"\nContato Removido com Sucesso da Agenda!")
    else:
        print("\nIndice de Contato Invalido.")
    return

# Lista Ultilizada como Agenda.
agenda_telefonica = []

while True:
    print("\nMenu Da Agenda de Contatos: ")
    print("1. Adicionar um Novo Contato")
    print("2. Exibir Lista de Contatos")
    print("3. Editar um Contato")
    print("4. Adicionar/Remover um Contato como Favorito")
    print("5. Exibir Lista de Contatos Favoritos")
    print("6. Deletar um Contato")
    print("7. Sair")

    opcao = int(input("Digite sua Escolha: "))

    if opcao == 1:
        nome = input("Digite o Nome de Seu Contato: ")
        telefone = input("Digite o Telefone (Sem Espaços e Hifem, Apenas Números): ")
        email = input("Digite o E-mail de Seu Contato: ")
        adicionar_contato(agenda_telefonica, nome, telefone, email)

    elif opcao == 2:
        visualizar_contato(agenda_telefonica)

    elif opcao == 3:
        visualizar_contato(agenda_telefonica)
        indice_contato = int(input("Digite o Contato que Você Deseja Alterar: "))
        novo_nome = input("Digite o Nome de Seu Contato: ")
        novo_telefone = input("Digite o Telefone (Sem Espaços e Hifem, Apenas Números): ")
        novo_email = input("Digite o E-mail de Seu Contato: ")
        atualizar_contato(agenda_telefonica, indice_contato, novo_nome, novo_telefone, novo_email)
    
    elif opcao == 4:
        visualizar_contato(agenda_telefonica)
        indice_contato = int(input("\nDigite o Indice do Contato que Deseja Adicionar/Remover dos Favoritos: "))
        adicionar_remover_favorito(agenda_telefonica, indice_contato)
    
    elif opcao == 5:
        visualizar_favoritos(agenda_telefonica)

    elif opcao == 6:
        visualizar_contato(agenda_telefonica)
        indice_contato = int(input("\nDigite o Indicie do Contato que Deseja Apagar: "))
        deletar_contato(agenda_telefonica, indice_contato)

    elif opcao == 7:
        break

    else:
        print("\nOpcao Invalida, Digite Novamente!")
        
print("Programa Finalizado")