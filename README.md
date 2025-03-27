# PythonRestaurantAPI

This project is a Python-based RESTful API for managing restaurant-related functionalities, including menu management, order processing, and user authentication.

## Table of Contents
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Features](#features)
- [Tech Stack](#tech-stack)

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/bcaron518/PythonRestaurantAPI.git
    cd PythonRestaurantAPI
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the server:
    ```sh
    python app.py
    ```

### Environment Variables

Create a `.env` file in the root directory with the following content:

    ```env
    DATABASE_URL=your_database_connection_string
    SECRET_KEY=your_secret_key

## API Endpoints

### User Endpoints
- `POST /api/users/register`: Register a new user
- `POST /api/users/login`: Authenticate a user

### Menu Endpoints
- `GET /api/menu`: Get all menu items
- `POST /api/menu`: Add a new menu item
- `PUT /api/menu/:id`: Update a menu item
- `DELETE /api/menu/:id`: Delete a menu item

### Order Endpoints
- `GET /api/orders`: Get all orders
- `POST /api/orders`: Create a new order
- `PUT /api/orders/:id`: Update an order
- `DELETE /api/orders/:id`: Cancel an order

## Features
- User authentication
- Menu management (CRUD operations)
- Order processing (CRUD operations)
- Responsive and efficient API design

## Tech Stack
- **Backend**: Python, Flask/Django, SQLAlchemy
- **Database**: PostgreSQL/MySQL
- **Authentication**: JWT, Flask-JWT-Extended/Django Rest Framework

## License
This repository is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as needed for your projects.

## Author
Benjamin Caron - https://github.com/bcaron518

## Contributing
If you'd like to contribute to this repository or improve the code examples, please feel free to open an issue or submit a pull request. Your contributions are welcome.
