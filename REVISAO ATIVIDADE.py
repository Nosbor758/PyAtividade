import json
import os

def carregar_dados(nome_arquivo):
    try:
        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        return []
    except (IOError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar dados do arquivo {nome_arquivo}: {e}")
        return []

def salvar_dados(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Erro ao salvar dados no arquivo {nome_arquivo}: {e}")

def cadastrar_artista(artistas):
    try:
        nome = input("Nome do artista: ")
        data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
        local_nascimento = input("Local de nascimento: ")
        biografia = input("Biografia: ")
        estilos = input("Estilos artísticos (separados por vírgula): ").split(',')

        artista = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'local_nascimento': local_nascimento,
            'biografia': biografia,
            'estilos': estilos
        }
        artistas.append(artista)
        salvar_dados('artistas.json', artistas)
        print("Artista cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar artista: {e}")

def cadastrar_obra(obras, artistas):
    try:
        titulo = input("Título da obra: ")
        data_criacao = input("Data de criação (AAAA-MM-DD): ")
        tema = input("Tema: ")
        estilo_artistico = input("Estilo artístico: ")
        descricao = input("Descrição: ")
        tecnica = input("Técnica utilizada: ")
        autor_nome = input("Nome do autor: ")
        localizacao = input("Localização na sala de exposição: ")

        autor = next((artista for artista in artistas if artista['nome'] == autor_nome), None)
        if not autor:
            print(f"Autor '{autor_nome}' não encontrado.")
            return

        obra = {
            'titulo': titulo,
            'data_criacao': data_criacao,
            'tema': tema,
            'estilo_artistico': estilo_artistico,
            'descricao': descricao,
            'tecnica': tecnica,
            'autor': autor,
            'localizacao': localizacao,
            'documentos_relacionados': []
        }
        obras.append(obra)
        salvar_dados('obras.json', obras)
        print("Obra cadastrada com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar obra: {e}")

def cadastrar_emprestimo(emprestimos, obras):
    try:
        titulo_obra = input("Título da obra a ser emprestada: ")
        periodo = input("Período de empréstimo (AAAA-MM-DD a AAAA-MM-DD): ")
        nome_evento = input("Nome do evento: ")
        responsavel = input("Responsável: ")
        tema_evento = input("Tema do evento: ")

        obra = next((obra for obra in obras if obra['titulo'] == titulo_obra), None)
        if not obra:
            print(f"Obra '{titulo_obra}' não encontrada.")
            return

        emprestimo = {
            'obra': obra,
            'periodo': periodo,
            'nome_evento': nome_evento,
            'responsavel': responsavel,
            'tema_evento': tema_evento
        }
        emprestimos.append(emprestimo)
        salvar_dados('emprestimos.json', emprestimos)
        print("Empréstimo cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar empréstimo: {e}")

def cadastrar_visita_guiada(visitas_guiadas, obras):
    try:
        tema = input("Tema da visita guiada: ")
        descricao = input("Descrição: ")
        titulos_obras = input("Obras a serem visitadas (separadas por vírgula): ").split(',')

        obras_visita = [obra for titulo in titulos_obras for obra in obras if obra['titulo'] == titulo.strip()]
        if not obras_visita:
            print("Nenhuma das obras especificadas foi encontrada.")
            return

        visita = {
            'tema': tema,
            'descricao': descricao,
            'obras': obras_visita
        }
        visitas_guiadas.append(visita)
        salvar_dados('visitas_guiadas.json', visitas_guiadas)
        print("Visita guiada cadastrada com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar visita guiada: {e}")

def listar_obras(obras):
    try:
        if not obras:
            print("Não há obras cadastradas.")
            return
        
        obras_ordenadas = sorted(obras, key=lambda obra: obra['titulo'])
        for obra in obras_ordenadas:
            print(f"Título: {obra['titulo']}, Autor: {obra['autor']['nome']}, Localização: {obra['localizacao']}")
    except Exception as e:
        print(f"Erro ao listar obras: {e}")

def listar_artistas(artistas):
    try:
        if not artistas:
            print("Não há artistas cadastrados.")
            return
        
        for artista in artistas:
            print(f"Nome: {artista['nome']}, Data de Nascimento: {artista['data_nascimento']}, Estilos: {', '.join(artista['estilos'])}")
    except Exception as e:
        print(f"Erro ao listar artistas: {e}")

def menu_interativo():
    artistas = carregar_dados('artistas.json')
    obras = carregar_dados('obras.json')
    emprestimos = carregar_dados('emprestimos.json')
    visitas_guiadas = carregar_dados('visitas_guiadas.json')

    while True:
        print("\nMenu do Museu de Artes")
        print("1. Cadastrar Artista")
        print("2. Cadastrar Obra")
        print("3. Cadastrar Empréstimo")
        print("4. Cadastrar Visita Guiada")
        print("5. Listar Obras")
        print("6. Listar Artistas")
        print("7. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_artista(artistas)
        elif escolha == '2':
            cadastrar_obra(obras, artistas)
        elif escolha == '3':
            cadastrar_emprestimo(emprestimos, obras)
        elif escolha == '4':
            cadastrar_visita_guiada(visitas_guiadas, obras)
        elif escolha == '5':
            listar_obras(obras)
        elif escolha == '6':
            listar_artistas(artistas)
        elif escolha == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_interativo()
