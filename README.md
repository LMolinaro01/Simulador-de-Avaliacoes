# Simulador de Avaliações

Este código em Python representa um sistema que simula avaliações, oferecendo uma gama de funcionalidades essenciais para uma experiência de usuário completa e segura. Vou detalhar suas principais características e destacar suas medidas de segurança e validação:

1. **Banco de Dados SQLite com Prevenção contra SQL Injection**: Utilizando um banco de dados SQLite3, o programa armazena localmente informações, como dados dos alunos, senhas, questões da prova e pontuações. Além disso, implementa medidas eficazes para prevenir ataques de [*SQL Injection*](#sqlinjection), garantindo a integridade dos dados.

2. **Interface Gráfica com Tkinter**: Desenvolvido com [Tkinter](#tkinter), o programa oferece uma interface gráfica intuitiva e agradável, facilitando a interação do usuário em todas as etapas do processo, desde o cadastro até a visualização das pontuações.

3. **Cadastro Seguro com Validações**: A função de cadastro foi projetada com validações abrangentes para garantir a integridade dos dados. Além de evitar campos vazios, o sistema realiza verificações minuciosas para detectar e prevenir a inserção de caracteres especiais, protegendo contra possíveis vulnerabilidades como injeção de SQL.

4. **Cálculo Automático de Pontuações**: Após a conclusão da prova, o programa realiza o cálculo automático da pontuação do aluno, baseando-se nas respostas fornecidas de forma precisa e confiável.

5. **Exibição de Respostas e Gabaritos**: A exibição das respostas corretas e do gabarito é feita de maneira segura, garantindo que apenas os alunos autorizados tenham acesso a essas informações após a conclusão da prova. Além disso, há um passo a passo de como solucionar cada questão.

6. **Manipulação de Imagens com PIL**: Para uma experiência visual aprimorada, o programa utiliza a biblioteca [PIL](#pil) para manipular e exibir imagens, como o logo da instituição, garantindo uma apresentação visual atraente e profissional.

7. **Cadastro de Questões**: O código possui uma função que permite adicionar questões ao banco de dados.

8. **Telas Principais**:
   - **Tela Inicial**: Apresenta as opções principais, como cadastro, realização de prova e visualização de pontuações.
     
    ![image](https://github.com/LMolinaro01/Projetos-em-Python/assets/126402616/2da75ebb-a158-40aa-a7a0-663efd4aedb2)

    ---
   
   - **Tela de Cadastro**: Permite que novos alunos se cadastrem fornecendo nome e senha.
     
    ![image](https://github.com/LMolinaro01/Projetos-em-Python/assets/126402616/ccc186f5-f629-465a-a9f4-5c38221e4d62)
    ![image](https://github.com/LMolinaro01/Projetos-em-Python/assets/126402616/33a2e786-b71c-4dba-af98-3b729cf8aab0)
    ![image](https://github.com/LMolinaro01/Projetos-em-Python/assets/126402616/c6e5171f-1508-42d3-b2cf-0a7ddff16cdf)

    ---
   
   - **Tela de Login**: Permite que alunos cadastrados realizem login para acessar a prova.
     
     ![image](https://github.com/LMolinaro01/Projetos-em-Python/assets/126402616/c4da515d-d84f-4f75-bef0-543bb9c7ce8e)

     ---
     
   - **Tela da Prova**: Apresenta as questões da prova, permitindo que o aluno selecione suas respostas.
     
     ![image](https://github.com/LMolinaro01/Projetos-em-Python/assets/126402616/ee72ebd3-6862-46e1-a6bb-ebd0dd0000c4)
     
     ![image](https://github.com/LMolinaro01/Projetos-em-Python/assets/126402616/3f36950d-0207-4ee1-8b45-fa7c0e1a95cf)

     ---
     
   - **Tela de Resultado**: Após finalizar a prova, exibe a pontuação obtida e oferece opções para visualizar a resolução das questões ou voltar para a tela inicial.

     ![image](https://github.com/LMolinaro01/Projetos-em-Python/assets/126402616/426387dd-2aee-4bf7-a5c7-3f37d9e5b5c2)

      ---
     
   - **Tela de Gabarito/Resolução**: Apresenta as questões da prova com as respostas corretas após a conclusão da prova.

     ![image](https://github.com/LMolinaro01/Projetos-em-Python/assets/126402616/ffb947b7-6e99-4873-a20f-6ea5b61729b6)

      ---
     
   - **Tela de Pontuações**: Exibe a pontuação dos alunos.

     ![image](https://github.com/LMolinaro01/Projetos-em-Python/assets/126402616/0c8a791c-6b6e-4b28-ba16-7d3a1b14a3e3)

      ---

Em resumo, este código implementa um sistema completo de simulador de avaliações, desde o cadastro de alunos até a realização e correção de provas, utilizando uma interface gráfica simples e agradável.

---

### Glossário:

- *SQL Injection*<a name="biblioteca-de-filmes"></a>: é uma técnica maliciosa utilizada por hackers para explorar vulnerabilidades em sistemas de bancos de dados. Imagine que um banco de dados é como uma gaveta cheia de informações organizadas em fichas. Com o SQL Injection, um invasor consegue inserir códigos maliciosos, como se fossem notas falsas, na caixa de busca dessa gaveta. Assim, ele pode enganar o sistema e obter acesso não autorizado a dados confidenciais ou até mesmo manipular, editar ou excluir informações importantes. É como se alguém conseguisse acesso à sua gaveta de informações secretas, mexesse em papéis importantes e até mesmo adicionasse ou removesse alguns, tudo sem você perceber. Por isso, é essencial que os sistemas tenham medidas de segurança para prevenir esse tipo de ataque.

---

- *PIL*<a name="pil"></a>: (Python Imaging Library) é uma biblioteca de processamento de imagens para Python. Com o PIL, os desenvolvedores podem realizar uma ampla variedade de operações em imagens, como abrir, editar, converter formatos, redimensionar, cortar, aplicar filtros, entre outras. Essa biblioteca é especialmente útil para aplicações que lidam com manipulação de imagens, como processamento de fotos digitais, reconhecimento de padrões, processamento de documentos, entre outros. O PIL oferece uma interface fácil de usar para realizar essas operações de forma eficiente, permitindo aos desenvolvedores criar e personalizar imagens de maneira flexível e poderosa.
---

- *Tkinter*<a name="tkinter"></a>: Tkinter é uma biblioteca padrão do Python usada para criar interfaces gráficas de usuário (GUI). Com Tkinter, os desenvolvedores podem criar janelas, botões, caixas de texto e outros elementos de interface de forma intuitiva. É uma ferramenta versátil que simplifica o desenvolvimento de aplicativos com uma interface de usuário interativa. Tkinter fornece uma maneira eficiente de criar aplicativos desktop com Python, permitindo aos desenvolvedores concentrarem-se na lógica do programa enquanto a biblioteca cuida da apresentação visual.
