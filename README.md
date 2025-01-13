![Screenshot 2025-01-13 133934](https://github.com/user-attachments/assets/2c37152e-f8f8-4e86-a0c9-84783255034f)
![Screenshot 2025-01-13 134002](https://github.com/user-attachments/assets/b10606b8-db10-4da7-8d77-89fa6c115f4b)
![Screenshot 2025-01-13 134044](https://github.com/user-attachments/assets/771e15f7-be45-413d-95d4-2d7fa378430a)
![Screenshot 2025-01-13 134121](https://github.com/user-attachments/assets/551869a4-8896-4f93-90b6-c65799ba1cc5)
![Screenshot 2025-01-13 134157](https://github.com/user-attachments/assets/dde766de-1332-4a5c-8331-863d87894d00)





# AI Chat System - REST API

This repository contains the implementation of REST APIs for an AI-powered chat system using Django. The system includes features like user registration, login, interaction with a chatbot, and token balance management.

---

## Features

1. **User Registration**
   - Allows users to register with a unique username and password.
   - New users are assigned 4000 tokens by default.

2. **User Login**
   - Users can log in with their username and password.
   - Returns an authentication token for subsequent API calls.

3. **Chat**
   - Accepts user messages and provides AI-generated responses.
   - Deducts 100 tokens from the user's account for each query.
   - Saves chat history, including the message, response, and timestamp.

4. **Token Balance**
   - Allows users to check their remaining token balance.

---

## Installation

Follow the steps below to set up the project on your local machine:

### Prerequisites

1. Python (3.8 or higher)
2. pip (Python package manager)
3. Virtual environment tool (optional but recommended)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Shree-ranjan/AI-Chat-System.git
   cd ai_chat
   ```

2. **Create a Virtual Environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser** (for admin panel access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Admin Panel** (Optional):
   - URL: `http://127.0.0.1:8000/api/admin/`
   - Login with the superuser credentials created earlier.

---

## API Endpoints

### 1. **User Registration**
- **URL**: `http://127.0.0.1:8000/api/register/`
- **Method**: POST
- **Headers**:
  - `Content-Type: application/json`
- **Body**:
  ```json
  {
    "username": "ram_sharma",
    "password": "sharma123"
  }
  ```
- **Response**:
  ```json
  {
    "message": "User registered successfully"
  }
  ```

### 2. **User Login**
- **URL**: `http://127.0.0.1:8000/api/login/`
- **Method**: POST
- **Headers**:
  - `Content-Type: application/json`
- **Body**:
  ```json
  {
    "username": "ram_sharma",
    "password": "sharma123"
  }
  ```
- **Response**:
  ```json
  {
    "token": "8d4108d7-26d9-4f7f-875e-046f29c08025"
  }
  ```

### 3. **Chat**
- **URL**: `http://127.0.0.1:8000/api/chat/`
- **Method**: POST
- **Headers**:
  - `Content-Type: application/json`
  - `Authorization: <your-token>`
- **Body**:
  ```json
  {
    "message": "What is AI?"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "user": 1,
    "message": "What is AI?",
    "response": "This is a dummy AI response",
    "timestamp": "2025-01-11T12:00:00Z"
  }
  ```

### 4. **Token Balance**
- **URL**: `http://127.0.0.1:8000/api/balance/`
- **Method**: GET
- **Headers**:
  - `Authorization: <your-token>`
- **Response**:
  ```json
  {
    "tokens": 3900
  }
  ```

---

## Testing with Postman

1. Import the API details into Postman.
2. Test the endpoints in the following order:
   - **Register a new user**.
   - **Log in with the registered user** to get the token.
   - Use the **token** to test the Chat and Token Balance endpoints.

---

## Challenges & Suggestions

### Challenges
- Implementing authentication securely without Django's built-in `TokenAuthentication` for simplicity.
- Managing token expiration or invalidation was skipped for simplicity but is essential for production-grade applications.

### Suggestions for Improvement
1. Replace the in-memory token store with Django's `rest_framework.authtoken` or JWT for better scalability and security.
2. Integrate an actual AI service (e.g., OpenAI's GPT API) for generating real responses.
3. Add token expiration and renewal mechanisms.
4. Implement rate limiting to prevent abuse of the Chat API.

---


