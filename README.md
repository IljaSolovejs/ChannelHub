# ChannelHub - CSC1025 Project 2

**Group ID:** 412  
**Student:** Ilja Solovejs 
**Module:** CSC1025 - Developing Internet Applications 

## About

ChannelHub is a Django-based web application for browsing and managing TV channels and their programmes. Users can browse channels by genre, view channel details and their programmes and register an account to add, edit or delete content.

## Features

- Browse TV channels with genre filtering
- Search channels by name
- View channel details and their programmes
- User registration and login system
- Add, edit and delete channels (authenticated users only)
- Add programmes to channels
- Image/logo uploads for channels and programmes
- Contact form
- Django admin panel

## Tech Stack

- Python / Django
- Bootstrap 5 (CDN)
- SQLite
- Pillow (image uploads)

## Apps

- `channels` - core app handling channels, programmes, views and contact form
- `accounts` - user registration and authentication

## Models

- `Channel` - name, description, genre, country, logo (ImageField), ForeignKey to User
- `Programme` - title, description, air time, image, ForeignKey to Channel

## How to Run

1. Install dependencies: `pip install django pillow`
2. Run migrations: `python manage.py migrate`
3. Start the server: `python manage.py runserver`
4. Visit `http://127.0.0.1:8000`

## Git Branching

- `main` - stable code
- `dev` - development branch
- `feature/*` - individual feature branches merged into dev