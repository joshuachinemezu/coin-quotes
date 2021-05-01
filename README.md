# Currency Exchange Quotes

This API returns the real-time exchange rate for any pair of digital currency (e.g., Bitcoin) or physical currency (e.g., USD) using https://alphavantage.co

# Installation

-   Clone this repository.
-   Copy Sample of Environment Variables and Update the missing values
    <br/>`cp .env.example .env`
-   Get `ALPHAVANTAGE_API_KEY` from https://www.alphavantage.co/support/#api-key

## Building and Running without Docker

-   Install virtualenv https://virtualenv.pypa.io/en/stable/installation.html
-   Setup virtualenv `virtualenv venv`
-   Activate virtualenv `source venv/bin/activate`
-   Install dependencies
    <br>`make install` or `pip install -r requirements.txt`
-   Run the project
    <br>`make run` or `python manage.py runserver`

## Building and Running with Docker Compose

-   Build and Run with Docker
    <br>`make docker-up` or `docker-compose up --build`

<a name="admin-management"></a>

## Access Control and Management

-   Create Default Admin Account and follow the prompts
    <br> `make createsuperuser` or `python manage.py createsuperuser`
-   Visit http://127.0.0.1:8000/admin/rest_framework_api_key/apikey/ to create a new API KEY

### Available Endpoints

```
/api/v1/quotes/` - POST
    Headers:
         Api-Key: {API_KEY_GENERATED_BY_ADMIN}


/api/v1/quotes/` - GET
    Headers:
         Api-Key: {API_KEY_GENERATED_BY_ADMIN}

```

<br>

### Expected Response:

```
(Success): Status Code: 200
         {
              "status": true,
              "error": [],
              "data": {
                  "from_currency_code": "BTC",
                  "from_currency_name": "Bitcoin",
                  "to_currency_code": "USD",
                  "to_currency_name": "United States Dollar",
                  "exchange_rate": "58073.74000000",
                  "last_refreshed": "2021-05-01 02:58:06",
                  "time_zone": "UTC",
                  "bid_price": "58073.74000000",
                  "ask_price": "58073.75000000"
              },
              "message": "Operation was successful"
         }


(Error): Status Code: 401
         {
            "status": false,
            "data": [],
            "message": "Something went wrong",
            "error": {
                "detail": "Authentication credentials were not provided."
            }
        }

```

## Technologies:

-   Python (Django)
-   PosgreSQL
-   Redis
-   Celery
-   Docker
