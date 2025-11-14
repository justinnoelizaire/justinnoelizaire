# Basketball Analytics App

## Setup Instructions

1. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up database
```bash
# Adjust according to your database setup
createdb basketball_db
```

4. Run the Flask backend
```bash
python -m backend.app
```

5. Run Streamlit analytics
```bash
streamlit run streamlit_app/analytics.py
```

## Features
- User Authentication
- Player Management
- Game Tracking
- Advanced Analytics Dashboard
- Responsive Frontend
