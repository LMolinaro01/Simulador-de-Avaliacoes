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

def InserirQuestao(enunciado, resposta, alternativa2, alternativa3, alternativa4, ID):
    query = "SELECT * FROM Questoes WHERE enunciado=?"
    cursor.execute(query, (enunciado,))
    if not cursor.fetchone():  
        cursor.execute("INSERT INTO Questoes (enunciado, resposta, alternativa2, alternativa3, alternativa4, ID) VALUES (?, ?, ?, ?, ?, ?)",
                       (enunciado, resposta, alternativa2, alternativa3, alternativa4, ID))
        connection.commit()
    else:
        print("A questão já existe na base de dados.")

InserirQuestao("Escolha o resultado da seguinte operação: Integral de 2x dx",
                "x² + c", "2x²", "x²/3 + c", "x²/2 + c", "1")
InserirQuestao("Calcule a derivada da seguinte função: f(x) = 2x+1",
                "2", "2x", "x + 1", "x/2", "2")
InserirQuestao("A área de um triângulo que possui 12 cm de altura e base medindo 9 cm é:",
                "54 cm²", "70 cm²", "85 cm²", "108 cm²", "3")
connection.commit()

def Center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frmWidth = win.winfo_rootx() - win.winfo_x()
    winWidth = width + 2 * frmWidth
    height = win.winfo_height()
    titlebarHeight = win.winfo_rooty() - win.winfo_y()
    winHeight = height + titlebarHeight + frmWidth
    x = win.winfo_screenwidth() // 2 - winWidth // 2
    y = win.winfo_screenheight() // 2 - winHeight // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def TelaInicial():
    global root
    root = tkinter.Tk()
    root.title("Página Inicial")
    root.resizable(False, False)
    root.geometry("400x600")

    Center(root)

    label = tkinter.Label(root, text="Bem vindo ao Simulador de Avaliações!", font="Consolas 13 bold")
    label.grid(row=0, column=1, pady=10)

    image1 = Image.open("Arquivos\logoEstacio2.png")
    width, height = 400, 300
    image1.thumbnail((width, height))
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(root, image=test)
    label1.image = test
    label1.grid(row=1, column=1, pady=10, padx=47)

    button = tkinter.Button(root, text="Cadastre-se",
                            bg="#009FD6", fg="white", command=AbrirJanelaAluno)
    button.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

    botaoProva = tkinter.Button(
        root, text="Realizar Prova", bg="#009FD6", fg="white", command=ValidarJanelaProva)
    botaoProva.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    botaoTabela = tkinter.Button(
        root, text="Ver Pontuações", bg="#009FD6", fg="white", command=ExibirTabelaParticipantes)
    botaoTabela.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

    button = tkinter.Button(root, text="Sair do Programa",
                            bg="#009FD6", fg="white", command=lambda: root.destroy())
    button.grid(row=5, column=1, padx=10, pady=10,
                sticky='e')

    root.mainloop()

def ExibirTabelaParticipantes():
    global root
    root.withdraw()

    root.resizable(False, False)

    janelaTabela = tkinter.Toplevel()
    janelaTabela.title("Tabela de Participantes")

    cursor.execute("SELECT * FROM Participantes")
    dados = cursor.fetchall()

    tabela = tkinter.Frame(janelaTabela)
    tabela.grid(row=0, column=0, padx=10, pady=10)

    tv = tkinter.ttk.Treeview(tabela, columns=(
        'Nome', 'Curso', 'Pontuação'), show='headings')
    tv.heading('Nome', text='Nome')
    tv.heading('Curso', text='Curso')
    tv.heading('Pontuação', text='Pontuação')

    for linha in dados:
        tv.insert('', 'end', values=(linha[0], linha[2], linha[1]))

    tv.pack()

    botaoFechar = tkinter.Button(janelaTabela, text="Voltar", bg="#009FD6", fg="white", command=lambda: [
                                  janelaTabela.destroy(), root.deiconify()])
    botaoFechar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

def AbrirJanelaAluno():
    global root
    root.withdraw()
    JanelaAluno()

