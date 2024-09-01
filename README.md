# Activity Monitoring System

A boilerplate for a real-time user activity monitoring system built with Python, Kafka, and PostgreSQL. This project provides RESTful APIs for user management and tracks user activities through Kafka, processing and logging them into a PostgreSQL database. Ideal for developers looking to implement scalable, real-time activity tracking in their applications.

## Features

- **User Management:**
  - Create a new user
  - Retrieve a list of all users

- **Activity Tracking:**
  - Insert a new activity record for a user
  - Kafka consumer that processes messages from the `activity_tracking` topic and logs them into the database

## Architecture Overview

The system consists of the following components:

- **API Server:** Exposes RESTful APIs for user management and activity insertion.
- **Kafka Consumer:** Consumes messages from the `activity_tracking` Kafka topic, processes the data, and inserts it into the `activity` table.
- **Database:** Contains two tables, `user` and `activity`, for storing user information and their activities respectively.

## API Endpoints

1. **Create a New User**
   - **Endpoint:** `POST /user/v1/create`
   - **Description:** Creates a new user in the system.
   - **Request Body:**
     ```json
     {
       "name": "John Doe",
       "mobile": "1234567890",
       "email": "john.doe@example.com"
     }
     ```
   - **Response:**
     ```json
     {
       "id": "550e8400-e29b-41d4-a716-446655440000",
       "name": "John Doe",
       "mobile": "1234567890",
       "email": "john.doe@example.com",
       "created_at": "2024-09-01T12:34:56Z",
       "updated_at": "2024-09-01T12:34:56Z"
     }
     ```

2. **Get Users List**
   - **Endpoint:** `GET /user/v1/list`
   - **Description:** Retrieves a list of all users in the system.
   - **Response:**
     ```json
     [
       {
         "id": "550e8400-e29b-41d4-a716-446655440000",
         "name": "John Doe",
         "mobile": "1234567890",
         "email": "john.doe@example.com",
         "created_at": "2024-09-01T12:34:56Z",
         "updated_at": "2024-09-01T12:34:56Z"
       },
       {
         "id": "7d5b9d0a-1f2e-4c8b-9bd7-3e3f69573b90",
         "name": "Jane Smith",
         "mobile": "9876543210",
         "email": "jane.smith@example.com",
         "created_at": "2024-09-02T08:15:30Z",
         "updated_at": "2024-09-02T08:15:30Z"
       }
     ]
     ```

3. **Insert Activity (via Kafka)**
   - **Description:** Activities are inserted into the system through Kafka. The Kafka consumer listens to the `activity_tracking` topic, processes incoming messages, and logs the activity into the `activity` table.
   - **Sample Kafka Message:**
     ```json
     {
       "name": "User Login",
       "description": "User logged in successfully"
     }
     ```
   - The above message would be consumed by the Kafka consumer, processed, and then inserted into the `activity` table with the provided `name` and `description`.
  

## Database Schema

### 1. `user` Table

| Column      | Type      | Description                                |
|-------------|-----------|--------------------------------------------|
| `id`        | UUID      | Primary Key, Unique Identifier for the user |
| `name`      | String    | Name of the user, cannot be null            |
| `mobile`    | String    | Mobile number of the user, can be null      |
| `email`     | String    | Email of the user, must be unique, can be null |
| `created_at`| DateTime  | Timestamp of when the user was created      |
| `updated_at`| DateTime  | Timestamp of the last update to the user record |


### 2. `activity` Table

| Column      | Type      | Description                                |
|-------------|-----------|--------------------------------------------|
| `id`        | UUID      | Primary Key, Unique Identifier for the activity |
| `name`      | String    | Name of the activity, cannot be null        |
| `description`| String   | Description of the activity, can be null    |
| `created_at`| DateTime  | Timestamp of when the activity was created  |
| `updated_at`| DateTime  | Timestamp of the last update to the activity record |


### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rishabh30/kafka-activity-tracker.git
   cd kafka-activity-tracker

2. Install dependencies:
   pip install -r requirements.txt

3. Set up the database:
   *- Start a PostgreSQL database with the following environment variables:*
   - HOSTNAME = os.getenv("DATABASE_HOSTNAME", "localhost")
   - USERNAME = os.getenv("DATABASE_USERNAME", "postgres")
   - PASSWORD = os.getenv("DATABASE_PASSWORD", "password")
   - DB = os.getenv("DATABASE_DB", "activity_tracking")
   - PORT = int(os.getenv("DATABASE_PORT", 5432))
**Note:** The database and tables will be automatically created on the service startup.

5. Configure Kafka:
   - Ensure that a Kafka broker is running and accessible.
   - Create the activity_tracking topic.

6. Configure environment variables:
   - Update the database and Kafka configurations.

### Running the System

*Start the API Server:*
- python app.py
The server will start on the default port (e.g., http://localhost:8080/).

### Testing
You can also produce messages to the activity_tracking Kafka topic to simulate activity insertion.
