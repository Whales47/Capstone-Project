# Movie Listing API

## Overview
The Movie Listing API allows users to list, view, rate, and comment on movies. It uses FastAPI and JWT for authentication. 

## Features
- **User Authentication**: Register, login, and generate JWT tokens.
- **Movie Listing**: Add, view, edit, and delete movies.
- **Movie Rating**: Rate and view ratings of movies.

## Requirements
- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie_listing_api.git
   cd movie_listing_api
2. Create a virtual environment and install dependencies
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
3. Set up the database (update DATABASE_URL in app/database.py).

4.  Run the application:
    uvicorn app.main:app --reload


