# HOW TO CREATE DJANGO ADMIN PANEL

## Create User
- To be able to log into the admin application, we need to create a user.
- This is done by typing this command in the command view:
    ```bash
    python manage.py createsuperuser
    ```
- Which will give this prompt: Here you must enter: username, e-mail address, (you can just pick a fake e-mail address), and password:
    ```bash
    Username: johndoe
    Email address: johndoe@dummymail.com
    Password:
    Password (again):
    This password is too short. It must contain at least 8 characters.
    This password is too common.
    This password is entirely numeric.
    Bypass password validation and create user anyway? [y/N]:
    ```
- My password did not meet the criteria, but this is a test environment, and I choose to create user anyway, by enter y:
    ```bash
    Bypass password validation and create user anyway? [y/N]: y
    ```
- If you press [Enter], you should have successfully created a user:
    ```bash
    Superuser created successfully.
    ```
- Now start the server again:
    ```bash
    python manage.py runserver
    ```
- In the browser window, type 127.0.0.1:8000/admin/ in the address bar. And fill in the form with the correct username and password.
- Now, Here you can perform CRUD operations i.e. Create, Read, Update and Delete groups and users.