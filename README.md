# Bank security panel

## Project Description
 - This program is designed to monitor the monitoring of visits to the repository and identify suspicious activity in the repository.

## Technologies and tools
 - Python

## How to use
1. Clone this repository and go to the project folder:
   ```bash
   cd /c/project_folder # for example
   
   git clone https://github.com/JacobKleim/Bank_security_panel
   
   cd /c/project_folder/Bank security panel 
   ```

2. Create a file .new with parameters for the database and enter variables to connect to the database:
   for example:
   ```
   POSTGRES_USER=user
   POSTGRES_PASSWORD=password
   POSTGRES_DB=postgres
   DB_HOST=host
   DB_PORT=5432
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
   python main.py
   ```

## Example of work
![карта](https://github.com/JacobKleim/django-orm-watching-storage/assets/119351169/b108027b-0160-46c9-a7a3-50b21d2a2919)

![в хранилще](https://github.com/JacobKleim/django-orm-watching-storage/assets/119351169/64969470-ebf1-4e5e-8d13-9355087f6be4)

![карты](https://github.com/JacobKleim/django-orm-watching-storage/assets/119351169/b87a94f3-e724-459e-af2e-f91087b66595)



