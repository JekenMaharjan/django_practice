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


## Set Fields to Display

- **Make the List Display More Reader-Friendly**:   
    When you display a Model as a list, Django displays each record as the string representation of the record object, which in our case is "Member object (1)", "Member object(2)" etc.

To change this to a more reader-friendly format, we have two choices:

1. **Change the string representation function, __str__() of the Member Model**

    To change the string representation, we have to define the __str__() function of the Member Model in models.py, like this:

    *firstproject/firstapp/models.py:*
    ```py
    from django.db import models

    class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    ```

2. **Set the list_display property of the MemberAdmin class**

    We can control the fields to display by specifying them in a list_display property in the admin.py file.
    First create a MemberAdmin() class and specify the list_display tuple, like this:

    *firstproject/firstapp/admin.py:*
    ```py
    from django.contrib import admin
    from .models import Member

    # Register your models here.

    class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)
    
    admin.site.register(Member, MemberAdmin)
    ```


## Update Members

Now we are able to create, update, and delete members in our database, and we start by giving them all a date for when they became members.

Click the first member, Stalikken, to open the record for editing, and give him a joined_date.  
While we are in here, let us give him a phone number as well.  
Click "SAVE" and go back to the list of all members.  
Repeat these steps and give all members a date and a phone number, and end up with a list like this i.e. full info given.

