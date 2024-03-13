
import os

# caminho = r"C:\Users\Python\Desktop\Mover e Renomear Arquivos com Python"
lista_arquivos = os.listdir("Mover")

for arquivo in lista_arquivos:
    if ".xlsx" in arquivo:
        if "Jan" in arquivo:
            # jogar pra pasta de janeiro
            os.rename(f"Mover/{arquivo}", f"Mover/Jan/{arquivo}")
        if "Fev" in arquivo:
            # jogar pra pasta de fevereiro
            os.rename(f"Mover/{arquivo}", f"Mover/Fev/{arquivo}")
        if "Mar" in arquivo:
            # jogar pra pasta de março
            os.rename(f"Mover/{arquivo}", f"Mover/Mar/{arquivo}")