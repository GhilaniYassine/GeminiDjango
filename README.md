# Chat Application

## Overview
This is a Django-based chat application that integrates with Google's Gemini API to provide AI-powered conversations. The application allows users to have interactive conversations with the Gemini model and stores the chat history in a database.

## Features
- Real-time chat interface
- AI-powered responses using Google's Gemini API
- Chat history storage and retrieval

## Technical Stack
- **Backend**: Django
- **AI Integration**: Google Gemini API
- **Database**: SQLite (default Django DB)

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd chat
```

2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
- Create a `.env` file with your Gemini API key (already done)

5. Run migrations
```bash
python manage.py migrate
```

6. Start the server
```bash
python manage.py runserver
```

## API Endpoints

- `POST /api/chat/`: Send a message to the AI and receive a response
  - Request body: `{"message": "Your message here"}`

## Future Enhancements
- User preferences for AI interactions
- Multiple conversation threads
- Rich text and media support
- Mobile app integration

## Author
Yassine Ghilani

## License
This project is licensed under the MIT License
