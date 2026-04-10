# INSTRUCTION TO UPDATE DATA USING PYTHON SHELL

To open a Python shell, type this command:
```bash
python manage.py shell
```

The result should be something like this:
```bash
Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
```

Now, Type your commands into python shell starting with '>>>',

## Update Records

To update records that are already in the database, we first have to get the record we want to update:
```bash
>>> from members.models import Member
>>> x = Member.objects.all()[4]
```

x will now represent the member at index 4, which is "Stale Refsnes", but to make sure, let us see if that is correct:
```bash
>>> x.firstname
```

This should give you this result:
```bash
'Stale'
```

Now we can change the values of this record:
```bash
>>> x.firstname = "Stalikken"
>>> x.save()
```

Execute this command to see if the Member table got updated:
```bash
>>> Member.objects.all().values()
```

Hopefully, the result will look like this:
```bash
<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'},
{'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'},
{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
{'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
{'id': 5, 'firstname': 'Stalikken', 'lastname': 'Refsnes'},
{'id': 6, 'firstname': 'Jane', 'lastname': 'Doe'}]>
```