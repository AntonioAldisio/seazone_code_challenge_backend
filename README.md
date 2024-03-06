# Projeto de API's com Django

## 1. Introdução

Neste projeto, o desafio consiste em desenvolver três APIs REST utilizando a linguagem de programação Python em conjunto com os frameworks Django e Django Rest Framework. Além disso, será utilizado o banco de dados MySQL para armazenar e gerenciar os dados necessários para o funcionamento das APIs. Para facilitar o processo de implantação e execução do projeto, também será adotado o Docker, permitindo a criação de contêineres para cada componente da aplicação.


### 1.1 Modelagem do Banco de Dados

Um imóvel pode ter diversos anúncios, mas um anúncio é referente apenas a um imóvel. Um anúncio pode ter várias reservas, mas uma reserva se refere a apenas um anúncio.

#### 1.1.3 Diagramas

![img](/asset//imgs/diagramaConceitual.jpg)
<center> Diagrama conceitual</center>

![img](/asset//imgs/DiagramaLogico.png)
<center> Diagrama lógico</center>


### 1.2 Desenvolvimento do projeto

O desenvolvimento do projeto seguiu uma sequência estruturada, que envolveu as seguintes etapas:

1. Modelagem do banco de dados: Nesta fase, foi realizada a definição da estrutura do banco de dados, incluindo a identificação das tabelas necessárias, seus relacionamentos e os atributos de cada entidade.

2. Desenvolvimento da API Imóveis, Anúncios e Reservas: Nessa etapa, foi implementada a lógica das três APIs REST, cada uma responsável por um aspecto específico do projeto. A API Imóveis tratou das operações relacionadas à gestão dos imóveis disponíveis, a API Anúncios cuidou das funcionalidades relacionadas à criação e exibição de anúncios dos imóveis e a API Reservas foi responsável pelas operações de reserva dos imóveis por parte dos usuários.

3. Desenvolvimento de testes unitários: Para assegurar a qualidade e o bom funcionamento das APIs, foram criados testes unitários. Esses testes verificam se as funcionalidades implementadas estão produzindo os resultados esperados e ajudam a identificar e corrigir possíveis erros ou falhas no código.

Ao seguir essa linha de desenvolvimento, foi possível estruturar o projeto de forma organizada, desde a modelagem do banco de dados até a implementação das APIs e a realização de testes para assegurar a qualidade do código.


## 2. Requisitos

 - Docker => 20.10 <br>
- Docker-compose => 1.29

## 3. Como rodar

### 3.1 Docker

Clone o repositorio e entre na pasta Estudo_Django
```bash
$ git clone https://github.com/AntonioAldisio/Estudo_Django.git && cd Estudo_Django
```

Para realizar o build e subir os container
```bash
$ docker-compose up -d --build
```

Parar os container
```bash
$ docker-compose down
```
Obs:
Insomnia para realizar os testes, [clique aqui para visulaizar](./asset/insomnia/Insomnia.json)

### 3.1 Documentação das API's

1. Api Imoveis:
    - http://0.0.0.0:8000/swagger

2. Api Anuncios:
    - http://0.0.0.0:8001/swagger

3. Api Reservas:
    - http://0.0.0.0:8002/swagger

## 4. Execução dos teste

### 4.1 Requisitos

- Python => 3.10


### 4.1 Comandos

Instalação e configuração do ambiente

```bash
$ pip3 install virtualenv && \
python3 -m venv desenv && \
source desenv/bin/activate && \
python3 install -r requirements-dev.txt
```

Execute o comando abaixo dentro da pasta src/<Nome_API>
```bash
$ python3 python3 manage.py test --verbosity=2
```

## 4. Melhorias

Durante o desenvolvimento deste projeto, foram identificadas algumas possíveis melhorias e uma possível mudança de arquitetura. As melhorias visam adicionar recursos adicionais ao projeto, como autenticação, monitoramento das APIs via Prometheus e construção de mais testes. A mudança de arquitetura proposta é a consolidação das três APIs em uma única API, porém, essa evolução requer uma análise mais aprofundada de pontos como desempenho, escalabilidade e segurança.

Aqui estão as melhorias propostas em tópicos:

1. Autenticação: Adicionar um sistema de autenticação para controlar o acesso às APIs, garantindo que apenas usuários autenticados possam realizar determinadas ações. Isso pode ser implementado utilizando autenticação por token JWT (JSON Web Token), por exemplo.

2. Monitoramento das APIs com Prometheus: Integrar o Prometheus para coletar métricas e monitorar o desempenho das APIs. Isso permite identificar possíveis gargalos, monitorar o tempo de resposta, taxa de erros e outros indicadores-chave para garantir a qualidade e o bom funcionamento das APIs.

3. Construção de mais testes: Expandir a cobertura de testes unitários para garantir um maior nível de confiabilidade e robustez das APIs. Isso inclui testar diferentes cenários, validar entradas e saídas, além de considerar testes de integração para garantir a interoperabilidade entre os componentes.

Quanto à mudança de arquitetura, é proposto a consolidação das três APIs em uma única API. No entanto, essa evolução requer uma análise detalhada dos requisitos e considerações específicas do projeto, como desempenho, escalabilidade e segurança. Essa mudança pode simplificar o gerenciamento e manutenção do sistema, mas é importante avaliar cuidadosamente os impactos e trade-offs envolvidos antes de prosseguir com a implementação.