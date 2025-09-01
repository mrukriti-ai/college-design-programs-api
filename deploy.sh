#!/bin/bash

# College App Deployment Script
echo "🚀 Starting College App Deployment..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit"
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi

# Check if remote origin is set
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "🔗 Please set your GitHub remote origin:"
    echo "git remote add origin https://github.com/yourusername/college-app.git"
    echo "git push -u origin main"
else
    echo "✅ Remote origin is set"
    echo "📤 Pushing to GitHub..."
    git add .
    git commit -m "Update for deployment"
    git push origin main
fi

echo ""
echo "🎯 Next Steps:"
echo "1. Deploy Frontend to Streamlit Cloud:"
echo "   - Go to https://share.streamlit.io"
echo "   - Connect your GitHub repository"
echo "   - Deploy streamlit_app/main.py"
echo ""
echo "2. Deploy Backend to Railway:"
echo "   - Go to https://railway.app"
echo "   - Connect your GitHub repository"
echo "   - Deploy the fastapi_app directory"
echo ""
echo "3. Update environment variables with production URLs"
echo ""
echo "🌍 Your app will then be accessible to users worldwide!"
