@echo off
chcp 65001 >nul
echo 🚀 Heroku Deployment Script for Fake News Detector
echo ================================================

echo.
echo 📋 Prerequisites Check:
echo ======================

REM Check if git is initialized
if not exist ".git" (
    echo ❌ Git repository not found!
    echo Please initialize git first:
    echo    git init
    echo    git add .
    echo    git commit -m "Initial commit"
    pause
    exit /b 1
)

REM Check if there are uncommitted changes
git status --porcelain >nul 2>&1
if %errorlevel% equ 0 (
    for /f "tokens=*" %%i in ('git status --porcelain') do (
        echo ⚠️  You have uncommitted changes!
        git status --short
        echo.
        echo Please commit them first:
        echo    git add .
        echo    git commit -m "Prepare for Heroku deployment"
        pause
        exit /b 1
    )
)

echo ✅ Git repository is clean

REM Check if Heroku CLI is installed
heroku --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Heroku CLI not found!
    echo Installing Heroku CLI...
    winget install --id=Heroku.HerokuCLI -e
    echo.
    echo Please restart this script after installation
    pause
    exit /b 1
)

echo ✅ Heroku CLI is installed

REM Check if logged into Heroku
heroku auth:whoami >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Not logged into Heroku
    echo Please login first:
    echo    heroku login
    pause
    exit /b 1
)

echo ✅ Logged into Heroku

echo.
echo 🚀 Starting Heroku Deployment:
echo =============================

REM Push to remote if not already done
echo 📤 Pushing to GitHub...
git push origin main

REM Check if Heroku app exists
heroku apps:info >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo 🆕 Creating new Heroku app...
    set /p APP_NAME="Enter app name (or press Enter for auto-generated): "
    if "%APP_NAME%"=="" (
        heroku create
    ) else (
        heroku create %APP_NAME%
    )
) else (
    echo ✅ Heroku app already exists
)

REM Get app name
for /f "tokens=*" %%i in ('heroku apps:info --json ^| findstr "name"') do (
    set APP_INFO=%%i
)

echo.
echo ⚙️  Configuring environment variables...
heroku config:set ALLOWED_ORIGINS="https://your-frontend-domain.vercel.app,http://localhost:3000"

echo.
echo 🚀 Deploying to Heroku...
git push heroku main

echo.
echo ✅ Deployment complete!
echo.
echo 🌐 Your backend is now live at:
heroku info -s | findstr "web_url"
echo.
echo 🔍 Testing your deployment...
heroku open

echo.
echo 🎯 Next Steps:
echo ==============
echo 1. Copy your backend URL above
echo 2. Deploy frontend to Vercel
echo 3. Set NEXT_PUBLIC_API_URL to your Heroku URL
echo 4. Test the full application
echo.
echo 📖 See DEPLOYMENT.md for frontend deployment
echo.
pause 