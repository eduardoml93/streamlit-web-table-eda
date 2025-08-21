# 📊 Web Table Analyzer

Uma aplicação web interativa desenvolvida com Streamlit para análise e visualização de tabelas extraídas de páginas web.

## 🚀 Funcionalidades

- **Extração Automática de Tabelas**: Extrai automaticamente todas as tabelas HTML de qualquer página web
- **Visualização Interativa**: Exibe os dados em formato tabular com interface amigável
- **Análise Estatística Avançada**: Gera gráficos e visualizações usando Plotly
- **Interface Moderna**: Design responsivo com background personalizado e tema escuro
- **Múltiplas Tabelas**: Suporte para análise de várias tabelas da mesma página

## 📈 Tipos de Visualizações

- **Histogramas**: Distribuição de dados numéricos
- **Gráficos de Dispersão**: Relacionamento entre variáveis numéricas
- **Boxplots**: Análise de distribuição e outliers
- **Heatmaps de Correlação**: Matriz de correlação entre variáveis
- **Gráficos de Barras**: Contagem de categorias

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework para aplicações web em Python
- **Pandas**: Manipulação e análise de dados
- **Plotly**: Visualizações interativas e gráficos
- **BeautifulSoup4**: Web scraping e parsing HTML
- **Requests**: Requisições HTTP

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/eduardoml93/streamlit-web-table-eda.git
   cd web-table-analyzer
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação**
   ```bash
   streamlit run main.py
   ```

4. **Acesse no navegador**
   ```
   http://localhost:8501
   ```

## 📖 Como Usar

1. **Inicie a aplicação** executando `streamlit run main.py`
2. **Cole a URL** da página web que contém as tabelas que deseja analisar
3. **Clique em "Carregar Tabelas da Página"** para extrair as tabelas
4. **Selecione a tabela** que deseja analisar (se houver múltiplas)
5. **Explore as visualizações** disponíveis para diferentes tipos de dados

## 🎯 Casos de Uso

- **Análise de Dados Financeiros**: Tabelas de preços, indicadores econômicos
- **Relatórios Empresariais**: Dados de vendas, métricas de performance
- **Pesquisas Acadêmicas**: Estatísticas, resultados de estudos
- **Monitoramento de Mercado**: Preços de produtos, dados competitivos
- **Análise de Dados Públicos**: Estatísticas governamentais, censos

## 📁 Estrutura do Projeto

```
web-table-analyzer/
├── main.py              # Aplicação principal Streamlit
├── requirements.txt     # Dependências do projeto
├── bg.jpg              # Imagem de background
└── README.md           # Este arquivo
```

## 🔍 Funcionalidades Técnicas

- **Web Scraping Inteligente**: Detecta e extrai tabelas HTML automaticamente
- **Processamento de Dados**: Identifica tipos de dados (numérico/categórico)
- **Gráficos Responsivos**: Visualizações que se adaptam ao tamanho da tela
- **Persistência de Estado**: Mantém seleções do usuário durante a sessão
- **Tratamento de Erros**: Mensagens informativas para diferentes cenários

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela no repositório!**
