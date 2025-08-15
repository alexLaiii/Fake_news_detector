# Quick Deployment Checklist 🚀

## Prerequisites
- [ ] GitHub repository with your code
- [ ] **Heroku account (PAID - Recommended for backend)** - [Dashboard](https://dashboard.heroku.com/)
- [ ] Vercel account (free) - [Sign up](https://vercel.com/)

## Backend Deployment (Heroku) - 5 minutes
1. [ ] Install Heroku CLI: `winget install --id=Heroku.HerokuCLI -e` (Windows)
2. [ ] Login: `heroku login`
3. [ ] Create app: `heroku create your-fake-news-detector-backend`
4. [ ] Set environment: `heroku config:set ALLOWED_ORIGINS="https://your-frontend-domain.vercel.app,http://localhost:3000"`
5. [ ] Deploy: `git push heroku main`
6. [ ] Test: `heroku open` - should show health message
7. [ ] Copy your backend URL (e.g., `https://your-app.herokuapp.com`)

## Frontend Deployment (Vercel) - 5 minutes
1. [ ] Go to [Vercel.com](https://vercel.com/)
2. [ ] Click "New Project" → "Import Git Repository"
3. [ ] Select your repository
4. [ ] Set Root Directory: `frontend`
5. [ ] Set environment variable: `NEXT_PUBLIC_API_URL=https://your-backend-url.herokuapp.com`
6. [ ] Deploy

## Update Configuration
1. [ ] In `frontend/config.js`, replace `'https://your-backend-url.railway.app'` with your actual Heroku URL
2. [ ] Redeploy frontend if needed

## Test
1. [ ] Visit your backend URL - should see health message
2. [ ] Visit your frontend URL - should work with backend
3. [ ] Try submitting a news statement

## Done! 🎉
Your fake news detector is now live on the internet!

---
**Need help?** See `DEPLOYMENT.md` for detailed instructions.
**Run locally first:** `deploy.bat` (Windows) or `./deploy.sh` (Mac/Linux)
**Heroku benefits:** Better performance, more memory for ML models, SSL included 