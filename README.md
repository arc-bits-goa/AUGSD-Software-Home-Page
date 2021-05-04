# AUGSD-Software-Home-Page

The Software Homepage is a web portal which can be used to store all augsd-software links so that they can be used/ downloaded whenever required by looking for the link on the web page of this web portal . Frontend is built on HTML/CSS and backend using Django python. The database used is PostgreSQL. Hosted using Heroku 

## Installation
Clone this repository into your system
```bash
git clone https://github.com/arc-bits-goa/AUGSD-Software-Home-Page.git
```
## Usage

->Create and activate a virtualenv.
```bash
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
virtualenv venv 
source venv/bin/activate
```

->Install required dependencies.
```bash
pip install -r requirements.txt
```
->Initial setup
```bash
python manage.py makemigrations
python manage.py migrate
```

->Run the server.
```bash
python manage.py runserver
```
