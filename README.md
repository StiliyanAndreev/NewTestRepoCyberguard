# CloudSync API

A REST API for secure file synchronization and user management.

## Features
- JWT-based authentication
- File sync with conflict resolution
- PostgreSQL backend
- Docker support

## Setup
1. Clone the repository
2. Copy `.env.example` to `.env` and fill in values
3. Run `docker-compose up`
4. API runs on port 5000

## API Endpoints
- `POST /api/auth/login` — Authenticate user
- `POST /api/auth/register` — Register new user
- `GET /api/files` — List user files
- `POST /api/files/sync` — Upload and sync file
- `DELETE /api/files/<id>` — Remove file

## Tech Stack
- Flask 3.0, SQLAlchemy, PostgreSQL, JWT, bcrypt
