# 📝 Blog Application Backend

A modern, scalable blog backend API built with FastAPI, featuring user authentication, CRUD operations for blog posts, and a clean, well-documented REST API architecture.

## 🚀 Features

- **User Authentication & Authorization**: JWT-based authentication with secure user registration and login
- **Blog Post Management**: Full CRUD operations for blog posts (Create, Read, Update, Delete)
- **User Management**: User profile management and user-specific blog posts
- **Category Management**: Organize blog posts by categories
- **Search & Filtering**: Search blog posts by title, content, or author
- **Pagination**: Efficient data retrieval with pagination support
- **Input Validation**: Comprehensive request validation using Pydantic models
- **API Documentation**: Auto-generated interactive API documentation with Swagger UI
- **Database Integration**: SQLAlchemy ORM with support for multiple databases
- **Security**: Password hashing, JWT tokens, and secure API endpoints
- **Error Handling**: Comprehensive error handling and meaningful error messages

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Database**: SQLModel/SQLAlchemy (MySQL)
- **Authentication**: JWT (JSON Web Tokens)
- **Validation**: Pydantic
- **Password Hashing**: bcrypt
- **Documentation**: Swagger UI (built-in with FastAPI)
- **Testing**: pytest
- **Environment Management**: python-dotenv

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- PostgreSQL/MySQL/SQLite (depending on your database choice)

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/AkshayRane05/Blog-Application-Backend.git
   cd Blog-Application-Backend
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:

   ```env
   DATABASE_URL=postgresql://username:password@localhost/blog_db
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. **Set up the database**

   ```bash
   # Create database tables
   python -c "from blog.database import create_tables; create_tables()"
   ```

6. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

## 📁 Project Structure

```
Blog-Application-Backend/
├── blog/
│   ├── database.py          # Database configuration and connection
│   ├── hashing.py           # Hashing the passwords
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py
│   ├── token.py
│   ├── routers/             # API route handlers
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── blog.py
│   │   ├── authentication.py
│   │   └── oauth2.py
|   ├── repository/             # API route handlers
│   │   ├── user.py
│   │   └── blog.py
├── main.py                  # FastAPI application entry point
├── requirements.txt         # Python dependencies
├── .gitignore
├── README.md
└── LICENSE
```

## 🔗 API Endpoints

### Authentication

- `POST /login` - User login (returns JWT token)

### Users

- `POST /user/` - Create a new user profile
- `GET /user/{id}` - Get user by ID

### Blog Posts

- `GET /blog/` - Get all blog posts (with pagination)
- `POST /blog/` - Create a new blog post
- `GET /blog/{id}` - Get a specific blog post
- `PUT /blog/{id}` - Update a blog post
- `DELETE /blog/{id}` - Delete a blog post

## 📚 API Documentation

Once the server is running, you can access the interactive API documentation at:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🧪 Testing

Run the test suite using pytest:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_auth.py
```

## 🚀 Deployment

### Using Docker

1. **Build the Docker image**

   ```bash
   docker build -t blog-backend .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 --env-file .env blog-backend
   ```

### Using Docker Compose

```bash
docker-compose up -d
```

### Manual Deployment

1. Set up your production environment variables
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your production database
4. Run with a production ASGI server:
   ```bash
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

## 🔐 Security Features

- **Password Hashing**: Uses bcrypt for secure password storage
- **JWT Authentication**: Stateless authentication with configurable expiration
- **Input Validation**: All inputs validated using Pydantic schemas
- **SQL Injection Protection**: SQLAlchemy ORM provides protection against SQL injection
- **CORS Configuration**: Configurable CORS settings for frontend integration

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Akshay Rane**

- GitHub: [@AkshayRane05](https://github.com/AkshayRane05)

## 📞 Support

If you have any questions or need help with setup, feel free to:

- Open an issue on GitHub
- Contact the author directly

## 🔄 Version History

- **v1.0.0** - Initial release with basic blog functionality
- More updates coming soon...

---

⭐ If you found this project helpful, please give it a star on GitHub!
