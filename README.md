# Supervive Tracker

Durante uma discussão amistosa (mas levemente competitiva) com um amigo numa noite de jogatina, ele disse que sempre ganhava de mim quando caíamos em lados opostos.
Então pensei: por que não provar — com dados? 😆

A ideia virou uma brincadeira que acabou me servindo de desculpa pra finalmente aprender a criar um app web "de verdade" — com backend, HTML, deploy em nuvem e tudo mais.
O **Supervive Tracker** nasceu daí: uma mistura de piada interna e laboratório pessoal pra entender melhor Flask, requisições HTTP e como colocar um projetinho no ar do jeito certo.

---

## 🧭 Visão Geral

O **Supervive Tracker** é um pequeno aplicativo Flask desenvolvido para rastrear estatísticas de partidas em tempo real, utilizando a API pública do Supervive.
Ele exibe de forma simples o número total de vitórias e derrotas, com um layout leve em HTML e CSS.

---

## ⚙️ Requisitos

Antes de começar, certifique-se de ter instalado:

* **Python 3.10+**
* **Git**
* **pip** e **venv**

---

## 🚀 Instalação e Execução

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Psor1107/supervive-tracker.git
cd supervive-tracker
```

---

### 2️⃣ Criar e ativar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` ainda não exista:

```bash
pip install flask requests gunicorn
pip freeze > requirements.txt
```

---

### 4️⃣ Executar em modo desenvolvimento

```bash
python app.py
```

O aplicativo será acessível em:

```
http://127.0.0.1:80
```

---

### 5️⃣ Executar em produção com Gunicorn

Para rodar manualmente em modo servidor:

```bash
sudo env "PATH=$PATH" gunicorn --reload --bind 0.0.0.0:80 --timeout 30 app:app
```

---

## 🧱 Execução automática com Systemd (Linux)

Para rodar o app automaticamente após o boot:

Crie o arquivo `/etc/systemd/system/supervive-tracker.service`:

```ini
[Unit]
Description=Supervive Tracker Flask App
After=network.target

[Service]
User=azureuser
WorkingDirectory=/home/azureuser/supervive-tracker
Environment="PATH=/home/azureuser/supervive-tracker/venv/bin"
ExecStart=/home/azureuser/supervive-tracker/venv/bin/gunicorn app:app \
          --bind 127.0.0.1:8000 --workers 3 --timeout 30
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Ativar e iniciar o serviço:

```bash
sudo systemctl daemon-reload
sudo systemctl enable supervive-tracker
sudo systemctl start supervive-tracker
sudo systemctl status supervive-tracker
```

---

## 🧠 Comandos úteis

| Ação                 | Comando                                   |
| -------------------- | ----------------------------------------- |
| Iniciar localmente   | `python app.py`                           |
| Iniciar com Gunicorn | `gunicorn --bind 0.0.0.0:80 app:app`      |
| Ativar auto-start    | `sudo systemctl enable supervive-tracker` |
| Ver status           | `sudo systemctl status supervive-tracker` |
| Ver logs             | `sudo journalctl -u supervive-tracker -f` |

---

## 🌿 Sophia Chablau e Uma Enorme Perda de Tempo