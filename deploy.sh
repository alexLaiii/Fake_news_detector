#!/bin/bash

# Deployment Script for Fake News Detector
# This script helps automate the deployment process

echo "🚀 Fake News Detector Deployment Script"
echo "======================================"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not found. Please initialize git first:"
    echo "   git init"
    echo "   git add ."
    echo "   git commit -m 'Initial commit'"
    exit 1
fi

# Check if there are uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  You have uncommitted changes. Please commit them first:"
    git status --short
    echo ""
    echo "Run: git add . && git commit -m 'Prepare for deployment'"
    exit 1
fi

echo "✅ Git repository is clean"

# Push to remote if not already done
echo "📤 Pushing to remote repository..."
git push origin main

echo ""
echo "🎯 Next Steps (Heroku + Vercel - RECOMMENDED):"
echo "============================================="
echo ""
echo "1. Deploy Backend to Heroku (PAID ACCOUNT):"
echo "   - Install Heroku CLI: curl https://cli-assets.heroku.com/install.sh | sh"
echo "   - Login: heroku login"
echo "   - Create app: heroku create your-fake-news-detector-backend"
echo "   - Set environment: heroku config:set ALLOWED_ORIGINS=\"https://your-frontend-domain.vercel.app,http://localhost:3000\""
echo "   - Deploy: git push heroku main"
echo "   - Test: heroku open"
echo "   - Note your backend URL (e.g., https://your-app.herokuapp.com)"
echo ""
echo "2. Deploy Frontend to Vercel:"
echo "   - Go to https://vercel.com/"
echo "   - Import your GitHub repo"
echo "   - Set Root Directory to 'frontend'"
echo "   - Set environment variable: NEXT_PUBLIC_API_URL=https://your-backend-url.herokuapp.com"
echo ""
echo "3. Update frontend/config.js with your actual Heroku URL"
echo ""
echo "📖 See DEPLOYMENT.md for detailed instructions"
echo ""
echo "🔗 Quick Links:"
echo "   - Heroku Dashboard: https://dashboard.heroku.com/"
echo "   - Vercel: https://vercel.com/"
echo "   - Deployment Guide: DEPLOYMENT.md"
echo ""
echo "💡 Heroku Benefits (PAID ACCOUNT):"
echo "   - Better performance and memory for ML models"
echo "   - SSL certificates included"
echo "   - Easy rollbacks and monitoring" 