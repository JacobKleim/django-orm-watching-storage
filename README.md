# Bank security panel

## Project Description
 - This program is designed to monitor the monitoring of visits to the repository and identify suspicious activity in the repository.

## Technologies and tools
 - Python 3.9.10

## How to use
1. Clone this repository and go to the project folder:
   ```bash
   cd /c/project_folder # for example
   
   git clone https://github.com/JacobKleim/Bank_security_panel
   
   cd /c/project_folder/Bank security panel 
   ```

2. Create a file .new with parameters for the database and enter variables to connect to the database:
   ```
   POSTGRES_USER: The username for connecting to the PostgreSQL database.
   
   POSTGRES_PASSWORD: The password for connecting to the PostgreSQL database.
   
   POSTGRES_DB: The name of the PostgreSQL database to use.
   
   DB_HOST: The hostname or IP address of the database server.
   
   DB_PORT: The port number on which the database server is listening.
   
   SECRET_KEY=A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value.
   
   DEBUG=A boolean that turns on/off debug mode. If your app raises an exception when DEBUG is True, Django will display a detailed traceback, including a lot of metadata about your environment, such as all the currently defined Django settings (from settings.py).
   
   ALLOWED_HOSTS=A list of strings representing the host/domain names that this Django site can serve. This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations.
   ```

3. Сreate and activate a virtual environment:
   ```bash
   python -m venv venv 
   
   source venv/Scripts/activate
   ```

4. Install dependencies:
   ```bash
   python -m pip install --upgrade pip

   pip install -r requirements.txt
   ```

5. Start the project:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
   open the website http://127.0.0.1:8000/


## Example of work
![карта](https://github.com/JacobKleim/django-orm-watching-storage/assets/119351169/b108027b-0160-46c9-a7a3-50b21d2a2919)

![в хранилще](https://github.com/JacobKleim/django-orm-watching-storage/assets/119351169/64969470-ebf1-4e5e-8d13-9355087f6be4)

![карты](https://github.com/JacobKleim/django-orm-watching-storage/assets/119351169/b87a94f3-e724-459e-af2e-f91087b66595)



