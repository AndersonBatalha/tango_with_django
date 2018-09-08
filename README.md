# Tango With Django - Tutorial

1.  Instalar o pip, gerenciador de pacotes do Python

		$ sudo apt-get install python-pip

2.  Criar o ambiente virtual

	1.  Instalar o pacote virtualenv
	
			$ sudo apt-get install virtualenv virtualenvwrapper

	2. Na pasta do projeto, criar o ambiente virtual
	 
			$ mkvirtualenv -p `which python3` my_env

	3. Ativar / desativar o ambiente virtual
	
			$ source env/bin/activate
			$ deactivate
	
	4. Principais comandos
		
		1. Criar um novo ambiente
			
				$ mkvirtualenv -p `which python` my_env
					   
		2. Listar os ambientes criados
			
				$ lsvirtualenv

		3. Remover
			
				$ rmvirtualenv my_env

		4. Mostrar detalhes do ambiente virtual
			
				$ showvirtualenv env2

		5. Alternar entre ambientes
			
				(env) $ workon env2

3.  Controle de versão
 
	1. Criar repositório no GitHub / Bitbucket
	
	2. Adicionar .gitignore
		1.  http://gitignore.io
	
	3. Alterar arquivo README.md
	
	4. Comandos principais
		1. Obter o status atual do repositório

				$ git status
		2. Adicionar arquivos ao HEAD

				$ git add *
			
		3. Enviar os arquivos ao repositório local

				$ git commit -m "mensagem" 

		4. Enviar os arquivos ao repositório remoto

				$ git push origin master 


4. Gerenciar as dependências do projeto

	1. Listar todas as dependências instaladas
	
			$ pip freeze

	2. Após instalar todos os pacotes necessários, é possível gerar um arquivo com as dependências instaladas.
	
			$ pip freeze > requirements.txt

	3. Caso seja necessário reinstalar esses pacotes em outra máquina, basta executar:
	
			$ pip install -r requirements.txt

5.  Verificar as versões instaladas
	1. Python
	
			$ python --version

	2. Django
	
			$ python -c ‘import django; print (django.get_version())’

6. Criar um projeto Django
	
		$ django-admin startproject my_project
	* troque my_project pelo nome do seu projeto

7. Para executar, entre na pasta onde o projeto Django foi criado e execute:
	
		$ python manage.py runserver

Em seguida, acesse no navegador: 

http://127.0.0.1:8000 ou http://localhost:8000
	
Opcionalmente, você pode substituir pelo IP da sua máquina, fazendo com que seu aplicativo possa ser acessado por outras máquinas

	$ python manage.py runserver http://<seu_endereco_ip>:5555

8.  Criando um aplicativo 

	1. Na mesma pasta onde foi criado o projeto Django deve ser criado o aplicativo.

			$ python manage.py startapp my_app
		
 * troque my_app pelo nome do seu aplicativo

	2. Inclua o aplicativo criado no arquivo de configuração my_project/settings.py
Onde se encontra "INSTALLED_APPS", inserir ao fim da lista:
	
			INSTALLED_APPS = [
				(...)
				'my_app',
			]

	3. Opcional: ainda no arquivo settings.py, é possível alterar o fuso horário e idioma
	
			LANGUAGE_CODE = 'pt-br'
			TIME_ZONE = 'America/Sao_Paulo'

9.  Criando uma view simples: no arquivo my_app/views.py, uma view pode ser criada apenas importando o módulo HttpResponse

		from django.http import HttpResponse
		def index(request):
			return HttpResponse("Olá mundo!")

	* Toda view no Django possui um parâmetro obrigatório: request
	* HttpResponse retorna apenas texto puro
	* existe outra forma de exibir uma view, utilizando a função render() do Django

10. Mapeando URLs: no arquivo my_project/urls.py são configuradas as URLs referentes ao site

Exemplo:

	urlpatterns = [
		url('^$', views.index, name="index"), 
		url('^my_app/', include(my_app.urls)), 
		url('^admin/, admin.site.urls'),
	]


