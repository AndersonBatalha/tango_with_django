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

    1. Dentro da pasta onde foi criado seu projeto Django deve ser criado o aplicativo. Ex: na pasta my_project/<nome_do_aplicativo>

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

