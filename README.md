# Quotation Capstone Project

This is my final capstone project for Udacity's FullStack Web Developer Nanodegree.
Web app can be accessed at [here](https://quotation-m.herokuapp.com/)

##### Project Dependencies
* __Flask__ - Slim python web library.
* __SQLAlchemy__ - Python ORM library
* __Heroku__ - PaaS platform for easy hosting of web apps
* __curl__ - API testing tool

### Installation instructions
* Clone project to directory of your choice.
* Create a virtualenv in project directory 
* run ```pip install -r requirements.txt``` to install project dependencies
* add ```DATABASE_URL``` to environment variables of your system. 
On Unix systems, use ```export DATABASE_URL={username}:{password}@{host}:{port}/{database_name}```
* run ```python3 app.py```


###Endpoints:
* GET /persons and /quotes
* DELETE /persons and /quotes
* POST /persons and /quotes
* PATCH /persons and /quotes

### Roles
* reader
    * GET /persons/ and /quotes

* editor
    * GET /persons/ and /quotes
    * ADD /persons/ and /quotes
    * PATCH /persons/ and /quotes
    
* admin
    * GET /persons/ and /quotes
    * ADD /persons/ and /quotes
    * PATCH /persons/ and /quotes
    * DELETE /persons/ and /quotes

### Auth0 Account Setup
If you would like to setup your own account with my Auth0 instance, you can do so at the URL below.
Auth0 URL: [here](https://mohamedspicer.eu.auth0.com/authorize?audience=quotation&response_type=token&client_id=HcABvWdLt6MKtY5BCcKh4EzR66qvZxjv&redirect_uri=http://localhost:5000/login-result)


## API Endpoints

### Default Path

#### GET /
Verifies that application is up and running on Heroku.

Sample response:
```
{
    "description": 'Quotation system is running.'
    "success": true
}
```

### GET Endpoints

#### GET /quotes
Displays all quotes listed in the database.

Sample response:
```
{
  "quotes": [
    {
      "description": "do something useful",
      "id": 1,
      "person_id": 3,
      "title": "Do somethingelse"
    },
    {
      "description": "do something useful",
      "id": 2,
      "person_id": 3,
      "title": "Mohamed"
    },
  ],
  "success": true,
  "total_quotes": 2
}
```

#### GET /persons
Displays all persons listed in the database.

Sample response:
```
{
  "persons": [
    {
      "id": 1,
      "name": "Mohamed"
    },
    {
      "id": 2,
      "name": "Mohamed"
    },
  ],
  "success": true,
  "total_persons": 2
}
}
```

### POST Endpoints

#### POST /persons
Creates a new person entry in the database.

Sample response:
```
{
  "created": 3,
  "persons": [
    {
      "id": 1,
      "name": "Mohamed"
    },
    {
      "id": 2,
      "name": "Mohamed"
    },
    {
      "id": 3,
      "name": "Mohamed"
    },
  ],
  "success": true,
  "total_persons": 3
}
```

#### POST /quotes
Creates a new quote entry in the database.

Sample response:
```
{
  "created": 12,
  "quotes": [
    {
      "description": "do something useful",
      "id": 1,
      "person_id": 3,
      "title": "Do somethingelse"
    },
    {
      "description": "do something useful",
      "id": 2,
      "person_id": 3,
      "title": "Mohamed"
    },
    {
      "description": "do something useful",
      "id": 3,
      "person_id": 4,
      "title": "Mohamed"
    },
  ],
  "success": true,
  "total_quotes": 3
}
```

### PATCH Endpoints

#### PATCH /quotes/<quote_id>
Updates quote information given a quote_id and newly updated attribute info.

Sample response:
```
{
  "quote_id": 4,
  "success": true
}
```

#### PATCH /persons/<person_id>
Updates person information given a person_id and newly updated attribute info.

Sample response:
```
{
  "person_id": 4,
  "success": true
}
```

### DELETE Endpoints

#### DELETE /quotes/<quote_id>
Deletes a quote entry from the database given the inputted quote_id.

Sample response:
```
{
    "id": 7,
    "success": true
}
```

#### DELETE /persons/<person_id>
Deletes an person entry from the database given the inputted person_id.

Sample response:
```
{
    "id": 7,
    "success": true
}
```
