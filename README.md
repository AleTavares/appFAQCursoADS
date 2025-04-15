# Aplicação para Controle de Duvidas 

## Descrição do Projeto

O **appFAQCursoADS** é uma aplicação desenvolvida com fins didáticos para a disciplina de Implantação de Servidores no curso de Análise e Desenvolvimento de Sistemas. Seu objetivo principal é demonstrar a aplicação prática de tecnologias modernas de infraestrutura e orquestração de serviços, replicando cenários e desafios reais do mercado de tecnologia.

Este projeto consiste em um sistema de FAQ (Frequently Asked Questions) robusto e eficiente, construído sobre uma arquitetura modular e escalável, baseada em contêineres Docker. A aplicação permite o gerenciamento completo do ciclo de vida de perguntas e respostas, desde o cadastro de novas dúvidas por usuários até a publicação de respostas por especialistas.

Para ilustrar as melhores práticas de operação e manutenção de sistemas modernos, o **appFAQCursoADS** integra **observabilidade e monitoramento** como pilares fundamentais da sua arquitetura. Serão implementadas soluções para:

* **Monitoramento de Desempenho:** Acompanhamento em tempo real de métricas cruciais da aplicação (uso de CPU, memória, tráfego de rede) e do banco de dados, utilizando ferramentas como Prometheus.
* **Visualização de Métricas:** Criação de dashboards intuitivos e personalizados no Grafana para facilitar a análise do desempenho e a identificação de possíveis gargalos ou anomalias.
* **Gerenciamento de Logs Centralizado:** Implementação de um sistema de coleta e análise de logs (a ser definido, como ELK Stack ou Loki/Promtail) para facilitar o diagnóstico de problemas, o rastreamento de eventos e a auditoria do sistema.
* **Monitoramento de Saúde da Aplicação:** Definição de health checks e alertas para garantir a disponibilidade e a integridade dos serviços, permitindo a detecção proativa de falhas.

Através do **appFAQCursoADS**, os estudantes poderão vivenciar na prática os conceitos de conteinerização com Docker, orquestração de serviços com Docker Compose (ou potencialmente um orquestrador mais avançado), configuração de bancos de dados em contêineres, e a importância crucial da **observabilidade e monitoramento** para a gestão eficiente de aplicações em ambientes de produção. O projeto visa proporcionar uma compreensão abrangente do processo de implantação e operação de sistemas modernos, preparando os futuros profissionais para os desafios do mercado.

## Estura de Pastas
```
appFAQCursoADS
├── app
│   └── dockerfile # Configuraçã da Imagem da Aplicação
├── bd
│   ├── dockerfile     # configuração da Imagem Docker do Banco de Dados
│   └── ddlFAQ.sql     # DDL de criação do Banco de Dados
├── Prmetheus
│   ├── dockerfile     # configuração da Imagem Docker do Prometheus
│   └── prometheus.yml # Configurador do Prometheus
└── README.md             # Documentação do projeto
```
## Tecnologias Utilizadas

- **Docker**: Para criação e gerenciamento de contêineres.
- **Docker Compose**: Para orquestração de múltiplos serviços.
- **PostgreSQL**: Banco de dados relacional para armazenamento das informações.
- **Node.js**: Backend da aplicação, responsável pela lógica de negócios e APIs.
- **Prometheus e Grafana**: Para monitoramento e visualização de métricas.

## Estrutura da Infraestrutura

De acordo com o documento _"Solicitação de Infraestrutura Docker para Aplicação de FAQ"_, a aplicação é composta pelos seguintes serviços:

1. **Backend**:
   - Desenvolvido em Node.js.
   - Exposto na porta `3000`.
   - Conexão com o banco de dados PostgreSQL.

2. **Banco de Dados**:
   - PostgreSQL configurado para persistência de dados.
   - Volume Docker para armazenamento dos dados.

3. **Monitoramento**:
   - Prometheus para coleta de métricas.
   - Grafana para visualização e análise de dados.

4. **Orquestração**:
   - Utilização do Docker Compose para gerenciar os serviços de forma integrada.

## Como Executar

1. Certifique-se de ter o **Docker** e o **Docker Compose** instalados em sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/appFAQCursoADS.git
   cd appFAQCursoADS

3. Inicie os serviços com o Docker Compose:
```bash
docker-compose up
```
4. Acesse os serviços:
- Aplicação: http://localhost:3000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3001

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
