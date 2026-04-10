# INSTRUCTION TO INSERT DATA USING PYTHON SHELL

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

1. Import Member table from firstapp.models
    ```bash
    >>> from firstapp.models import Member
    ```

2. Check Member table which must be empty.
    ```bash
    >>> Member.objects.all()
    ```

    Result:
    ```bash
    <QuerySet []>
    ```

    A QuerySet is a collection of data from a database.

3. Add a record to the table, by executing these two lines:
    ```bash
    >>> member = Member(firstname='Emil', lastname='Refsnes')
    >>> member.save()
    ```

4. Execute this command to see if the Member table got a member:
    ```bash
    >>> Member.objects.all().values()
    ```

5. Hopefully, the result will look like this:
    ```bash
    <QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}]>
    ```

6. Add Multiple Records like this:
    ```bash
    >>> member1 = Member(firstname='Tobias', lastname='Refsnes')
    >>> member2 = Member(firstname='Linus', lastname='Refsnes')
    >>> member3 = Member(firstname='Lene', lastname='Refsnes')
    >>> member4 = Member(firstname='Stale', lastname='Refsnes')
    >>> member5 = Member(firstname='Jane', lastname='Doe')
    >>> members_list = [member1, member2, member3, member4, member5]
    >>> for x in members_list:
    ...   x.save()
    ...
    >>>
    ```

7. Check member table like this:
    ```bash
    >>> Member.objects.all().values()
    ```

8. Member table result should look something like this:
    ```bash
    <QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'},
    {'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'},
    {'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
    {'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
    {'id': 5, 'firstname': 'Stale', 'lastname': 'Refsnes'},
    {'id': 6, 'firstname': 'Jane', 'lastname': 'Doe'}]>
    ```
