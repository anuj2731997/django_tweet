


# Simple Tweet App (Django)

Minimal Django app that supports: **signup (register)**, **login**, **logout**, and **simple tweets** with **add / edit / delete / list**.

---

## 📦 Installation

### Clone the repository
```bash
git clone https://github.com/Leon-glitch-png/django_learning.git
cd django_learning
````

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Setup Tailwind CSS

If your project uses Tailwind (django-tailwind):

```bash
python manage.py tailwind install
python manage.py tailwind start
```

---

##  Apply Database Migrations

```bash
python manage.py makemigration 

python manage.py migrate

```

---

## Run the Development Server

```bash
python manage.py runserver
```

Open your browser:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)







