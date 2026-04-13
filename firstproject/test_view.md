# Test View

When testing different aspects of Django, it can be a good idea to have somewhere to test code without destroying the main project.

- Start by adding a view called "testing" in the views.py file.
- We have to make sure that incoming urls to /testing/ will be redirected to the testing view. This is done in the urls.py file.
- We also need a template where we can play around with HTML and Django code. Create a template called "template.html" in the templates folder.