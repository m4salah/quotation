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

* editor- ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFUVm1yTTA2eTFXd0h4U2hHNlZncSJ9.eyJpc3MiOiJodHRwczovL21vaGFtZWRzcGljZXIuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxNGI0NDk0MTBhNjUwMDA2ODk4OTNlMSIsImF1ZCI6InF1b3RhdGlvbiIsImlhdCI6MTYzMjMyMjc2NCwiZXhwIjoxNjMyMzI5OTY0LCJhenAiOiJIY0FCdldkTHQ2TUt0WTVCQ2NLaDRFelI2NnF2WnhqdiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOnBlcnNvbiIsImNyZWF0ZTpxdW90ZSIsImVkaXQ6cGVyc29uIiwiZWRpdDpxdW90ZSIsImdldDpwZXJzb25zIiwiZ2V0OnF1b3RlcyJdfQ.gJ7eirIPBRue6ncTK125zKDh3bqtsqBK8gZzuiGujDpH8VmyNRsFtqwwtecjNFKwH28wucxhaqpTBGANLLJYBmCKyzMqOYTDfqR0VR5V8JoseevAmmT_1ofLu9Po-Bpccl9GL88O4YKuD1JPwdbAWRac_XGsToDF92dcrJ2gEnz3rp3eazYjdKZoiCZGSZldOiHKhQ9fD8derYSTC4VUr0o9tjcyRVUPj3oQSf4Le6Ra7kywZGS65GbhhQaG3UMP-wlm-dumtjIMrTGQU4S9dMdtx0Qedt79V3hhgy7Qr7O0sYVmocy-PDveZVKYuJNWaFcYo13UwAJThVpHeuxeGw```

* admin - ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFUVm1yTTA2eTFXd0h4U2hHNlZncSJ9.eyJpc3MiOiJodHRwczovL21vaGFtZWRzcGljZXIuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxNGIzZjg4YjM1ODNmMDA3MDVmMGFmMiIsImF1ZCI6InF1b3RhdGlvbiIsImlhdCI6MTYzMjMyMTQ3NSwiZXhwIjoxNjMyMzI4Njc1LCJhenAiOiJIY0FCdldkTHQ2TUt0WTVCQ2NLaDRFelI2NnF2WnhqdiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOnBlcnNvbiIsImNyZWF0ZTpxdW90ZSIsImVkaXQ6cGVyc29uIiwiZWRpdDpxdW90ZSIsImdldDpwZXJzb25zIiwiZ2V0OnF1b3RlcyIsInJlbW92ZTpwZXJzb24iLCJyZW1vdmU6cXVvdGUiXX0.Pfvw4qZmKgSnbdXjTzX-DIAP_71snVDib3bvyyLARSYvPfFUcW2qd6AQ-_aw0xhR-tCGJChkH0-MFulhAFzhjTAvO4W_OaK9JpKZVYVZjkvRH0bcZBNXLiOgmGri8gC9Oj8tvHJg1Xz9mCPdk0bUsa3BTFQHS7-a8w_mMgYq6dMLNMiZjCvdNEpZW2FwXij27zaY8Ps0OeEtUiipJsj9daKKeDdam2TbtWv-VG5QAvsBy5fGrHqpKq3LOZAwxgA7B1nqAji0RgtT1vdBXj5tMHrEDatKKaILvuWClxqkc4IOBXh9XmjBSb84biYwMxlISD8cO6Qw2syIHcBTUPnFXQ```

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
