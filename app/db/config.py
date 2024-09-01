import os


class DatabaseConfig:
    HOSTNAME = os.getenv("DATABASE_HOSTNAME", "localhost")
    USERNAME = os.getenv("DATABASE_USERNAME", "postgres")
    PASSWORD = os.getenv("DATABASE_PASSWORD", "password")
    DB = os.getenv("DATABASE_DB", "activity_tracking")
    PORT = int(os.getenv("DATABASE_PORT", 5432))


class Constants:
    APP_HOST = os.getenv("APP_HOST", "localhost")
    APP_PORT = int(os.getenv("APP_PORT", 8080))


class Messages:
    CREATE_USER_SUCCESS = "User created successfully"
    CREATE_USER_FAILED = "User creation failed due to database error"
    GET_USER_SUCCESS = "Retrieved User successfully"
    USER_NOT_FOUND = "User not found with the given filters"
