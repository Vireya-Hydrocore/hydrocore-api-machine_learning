# 💧 Projeto de Previsão da Qualidade da Água

Este projeto tem como objetivo **analisar e prever a potabilidade da água** — ou seja, identificar se uma amostra é **potável (1)** ou **não potável (0)** — utilizando técnicas de **Machine Learning** e **API com FastAPI**.

O sistema foi dividido em duas partes:
1. Um **modelo de Machine Learning** desenvolvido e treinado no Jupyter Notebook.  
2. Uma **API** que carrega o modelo serializado e permite fazer previsões em tempo real.

---

## 🧠 Visão Geral

O projeto parte de um conjunto de dados físico-químicos da água (disponível no Kaggle) e aplica algoritmos de aprendizado supervisionado para classificar cada amostra.  
Após o treinamento, o modelo é **salvo em um arquivo `.pkl`** e integrado a uma **API FastAPI**, permitindo que previsões sejam feitas por meio de requisições HTTP.

---

## 📂 Estrutura do Projeto

```
📦 previsao_agua
├── Previsao_Qualidade_agua.ipynb   # Notebook de treino e análise do modelo
├── api_modelo.py                   # API FastAPI para servir o modelo
├── model.pkl                       # Modelo serializado (Random Forest / Decision Tree)
├── health.py                       # Endpoint de health check (retorna 200 OK)
├── requirements                    # Dependências principais
├── requirements_health             # Dependências do health check
├── runtime                         # Versão do Python usada no deploy
├── start_health.sh                 # Script de inicialização automática do health check
```

---

## 📊 Objetivo do Projeto

Treinar um modelo de machine learning capaz de **prever a qualidade da água** com base em nove variáveis físico-químicas medidas em laboratório:

| Variável | Descrição |
|-----------|------------|
| `ph` | Nível de acidez |
| `Hardness` | Dureza da água |
| `Solids` | Sólidos dissolvidos totais |
| `Chloramines` | Presença de cloraminas |
| `Sulfate` | Concentração de sulfato |
| `Conductivity` | Condutividade elétrica |
| `Organic_carbon` | Carbono orgânico |
| `Trihalomethanes` | Substâncias químicas geradas no tratamento |
| `Turbidity` | Grau de turbidez da amostra |

A variável-alvo é **Potability**, que assume:
- `1` → Água potável  
- `0` → Água não potável

---

## ⚙️ Etapas do Projeto

### 🧩 1. Análise e Treinamento do Modelo (`Previsao_Qualidade_agua.ipynb`)

1. **Leitura e análise dos dados**
   - Uso de `pandas`, `numpy`, `matplotlib` e `seaborn`  
   - Visualização de correlações e padrões nas variáveis  

2. **Pré-processamento**
   - Tratamento de valores ausentes  
   - Normalização dos dados  
   - Separação entre treino e teste  

3. **Modelagem**
   - Teste com **Decision Tree** e **Random Forest**  
   - Avaliação usando **accuracy_score**

4. **Resultados**
   - Random Forest obteve o melhor desempenho geral  
   - O modelo final foi salvo como `model.pkl`

---

### 🌐 2. Implementação da API (`api_modelo.py`)

A API foi criada com **FastAPI** para consumir o modelo treinado e realizar previsões de forma simples e rápida.

#### 🔹 Funcionamento

1. O arquivo `model.pkl` é carregado na inicialização.  
2. O endpoint `/predict` recebe dados em formato JSON.  
3. Os dados são convertidos em um `DataFrame` e enviados ao modelo.  
4. O modelo retorna `Potability = 1` (potável) ou `0` (não potável).

---

## 📡 Endpoints da API

### `POST /predict`
Recebe os parâmetros da amostra e retorna a previsão.

**Exemplo de Requisição:**
```json
{
  "ph": 7.1,
  "Hardness": 150.0,
  "Solids": 20000.0,
  "Chloramines": 7.0,
  "Sulfate": 350.0,
  "Conductivity": 450.0,
  "Organic_carbon": 12.0,
  "Trihalomethanes": 75.0,
  "Turbidity": 3.0
}
```

**Exemplo de Resposta:**
```json
{
  "Potability": 1
}
```

---

### `GET /docs`
Acesso à interface interativa da documentação (Swagger UI):  
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

### `GET /health`
Endpoint de verificação de status, usado para monitoramento em produção (retorna `200 OK`).

---

## 🚀 Como Executar Localmente

### 1️⃣ Instalar as dependências
```bash
pip install -r requirements
```

### 2️⃣ Executar a API
```bash
uvicorn api_modelo:app --host 0.0.0.0 --port 8000
```

### 3️⃣ Testar no navegador
Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧠 Tecnologias Utilizadas

- **Python 3.x**
- **pandas**
- **numpy**
- **seaborn**
- **matplotlib**
- **scikit-learn**
- **FastAPI**
- **Uvicorn**
- **pickle**

---

## 📈 Resultados (do modelo)

*(Substitua pelos valores reais do seu notebook)*

| Modelo | Acurácia |
|--------|-----------|
| Decision Tree | XX% |
| Random Forest | XX% |

O modelo **Random Forest** foi escolhido para serialização e uso na API.

---

## 🌍 Deploy

O projeto foi configurado para deploy em plataformas como **Render**, **Railway** ou **Vercel**.  
Os arquivos `runtime`, `requirements_health` e `start_health.sh` garantem que o health check rode automaticamente no ambiente de produção.

---

## 🧾 Fonte de Dados

> Dataset: [Water Potability Dataset - Kaggle](https://www.kaggle.com/datasets/adityakadiwal/water-potability)

---

## ✍️ Autor

**Guilherme Costa**  
Estudante do Instituto Germinare Tech  
💼 Interesse em dados, IA e aplicações sustentáveis  
📅 2025
