# Deployment Guide for Fake News Detector

This guide will walk you through deploying your fake news detector application to production.

## Prerequisites

- GitHub account
- **Heroku account (PAID - Recommended for your backend)** - [Dashboard here](https://dashboard.heroku.com/)
- Vercel account (for frontend) - [Sign up here](https://vercel.com/)

## Option 1: Deploy to Heroku + Vercel (RECOMMENDED - You have paid Heroku)

### Step 1: Deploy Backend to Heroku

1. **Install Heroku CLI** (if not already installed):
   ```bash
   # Windows
   winget install --id=Heroku.HerokuCLI -e
   
   # Mac
   brew tap heroku/brew && brew install heroku
   
   # Linux
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Login to Heroku**:
   ```bash
   heroku login
   ```

3. **Create Heroku app**:
   ```bash
   heroku create your-fake-news-detector-backend
   ```

4. **Set environment variables**:
   ```bash
   heroku config:set ALLOWED_ORIGINS="https://your-frontend-domain.vercel.app,http://localhost:3000"
   ```

5. **Deploy to Heroku**:
   ```bash
   git push heroku main
   ```

6. **Verify deployment**:
   ```bash
   heroku open
   # Should show: {"message": "Fake News Detector API is running!", "status": "healthy"}
   ```

7. **Note your backend URL** (e.g., `https://your-fake-news-detector-backend.herokuapp.com`)

### Step 2: Deploy Frontend to Vercel

1. **Update the config**:
   - In `frontend/config.js`, replace `'https://your-backend-url.railway.app'` with your actual Heroku URL

2. **Deploy to Vercel**:
   - Go to [Vercel.com](https://vercel.com/)
   - Click "New Project" → "Import Git Repository"
   - Select your repository
   - Set the following:
     - Framework Preset: Next.js
     - Root Directory: `frontend`
     - Build Command: `npm run build`
     - Output Directory: `.next`
     - Install Command: `npm install`

3. **Set Environment Variables**:
   - Add: `NEXT_PUBLIC_API_URL=https://your-fake-news-detector-backend.herokuapp.com`

4. **Deploy**:
   - Click "Deploy"
   - Vercel will build and deploy your frontend

## Option 2: Deploy to Railway + Vercel

### Step 1: Deploy Backend to Railway

1. **Push your code to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

2. **Deploy to Railway**:
   - Go to [Railway.app](https://railway.app/)
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will automatically detect it's a Python app

3. **Configure Railway**:
   - Set the following environment variables:
     ```
     ALLOWED_ORIGINS=https://your-frontend-domain.vercel.app,http://localhost:3000
     ```
   - Railway will automatically assign a `PORT` environment variable

4. **Deploy**:
   - Railway will build and deploy your app
   - Note the generated URL (e.g., `https://your-app-name.railway.app`)

### Step 2: Deploy Frontend to Vercel
(Same as Option 1, Step 2)

## Option 3: Deploy to DigitalOcean

### Backend Deployment

1. **Create a Droplet** (Ubuntu 20.04 recommended)
2. **SSH into your server**:
   ```bash
   ssh root@your-server-ip
   ```

3. **Install dependencies**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip nginx
   ```

4. **Clone your repository**:
   ```bash
   git clone https://github.com/yourusername/fake_news_detector.git
   cd fake_news_detector/backend
   ```

5. **Install Python dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

6. **Create systemd service**:
   ```bash
   sudo nano /etc/systemd/system/fake-news-detector.service
   ```
   
   Add:
   ```ini
   [Unit]
   Description=Fake News Detector API
   After=network.target

   [Service]
   User=root
   WorkingDirectory=/root/fake_news_detector/backend
   Environment="PATH=/root/.local/bin"
   ExecStart=/root/.local/bin/uvicorn app:app --host 0.0.0.0 --port 8000
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

7. **Start the service**:
   ```bash
   sudo systemctl enable fake-news-detector
   sudo systemctl start fake-news-detector
   ```

8. **Configure Nginx**:
   ```bash
   sudo nano /etc/nginx/sites-available/fake-news-detector
   ```
   
   Add:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

9. **Enable the site**:
   ```bash
   sudo ln -s /etc/nginx/sites-available/fake-news-detector /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl reload nginx
   ```

## Testing Your Deployment

1. **Test Backend**:
   - Visit your backend URL
   - Should see: `{"message": "Fake News Detector API is running!", "status": "healthy"}`

2. **Test Frontend**:
   - Visit your frontend URL
   - Try submitting a news statement
   - Check if it connects to your backend

## Troubleshooting

### Common Issues:

1. **CORS Errors**:
   - Ensure `ALLOWED_ORIGINS` includes your frontend domain
   - Check that the domain is exactly correct (including protocol)

2. **Port Issues**:
   - Railway/Heroku automatically set the `PORT` environment variable
   - Ensure your app uses `os.getenv("PORT", "8000")`

3. **Model Loading Issues**:
   - Ensure all model files are committed to Git
   - Check file paths are relative to the app directory

4. **Memory Issues**:
   - PyTorch models can be large
   - With paid Heroku, you have access to better dynos with more memory
   - Consider using Heroku's Performance-M or Standard-2X dynos for ML workloads

## Security Considerations

1. **CORS**: Only allow your frontend domain
2. **Rate Limiting**: Consider adding rate limiting to prevent abuse
3. **Input Validation**: Ensure proper input sanitization
4. **Environment Variables**: Never commit sensitive data to Git

## Cost Estimation

- **Heroku (PAID)**: From $7/month (Hobby dyno) to $25/month (Standard-1X) - Recommended for your ML backend
- **Vercel**: Free tier available, paid from $20/month
- **Railway**: Free tier available, paid from $5/month
- **DigitalOcean**: From $5/month

## Next Steps

After deployment:
1. Set up a custom domain
2. Add SSL certificates (included with Heroku)
3. Set up monitoring and logging
4. Implement CI/CD pipeline
5. Add health checks and uptime monitoring

## Heroku-Specific Benefits (Since you have paid account)

1. **Better Performance**: Access to Standard and Performance dynos
2. **More Memory**: Essential for ML models (PyTorch can be memory-intensive)
3. **Custom Domains**: Easy SSL certificate management
4. **Add-ons**: Database, monitoring, logging services
5. **Team Collaboration**: Multiple developers can access the same app
6. **Rollback**: Easy deployment rollbacks if something goes wrong 