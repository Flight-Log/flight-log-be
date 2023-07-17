# Flight Log - REST API

![Workflow Badge](https://github.com/Flight-Log/flight-log-be/actions/workflows/run-tests.yml/badge.svg)

## About Flight Log

Flight Log is a mobile application that allows aviation industry professionals to easily track their flight hours. Users will love the simple and easy-to-use app that enables them to log their flights digitally instead of in a physical notebook.

This RESTful API back end is built with Python and Django, and utilizes the [Django-REST-Framework](https://www.django-rest-framework.org/) toolkit.

Flight Log was conceptualized, designed, and developed over two weeks in July 2023, as part of the Capstone project for students in the Turing School of Software and Design.  More information about this project is available [here](https://mod4.turing.edu/projects/capstone/).

## Table of Contents

- [RESTful Endpoints](#restful-endpoints)
- [Set-Up](#set-up)
- [Usage](#usage)
- [Contributors](#contributors)

## RESTful Endpoints

<details close>

### [Get A User](https://flight-log-be-24cea5be4c8e.herokuapp.com/api/v1/users/1/)

<details close>

```http
GET /api/v1/users/:id/
```

<summary>  Details </summary>
<br>

Parameters: <br>

```
User ID
```

| Code | Description |
| :--- | :---------- |
| 200  | `OK`        |

Example Value:

```json
{
  "data": {
    "id": "1",
    "type": "user",
    "attributes": {
      "first_name": "Samuel",
      "last_name": "Adams"
    }
  }
}
```

| Code | Description |
| :--- | :---------- |
| 404  | `Not Found` |

Example Value:

```json
{
  "errors": [{ "detail": "User not found." }]
}
```

</details>

### [Get All Users](https://flight-log-be-24cea5be4c8e.herokuapp.com/api/v1/users/)

<details close>

```http
GET /api/v1/users/
```

<summary>  Details </summary>
<br>

Parameters: <br>

```
None
```

| Code | Description |
| :--- | :---------- |
| 200  | `OK`        |

Example Value:

```json
{
  "data": [
    {
      "id": "1",
      "type": "user",
      "attributes": {
        "first_name": "Samuel",
        "last_name": "Adams"
      }
    },
    {
      "id": "2",
      "type": "user",
      "attributes": {
        "first_name": "Mike",
        "last_name": "Jones"
      }
    }
  ]
}
```

</details>

### [Get All Flights for a User](https://flight-log-be-24cea5be4c8e.herokuapp.com/api/v1/users/1/flights/)

<details close>

```http
GET /api/v1/users/:id/flights/
```

<summary>  Details </summary>
<br>

Parameters: <br>

```
User ID
```

| Code | Description |
| :--- | :---------- |
| 200  | `OK`        |

Example Value:

```json
{
  "data": [
    {
      "id": "1",
      "type": "flight",
      "attributes": {
        "night_hours": "2.0",
        "day_hours": "1.0",
        "aircraft": "Boeing 737",
        "description": "great time!",
        "date": "2023-03-09",
        "start_location": "DEN",
        "end_location": "LAX",
        "role": "pilot"
      }
    },
    {
      "id": "2",
      "type": "flight",
      "attributes": {
        "night_hours": "4.0",
        "day_hours": "0.0",
        "aircraft": "Boeing 737",
        "description": "whoops we crashed!",
        "date": "2023-05-09",
        "start_location": "MIA",
        "end_location": "MSY",
        "role": "co-pilot"
      }
    },
    {
      "id": "3",
      "type": "flight",
      "attributes": {
        "night_hours": "9.0",
        "day_hours": "1.0",
        "aircraft": "Boeing 737",
        "description": "meh",
        "date": "2023-04-31",
        "start_location": "ATL",
        "end_location": "DAL",
        "role": "pilot"
      }
    }
  ]
}
```

| Code | Description |
| :--- | :---------- |
| 404  | `Not Found` |

Example Value:

```json
{
  "errors": [{ "detail": "Invalid user id." }]
}
```

</details>

### Create a Flight

<details close>

```http
POST /api/v1/users/:id/flights/
```

<summary>  Details </summary>
<br>

Required Parameters: <br>

```
Aircraft, Date, Start Location, End Location, Role
```

Optional Parameters: <br>

```
Night Hours, Day Hours, Description
Note: Hours will default to 0 if left blank
```

| Code | Description |
| :--- | :---------- |
| 201  | `OK`        |

Example Value:

```json
{
  "data": {
    "id": "1",
    "type": "flight",
    "attributes": {
      "night_hours": "2.0",
      "day_hours": "1.0",
      "aircraft": "Boeing 737",
      "description": "great time!",
      "date": "2023-03-09",
      "start_location": "DEN",
      "end_location": "LAX",
      "role": "pilot"
    }
  }
}
```

| Code | Description            |
| :--- | :--------------------- |
| 422  | `Unprocessable Entity` |

Example Value:

```json
{
  "errors": [{ "detail": "All fields must be filled in." }]
}
```

</details>
</details>

## Set-Up

### Prerequisites

Before getting started, ensure that you have the following installed on your system:

- Python (version 3.6 or higher)
- pip (Python package manager)

### Installation

Follow these steps to set up the Django REST app:

1. Clone the repository:

```
git clone https://github.com/Flight-Log/flight-log-be.git
```

2. Navigate to the project directory:

```
cd flight-log-be
```

3. Create a virtual environment (optional but recommended):

```
python -m venv env
```

4. Activate the virtual environment:

macOS/Linux:

```
source env/bin/activate
```

Windows:

```
source env/Scripts/activate
```

5. Install the dependencies:

```
pip install -r requirements.txt
```

6. Create a new Postgres user and give the user permissions to create a database:

```
psql
CREATE USER flightlog WITH PASSWORD 'flightlog';
ALTER USER flightlog CREATEDB;
\q
```

7. Create a database:

```
createdb -U flightlog -W "FlightLog"
```

When prompted to enter the password, enter `flightlog`

8. Run migrations:

```
python manage.py migrate
```

9. Create a superuser (admin) account:

```
python manage.py createsuperuser
```

10. Start the development server:

```
python manage.py runserver
```

The server should start running at http://127.0.0.1:8000/. You can access the admin interface at http://127.0.0.1:8000/admin/.

## Usage

Once the development server is running, you can start interacting with the API endpoints using tools like cURL, Postman, or your web browser. This API is also deployed on Heroku (links in [RESTful Endpoints section](#restful-endpoints) above).

## Contributors

- Caroline Peri
  - [LinkedIn](https://www.linkedin.com/in/carolineperi/)
  - [GitHub](https://github.com/cariperi)
- Brandon Johnson
  - [LinkedIn](https://www.linkedin.com/in/brandon-j-94b740b2/)
  - [GitHub](https://github.com/brenicillin)
- Katie Lonsdale
  - [LinkedIn](https://www.linkedin.com/in/katie-lonsdale-7b215185/)
  - [GitHub](https://github.com/KatieLonsdale)