* urlpatterns é uma lista que contém os mapeamentos uma view para uma URL
* views.index se refere a função index() presente no arquivo my_app/views.py
* name é um parâmetro adicional que identifica a view
* expressões regulares:
	^ começa com, $ termina com

	1. Em seguida crie o arquivo my_app/urls.py (na pasta do aplicativo)

			urlpatterns = [
				url('^$', views.index, name="index"), 
			]

11. Implantação

	1. Criar conta no PythonAnywhere
		1. https://www.pythonanywhere.com/
		
	2. Interface do PythonAnywhere
		1. Consoles: criar e gerenciar terminais 
		2. Files: fazer upload e gerenciar o espaço em disco
		3. Web: configurações da aplicação web
		4. Schedule: configurar tarefas a serem executadas em determinados horários
		5. Databases: configuração do banco de dados MySQL
	
	3. Acessar a aba "Consoles" e criar um novo terminal. Neste terminal, criar um novo ambiente virtual (ver item 2)
	
	4. Clonar o repositório
	
			$ git clone <url_do_repositorio>
	
	5. Utilizar o arquivo requirements.txt para instalar os pacotes (ver item 4)
	
	6. Acessar a aba "Web", e alterar as seguintes configurações
		1. Diretório do projeto
		
				~/my_project

		2. Arquivo WSGI
		
				import os
				import sys

				path = '/home/<usuario>/tango_with_django/tango_with_django_project'

				if path not in sys.path:
					sys.path.append(path)
				
				os.environ['DJANGO_SETTINGS_MODULE'] = 'tango_with_django_project.settings'
				
				from django.core.wsgi import get_wsgi_application
				application = get_wsgi_application()
 
		3. Diretório onde está localizado o virtualenv
		
				~/.virtualenvs/my_env

		4. Arquivos estáticos
				
				~/.virtualenvs/rango/lib/<python-version>/site-packages/django/contrib/admin/static/admin

12. Templates

    O uso de templates tem o objetivo de separar a lógica do aplicativo (views e models) da apresentação e aparência (templates).
	
	1.  Criar diretório de templates

        1. No diretório onde está localizado o projeto Django, criar um diretório de nome 'templates'. Dica: encontre o arquivo manage.py
            
                (env) $ mkdir templates
                
        2. Em seguida, crie dentro da pasta templates um diretório de nome 'rango'. Neste diretório serão armazenados os templates do app rango. \* É uma boa prática separar os templates em pastas separadas para cada aplicativo do seu projeto Django

                  (env) $ mkdir templates/rango

	2.  Alterar o arquivo settings.py
	    1. No arquivo settings.py localizar as seguintes linhas e alterar:
			
				TEMPLATES = [
					{
						(...)
						DIRS = [<caminho_da_pasta>/tango_with_django_project/templates]
						(...)
					}
				
				]
	
        2.  A lista DIRS informa ao Django onde os templates estarão armazenados. \* esta não é a maneira correta. Caso este projeto seja utilizado em colaboração por outras pessoas, o caminho da pasta poderá variar. Para resolver esse problema, é possível utilizar as funções do Python para obter o diretório do seu projeto, independente de onde ele esteja.

	3.  Utilizar caminhos relativos
	    1. Criar uma variável TEMPLATE_DIR e alterar a lista DIRS para:
				
                TEMPLATE_DIR = os.path.join(BASE_DIR, "templates") 
                
                TEMPLATES = [
                    {
                        (...)
                        DIRS = [TEMPLATE_DIR,]
                        (...)
                    }
                ]

    \* BASE_DIR é uma variável que já existe no arquivo settings.py, ela representa a localização do projeto Django.
	   
	4. Adicionando templates
	    1. Na pasta templates/rango, crie um arquivo chamado index.html, e adicione a este arquivo:
    
        <!DOCTYPE html>
        <html>
        
            <head>
                <title>Rango</title>
            </head>
        
            <body>
                <h1>Rango says...</h1>
                <div>
                    hey there partner! <br /> 
                    <strong>{{ boldmessage }}</strong><br />
                </div>
                <div>
                    <a href="/rango/about/">About</a><br />
                </div>
            </body>
        
        </html>
        
        \* Tudo o que está entre colchetes duplos {{ }} representa variáveis. A variável {{ boldmessage }} 
 deve estar definida na view para ser exibida no template. 
        
        \* O que está dentro de {% %} são comandos específicos da linguagem de templates do Django

        2. A partir deste código HTML será retornada uma página. Para isso é necessário alterar a view index() para retornar a página HTML ao invés de texto puro.
    
	    3. No arquivo rango/views.py:
        
                def index(request):
                    context_dict = {'boldmessage': 'olá rango'}
                    return render(request, 'rango/index.html', context=context_dict)    
            
            1. context_dict é a variável que representa um dicionário onde serão passados os valores a serem exibidos no template. O contexto é responsável por mapear as variáveis Python com variáveis de template
            2. A função render() recebe como parâmetros uma requisição (request), o template a ser processado (rango/index.html), e opcionalmente um contexto (context_dict).   
            
            
