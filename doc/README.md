# Instrucoes

## Estrutura de pastas da api
-   Main.py → é o maestro, quem organiza a brincadeira.

-   Database.py → é o motor que fala com o banco de dados (o “baú” onde os bonecos ficam guardados).

-   Models → descrevem como é cada boneco (ex.: Student tem id, nome, curso).

-   Schema → descreve como você conta para os outros como é o boneco (ex.: quando alguém pede um estudante, você mostra esses campos).

-   Service → é quem sabe mexer nos bonecos dentro do baú (buscar, criar, atualizar, deletar).

-   Router → é a ponte entre quem pede (a API) e quem sabe mexer (o Service).

- Script para teste das apis, recurso.rest → é o caderno de instruções, mostrando como pedir os bonecos pela internet.


## 🧩 Como cada parte funciona
-       1. Main.py
    -   Cria o aplicativo FastAPI (app = FastAPI()).
    -   Cria a conexão com o banco (db = SessionLocal()).
    -   Junta o service e o router para formar as rotas /student.
    -   Diz: “Se alguém pedir /student, use esse roteador”.
    -   👉 É como o mapa da brincadeira.

-       2. Database.py
    -   Pega a URL do banco (DATABASE_URL).
    -   Cria o motor (engine) que abre e fecha o baú.
    -   Cria a sessão (SessionLocal) para conversar com o baú.
    -   Cria a base (Base) para os modelos.
    -   👉 É como o baú de brinquedos onde os estudantes ficam guardados.

-       3. Schema (StudentData)
    -   Diz quais informações um estudante tem: id, nome, matrícula, curso, ativo.
    -   Usa orm_mode = True para poder transformar o boneco do banco em resposta JSON.
    -   👉 É como a ficha de cada boneco.

-       4. Model (Student)
    -   Define a tabela students no banco.
    -   Cada coluna é um campo: id, nome, matrícula, curso, ativo.
    -   👉 É como o molde dos bonecos dentro do baú.

-       5. Service (StudentService)
    -   Tem métodos para:
    -   getAll → pegar todos os bonecos ativos.
    -   getById → pegar um boneco específico.
    -   post → criar um novo boneco.
    -   put → atualizar um boneco.
    -   delete → marcar boneco como “N” (não ativo).
    -   👉 É como o amigo que sabe mexer dentro do baú.

-       6. Router (StudentRouter)
    -   Recebe pedidos da API e chama o Service.
    -   Exemplo: se alguém faz GET /student, o Router chama service.getAll().
    -   👉 É como a ponte entre quem pede e quem mexe no baú.

-       7. recursos.rest (documentação)
    -   Mostra exemplos de como pedir os bonecos pela internet:
    -   GET /student → lista todos.
    -   GET /student/1 → pega o boneco 1.
    -   POST /student → cria novo boneco.
    -   PUT /student/11 → atualiza boneco 11.
    -   DELETE /student/6 → remove boneco 6.
    -   👉 É como o manual de instruções da brincadeira.

-       🎯 Resumindo
    -   Main.py → organiza tudo.
    -   Database.py → conecta ao baú (banco).
    -   Model → define como é o boneco.
    -   Schema → define como mostrar o boneco.
    -   Service → sabe mexer nos bonecos.
    -   Router → leva os pedidos até o Service.
    -   .rest → mostra exemplos de como brincar.