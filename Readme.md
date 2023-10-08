# MoveAPI - Movie Review REST API

MoveAPI is a Django REST API that allows users to access and review movies. Users can view movie details, add reviews, and retrieve a list of reviews. Additionally, the API provides information about the number of reviews and the average rating for each movie. Only administrators can add movies and the platforms that have those movies. Token Authentication is used to secure API access.

## Getting Started

These instructions will guide you through setting up and using the MoveAPI on your local machine.

### Prerequisites

Before you begin, make sure you have the following installed:

- Python (3.7 or higher)
- Django (3.0 or higher)
- Django Rest Framework (3.12 or higher)
- PostgreSQL (optional, but recommended for production)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/bhrayhaw/movieapi.git
2. Change into the project directory:
    ```bash
   cd movieapi
3. Create a virtual environment (recommended) and activate it:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
4. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Apply database migrations
    ```bash
    python manage.py migrate
    ```
6. Create a superuser account (an admin):
    ```bash 
    python manage.py createsuperuser
    ```
7. Start Development Server
    ```bash
    python manage.py runserver
### API Endpoints
For anyone to access all the endpoints you need to be a registered user or an admin

User Endpoints

`GET /api/movies/{movie_id}/ - Retrieve details of a specific movie.`