13. Arquivos estáticos

    Arquivos CSS, JavaScript e imagens são exemplos de arquivos estáticos 
	
	1.  Criar diretório

        1. No mesmo diretório onde foi criada a pasta templates, criar outra pasta, de nome 'static':
            
                (env) $ mkdir static
                
        2. Para armazenar imagens, crie uma pasta de nome 'images'

                  (env) $ mkdir static/images

	2.  Alterar o arquivo settings.py
	    1. Semelhante ao que foi feito com a pasta templates, o arquivo settings.py deve ser configurado para suportar arquivos estáticos:

	    2. Adicionar as seguintes linhas:
				
                STATIC_DIR = os.path.join(BASE_DIR, "static") 
                STATICFILES_DIRS = [STATIC_DIR,]
                STATIC_URL = '/static/'
        
	4. Testando
	    1. Para testar suas configurações, salve uma imagem qualquer na pasta 'static', e tente acessar no navegador:
	    
        ```
        http://localhost:8000/static/images/rango.jpg
        ```
        \* Troque rango.jpg pelo nome do seu arquivo

    5. Inserindo arquivos estáticos no template
         1. Exemplos
                
                {% load staticfiles %}
                
                <!-- Imagens -->
                <img src="{% static "images/rango.jpg" %}"
                     alt="Picture of Rango" />
                <!-- CSS -->
                <link rel="stylesheet" href="{% static "css/base.css" %}" />
                <!-- JavaScript -->
                <script src="{% static "js/jquery.js" %}"></script>
              
        2. Os comandos ```{% load staticfiles %}``` e ```{% static "nome_do_arquivo" %}``` devem ser utilizados ao inserir arquivos estáticos
        
