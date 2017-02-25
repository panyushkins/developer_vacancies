This project about programmer vacancies from Russian HR-site Superjob. It uses Superjob's API for download information about job vacancies.

For using this applications, you should have API code for Superjob. You can get it from [Developer's portal Superjob](https://api.superjob.ru/).    
Firstly, you should register your application. After it you will get a key.

**Requirements**  
This applications use additionally installing package: 
* requests

###List of vacancies (`list_of_vacancies.py`)
In this application you can get around 100 vacancies for programmers, downloaded from Superjob's API. It will be stored in the txt-file in JSON-format.

Please, input your API-key (from Developer's Superjob section) and name (or path) of file with vacancies.

You can start the application with cmd: `python list_of_vacancies.py`. 