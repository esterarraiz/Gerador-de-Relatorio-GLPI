from glpi import GLPIBot
from enviar_email import EnvioEmail
from formatacao_email import EmailFormatar
from gerar_relatorios import Relatorio
import getpass
import msvcrt
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
data_atual = datetime.now().strftime("%d de %B de %Y").replace("marÃ§o", "Março")
hora_atual = datetime.now().strftime("%H:%M")
print("\n----- SEJA BEM-VINDO! -----\n")
print("Escolha um usuário para acessar o sistema GLPI:\n")

usuarios = {
    "1": "ester.matos",
    "2": "joao.gomes",
    "3": "luis.andrade",
    "4": "zairo.cunha"
}

for key, value in usuarios.items():
    print(f"{key} - {value}")

op = input("\nDigite o número correspondente ao usuário desejado: ")

print(f"Você escolheu o usuário: {usuarios[op]}")


while op not in usuarios:
    print("Opção inválida. Tente novamente.")
    op = input("Digite o número correspondente ao usuário desejado: ")

usuario = usuarios[op]
senha = getpass.getpass("Digite a senha (GLPI): ")

glpi = GLPIBot(usuario, senha)
glpi.login()

chamados = glpi.extrair_chamados()
chamados1 = glpi.extrair_chamados1()
chamados2 = glpi.extrair_chamados2()

relatorio = Relatorio(chamados)
relatorio.categorias()
dados_relatorio = relatorio.get_relatorio()

relatorio1 = Relatorio(chamados1)
relatorio1.categorias()
dados_relatorio1 = relatorio1.get_relatorio()

relatorio2 = Relatorio(chamados2)
relatorio2.categorias()
dados_relatorio2 = relatorio2.get_relatorio()

print("\nRelatório gerado com sucesso!\n")

print("\n----- Relatório -----")
print("\nSLAS VENCIDOS:")
for categoria, lista in dados_relatorio.items():
    print(f"{categoria}: {lista}")

print("\n--------------------------\nSLAS QUE VENCEM HOJE:")

for categoria, lista in dados_relatorio2.items():
    print(f"{categoria}: {lista}")

print("\n--------------------------\n CHAMADOS SEM TÉCNICO ATRIBUIDO:\n")

for categoria, lista in dados_relatorio.items():
    print(f"{categoria}: {lista}")

print("\n--------------------------")
print("\nDados do E-mail:")

remetente = usuario + "@idxdatacenters.com.br"
print(f"\nRemetente: {remetente}")
senha_email = getpass.getpass("Senha do seu E-mail: ")
nome=usuario.replace("."," ").title()

destinatarios = {
        "1": "wanessa.ferreira@idxdatacenters.com.br",
        "2": "talles.lopes@idxdatacenters.com.br",
        "3": "simpson.oliveira@idxdatacenters.com.br",
        "4": "Outro (digitar manualmente)"
    }
    
print("\nEscolha o destinatário do relatório:\n")
for key, email in destinatarios.items():
    print(f"{key} - {email}")
    
opcao = input("\nDigite o número da opção desejada: ")
destinatario = destinatarios[opcao]
if opcao == "4":
    destinatario = input("Digite o e-mail do destinatário: ")


cc=["talles.lopes@idxdatacenters.com.br","rogerio.moura@idxdatacenters.com.br", "neuziron.santos@idxdatacenters.com.br", "antonio.santos@idxdatacenters.com.br", "simpson.oliveira@idxdatacenters.com.br", "tayna.santos@idxdatacenters.com.br", "igor.silva@idxdatacenters.com.br", "jose.nunes@idxdatacenters.com.br"]
print(f"Enviando para: {destinatario}, CC: {cc}")

destinatarios_envio = [destinatario] + cc 
email_formatter = EmailFormatar(remetente, destinatarios_envio, nome)
conteudo_email = email_formatter.formatar_email(

    dados_relatorio1["NOC"], dados_relatorio1["SOC"], dados_relatorio1["N1 Palmas"], 
    dados_relatorio1["N1 Araguaína"], dados_relatorio1["DC"], dados_relatorio1["Infra"], 
    dados_relatorio1["Telefonia"], dados_relatorio1["CRP"],

    dados_relatorio2["NOC"], dados_relatorio2["SOC"], dados_relatorio2["N1 Palmas"], 
    dados_relatorio2["N1 Araguaína"], dados_relatorio2["DC"], dados_relatorio2["Infra"], 
    dados_relatorio2["Telefonia"], dados_relatorio2["CRP"],

    dados_relatorio["NOC"], dados_relatorio["SOC"], dados_relatorio["N1 Palmas"], 
    dados_relatorio["N1 Araguaína"], dados_relatorio["DC"], dados_relatorio["Infra"], 
    dados_relatorio["Telefonia"], dados_relatorio["CRP"]
)


email_sender = EnvioEmail(remetente, senha)
email_sender.enviar_email(destinatario, f"[IDX] Relatório de SLAs e Chamados Sem Técnico - {data_atual} {hora_atual}", conteudo_email, cc)

print("Aperte qualquer tecla para sair...")
msvcrt.getch()

