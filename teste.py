import os
import sys

def listar_diretorios(caminho):
    try:
        if not os.path.isdir(caminho):
            raise FileNotFoundError(f"O caminho '{caminho}' não é um diretório válido.")
        
        print(f"Conteúdo do diretório '{caminho}':")
        for item in os.listdir(caminho):
            print(item)
    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except PermissionError:
        print(f"Erro: Permissão negada para acessar '{caminho}'.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def criar_diretorio(caminho):
    try:
        os.makedirs(caminho, exist_ok=True)
        print(f"Diretório '{caminho}' criado com sucesso!")
    except PermissionError:
        print(f"Erro: Permissão negada para criar o diretório '{caminho}'.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def main():
    if len(sys.argv) < 3:
        print("Erro: É necessário fornecer ao menos um argumento para operação e um caminho.")
        sys.exit(1)

    operacao = sys.argv[1].lower()
    caminho = sys.argv[2]

    if operacao == 'listar':
        listar_diretorios(caminho)
    elif operacao == 'criar':
        criar_diretorio(caminho)
    else:
        print("Erro: Operação inválida. Use 'listar' ou 'criar'.")
        sys.exit(1)
