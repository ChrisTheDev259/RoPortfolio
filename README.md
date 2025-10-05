# Marketplace Project

This is a Django + Vite/Tailwind starter project.

Quick start

1. Create and activate a Python virtual environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Install frontend dependencies (from `taiwind` folder)

```bash
cd taiwind
npm install
```

3. Run Django migrations and start server

```bash
cd ..
python manage.py migrate
python manage.py runserver
```

4. Build frontend assets

```bash
cd taiwind
npm run build
```

Pushing to GitHub

1. Create a repository on GitHub (via website) and copy the repo URL (SSH or HTTPS).
2. Initialize git (if not already) and push:

```bash
cd market
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git branch -M main
git push -u origin main
```

Replace `<your-github-repo-url>` with your repo's URL.
