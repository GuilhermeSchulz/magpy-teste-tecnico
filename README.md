# Teste Técnico Desenvolvedor(a) Python Júnior [REMOTO]

## Como Rodar a API do projeto

<ol>
    <li> Clonar este repositório;
    <li> Abrir um terminal na pasta onde foi clonado o repositório;
    <li> Rodar o comando "pipenv install --dev"; 
    <li> Utilizar o comando "pipenv shell" para acessar o ambiente virtual;
    <li> Rodar a API com o comando "python manage.py runserver";
    <li> Para testar as rotas:</li>
    <li>
      Envie uma requisiçao POST para http://localhost:8000/api/projects/ com o corpo:  
        
    ````
    POST /api/projects
    {
        "name": "titan",
        "packages": [
            {"name": "Django"},
            {"name": "graphene", "version": "2.0"}
        ]
    }
    ```
    O código HTTP de retorno deve ser 201 e o corpo esperado na resposta é:
        
    ```
    {
        "name": "titan",
        "packages": [
            {"name": "Django", "version": "3.2.5"},  // Usou a versão mais recente
            {"name": "graphene", "version": "2.0"}   // Manteve a versão especificada
        ]
    }
    ```
    
</li>
<li>
Também deve ser possível visitar projetos previamente cadastrados, usando o
nome na URL, enviando um GET em http://localhost:8000/api/projects/titan
    
```
GET /api/projects/titan
{
    "name": "titan",
    "packages": [
        {"name": "Django", "version": "3.2.5"},
        {"name": "graphene", "version": "2.0"}
    ]
}
```
</li>
<li>
    Também é possivel puxar todos os projetos cadastrados utilizando um GET no endpoint: http://localhost:8000/api/projects/
</li>
<li>E deletar projetos pelo nome:
    
```
DELETE http://localhost:8000/api/projects/titan
```
</li>

<li>
    Se um dos pacotes informados não existir, ou uma das versões especificadas for
inválida, um erro deve ser retornado.

Para uma chamada semelhante ao exemplo abaixo:
```
POST /api/projects
{
    "name": "titan",
    "packages": [
        {"name": "pypypypypypypypypypypy"},
        {"name": "graphene", "version": "1900"}
    ]
}
```
O código HTTP de retorno deve ser 400 e o corpo esperado na resposta é:
```
{
    "error": "One or more packages doesn't exist"
}
```
</li>
</ol>
