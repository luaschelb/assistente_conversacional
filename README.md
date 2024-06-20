# Assistente Conversacional Baseado em LLM

Este é um projeto de assistente conversacional baseado em LLM (Language Model) que indexa vetores de documentos PDF para responder a perguntas através de uma interface de conversação.

O Código está disponilizado online na plataforma HuggingFace Spaces no link: https://huggingface.co/spaces/luaschelb/assistente_conversacional

## Configuração do Ambiente de Desenvolvimento

### 1. Clonar o Repositório

Clone este repositório para seu ambiente local:

```bash
git clone https://github.com/seu-usuario/assistente-conversacional.git
cd assistente-conversacional
```

### 2. Configurar e Ativar um Ambiente Virtual (venv)

Recomenda-se usar um ambiente virtual para isolar as dependências do projeto. Para configurar e ativar um ambiente virtual:

#### No Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### No macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências

Com o ambiente virtual ativado, instale os pacotes necessários usando `pip`:

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

Para executar a aplicação localmente:

```bash
streamlit run app.py
```

Isso iniciará a aplicação Streamlit no seu navegador padrão.

### 5. Upload de Documentos PDF

Para indexar documentos PDF e testar a aplicação, faça upload dos arquivos PDF na interface da aplicação.

### 6. Uso da Aplicação

- Abra a aplicação no navegador após iniciar com `streamlit run app.py`.
- Insira uma pergunta na interface e veja as respostas baseadas nos documentos PDF indexados.
