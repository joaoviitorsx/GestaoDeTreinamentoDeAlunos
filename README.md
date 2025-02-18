Projeto de Gestão de Treinamento de Alunos
Esta é uma aplicação web desenvolvida com o framework Django para gerenciar o progresso de alunos em um sistema de treinamento. A aplicação possibilita a criação, listagem e atualização de informações dos alunos, além do registro de aulas concluídas e o cálculo do progresso dos alunos em relação às suas graduações.

Visão Geral
O sistema tem como objetivo central auxiliar no gerenciamento do treinamento dos alunos, permitindo:

Criação e gerenciamento de alunos: Cadastro de informações básicas, como nome, email, data de nascimento e faixa.
Registro de aulas concluídas: Armazenamento das aulas realizadas por cada aluno, com a data e a faixa atual.
Cálculo de progresso: Cálculo e exibição do progresso dos alunos com base nas aulas registradas e nas graduações alcançadas.
Estrutura do Projeto
O projeto está organizado em dois diretórios principais: core e treino.

Diretório core
settings.py
Configurações do projeto, incluindo banco de dados, aplicativos instalados, middleware, etc.
urls.py
Define as rotas principais, incluindo a rota para a administração do Django e a rota para a API.
wsgi.py
Configuração do WSGI para implantação do projeto.
asgi.py
Configuração do ASGI, voltada para aplicações assíncronas.
api.py
Configuração da API utilizando o Ninja API, definindo o roteador principal.
Diretório treino
models.py
Define os modelos Alunos e AulasConcluidas, que representam os dados dos alunos e das aulas concluídas, respectivamente.
schemas.py
Define os esquemas para a API: AlunosSchema, ProgressoAlunoSchema e AulaRealizadaSchema.
api.py
Implementa as rotas e a lógica da API, com endpoints para criação, listagem e atualização de alunos, registro de aulas concluídas e cálculo do progresso.
admin.py
Registra os modelos no admin do Django.
apps.py
Configuração do aplicativo treino.
views.py
Define as views (não utilizado neste projeto).
tests.py
Contém testes (não utilizado neste projeto).
graduacao.py
Funções auxiliares para o cálculo de progresso dos alunos.
Funcionalidades e Endpoints da API
Modelos
Alunos:
Representa os alunos do sistema, com campos para nome, email, data de nascimento e faixa.
AulasConcluidas:
Representa as aulas concluídas, com campos para o aluno, data e faixa atual.
Esquemas
AlunosSchema:
Esquema para representar os dados dos alunos na API.
ProgressoAlunoSchema:
Esquema para representar o progresso dos alunos.
AulaRealizadaSchema:
Esquema para representar o registro das aulas realizadas.
Endpoints da API
Criar Aluno

Método: POST /api/
Request Body: AlunosSchema
Response: AlunosSchema
Descrição: Cria um novo aluno no sistema.
Listar Alunos

Método: GET /api/alunos/
Response: Lista de AlunosSchema
Descrição: Retorna todos os alunos cadastrados.
Progresso do Aluno

Método: GET /api/progresso_aluno/
Query Param: email_aluno
Response: ProgressoAlunoSchema
Descrição: Calcula e retorna o progresso de um aluno específico.
Registrar Aula Realizada

Método: POST /api/aula_realizada/
Request Body: AulaRealizadaSchema
Response: ProgressoAlunoSchema
Descrição: Registra uma ou mais aulas realizadas por um aluno.
Atualizar Aluno

Método: PUT /api/alunos/{aluno_id}
Request Body: AlunosSchema
Response: AlunosSchema
Descrição: Atualiza as informações de um aluno específico.
