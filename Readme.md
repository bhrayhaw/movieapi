# MoveAPI - Movie Review REST API

MoveAPI is a Django REST API that allows users to access and review movies. Users can view movie details, add reviews, and retrieve a list of reviews. Additionally, the API provides information about the number of reviews and the average rating for each movie. Only administrators can add movies and the platforms that have those movies. Token Authentication is used to secure API access.

## Author

- Author: Elijah Yaw Apreko
- Email: elijahapreko@gmail.com

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
   ```

2. Change into the project directory:
   ```bash
   cd movieapi
   ```
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
   ```

### API Endpoints

For anyone to access all the endpoints you need to be a registered user or an admin

#### User Endpoints

**Create a user**

- To create a user you have to pass a post request with the data in the body of the POST request

`POST account/register/`

**Response**

- This is an example of a response from a successful registration
        
        {
        "response": "Registration successful",
        "username": "bhrayhawkwasi",
        "email": "kwasi1232@xyz.com",
        "token": "835c1072f5305051595b2181efec83baff1308b8"
        }

**Login as a User or Administrator**

- To login in as a user or an administrator you will need the username and password

`POST account/login/`

**Response**

- The login api retrieves the token provided upon registration and with that you can make any request

        {
        "token": "835c1072f5305051595b2181efec83baff1308b8"
        }

**Logout a user**

- This api signs a user out of the application and deletes the token associated with the user

`POST account/logout/`

**Response**

- This api returns a status code

#### Authentication

- To access any restricted endpoint you will need to include the token in the Authorization header for subsequent requests as follows: Token your_token_here

#### Movie Endpoints

`GET movies/`

- List all movies with pagination

`GET movies/{movie_id}`

- Retrieve details of a specific movie

#### Reviews Endpoints

`POST movies/{movie_id}/reviews-create/`

- Add a review for a movie (authenticated users only, one review per user per movie).

`GET movies/{movie_id}/reviews`

- List reviews for a movie

`GET movies/{movie_id}/reviews/{review_id}/`

- Retrieve details of a review for a movie by an authenticated user

`PUT movies/{movie_id}/reviews/{review_id}`

- Update review by the creator

`DELETE movies/{movie_id}/reviews/{review_id}`

- Delete review by the creator

### Administration

- Access the Django admin interface at http://localhost:8000/admin/ to add movies and platforms.

### Deployment

For production deployment, it's recommended to use a production-ready database (e.g., PostgreSQL) and a web server (e.g., Gunicorn or uWSGI). Ensure that you set proper environment variables for security and performance.

### Contributing

If you'd like to contribute to this project, please open an issue or submit a pull request on the GitHub repository.

### Acknowledgements

Thanks to the Django and Django Rest Framework communities for their excellent documentation and support.
