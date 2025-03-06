# FastAPI Backend Project

This Template is a FastAPI backend-only application that uses SQLAlchemy for ORM, RabbitMQ for messaging, and PostgreSQL as the database. The structure is organized to maintain clean separation of concerns and follows best practices for a scalable and maintainable project.

## Folder Structure

```plaintext
myproject/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   │   └── dependencies.py
│   ├── main.py
│   ├── models/
│   │   ├── user.py # sample model, you'll add others below
│   │   └── __init__.py
│   ├── routers/
│   │   ├── user.py
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── user.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── rabbitmq.py
│   │   └── user.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       ├── common.py
│       └── email.py
├── docker-compose.yml
├── requirements.txt
├── Dockerfile
└── README.md
```

### Explanation of Folder Structure

- **src/**: Main source directory.
  - **core/**: Core utilities and configurations.
    - **config.py**: Configuration settings (e.g., environment variables).
    - **security.py**: Security-related functions (e.g., password hashing).
    - **dependencies.py**: Common dependencies to be injected into routes.
  - **main.py**: The entry point of the FastAPI application.
  - **models/**: Database models.
    - **user.py**: Database model for the user entity.
  - **routers/**: API routers.
    - **user.py**: API routes for user operations.
  - **schemas/**: Pydantic schemas for data validation and serialization.
    - **user.py**: Pydantic schemas for the user entity.
  - **services/**: Business logic and service layer.
    - **database.py**: Database connection and session management.
    - **rabbitmq.py**: RabbitMQ connection and utility functions.
    - **user.py**: Business logic for user-related operations.
  - **utils/**: Utility functions and helpers.
    - **logger.py**: Logging configuration and utilities.
    - **common.py**: Common utility functions.
    - **email.py**: Email sending utilities.

### Docker and Requirements

- **docker-compose.yml**: Docker Compose file for setting up the application with PostgreSQL and RabbitMQ.
- **requirements.txt**: List of Python dependencies for the project.
- **Dockerfile**: Dockerfile for building the FastAPI application container.

### Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MurungaOwen/fast-api_starter_template.git
   cd fast-api_starter_template
   ```

2. **Set up the environment**:
   Create a `.env` file in the root directory and add the necessary environment variables.

3. **Build and run the application**:
   ```bash
   docker-compose up --build
   ```

4. **Access the API**:
   The API will be available at `http://localhost:8000`.

### Usage

#### Logging

The `logger.py` file provides a simple logging setup:

```python
from src.utils.logger import get_logger

logger = get_logger(__name__)

logger.info("This is an info message")
logger.error("This is an error message")
```

#### API Endpoints

- **Root Endpoint**: `GET /` - Returns a "Hello World" message.
- **User Endpoint**: `POST /users/` - Creates a new user.

### Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

### License

This project is licensed under the MIT License.