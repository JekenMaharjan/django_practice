# INSTRUCTION TO UPDATE MODEL

## Add Fields in the Model

To add a field to a table after it is created, open the models.py file, and make your changes:
```py
from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField()
    joined_date = models.DateField()
```

As you can see, we want to add phone and joined_date to our Member Model.

This is a change in the Model's structure, and therefore we have to make a migration to tell Django that it has to update the database:
```bash
python manage.py makemigrations members
```

> Note: Make sure you are back in the virtual environment before running the command.

The command above will result in a prompt, because we try to add fields that are not allowed to be null, to a table that already contains records.

As you can see, Django asks if we want to provide the fields with a specific value, or if we want to stop the migration and fix it in the model:
```bash
python manage.py makemigrations members
You are trying to add a non-nullable field 'joined_date' to members without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option:
```

I will select option 2, and open the models.py file again and allow NULL values for the two new fields:
```py
from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
```

And make the migration once again:
```bash
python manage.py makemigrations members
```

Run the migrate command:
```bash
python manage.py migrate
```

## Insert Data

First we enter the Python Shell:
```bash
python manage.py shell
```

Run these commands:
```bash
>>> from members.models import Member
>>> x = Member.objects.all()[0]
>>> x.phone = 5551234
>>> x.joined_date = '2022-01-05'
>>> x.save()
```

Execute this command to see if the Member table got updated:
```bash
>>> Member.objects.all().values()
```

The result should look like this:
```bash
<QuerySet [
{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes', 'phone': 5551234, 'joined_date': datetime.date(2022, 1, 5)},
{'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None},
{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None},
{'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None},
{'id': 5, 'firstname': 'Stalikken', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None}]>
```

