# 🚀 Railway Deploy Guide for AgentOS

## 🛠️ Included Files
- `Dockerfile`: Defines how to build and run the app
- `Procfile`: Instructs Railway how to start the web process
- `requirements.txt`: Python package dependencies
- `.env.example`: Template for environment variables

## 📦 Deploy Steps

1. **Upload your project to GitHub** with all core folders in the repo root
2. **Copy all these files** to the root of the repository
3. On Railway, **create a new project** using "Deploy from GitHub"
4. Railway will auto-detect your Dockerfile and set it up
5. In the Railway dashboard, go to **"Variables"** and copy everything from `.env.example`
6. Once deployed, your app will be live at:  
   `https://<your-app-name>.up.railway.app`

---

## ✅ Checklist

- [ ] Dockerfile is at root
- [ ] Procfile exists with correct start command
- [ ] All environment variables set in Railway dashboard
- [ ] Your core app file is at `agentos-core/main.py` with FastAPI instance `app`

---

ℹ️ For advanced deploys (multi-service, Grafana, Redis, Prometheus), refer to the full Docker Compose mode or use Railway CLI.