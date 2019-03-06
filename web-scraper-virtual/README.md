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

Deployment + Easier way to run the app
======================================
#### If You will be using gunicorn you can use the command $ gunicorn -w 4 -b 127.0.0.1:8000 app:app. , that command will create 4 workers and binds the IP address given with the port number assigned
#### NB: you will need a configuration file to serve application via gunicorn and ngnix when in production to run web server as a service.
#### The coolest way to deploy a python app I've seen so far is using docker.Here is how to get started:
  1. Install docker from https://docs.docker.com/docker-for-mac/install/ , depending on your operations system
  2. while in same directory for web-sraper-virtual create a new file called Dockerfile. The content of the file:
   ~~~
   FROM python:3.6
   COPY . /app
   WORKDIR /app
   RUN pip install -r requirement.txt
   ENTRYPOINT ["python"]
   CMD ["app.py"]
   ~~~
  now when you type $ ls you should see the following folders:
  Dockerfile		app.py			README.md			templates requirement.txt
  3. Run $docker build -t web-scraper 
  4. Run $docker run -d -p 5000:5000 web-scraper:latest
  that is it! you should now go to your favourite browser and enter localhost:5000 you should see the app up and running.
  ![screen shot 2019-03-06 at 09 25 12](https://user-images.githubusercontent.com/20061747/53866615-3ed08800-3ff2-11e9-8c51-5ac5d6f89f30.png)
![screen shot 2019-03-06 at 09 29 21](https://user-images.githubusercontent.com/20061747/53866681-632c6480-3ff2-11e9-9a91-41dbf2c9e7d7.png)
![screen shot 2019-03-06 at 09 30 36](https://user-images.githubusercontent.com/20061747/53866780-a555a600-3ff2-11e9-9dd8-c1dd72b5ef23.png)
  
  
#### samson Takele Demma 
#### +421-949-227-950
#### sami.dsami@gmail.com 


