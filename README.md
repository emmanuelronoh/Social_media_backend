# Social Media Backend Application

A robust backend application for managing a social media platform. Built with Flask, SQLAlchemy, and JWT for secure user authentication, this application supports user registration, post management, and comment functionalities.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (registration, login, token-based authentication)
- Post management (create, read, update, delete posts)
- Comment management (add, read comments for posts)
- User profile management (view and update user details)
- Role-based access control (admin and user roles)
- Pagination and filtering for posts

## Technologies

- **Backend**: Flask
- **Database**: PostgreSQL or SQLite
- **Authentication**: JWT (JSON Web Tokens)
- **ORM**: SQLAlchemy
- **Environment Management**: dotenv

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- PostgreSQL (if using PostgreSQL)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/social-media-backend.git
    cd social-media-backend
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Set up your environment variables**:  
   Create a `.env` file in the root directory and add the following:
    ```env
    SECRET_KEY=your_secret_key
    DATABASE_URL=your_database_url
    ```

6. **Initialize the database**:
    ```bash
    flask db upgrade
    ```

## Usage

1. **Run the application**:
    ```bash
    flask run
    ```
   The API will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

2. **Use Postman or any API client to interact with the API endpoints**.

## API Endpoints

### Authentication

- **Register User**
  - `POST /api/register`
  
- **Login User**
  - `POST /api/login`

### Posts

- **Get All Posts**
  - `GET /api/posts`
  
- **Create Post**
  - `POST /api/posts`
  
- **Update Post**
  - `PUT /api/posts/<post_id>`

- **Delete Post**
  - `DELETE /api/posts/<post_id>`

### Comments

- **Add Comment to Post**
  - `POST /api/posts/<post_id>/comments`
  
- **Get Comments for Post**
  - `GET /api/posts/<post_id>/comments`

## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request.

1. **Fork the repository**.
2. **Create a new branch for your feature or bug fix**.
3. **Make your changes and commit them**.
4. **Push to the branch and create a pull request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
