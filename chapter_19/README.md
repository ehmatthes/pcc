---
layout: default
title: Chapter 19
---

Updates
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

