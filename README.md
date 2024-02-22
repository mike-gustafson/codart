# Codart

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Using Codart](#using-codart)
- [Testing](#testing)
- [Deployment](#deployment)

## Introduction

Codart is a social media application focused on sharing code snippets with other developers

## Features

Key features:
- User authentication and profile management
- Real-time collaboration on code
- Networking with fellow engineers

## Technologies Used

Mention the technologies, frameworks, and libraries used in Codart. For example:
- Django
- SQLite3
- HTML/CSS/JavaScript
- Django REST Framework
- Bootstrap

## Setup

### Prerequisites

Python,
pip

### Installation

Follow the commands below

```bash
git clone https://github.com/yourusername/codart.git
cd codart
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

### Starting the App

```bash
python manage.py runserver
```

Go to 127.0.0.1:8000 in your browser

Create an account and try it out

### Testing

```bash
python manage.py test
```

### Deployment

Codart is deployed at: http://codart.social