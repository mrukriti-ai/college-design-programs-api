# College App Deployment Guide

This guide will help you deploy your college app so it's accessible to all users on the internet.

## 🚀 Quick Start - Deploy to Streamlit Cloud (Frontend)

### 1. Push Your Code to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/college-app.git
git push -u origin main
```

### 2. Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository and main branch
5. Set the path to `streamlit_app/main.py`
6. Click "Deploy"

Your app will be available at: `https://your-app-name.streamlit.app`

## 🔧 Backend Deployment Options

### Option A: Railway (Recommended)

1. **Sign up** at [railway.app](https://railway.app)
2. **Connect GitHub** repository
3. **Create new project** from GitHub repo
4. **Set environment variables**:
   - `DATABASE_URL`: Your database connection string
   - `ADMIN_TOKEN`: Secure admin token
   - `ALLOWED_ORIGINS`: Your Streamlit app URL
5. **Deploy** - Railway will automatically detect and deploy your FastAPI app

### Option B: Render

1. **Sign up** at [render.com](https://render.com)
2. **Create new Web Service**
3. **Connect GitHub** repository
4. **Configure**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. **Set environment variables** (same as Railway)
6. **Deploy**

### Option C: Heroku

1. **Install Heroku CLI** and sign up
2. **Login and create app**:
   ```bash
   heroku login
   heroku create your-college-app-name
   ```
3. **Set environment variables**:
   ```bash
   heroku config:set DATABASE_URL=your_database_url
   heroku config:set ADMIN_TOKEN=your_admin_token
   heroku config:set ALLOWED_ORIGINS=https://your-streamlit-app.streamlit.app
   ```
4. **Deploy**:
   ```bash
   git push heroku main
   ```

## 🌐 Update Frontend Configuration

After deploying your backend, update your Streamlit app's environment variables:

1. **In Streamlit Cloud**:
   - Go to your app settings
   - Add environment variable: `API_BASE_URL=https://your-backend-url.com`

2. **Or update config.py**:
   ```python
   'api_base_url': os.getenv('API_BASE_URL', 'https://your-backend-url.com')
   ```

## 🔒 Security Considerations

### 1. Environment Variables
- Never commit sensitive data to GitHub
- Use environment variables for all secrets
- Rotate admin tokens regularly

### 2. CORS Configuration
Update your FastAPI CORS settings in `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-streamlit-app.streamlit.app",
        "https://your-custom-domain.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 3. Database Security
- Use environment variables for database credentials
- Consider using PostgreSQL for production (more secure than SQLite)
- Enable database backups

## 📱 Custom Domain (Optional)

### Streamlit Cloud
1. Go to app settings
2. Click "Custom domain"
3. Add your domain and follow DNS instructions

### Backend
- Use a reverse proxy (Nginx) for custom domains
- Set up SSL certificates (Let's Encrypt)

## 🧪 Testing Your Deployment

1. **Test Frontend**: Visit your Streamlit app URL
2. **Test Backend**: Visit your API URL + `/api/health`
3. **Test Integration**: Use the app to search for colleges
4. **Monitor Logs**: Check deployment platform logs for errors

## 📊 Monitoring & Maintenance

### Streamlit Cloud
- Built-in analytics
- Error tracking
- Performance monitoring

### Backend Platforms
- **Railway**: Built-in monitoring
- **Render**: Logs and metrics
- **Heroku**: Add-ons for monitoring

## 🆘 Troubleshooting

### Common Issues

1. **CORS Errors**: Check `ALLOWED_ORIGINS` in backend
2. **Database Connection**: Verify `DATABASE_URL` format
3. **Port Issues**: Ensure platforms use `$PORT` environment variable
4. **Build Failures**: Check `requirements.txt` for compatibility

### Getting Help
- Check platform-specific documentation
- Review deployment logs
- Test locally with production environment variables

## 🎯 Next Steps

1. **Deploy frontend** to Streamlit Cloud
2. **Deploy backend** to Railway/Render/Heroku
3. **Update configuration** with production URLs
4. **Test thoroughly** with real users
5. **Set up monitoring** and alerts
6. **Plan scaling** for increased traffic

## 📚 Additional Resources

- [Streamlit Cloud Documentation](https://docs.streamlit.io/streamlit-community-cloud)
- [Railway Documentation](https://docs.railway.app)
- [Render Documentation](https://render.com/docs)
- [Heroku Documentation](https://devcenter.heroku.com)

---

**Your college app will be accessible to users worldwide once deployed!** 🌍

