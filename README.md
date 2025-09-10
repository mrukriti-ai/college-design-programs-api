# College Design Programs - Streamlit Frontend

A modern, modular Streamlit web application for discovering and comparing design programs at colleges worldwide.

## 🎨 Features

### Core Features
- **Smart Search**: Filter colleges by program type, budget, and location
- **Global Coverage**: Explore design programs from top schools worldwide
- **Favorites System**: Save and compare your favorite programs
- **Detailed Information**: Comprehensive program details and contact information
- **Admin Panel**: Excel file upload for data management

### Design Programs Supported
- Graphic Design
- UX/UI Design
- Fashion Design
- Product Design
- Architecture
- Animation

## 🏗️ Architecture

### Modular Structure
```
streamlit_app/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── pages/                 # Page modules
│   ├── home.py           # Home page
│   ├── profile.py        # User profile and search
│   ├── results.py        # Search results display
│   ├── details.py        # College details view
│   └── admin.py          # Admin panel
├── components/            # Reusable components
│   ├── cards.py          # College card components
│   ├── forms.py          # Form components
│   └── filters.py        # Filter components
└── utils/                # Utility modules
    ├── session_state.py  # Session state management
    └── config.py         # Configuration management
```

### Key Components

#### Pages
- **Home**: Welcome page with value proposition and features
- **Profile**: User input form for search preferences
- **Results**: Display and filter search results
- **Details**: Comprehensive college information
- **Admin**: Data management and Excel upload

#### Components
- **Cards**: Reusable college information cards
- **Forms**: Consistent form elements
- **Filters**: Search and results filtering

#### Utilities
- **Session State**: User data and preferences persistence
- **Config**: Application configuration and constants

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd streamlit_app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run main.py
   ```

4. **Open your browser**
   - Navigate to `http://localhost:8501`
   - The application will open automatically

### Development Setup

1. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install development dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run in development mode**
   ```bash
   streamlit run main.py --server.port 8501
   ```

## 📱 User Flow

### Basic User Journey
1. **Home Page**: Welcome and feature overview
2. **Profile Setup**: Enter preferences and search criteria
3. **Search Results**: View matching programs with filters
4. **College Details**: Explore comprehensive program information
5. **Favorites**: Save and manage preferred programs

### Navigation
- **Sidebar Navigation**: Easy access to all pages
- **Breadcrumbs**: Clear navigation context
- **Quick Actions**: Direct access to key features

## 🎯 Key Features

### Search & Filter
- Program type selection
- Budget range filtering
- Location preferences
- Degree level options
- Real-time filtering

### College Information
- Program details
- Tuition information
- Application deadlines
- Contact information
- Website links

### User Experience
- Responsive design
- Intuitive navigation
- Consistent styling
- Helpful tooltips
- Error handling

## 🔧 Configuration

### Environment Variables
```bash
# API Configuration (for future backend integration)
API_BASE_URL=http://localhost:8000
API_TIMEOUT=30

# Application Settings
MAX_RESULTS_PER_PAGE=20
ENABLE_DEBUG=false

# Admin Settings
ADMIN_TOKEN=dev
```

### Customization
- **Styling**: Modify CSS in `main.py`
- **Constants**: Update values in `utils/config.py`
- **Components**: Extend components in `components/` directory

## 📊 Data Structure

### College Data Format
```json
{
  "id": 1,
  "name": "College Name",
  "location_city": "City",
  "location_country": "Country",
  "program_name": "Program Name",
  "program_type": "Graphic Design",
  "degree_level": "Bachelor",
  "tuition_min": 45000,
  "tuition_max": 50000,
  "application_deadline": "2024-01-15",
  "program_description": "Description...",
  "contact_email": "email@.edu",
  "website_url": "https://college.edu"
}
```

### Excel Import Format
Required columns for admin upload:
- `name`: College/University name
- `location_city`: City name
- `location_country`: Country name
- `program_name`: Program name
- `program_type`: Program category
- `degree_level`: Degree type
- `tuition_min`: Minimum annual tuition
- `tuition_max`: Maximum annual tuition

## 🚀 Deployment

### Local Development
```bash
streamlit run main.py
```

### Production Deployment
1. **Streamlit Cloud** (Recommended)
   - Connect GitHub repository
   - Automatic deployment
   - Free hosting

2. **Heroku**
   - Add `setup.sh` and `Procfile`
   - Configure buildpacks

3. **Docker**
   - Create `Dockerfile`
   - Build and run container

## 🔮 Future Enhancements

### Planned Features
- **Backend Integration**: Connect to FastAPI backend
- **User Authentication**: Login and user accounts
- **Advanced Search**: More sophisticated filtering
- **Comparison Tool**: Side-by-side program comparison
- **Export Features**: PDF and email export
- **Analytics**: Usage statistics and insights

### Technical Improvements
- **API Integration**: Real-time data from backend
- **Caching**: Improved performance
- **Testing**: Unit and integration tests
- **CI/CD**: Automated testing and deployment
- **Monitoring**: Application monitoring and logging

## 🤝 Contributing

### Development Guidelines
1. **Modular Design**: Keep components reusable
2. **Clean Code**: Follow Python best practices
3. **Documentation**: Add docstrings and comments
4. **Testing**: Write tests for new features
5. **Styling**: Maintain consistent UI/UX

### Code Structure
- **Functions**: Single responsibility principle
- **Variables**: Descriptive naming
- **Comments**: Clear and helpful
- **Error Handling**: Graceful error management

## 📝 License

This project is part of the College Design Programs application suite.

## 🆘 Support

### Common Issues
1. **Import Errors**: Check Python path and dependencies
2. **Styling Issues**: Verify CSS syntax
3. **Data Issues**: Validate Excel file format
4. **Performance**: Optimize large datasets

### Getting Help
- Check the documentation
- Review error messages
- Test with sample data
- Contact development team

---

**🎨 College Design Programs** - Your gateway to design education worldwide 