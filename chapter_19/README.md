---
layout: default
title: Chapter 19
---

Updates
---

- [Updates for Django 2.1](#updates-for-django-21)
- [Updates for Django 2.0](#updates-for-django-20)

Updates for Django 2.1
---

In Django 2.1, there is a slight change to the way user authentication is handled. This affects the way URLs in the `users` app are structured, and it affects the */users/views.py* file as well.

### p. 440, *The Login Page*

The */users/urls.py* file should look like this:

	"""Defines url patterns for users."""

	from django.urls import path
	from django.contrib.auth import views as auth_views

	from . import views

	app_name = 'users'
	urlpatterns = [
		# Login page.
	    path('login/',
	    	auth_views.LoginView.as_view(template_name='users/login.html'),
	    	name='login'),
	]

There are two differences here. We're importing a set of views from `django.contrib.auth`, as `auth_views`. Also, the path to the login view is structured differently, to use the default class-based view for logins, `LoginView`. In order to use our own login template, we provide the `template_name` argument in the call to the default view.

### p. 442, *The logout URL*

The */users/urls.py* file should look like this:

	"""Defines url patterns for users."""

	from django.urls import path
	from django.contrib.auth import views as auth_views

	from . import views

	app_name = 'users'
	urlpatterns = [
		# Login page.
	    path('login/',
	    	auth_views.LoginView.as_view(template_name='users/login.html'),
	    	name='login'),

	    # Logout page.
	    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	]

Again, the logout view uses the default class-based `LogoutView`. We don't need to pass a template name, because there is no template for logging out.

### p. 442-443, *The logout_view() View Function*

In Django 2.1 there is no need for a logout view, so ignore what you see in this section in the book. Instead, we'll use a setting called `LOGOUT_REDIRECT_URL` in *settings.py*. It doesn't really matter where this setting goes, but I like to put it in a section at the end of the file labeled `# My settings`:

	--snip--
	# My settings
	LOGOUT_REDIRECT_URL = '/'

This tells Django what page to redirect the user to when they click the logout link. After adding this setting to *settings.py*, move on to the section *Linking to the logout View*.

### p. 444, *The register() View Function*

Nothing has really changed about the way the register page is built. The only thing to note here is that the `django.contrib.auth` import line will look slightly different in Django 2.1, because we don't need to import the logout function. The import statement will look like this:

    from django.contrib.auth import login, authenticate


Updates for Django 2.0
---

### p. 429, *The new_topic URL*

The new_topic URL pattern should look like this:

	urlpatterns = [
	    --snip--
	    # Page for adding a new topic.
	    path('new_topic/', views.new_topic, name='new_topic'),
	]

*The `new_topic()` View Function*

The `reverse()` function has been moved to a different module, so its `import` statement has changed:

	from django.shortcuts import render
	from django.http import HttpResponseRedirect
	from django.urls import reverse

### p. 433, *The new_entry URL*

The new_entry URL pattern should look like this:

	urlpatterns = [
	    --snip--
	    # Page for adding a new entry.
	    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	]

### p. 436, *The edit_entry URL*

The edit_entry URL pattern should look like this:

	urlpatterns = [
	    --snip--
	    # Page for editing an entry.
        path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
	]

### p. 439, *Including the URLs from users*

The line to include the URLs from the `users` app should look like this:

	from django.urls import path, include
	from django.contrib import admin

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('users/', include('users.urls')),
	    path('', include('learning_logs.urls')),
	]

As we saw when including the URLs from `learning_logs`, we write a simple string for the base of the URL, `'users/'`. We leave out the `namespace` argument, because the namespace will be defined in the *users/urls.py* file.

### p. 440, *The Login Page*

The *users/urls.py* file should look like this:

	"""Defines url patterns for users."""

	from django.urls import path
	from django.contrib.auth.views import login

	from . import views

	app_name = 'users'
	urlpatterns = [
	    # Login page.
	    path('login/', login, {'template_name': 'users/login.html'},
	        name='login'),
	]

Here we've defined the `app_name` variable, which defines the namespace for the URLs associated with the `users` app. We've also used the `path()` function to define the URL pattern for the login page.

### p. 442, *The logout URL*

The logout URL pattern should look like this:

	urlpatterns = [
	    --snip--    
	    # Logout page.
	    path('logout/', views.logout_view, name='logout'),
	]

### p. 442-3, *The `logout_view()` View Function*

In *users/views.py*, the `reverse()` function needs to be imported from `django.urls`:

	from django.urls import reverse

### p. 444, *The register URL*

The register URL should look like this:

	urlpatterns = [
	    --snip--    
	    # Registration page.
	    path('register/', views.register, name='register'),
	]

### p. 449, *Modifying the Topic Model*

In *learning_logs/models.py*, the line that defines the foreign key relationship between topics and users should look like this:

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

This tells Django that when a user is deleted, all of the topics owned by that user should be deleted as well.
