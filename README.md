# GEAR-UP

Este é um sistema para gerenciamento de itens para trilhas, travessias, viagens e mochilões

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) ![Made With Python](https://img.shields.io/badge/Made%20with%20-%20Python%203%20-%20blue?style=flat) ![Streamlit](https://img.shields.io/badge/Framework%20-%20Streamlit%20-%20orange) ![Static Badge](https://img.shields.io/badge/Mantained%20-%20No%20-%20green?style=flat)

## Funcionalidades
- Gerenciamento de carga da mochila em KG/lbs.
- Equipar e desequipar itens, testar possíveis cenários
- Gerenciar lista de desejos e próximas compras.
- Monitorar preços e promoções.

## Requisitos
- Python 3.11+
- Máquina ou container com acesso à rede

## Instalação
#### Caso esteja instalando em um container, o arquivo Dockerfile funcional está na raiz do projeto:
1. Clone o repositório:

       git clone https://github.com/FranciscoValadao/GEARUP
1. Crie a Imagem:

       sudo docker build -t gearup .
3. Construa o container:

       sudo docker run --name gearup --env=PYTHON_VERSION=3.11 --env=PYTHON_PIP_VERSION=23.2.1 --workdir=/app -p 8080/8501 --runtime=runc -d gearup:latest
4. Obtenha o a URL utilizando o comando

       sudo docker container logs <containerhash>

#### Caso esteja instalando em uma VM:
1. Clone o repositório:

        git clone https://github.com/FranciscoValadao/Gearup

2. Crie um ambiente virtual:

        python -m venv venv
3. e ative-o:
   ###### MAC/linux>
       source venv/bin/activate
   ###### Windows>
       venv\Scripts\activate

4. Instale as dependências:

       pip install -r requirements.txt


## Uso
Inicializando a Aplicação:
- Para inicializar a aplicação, use o seguinte comando:

        streamlit run app.py
- Ao executar o comando acima, o site estará online e pronto para ser utilizado.

Editando credenciais

- As credenciais de acesso podem ser editadas na página [URL/config_page]

Limpeza de Arquivos Temporários
- Arquivos temporários sao excluídos automaticamente caso o sistema esteja rodando continuamente.
- Caso contrario, as pastas temp_files e reports devem ser limpas periódicamente.

## Contribuindo

    1. Faça um fork do projeto.
    2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).
    3. Commit suas mudanças (git commit -am 'Adiciona nova feature').
    4. Faça push para a branch (git push origin feature/nova-feature).
    5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Suporte
Para suporte, mande um email para farialotti@gmail.com