def JanelaAluno():
    global root
    root.withdraw()

    global janela2
    janela2 = tkinter.Tk()
    janela2.geometry("378x380")
    janela2.resizable(False, False)

    janela2.title("Cadastro Aluno")

    Center(janela2)

    label = tkinter.Label(
        janela2, text="Preencha os campos a seguir", font="Consolas 13 bold")
    label.grid(row=0, column=1, pady=10, sticky='ew')

    labelNome = tkinter.Label(janela2, text="Nome:")
    labelNome.grid(row=1, column=0, padx=10, pady=15, sticky='ew')
    textoNome = tkinter.StringVar()
    nome = tkinter.Entry(janela2, textvariable=textoNome)
    nome.grid(row=1, column=1, padx=10, pady=15, sticky='ew')

    labelSenha = tkinter.Label(janela2, text="Senha:")
    labelSenha.grid(row=2, column=0, padx=10, pady=15, sticky='ew')
    textoSenha = tkinter.StringVar()
    senha = tkinter.Entry(janela2, textvariable=textoSenha, show="*")
    senha.grid(row=2, column=1, padx=8, pady=15, sticky='ew')

    botaoCadastrar = tkinter.Button(janela2, text="Cadastre-se", bg="#009FD6",
                                     fg="white", command=lambda: VerificarCadastroAluno(nome.get(), senha.get()))
    botaoCadastrar.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    botaoVoltar = tkinter.Button(janela2, text="Voltar para Tela Inicial",
                                  bg="#009FD6", fg="white", command=lambda: VoltarTelaInicialCadastro(janela2))
    botaoVoltar.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

def VoltarTelaInicialCadastro(janela2):
    janela2.destroy()
    root.deiconify()

def AdicionarAluno(nome, senha):
    caracteresEspeciais = ";-'!+@#$%&*().=[]}`{|,"
    if any(caracter in caracteresEspeciais for caracter in str(nome) + str(senha)):
        print("Caracteres especiais não são permitidos.")
    else:
        cursor.execute(
            "INSERT INTO Alunos (nome, senha) VALUES (?, ?)", (nome, senha))
        connection.commit()

def VerificarLogin(nome, senha):
    query = "SELECT * FROM Alunos WHERE nome=? AND senha=?"
    cursor.execute(query, (nome, senha))
    aluno = cursor.fetchone()

    caracteresEspeciais = ";-'!+@#$%&*().=[]}`{|,"
    if any(caracter in caracteresEspeciais for caracter in str(nome) + str(senha)):
        mb.showinfo("Aviso", "Caracteres especiais não são permitidos.")

    elif not (nome and senha):
        mb.showinfo("Aviso", "O campo não pode ficar em branco.")

    elif aluno:
        AbrirJanelaProva()
    else:
        mb.showinfo("Aviso", "Credenciais inválidas.")

def VerificarCadastroAluno(nome, senha):
    global janela2
    caracteresEspeciais = ";-'!+@#$%&*().=[]}`{|,"
    if any(caracter in caracteresEspeciais for caracter in str(nome) + str(senha)):
        mb.showinfo("Aviso", "Caracteres especiais não são permitidos.")

    elif not (nome and senha):
        mb.showinfo("Aviso", "O campo não pode ficar em branco.")

    else:
        mb.showinfo

("Aviso", "Usuário cadastrado com sucesso!")
        AdicionarAluno(nome, senha)
        nome = ''
        senha = ''

def ValidarJanelaProva():
    global root
    root.withdraw()
    JanelaLogin()

def JanelaLogin():
    global root
    global janela3
    janela3 = tkinter.Toplevel()
    janela3.geometry("350x350")
    janela3.resizable(False, False)
    janela3.title("Login Aluno")

    Center(janela3)

    label = tkinter.Label(
        janela3, text="Informe os dados a seguir", font="Consolas 13 bold")
    label.grid(row=0, column=1, pady=10)

    labelNome = tkinter.Label(janela3, text="Nome:")
    labelNome.grid(row=1, column=0, padx=10, pady=15, sticky='ew')
    textoNome = tkinter.StringVar()
    nome = tkinter.Entry(janela3, textvariable=textoNome)
    nome.grid(row=1, column=1, padx=10, pady=15, sticky='ew')

    labelSenha = tkinter.Label(janela3, text="Senha:")
    labelSenha.grid(row=2, column=0, padx=10, pady=15, sticky='ew')
    textoSenha = tkinter.StringVar()
    senha = tkinter.Entry(janela3, textvariable=textoSenha, show="*")
    senha.grid(row=2, column=1, padx=8, pady=15, sticky='ew')

    button = tkinter.Button(janela3, text="Logar", bg="#009FD6",
                            fg="white", command=lambda: VerificarLogin(nome.get(), senha.get()))
    button.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

    botaoVoltar = tkinter.Button(janela3, text="Voltar para Tela Inicial",
                                  bg="#009FD6", fg="white", command=lambda: VoltarTelaInicialLogin(janela3))
    botaoVoltar.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

def VoltarTelaInicialLogin(janela3):
    janela3.destroy()
    root.deiconify()

