# HOW TO PREPARE TEMPLATE

1. **Create Template**: Create HTML file inside templates file that you want to display.

2. **Modify View**:
    - Import required Django tools
        ```py
        from django.http import HttpResponse
        from django.template import loader
        from .models import Member
        ```

    - Create a view function
        ```py
        def members(request):
        ```

    - Get data from database
        ```py
        mymembers = Member.objects.all().values()
        ```

    - Load HTML template
        ```py
        template = loader.get_template('all_members.html')
        ```

    - Send data to template
        ```py
        context = {
        'mymembers': mymembers,
        }
        ```

    - Return response to browser
        ```py
        return HttpResponse(template.render(context, request))
        ```

    - WorkFlow:  
        *Get data from database → Load HTML template → Send data to template → Show result in browser*

3. **Modify Urls**
    - Import required things
        ```py
        from django.urls import path
        from . import views
        ```

    - Create URL list
        ```py
        urlpatterns = [...]
        ```

    - Create URL path
        ```py
        path('members', views.members)
        ```

    - WorkFlow:  
        *User visits /members → Django checks urlpatterns → calls members view → view returns response → page shown in browser*

