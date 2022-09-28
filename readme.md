# To Run:

`uvicorn app.main:app --host localhost --port 8000 --reload`

# Alembic:

Generate migration scripts for Users table
`alembic revision --autogenerate -m "create users table"`

Push to PostgreSQL:
`alembic upgrade head`
