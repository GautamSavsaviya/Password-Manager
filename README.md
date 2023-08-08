# PasswordManager

A simple password manager project created using Django, HTML, and CSS.

## Features

* Securely store your passwords in a SQLite database.
* Generate strong passwords for your accounts.
* Easily search and manage your passwords.
* Access your passwords from anywhere with a web browser.
  

**Requirements to run this app:**
* Python 3.8+
* Virtualenv

## Getting Started

1. Clone the repository to your local machine.
   
   ```
   git clone https://github.com/GautamSavsaviya/Password-Manager.git
   ```

2. Create vitual environment:

   ```
   virtualenv venv
   ```
   
3. Install the dependencies by running the following command:

    ```
    pip install -r requirements.txt
    ```
4. Move into project folder 'vaaultguard':

   ```
   cd vualtguard
   ```

5. Run following command to migrate all models:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
   
6. Run the development server by running the following command:

   ```
   python manage.py runserver
   ```

   Open your web browser and navigate to ``` http://127.0.0.1:8000 ```.


   **For admin panel first create superuser:**
   ```
   python manage.py createsuperuser
   ```
   Now go to ```http://127.0.0.1:8000/admin/``` and login.


### Contributing
This project is open source and contributions are welcome. To contribute, please fork the repository and submit a pull request.


