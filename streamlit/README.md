# Document Manager with Deadline Warnings

## Features
- 🔐 Login/Signup pages
- 📂 PDF upload with calendar date marking
- ⚠️ Automatic deadline warnings (3 days before and overdue)
- 💬 Chat interface for document queries
- 🚪 Logout functionality

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the backend server:
```bash
python server.py
```

3. In a new terminal, start Streamlit:
```bash
streamlit run app.py
```

## Usage
1. Signup with username/password
2. Login with credentials
3. Upload PDF and set deadline date
4. View warnings for documents within 3 days of deadline
5. Chat with your documents
6. Logout to clear session
