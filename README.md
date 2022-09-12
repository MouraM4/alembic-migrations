### Migrações de Banco de Dados com Python e Alembic!

1. Criar um modelo e iniciar: 
    * ```alembic init <alembic_folder_name>```
    * Uma pasta será criada com o nome passado como argumento para o alembic init, no geral, usa-se o nome **alembic**
    * No arquivo *alembic.ini* devemos informar a url do banco no parâmetro *sqlalchemy.url*.

2. Com os arquivos do alembic criados, devemos criar a primeira migração:
    * ```alembic revision -m "primeira"```
    * Podemos alterar as funções **upgrade** e **downgrade** presentes no arquivo criado no diretório **version** com os comandos a serem executados na migração.

3. Realizar a migração com os comandos
    * **upgrade**: ```alembic upgrade head``` ou ```alembic upgrade +1```
    * **downgrade**: ```alembic downgrade base``` ou ```alembic downgrade -1``` 

### Gerar modelos ORM a partir de um DB já existente:

1. Instalar a biblioteca sqlacodegen: 
    * ```pip install sqlacodegen```

2. Gerar os modelos a partir de um DB
    * ```sqlacodegen sqlite:///local_db.db > models.py```
    * Outros tipos de schemas: https://pypi.org/project/sqlacodegen/

3. Ao gerar o script **models.py**, devemos referenciar o ORM gerado no arquivo **alembic/env.py** da seguinte maneira:
    * No arquivo env.py, importar o objeto Base do arquivo models com o seguinte comando:
        * ```from models import Base```
    * alterar o target_metadata para ```target_metadata = Base.metadata```

4. Incluir os seguintes parâmetros no *context.configure* das funções *run_migrations_offline()* e *run_migrations_online()*:
    * ```compare_type=True```
    * ```render_as_batch=True```

5. Agora, podemos criar mais modelos no arquivo **models.py** que as migrações serão geradas automaticamente criando novas **revisions** com o seguinte comando:
    * alembic revision --autogenerate -m "novo modelo criado ou atualizado"

6. Com isso, uma nova versão é adicionada automaticamente com a query necessária para adicionar as alterações.

7. Agora, precisamos executar o comando ```alembic upgrade +1``` ou ```alembic upgrade head``` para ir para nova revisão.
