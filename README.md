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

### JWT Tokens for each role:
* reader - ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFUVm1yTTA2eTFXd0h4U2hHNlZncSJ9.eyJpc3MiOiJodHRwczovL21vaGFtZWRzcGljZXIuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxNGE5Zjg5ZGU0NWQzMDA2OTJiMTk5ZiIsImF1ZCI6InF1b3RhdGlvbiIsImlhdCI6MTYzMjMyMTEzMiwiZXhwIjoxNjMyMzI4MzMyLCJhenAiOiJIY0FCdldkTHQ2TUt0WTVCQ2NLaDRFelI2NnF2WnhqdiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OnBlcnNvbnMiLCJnZXQ6cXVvdGVzIl19.VpjXa5_oUaaslJeyCcoPNR6t6aeEHXFI7q8K3QI_osLALyrhSu1bHkD9mpsgXR5RX5vBrqTzbaBU1hHhmYqO_lF4cNChzNjXnTsVL5R8c01lGH6Ba7LhlJnm0zRMyjdjoSQl_ujniTAxqRBtY_SEny2TCaTDJn4t0zv4MS5rrUmZHi_oHqAAz3dMpdtE-taZkmwaReSGtrLZXGfK2jyXkETUKu-NRLAOicjwg8zbbFvd_9K52M2hQYwH-DyxbGYWweutlzoidHL2JjmGTsK5DhcOxYrvEenMUwSncOHc_p4TXobCN5FbmdP59CcIuircpR_q9vkrFD7E7gwHbMVfQg```

* Casting Director- ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVPcHlkUXpPRFVjTUFIYjBtSmp5QyJ9.eyJpc3MiOiJodHRwczovL2dmcmVkLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTg5YzgxZjg1ZGQ5ODBjNjhlMzA0MmYiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg3MDMyNzQ3LCJleHAiOjE1ODcxMTkxNDYsImF6cCI6IlEzUHJVMWh6UUJJSjdEMFhjUXA0eUttN041dnJOV2pBIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiZGVsZXRlOmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIiwidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.B9A7vWXbJOg6KY1hBf2sczrqdyD8Ue0_zrqgdEbhS_LMtbBnpbqDudtOM0CJ_yd5pGMPK6lJDbiKKSRxgDyYl0XsHOsh6Za3aXXo14Xp_8zSTrI2B9mbbhRURxo6xK2uDJ6FfsV6e35HaWHWZxqYRikO0vRveTGmRWJu7I7PNjr1AO1YuAHQI5vkrCvWimThx8Awf99qUaja28CyWRwywg1OUxVVA33DND9PFazmfIZQNQbP0KjHIL8UwN-aLUpNJI7hHSqM1W1GLSqyOgzZj7Drhas54KDtUWnoyWyR8OfKV9wKEPkVZ_Gv81s9ILm42PPL_Q472JgSESnmWUEQbA```

* admin - ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVPcHlkUXpPRFVjTUFIYjBtSmp5QyJ9.eyJpc3MiOiJodHRwczovL2dmcmVkLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZThhNTBlNTg1ZGQ5ODBjNjhlNWFmZjAiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg3MDMyODIwLCJleHAiOjE1ODcxMTkyMTksImF6cCI6IlEzUHJVMWh6UUJJSjdEMFhjUXA0eUttN041dnJOV2pBIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6YWN0b3JzIiwiYWRkOm1vdmllcyIsImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.YOm5uNPiWbhqdt0ZD1czu9PLT4SlaqF8lWzj1Cdp_3LrPLD2JVIZbphE4z8X9iM2Afdz1GnG_Bclhz5O5TvrnvRILc2I83yX2p3nPZhPiUt-T-qdGfP0BPAqxaTaKRDSd-wXtW_aTgb0NbaLyOFXOgIQDW2or0rpiEoLEdL1Bn9oQhxW947ZUdwCtkd_ThOC2gVRREPgTB-bO_4h7EwqQJAnJVHmyHVtsM9v3s_jk48cb7M1T9N_zlGuq7NWK8wAwzwkPnKd7b7W9oVIm7XhTA3J3eMjVetKR0j6pkVkLKjZU4tOBmqnV-CJ6uN3s_xGJuxMsXKEqUedIrswixvpmw```

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
