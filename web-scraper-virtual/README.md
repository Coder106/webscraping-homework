 Web Scraper
 =============


### App is developed using Flask a Python web framework
### Main app file is named app.py , there is a separate templates directory which contains the static html files which will be rendered by the backend flask 

  ### After extracting the zip file follow the steps 
#### 1. Create virtual environment [optional step]
-command to create a virtual environment  $ virtualenv web-scraper-virtual 
    
#### 2. Activate virtualenv 
-command  to activate virtual environment $ source bin/activate

#### 3. Installl required modules/libraries using python's package manager pip 
pip install requests, pandas, pygal, flask, gunicorn
-command $ pip install requests
* all the libraries needed are included in requirements.txt file which was automically created by 
command $ pip freeze > requirements.txt .You can use pipenv to manage dependencies better in future. 
#### 4. Run the app.py file like you would any other python file 
-command $ python3 app.py 

#### 5. Go to your broswer and enter localhost:8000 to access the main page of the app 

#### 6. on the main page you will be presented with a form to submit the URL you are trying to extract data from

#### If You will be using gunicorn you can use the command $ gunicorn -w 4 -b 127.0.0.1:8000 app:app. , that command will create 4 workers and binds the IP address given with the port number assigned
#### NB: you will need a configuration file to serve application via gunicorn and ngnix when in production to run web server as a service.


#### samson Takele Demma 
#### +421-949-227-950
#### sami.dsami@gmail.com 


