# ReachLocal
ReachLocal's Django Project

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The following is the software stack required.
```
Python 3.x
pip
virtualenv
Django==2.0.3
djangorestframework
```

### Installing

A step by step series of examples that tell you how to get a development env running

#### Step1
Download python 3.x from https://www.python.org/downloads/ and install the exec.

#### Step2
Install pip from https://pip.pypa.io/en/stable/installing/

#### Step3
Install virtualenv with the following command.

```
pip install virtualenv
```

#### Step4
Create and activate a virtual environment. The following commands will create a new folder named myevn and activate it.

```
python -m venv myvenv
myvenv\Scripts\activate
```
#### Step5
Install Django 2.x and Django Rest Framework

```
pip install Django==2.0.3
pip install djangorestframework
```

## Migrating Data from newsapi.org to our local database

The below details will help you migrate the data from newsapi.org to our local database(sqlLite)

#### Step1

Open news/views.py file <br>
In the <strong>get</strong> method of the <strong>MigrateData class</strong>, input the api key of newsapi.org after "apikey="
and input a keyword of your search criteria after "q="
##### Example for migrating the news regarding Halloween to our local database update the URl as follows:	

``` 
url = 'https://newsapi.org/v2/everything?apiKey=theapikey&q=Halloween'
```

#### Step2
Start the server with the following command

```
python manage.py runserver
```
#### Step2
Access the URL http://127.0.0.1:8000/migratedata/ <br>
Each time we change the value of q= and load the above URL, new data will be migrated into our local database.

## Accessing Endpoints
The end points can be accessed from the URL http://127.0.0.1:8000/migratedata/ on clicking either HTML or JSON buttons.

## References
newsapi/articles - https://newsapi.org/docs/endpoints/sources <br>
djangorestframework - https://www.django-rest-framework.org/ <br>
class base views - https://docs.djangoproject.com/en/2.1/topics/class-based-views/ <br>
basic structuring of whole code - https://tutorial.djangogirls.org/en/ <br>

## Authors

* **Sudheer Singampalli** - (https://github.com/sudheersingampalli/)

