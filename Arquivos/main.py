import random
import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from PIL import Image, ImageTk

connection = sqlite3.connect("Database.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Alunos (nome TEXT, senha TEXT)")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Participantes (nomeP TEXT, nota INTEGER, cursoP TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS Questoes (enunciado TEXT, resposta TEXT, alternativa2 TEXT, alternativa3 TEXT, alternativa4 TEXT, ID TEXT)")


def inserir_questao(enunciado, resposta, alternativa2, alternativa3, alternativa4, ID):
    query = "SELECT * FROM Questoes WHERE enunciado=?"
    cursor.execute(query, (enunciado,))
    if not cursor.fetchone():  
        # Se não houver duplicata, inserir a questão na tabela
        cursor.execute("INSERT INTO Questoes (enunciado, resposta, alternativa2, alternativa3, alternativa4, ID) VALUES (?, ?, ?, ?, ?, ?)",
                       (enunciado, resposta, alternativa2, alternativa3, alternativa4, ID))
        connection.commit()
    else:
        print("A questão já existe na base de dados.")


# vai inserir as questões só se elas não existirem
inserir_questao("Escolha o resultado da seguinte operação: Integral de 2x dx",
                "x² + c", "2x²", "x²/3 + c", "x²/2 + c", "1")
inserir_questao("Calcule a derivada da seguinte função: f(x) = 2x+1",
                "2", "2x", "x + 1", "x/2", "2")
inserir_questao("A área de um triângulo que possui 12 cm de altura e base medindo 9 cm é:",
                "54 cm²", "70 cm²", "85 cm²", "108 cm²", "3")
connection.commit()

# TELA INICIAL
def telaInicial():
    global root
    root = tkinter.Tk()
    root.title("Página Inicial")
    root.resizable(False, False)
    root.focus_force()

    #root.geometry("300x500")

    label = tkinter.Label(root, text="Bem vindo ao Simulador de Avaliações!", font="Consolas 13")
    label.grid(row=0, column=1, pady=10)

    image1 = Image.open("Arquivos\logoEstacio2.png")
    width, height = 500, 300
    image1.thumbnail((width, height))
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(root, image=test)
    label1.image = test
    label1.grid(row=1, column=1, pady=10, padx=47)

    button = tkinter.Button(root, text="Cadastre-se",
                            bg="#3A8E9E", fg="white",
                            font="Consolas 10", command=abrirJanelaAluno)
    # sticky='ew' -> estica o botao horizontalmente
    button.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

    botao_prova = tkinter.Button(
        root, text="Realizar Prova", bg="#47ADC0", fg="white", font="Consolas 10",command=validarJanelaProva)
    botao_prova.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    botao_tabela = tkinter.Button(
        root, text="Ver Pontuações", bg="#51C6DB", fg="white", font="Consolas 10",command=exibirTabelaParticipantes)
    botao_tabela.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

    button = tkinter.Button(root, text="Sair do Programa",
                            bg="#4CBACF", fg="white", font="Consolas 10",command=lambda: root.destroy())
    button.grid(row=5, column=1, padx=10, pady=10,
                sticky='e')  # stiky e vai pra direita

    root.mainloop()


def exibirTabelaParticipantes():
    global root
    root.withdraw()

    root.resizable(False, False)

    janela_tabela = tkinter.Toplevel()
    janela_tabela.title("Tabela de Participantes")

    cursor.execute("SELECT * FROM Participantes")
    dados = cursor.fetchall()

    tabela = tkinter.Frame(janela_tabela)
    tabela.grid(row=0, column=0, padx=10, pady=10)

    # Criei uma tabela (Usei a Documentação)
    tv = tkinter.ttk.Treeview(tabela, columns=(
        'Nome', 'Curso', 'Pontuação'), show='headings')
    tv.heading('Nome', text='Nome')
    tv.heading('Curso', text='Curso')
    tv.heading('Pontuação', text='Pontuação')

    # Inserindo dados na tabela -> Documentação Tkinter
    for linha in dados:
        # os valores são partes da lista que criei com o fetchall
        tv.insert('', 'end', values=(linha[0], linha[2], linha[1]))

    tv.pack()

    botao_fechar = tkinter.Button(janela_tabela, text="Voltar", bg="#009FD6", fg="white", font="Consolas 10",command=lambda: [
                                  janela_tabela.destroy(), root.deiconify()])
    botao_fechar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")


def abrirJanelaAluno():
    global root
    root.withdraw()  # fecha janela inicial
    janelaAluno()

# TELA DE CADASTRO
def janelaAluno():
    global root
    root.withdraw()

    global janela2
    janela2 = tkinter.Tk()
    janela2.geometry("480x400")
    janela2.resizable(False, False)

    janela2.title("Cadastro Aluno")

    label = tkinter.Label(
        janela2, text="Preencha os campos a seguir", font="Consolas 13 bold")
    label.grid(row=0, column=1, pady=35, sticky='ew')

    # nome
    label_nome = tkinter.Label(janela2, text="Nome:", font="Consolas 10")
    label_nome.grid(row=1, column=0, padx=10, pady=15, sticky='ew')
    textoNome = tkinter.StringVar()
    nome = tkinter.Entry(janela2, textvariable=textoNome)
    nome.grid(row=1, column=1, padx=18, pady=15, sticky='ew')

    # senha
    label_senha = tkinter.Label(janela2, text="Senha:", font="Consolas 10")
    label_senha.grid(row=2, column=0, padx=10, pady=15, sticky='ew')
    textosenha = tkinter.StringVar()
    senha = tkinter.Entry(janela2, textvariable=textosenha, show="*")
    senha.grid(row=2, column=1, padx=18, pady=15, sticky='ew')

    botao_cadastrar = tkinter.Button(janela2, text="Cadastre-se", bg="#009FD6",
                                     fg="white", font="Consolas 10",command=lambda: verificarCadastroAluno(nome.get(), senha.get()))
    botao_cadastrar.grid(row=3, column=1, padx=18, pady=10, sticky='ew')

    botao_voltar = tkinter.Button(janela2, text="Voltar para Tela Inicial",
                                  bg="#009FD6", fg="white", font="Consolas 10",command=lambda: voltarTelaInicial_Cadastro(janela2))
    botao_voltar.grid(row=5, column=1, padx=100, pady=10, sticky='ew')


def voltarTelaInicial_Cadastro(janela2):
    janela2.destroy()
    root.deiconify()


def adicionarAluno(nome, senha):
    caracteres_especiais = ";-'!+@#$%&*().=[]}`{|,"
    if any(caracter in caracteres_especiais for caracter in str(nome) + str(senha)):
        print("Caracteres especiais não são permitidos.")
    else:
        cursor.execute(
            "INSERT INTO Alunos (nome, senha) VALUES (?, ?)", (nome, senha))
        connection.commit()


def verificarLogin(nome, senha):
    query = "SELECT * FROM Alunos WHERE nome=? AND senha=?"
    cursor.execute(query, (nome, senha))
    aluno = cursor.fetchone()

    caracteres_especiais = ";-'!+@#$%&*().=[]}`{|,"
    if any(caracter in caracteres_especiais for caracter in str(nome) + str(senha)):
        mb.showinfo("Aviso", "Caracteres especiais não são permitidos.")

    elif not (nome and senha):
        mb.showinfo("Aviso", "O campo não pode ficar em branco.")

    elif aluno:
        abrirJanelaProva()
    else:
        mb.showinfo("Aviso", "Credenciais inválidas.")


def verificarCadastroAluno(nome, senha):
    global janela2
    caracteres_especiais = ";-'!+@#$%&*().=[]}`{|,"
    if any(caracter in caracteres_especiais for caracter in str(nome) + str(senha)):
        mb.showinfo("Aviso", "Caracteres especiais não são permitidos.")

    elif not (nome and senha):  # verifica se está vazio
        mb.showinfo("Aviso", "O campo não pode ficar em branco.")

    else:
        mb.showinfo("Sucesso", "Cadastro válido.")
        adicionarAluno(nome, senha)
        validarJanelaProva()
        janela2.destroy()


def voltarTelaInicialLogin():
    global janelaValidProva
    janelaValidProva.destroy()
    root.deiconify()

# TELA DE LOGIN
def validarJanelaProva():
    global root
    root.withdraw()

    global janelaValidProva
    janelaValidProva = tkinter.Tk()
    janelaValidProva.geometry("470x400")
    janelaValidProva.title("Faça seu Login")
    janelaValidProva.resizable(False, False)


    label = tkinter.Label(
        janelaValidProva, text="Realize seu Login", font="Consolas 16 bold")
    label.grid(row=0, column=1, pady=35, sticky='ew')

    # nome
    label_nome = tkinter.Label(janelaValidProva, text="Nome:", font="Consolas 10")
    label_nome.grid(row=1, column=0, padx=10, pady=15, sticky='ew')
    textoNome = tkinter.StringVar()
    nome = tkinter.Entry(janelaValidProva, textvariable=textoNome)
    nome.grid(row=1, column=1, padx=18, pady=15, sticky='ew')

    # senha
    label_senha = tkinter.Label(janelaValidProva, text="Senha:", font="Consolas 10")
    label_senha.grid(row=2, column=0, padx=10, pady=15, sticky='ew')
    textosenha = tkinter.StringVar()
    senha = tkinter.Entry(janelaValidProva, textvariable=textosenha, show="*")
    senha.grid(row=2, column=1, padx=18, pady=15, sticky='ew')

    botao_cadastrar = tkinter.Button(janelaValidProva, text="Realize seu Login",
                                     bg="#009FD6", fg="white", font="Consolas 10",command=lambda: verificarLogin(nome.get(), senha.get()))
    botao_cadastrar.grid(row=3, column=1, padx=18, pady=10, sticky='ew')

    botao_voltar = tkinter.Button(janelaValidProva, text="Voltar para Tela Inicial",
                                  bg="#009FD6", fg="white", font="Consolas 10",command=lambda: voltarTelaInicialLogin())
    botao_voltar.grid(row=5, column=1, padx=100, pady=10, sticky='ew')

# TELA DA PROVA
def abrirJanelaProva():
    global janelaValidProva
    janelaValidProva.withdraw()

    global janelaProva
    janelaProva = tkinter.Toplevel()
    janelaProva.title("Prova da Estácio")
    janelaProva.resizable(False, False)

    # pegar do banco
    cursor.execute("SELECT * FROM Questoes")
    questoes = cursor.fetchall()

    variaveis_resposta = []  # armazena as alternativas

    for i, questao in enumerate(questoes):
        label_questao = tkinter.Label(
            janelaProva, text=f"Questão {i+1}) {questao[0]}")
        label_questao.grid(row=i*5, column=0, padx=10, pady=10)

        # Converti a tupla de alternativas em uma lista e aleatorizá-la
        alternativas = list(questao[1:-1])
        random.shuffle(alternativas)

        # Criei uma StringVar para armazenar a resposta selecionada para cada questão
        resposta_var = tkinter.StringVar()
        variaveis_resposta.append(resposta_var)

        for j, option_text in enumerate(alternativas):
            tkinter.Radiobutton(janelaProva, text=option_text, variable=resposta_var, value=option_text).grid(
                row=i*5+j+1, column=0, sticky="w", padx=10, pady=5)

    label_nome = tkinter.Label(janelaProva, text="Assine seu Nome:")
    label_nome.grid(row=len(questoes)*5+1, column=0,
                    padx=10, pady=10, sticky='ew')
    assinaturaNome = tkinter.StringVar()

    assinatura = tkinter.Entry(janelaProva, textvariable=assinaturaNome)
    assinatura.grid(row=len(questoes)*6+1, column=0,
                    padx=10, pady=10, sticky="ew")

    label_nome = tkinter.Label(janelaProva, text="Digite seu Curso:")
    label_nome.grid(row=len(questoes)*7+1, column=0,
                    padx=10, pady=10, sticky='ew')
    cursoP = tkinter.StringVar()
    assinaturacurso = tkinter.Entry(janelaProva, textvariable=cursoP)
    assinaturacurso.grid(row=len(questoes)*8+1, column=0,
                         padx=10, pady=10, sticky='ew')

    botao_finalizar = tkinter.Button(janelaProva, text="Concluir Prova", bg="#009FD6", fg="white",
                                     font="Consolas 10",command=lambda: verificarFimProva(variaveis_resposta, assinaturaNome, cursoP))
    botao_finalizar.grid(row=len(questoes)*8+1, column=1,
                         padx=10, pady=10, sticky='ew')


def verificarFimProva(variaveis_resposta, assinaturaNome, cursoP):
    global janelaProva
    # Verifica se os campos de assinatura e curso estão vazios
    if not assinaturaNome.get() or not cursoP.get():
        mb.showerror("Erro", "Por favor, preencha todos os campos.")
    else:
        resposta = mb.askyesno(
            "Finalizar Prova", "Deseja realmente finalizar a prova?")
        if resposta:
            finalizarProva(variaveis_resposta, assinaturaNome, cursoP)
            janelaProva.destroy()

# RESULTADO DA PROVA
def finalizarProva(variaveis_resposta, assinaturaNome, cursoP):
    global janelaProva
    pontuacao = calcular_pontuacao(variaveis_resposta)

    janelaResultProva = tkinter.Toplevel()
    janelaResultProva.title("Resultado")
    janelaResultProva.resizable(False, False)

    cursor.execute("INSERT INTO Participantes (nomeP, nota, cursoP) VALUES (?, ?, ?)",
                   (assinaturaNome.get(), pontuacao, cursoP.get()))
    connection.commit()

    label_pontuacao = tkinter.Label(
        janelaResultProva, text=f"""Prova Concluída, Parabéns pelo esforço {assinaturaNome.get()}!""", font="Consolas 13 bold")
    label_pontuacao.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

    image1 = Image.open("Arquivos\logoEstacio.png")
    width, height = 450, 300
    image1.thumbnail((width, height))
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(janelaResultProva, image=test)
    label1.image = test
    label1.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

    label_pontuacao = tkinter.Label(
        janelaResultProva, text=f"Sua Pontuação Final: {pontuacao}/3",font="Consolas 10")
    label_pontuacao.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

    botao_Resposta = tkinter.Button(
        janelaResultProva, text="Resolução das Questões", bg="#009FD6", fg="white", font="Consolas 10",command=ResolucaoProva)
    botao_Resposta.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

    button = tkinter.Button(janelaResultProva, text="Tela Inicial", bg="#009FD6", fg="white",font="Consolas 10", command=lambda: [
                            (janelaResultProva.destroy()), root.deiconify(), janelaProva.destroy()])
    button.grid(row=4, column=0, padx=10, pady=10, sticky='ew')

    button = tkinter.Button(janelaResultProva, text="Sair do Programa", bg="#009FD6",
                            fg="white", font="Consolas 10",command=lambda: [(janelaResultProva.destroy()), janelaProva.destroy()])
    button.grid(row=5, column=0, padx=10, pady=10, sticky='ew')


def calcular_pontuacao(variaveis_resposta):
    pontuacao = 0

    # Recuperar as respostas corretas do banco de dados
    cursor.execute("SELECT resposta FROM Questoes")
    respostas_corretas = [resposta[0] for resposta in cursor.fetchall()]

    # print("Respostas Corretas:", respostas_corretas)

    for i, resposta_selecionada in enumerate(variaveis_resposta):
        # print("Resposta Selecionada:", resposta_selecionada.get())
        # print("Resposta Correta:", respostas_corretas[i])

        if resposta_selecionada.get() == respostas_corretas[i]:
            pontuacao += 1

    # print("Pontuação Final:", pontuacao)
    return pontuacao

# TELA DO GABARITO
def ResolucaoProva():
    janelaRespProva = tkinter.Toplevel()
    janelaRespProva.title("Gabarito")
    janelaRespProva.resizable(False, False)

    # Questão 1
    label = tkinter.Label(
        janelaRespProva, text="Questão 1) Escolha o resultado da seguinte operação: Integral de 2x dx")
    label.grid(row=0, column=0, padx=10, pady=10)

    image1 = Image.open("q1.jpg")
    width, height = 200, 200
    image1.thumbnail((width, height))
    test1 = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(janelaRespProva, image=test1)
    label1.image = test1
    label1.grid(row=1, column=0, padx=10, pady=10)

    # Questão 2
    label2 = tkinter.Label(
        janelaRespProva, text="Questão 2) Calcule a derivada da seguinte função: f(x) = 2x+1")
    label2.grid(row=2, column=0, padx=10, pady=10)

    image2 = Image.open("q2.jpg")
    image2.thumbnail((width, height))
    test2 = ImageTk.PhotoImage(image2)
    label2 = tkinter.Label(janelaRespProva, image=test2)
    label2.image = test2
    label2.grid(row=3, column=0, padx=10, pady=10)

    # Questão 3
    label3 = tkinter.Label(
        janelaRespProva, text="Questão 3) A área de um triângulo que possui 12 cm de altura e base medindo 9 cm é:")
    label3.grid(row=4, column=0, padx=10, pady=10)

    image3 = Image.open("q3.jpg")
    image3.thumbnail((width, height))
    test3 = ImageTk.PhotoImage(image3)
    label3 = tkinter.Label(janelaRespProva, image=test3)
    label3.image = test3
    label3.grid(row=5, column=0, padx=10, pady=10)

    button = tkinter.Button(janelaRespProva, text="Fechar", bg="#009FD6",
                            fg="white", command=lambda: janelaRespProva.destroy())
    button.grid(row=6, column=1, padx=10, pady=10, sticky='ew')


telaInicial()

cursor.execute("SELECT * from Participantes")
row = cursor.fetchall()
print(row)

finalizarProva()