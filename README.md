# Simulador de Avaliações

Esse Projeto foi iniciado e desenvolvido em um outro repositório de minha autoria [Exercicios e Projetos em Python](https://github.com/LMolinaro01/Exercicios-e-Projetos-em-Python). Portanto, as commits iniciais estão armazenadas nele.

## Execução do Programa:
  
<p align="center">
  <a href="https://www.youtube.com/watch?v=2irwlujDGsA" target = "_blank">
    <img src="https://img.youtube.com/vi/2irwlujDGsA/0.jpg" alt="Video no Youtube">
  </a>
</p>

---

O código fonte em Python representa um sistema que simula avaliações, oferecendo uma gama de funcionalidades essenciais para uma experiência de usuário completa e segura. Vou detalhar suas principais características e destacar suas medidas de segurança e validação:

1. **Banco de Dados SQLite com Prevenção contra SQL Injection**: Utilizando um banco de dados SQLite3, o programa armazena localmente informações, como dados dos alunos, senhas, questões da prova e pontuações. Além disso, implementa medidas eficazes para prevenir ataques de [*SQL Injection*](#sqlinjection), garantindo a integridade dos dados.

2. **Interface Gráfica com Tkinter**: Desenvolvido com [Tkinter](#tkinter), o programa oferece uma interface gráfica intuitiva e agradável, facilitando a interação do usuário em todas as etapas do processo, desde o cadastro até a visualização das pontuações.

3. **Cadastro Seguro com Validações**: A função de cadastro foi projetada com validações abrangentes para garantir a integridade dos dados. Além de evitar campos vazios, o sistema realiza verificações minuciosas para detectar e prevenir a inserção de caracteres especiais, protegendo contra possíveis vulnerabilidades como injeção de SQL.

4. **Cálculo Automático de Pontuações**: Após a conclusão da prova, o programa realiza o cálculo automático da pontuação do aluno, baseando-se nas respostas fornecidas de forma precisa e confiável.

5. **Exibição de Respostas e Gabaritos**: A exibição das respostas corretas e do gabarito é feita de maneira segura, garantindo que apenas os alunos autorizados tenham acesso a essas informações após a conclusão da prova. Além disso, há um passo a passo de como solucionar cada questão.

6. **Manipulação de Imagens com PIL**: Para uma experiência visual aprimorada, o programa utiliza a biblioteca [PIL](#pil) para manipular e exibir imagens, como o logo da instituição, garantindo uma apresentação visual atraente e profissional.

7. **Cadastro de Questões**: O código possui uma função que permite adicionar questões ao banco de dados.


Em resumo, este código implementa um sistema completo de simulador de avaliações, desde o cadastro de alunos até a realização e correção de provas, utilizando uma interface gráfica simples e agradável.

---

### Glossário:

- *SQL Injection*<a name="biblioteca-de-filmes"></a>: é uma técnica maliciosa utilizada por hackers para explorar vulnerabilidades em sistemas de bancos de dados. Imagine que um banco de dados é como uma gaveta cheia de informações organizadas em fichas. Com o SQL Injection, um invasor consegue inserir códigos maliciosos, como se fossem notas falsas, na caixa de busca dessa gaveta. Assim, ele pode enganar o sistema e obter acesso não autorizado a dados confidenciais ou até mesmo manipular, editar ou excluir informações importantes. É como se alguém conseguisse acesso à sua gaveta de informações secretas, mexesse em papéis importantes e até mesmo adicionasse ou removesse alguns, tudo sem você perceber. Por isso, é essencial que os sistemas tenham medidas de segurança para prevenir esse tipo de ataque.

---

- *PIL*<a name="pil"></a>: (Python Imaging Library) é uma biblioteca de processamento de imagens para Python. Com o PIL, os desenvolvedores podem realizar uma ampla variedade de operações em imagens, como abrir, editar, converter formatos, redimensionar, cortar, aplicar filtros, entre outras. Essa biblioteca é especialmente útil para aplicações que lidam com manipulação de imagens, como processamento de fotos digitais, reconhecimento de padrões, processamento de documentos, entre outros. O PIL oferece uma interface fácil de usar para realizar essas operações de forma eficiente, permitindo aos desenvolvedores criar e personalizar imagens de maneira flexível e poderosa.
---

- *Tkinter*<a name="tkinter"></a>: Tkinter é uma biblioteca padrão do Python usada para criar interfaces gráficas de usuário (GUI). Com Tkinter, os desenvolvedores podem criar janelas, botões, caixas de texto e outros elementos de interface de forma intuitiva. É uma ferramenta versátil que simplifica o desenvolvimento de aplicativos com uma interface de usuário interativa. Tkinter fornece uma maneira eficiente de criar aplicativos desktop com Python, permitindo aos desenvolvedores concentrarem-se na lógica do programa enquanto a biblioteca cuida da apresentação visual.