def AbrirJanelaProva():
    global janelaProva
    global janela3
    global root
    janela3.destroy()
    janelaProva = tkinter.Tk()
    janelaProva.geometry("500x500")
    janelaProva.title("Prova")
    janelaProva.resizable(False, False)

    global NomeProva
    NomeProva = ""

    label = tkinter.Label(janelaProva, text="Insira seu Nome:", font="Consolas 13 bold")
    label.grid(row=0, column=1, pady=10, sticky='ew')

    labelNome = tkinter.Label(janelaProva, text="Nome:")
    labelNome.grid(row=1, column=0, padx=10, pady=15, sticky='ew')
    textoNome = tkinter.StringVar()
    nome = tkinter.Entry(janelaProva, textvariable=textoNome)
    nome.grid(row=1, column=1, padx=10, pady=15, sticky='ew')

    labelCurso = tkinter.Label(janelaProva, text="Curso:")
    labelCurso.grid(row=2, column=0, padx=10, pady=15, sticky='ew')
    textoCurso = tkinter.StringVar()
    curso = tkinter.Entry(janelaProva, textvariable=textoCurso)
    curso.grid(row=2, column=1, padx=10, pady=15, sticky='ew')

    button = tkinter.Button(janelaProva, text="Iniciar Prova", bg="#009FD6",
                            fg="white", command=lambda: IniciarProva(janelaProva, nome.get(), curso.get()))
    button.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

def IniciarProva(janelaProva, nome, curso):
    global NomeProva
    global CursoProva
    NomeProva = nome
    CursoProva = curso
    if not (nome and curso):
        mb.showinfo("Aviso", "O campo não pode ficar em branco.")
    else:
        janelaProva.withdraw()
        JanelaQuestoes()

def JanelaQuestoes():
    global janelaQuestoes
    global janelaProva
    global root

    janelaQuestoes = tkinter.Tk()
    janelaQuestoes.geometry("600x400")
    janelaQuestoes.resizable(False, False)
    janelaQuestoes.title("Questões")

    cursor.execute("SELECT * FROM Questoes")
    dadosQuestoes = cursor.fetchall()
    global questaoAtual
    questaoAtual = 0
    global score
    score = 0

    random.shuffle(dadosQuestoes)
    ExibirQuestao(janelaQuestoes, dadosQuestoes)

def ExibirQuestao(janelaQuestoes, dadosQuestoes):
    global questaoAtual
    global score
    if questaoAtual < len(dadosQuestoes):
        questao = dadosQuestoes[questaoAtual]
        questaoAtual += 1

        labelQuestao = tkinter.Label(
            janelaQuestoes, text=questao[0], font="Consolas 12 bold")
        labelQuestao.pack(pady=20)

        alternativa1 = tkinter.Button(janelaQuestoes, text=questao[1], command=lambda: VerificarResposta(
            janelaQuestoes, questao[1], questao[1], dadosQuestoes))
        alternativa1.pack(pady=5)

        alternativa2 = tkinter.Button(janelaQuestoes, text=questao[2], command=lambda: VerificarResposta(
            janelaQuestoes, questao[1], questao[2], dadosQuestoes))
        alternativa2.pack(pady=5)

        alternativa3 = tkinter.Button(janelaQuestoes, text=questao[3], command=lambda: VerificarResposta(
            janelaQuestoes, questao[1], questao[3], dadosQuestoes))
        alternativa3.pack(pady=5)

        alternativa4 = tkinter.Button(janelaQuestoes, text=questao[4], command=lambda: VerificarResposta(
            janelaQuestoes, questao[1], questao[4], dadosQuestoes))
        alternativa4.pack(pady=5)
    else:
        FinalizarProva()

def VerificarResposta(janelaQuestoes, respostaCorreta, respostaEscolhida, dadosQuestoes):
    global score
    if respostaCorreta == respostaEscolhida:
        score += 1
    for widget in janelaQuestoes.winfo_children():
        widget.destroy()
    ExibirQuestao(janelaQuestoes, dadosQuestoes)

def FinalizarProva():
    global janelaQuestoes
    global NomeProva
    global CursoProva
    global score

    cursor.execute("INSERT INTO Participantes (nomeP, nota, cursoP) VALUES (?, ?, ?)",
                   (NomeProva, score, CursoProva))
    connection.commit()

    for widget in janelaQuestoes.winfo_children():
        widget.destroy()

    labelFinal = tkinter.Label(janelaQuestoes, text=f"Prova Finalizada! Pontuação: {score}", font="Consolas 13 bold")
    labelFinal.pack(pady=20)

    button = tkinter.Button(janelaQuestoes, text="Voltar para Tela Inicial", bg="#009FD6",
                            fg="white", command=lambda: VoltarTelaInicialProva(janelaQuestoes))
    button.pack(pady=10)

def VoltarTelaInicialProva(janelaQuestoes):
    global root
    janelaQuestoes.destroy()
    root.deiconify()

TelaInicial()
