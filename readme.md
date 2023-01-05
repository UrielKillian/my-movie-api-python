# Initialize the project

## Create your own environment

``py -m venv venv``

Activate the environment

``
venv/Scripts/activate
``

## Dependencies

Install those dependencies

``
pip install fastapi uvicorn
``

or use this 

``
pip install -r requirements.txt``

If the file don't exist. You can create this file automatically using this command.

``
pip freeze > requirements.txt``


To start the project: ``uvicorn main:app --reload``

To change the port: ``uvicorn main:app --reload --port ${number_of_the_port}``

To make this available to all the devices of this red add the flag: ``--host 0.0.0.0``


# Swagger in OpenAPI

Enter to your localhost and add /docs to the url.
http://localhost:8000/docs
