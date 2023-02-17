# Job Insights - Trybe Project
<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto no qual você pode customizar e reutilizar todas as vezes que for executar o trybe-publisher.

Para deixá-lo com a sua cara, basta alterar o seguinte arquivo da sua máquina: ~/.student-repo-publisher/custom/_NEW_README.md

É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->
This project uses Python implements analysis based on a set of job data incorporated to a web app developed using Flask framework.

I had to write functions, tests and implement a route using Flask.

# Functions
The functions are in three files:
```bash
src/insights/industries.py
```
```bash
src/insights/jobs.py
```
```bash
src/insights/salaries.py
```
# Tests
The tests I implemented are in these files:
```bash
tests/brazilian/test_brazilian_jobs.py
```
```bash
tests/counter/test_counter.py
```
```bash
tests/sorting/test_sorting.py
```

# Flask Route
The Flask route I implemented is ```/jobs/<index> ``` is in the file:
```bash
src/flask_app/routes_and_views.py
```

# Running the app
<li>Clone repository</li>
<li>Create and run virtual environment</li>
[python3 -m .venv && source .venv/bin/activate]
<li>Install dependencies</li>
[python3 -m pip install -r dev-requirements.txt]
<li>Run app on web browser</li>
[flask run] and access [http://localhost:5000]
<li>Run tests</li>
[python3 -m pytest]
