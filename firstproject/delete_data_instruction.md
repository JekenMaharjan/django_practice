# INSTRUCTION TO DELETE DATA USING PYTHON SHELL

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

## Delete Records

To delete a record in a table, start by getting the record you want to delete:
```bash
>>> from members.models import Member
>>> x = Member.objects.all()[5]
```

x will now represent the member at index 5, which is "Jane Doe", but to make sure, let us see if that is correct:
```bash
>>> x.firstname
```

This should give you this result:
```bash
'Jane'
```

Now we can delete the record:
```bash
>>> x.delete()
```

The result will be:
```bash
(1, {'members.Member': 1})
```

Which tells us how many items were deleted, and from which Model.

If we look at the Member Model, we can see that 'Jane Doe' is removed from the Model:
```bash
>>> Member.objects.all().values()
<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'},
{'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'},
{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
{'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
{'id': 5, 'firstname': 'Stalikken', 'lastname': 'Refsnes'}]>
```