14. Arquivos de mídia

    Arquivos de mídia são aqueles que podem ser modificados pelos usuários. Por exemplo: a foto de perfil em uma rede social

    1. Modificando o settings.py
        1. Adicionar as seguintes linhas:
				
                MEDIA_DIR = os.path.join(BASE_DIR, "media") 
                MEDIA_ROOT = MEDIA_DIR
                MEDIA_URL = '/media/'
        
        2. Localize a lista TEMPLATES, e em seguida 'context_processors', e adicione:
        
                    TEMPLATES = [
                        {
                           'context_processors': [
                               (...)
                               'django.template.context_processors.media'
                           ]                  
                    }
                ]

        3. Altere o arquivo urls.py do projeto:
        
                from django.conf import settings
                from django.conf.urls.static import static

                urlpatterns = [
                    ...
                    ...
                ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

15. Modelos
    1. O Django utiliza o ORM (Object Relational Mapper) para realizar todas as operações de leitura, inserção, exclusão e atualização dos dados.
    2. Um modelo é um objeto Python que descreve os campos e os comportamentos essenciais dos dados a serem armazenados. 
    3. Em geral, cada modelo mapeia uma tabela no banco de dados. Cada modelo é uma função ou classe Python que herda da classe django.db.models.Model, e cada atributo da classe representa um campo.
    4. Configurando o banco de dados
        1. No arquivo settings.py, existe uma variável ```DATABASES```, responsável pelas configurações do banco de dados:

                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                    }
                }

    5. Exemplo de um modelo

            from django.db import models

            class Pessoa(models.model):
                nome = models.CharField(max_length=50)
                sobrenome = models.CharField(max_length=50)
                
                def __str__(self):
                    return self.nome

        1. Sempre importar: ```from django.db import models```
        2. Toda classe herda de ```models.model```
        3. nome e sobrenome são atributos da classe Pessoa, ou seja, atributos da tabela no banco de dados
        4. ```models.CharField``` representa o tipo de dados daquela variável
        5. A função ```__str__()``` serve para exibir uma representação em string do objeto
    
    6. Tipos de dados
        1. AutoField: incrementa automaticamente o valor da chave primária (não é necessário, ao criar um modelo, Django faz isso)
        2. BigIntegerField: inteiro de 64 bits
        3. BooleanField: booleano (verdadeiro/falso)
        4. CharField(max_length): caracteres de tamanho limitado
        5. DateField: representação de datas
        6. DateTimeField: data e hora
        7. DecimalField(max_digits, decimal_places): números decimais. Deve ser informado o número máximo de dígitos de número e o número de casas decimais após a vírgula
        8. EmailField: endereços de email
        9. FileField: upload de arquivos
        10. FloatField: números de ponto flutuante
        11. ImageField: upload de imagens
        12. IntegerField: números inteiros
        13. GenericIPAddressField: endereços IP
        14. PositiveIntegerField: inteiros positivos
        15. TextField: texto sem tamanho definido
        16. TimeField: horário (datetime.time)
        17. URLField: URL
    
    7. Relacionamentos entre as tabelas
        1. O Django possui três tipos de campos para representar os relacionamentos entre as tabelas:
            1. ForeignKey(model, on_delete)
Relacionamento de muitos-para-um. Possui dois argumentos obrigatórios:
model: a classe a qual o modelo está relacionado;
on_delete: qual o comportamento do banco de dados ao excluir um registro (CASCADE, PROTECT, SET_NULL, SET_DEFAULT, DO_NOTHING)

            2. ManyToManyField(model)
Relacionamento de muitos-para-muitos. Requer um argumento: a classe a qual está se relacionando

            3. OneToOneField(model)
Relacionamentos de um-para-um. Requer um argumento: a classe a qual está se relacionando
    
    8. Criando e migrando o banco de dados
        1. Com os modelos criados, devemos inicializar o banco de dados, para criar o banco de dados e suas tabelas:

                $ python manage.py migrate
     
        2. Sempre que ocorrer alguma alteração no modelos, deve ser executado o comando:
    
                $ python manage.py makemigrations

        3. Para atualizar apenas o aplicativo que está sendo modificado, basta executar. Substitua <nome_do_app> pelo nome do seu aplicativo 

                $ python manage.py makemigrations <nome_do_app>
        
        4. Para confirmar as migrações realizadas no aplicativo, é necessário executar novamente: 

                $ python manage.py migrate
                 
    9. Acessando a interface administrativa do Django
        1. A interface de admin do Django permite ver as tabelas criadas, além de excluir, inserir e editar dados.
        2. É necessário criar usuário e senha para acessar essa interface, executando o comando:
        
                $ python manage.py createsuperuser
        
        3. Preencha com usuário, senha e email (opcional)
        4. Execute o servidor

                $ python manage.py runserver

        5. Abra no navegador

                http://localhost:8000/admin

        6. Entre com usuário e senha
        7. Para que os modelos criados em ```models.py``` apareçam nesta interface, é necessário editar o arquivo admin.py (localizado em ```myapp/admin.py```)
        8. Neste arquivo, insira as seguintes linhas:
        
                admin.site.register(<model>)
                
            \* Troque ```<model>``` pelo nome das classes definidas em ```models.py```
