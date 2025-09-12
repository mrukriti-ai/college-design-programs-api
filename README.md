# 🎨 College Design Programs - Streamlit App

A modern, interactive web application for discovering and comparing design programs worldwide. Built with Streamlit, this app helps students find their perfect design education program.

## ✨ Features

- **🔍 Smart Search**: Filter programs by type, location, and degree level
- **🌍 Global Coverage**: Programs from USA, UK, China, and Australia
- **⭐ Favorites System**: Save and manage your favorite programs
- **📊 Analytics**: Visual insights into program distribution
- **📱 Responsive Design**: Works perfectly on all devices
- **🎨 Modern UI**: Beautiful, intuitive interface

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd college-design-app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run college_design_app.py
   ```

5. **Open in browser**
   Navigate to http://localhost:8501

## 🌐 Deployment Options

### Option 1: Streamlit Cloud (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and main file: `college_design_app.py`
   - Click "Deploy"

3. **Share your app**
   - Your app will be available at: `https://your-app-name.streamlit.app`
   - Share this URL with users

### Option 2: Heroku

1. **Create Procfile**
   ```
   web: streamlit run college_design_app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Deploy to Heroku**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Option 3: Railway

1. **Connect to Railway**
   - Go to [railway.app](https://railway.app)
   - Connect your GitHub repository
   - Railway will automatically detect and deploy your Streamlit app

### Option 4: Google Cloud Platform

1. **Deploy using Cloud Run**
   ```bash
   gcloud run deploy --source .
   ```

## 📁 Project Structure

```
college-design-app/
├── college_design_app.py    # Main Streamlit application
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
└── .gitignore             # Git ignore file
```

## 🎯 How to Use

1. **Browse Programs**: View all available design programs
2. **Search & Filter**: Use the search form to find specific programs
3. **Add Favorites**: Click the heart icon to save programs
4. **View Analytics**: Check the charts for program insights
5. **Visit Websites**: Click "Visit Website" to learn more

## 🔧 Customization

### Adding New Programs

Edit the `get_mock_data()` function in `college_design_app.py`:

```python
{
    "id": 9,
    "name": "Your University",
    "location_city": "City",
    "location_country": "Country",
    "program_name": "Program Name",
    "program_type": "Program Type",
    "degree_level": "Degree Level",
    "tuition_min": 30000,
    "tuition_max": 40000,
    "application_deadline": "2024-01-01",
    "program_description": "Program description",
    "website_url": "https://university.edu"
}
```

### Modifying Filters

Update the `filter_colleges()` function to add new filter criteria.

## 🌟 Features in Detail

### Search Filters
- **Program Type**: Graphic Design, UX/UI, Fashion, Product Design, Architecture, Animation
- **Location**: North America, Europe, Asia, Australia
- **Degree Level**: Bachelor, Master, Certificate

### Analytics
- Program types distribution (pie chart)
- Geographic distribution (bar chart)
- Quick statistics (total programs, countries, types)

### Favorites System
- Add/remove programs from favorites
- Persistent storage using Streamlit session state
- Visual indicators for favorite status

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Data Visualization**: Plotly
- **Data Processing**: Pandas
- **Deployment**: Streamlit Cloud, Heroku, Railway, or GCP

## 📊 Sample Data

The app includes 8 sample programs:
- Parsons School of Design (USA)
- Royal College of Art (UK)
- Central Saint Martins (UK)
- RISD (USA)
- MIT Architecture (USA)
- CalArts (USA)
- Central Academy of Fine Arts (China)
- RMIT University (Australia)

## 🔗 Links

- **Live Demo**: [Your Streamlit Cloud URL]
- **GitHub Repository**: [Your GitHub Repo URL]
- **Documentation**: [Your Docs URL]

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support, email [your-email@example.com] or create an issue in the GitHub repository.

---

**Made with ❤️ using Streamlit**
