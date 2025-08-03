# MyAwesomeCart 🛒

A Django-based eCommerce project with two apps: `blog` and `shop`.

---

## 🧩 Project Structure

MyAwesomeCart/
├── manage.py
├── db.sqlite3 # (Ignored in Git)
├── mac/ # Project settings
│ ├── settings.py
│ └── urls.py
├── blog/ # App: blog
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── migrations/
│ └── templates/
├── shop/ # App: shop
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── migrations/
│ └── templates/
├── media/ # (User uploads - Ignored in Git)
└── static/ # App-level static files

yaml
Copy
Edit

---

## 🚀 Features

- 🔗 **Modular apps**: `blog` and `shop`
- 🗂️ Uses Django templates and static asset system
- 🛠️ Uses Django migrations for DB schema evolution

---

## 🛡️ Version Control Strategy

### Tracked

- All source code (`.py`, `.html`, `.css`, etc.)
- Migrations (`*.py` inside `migrations/`)
- Templates and static app files

### Ignored

- `*.pyc`, `__pycache__` (auto-generated)
- `db.sqlite3` (local dev DB)
- `media/` folder (user uploads)
- `.idea/` / `.vscode/` (editor-specific)
- `.env` file for secrets

---

## 🧪 Running Locally

```bash
# Create virtual env
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run server
python manage.py runserver