Chapter 20
===

Deploying a Project to Heroku
---

In this chapter you'll style Learning Log, and then deploy it to Heroku's servers. Once you've deployed the app, you'll be able to access it from any device, and you'll be able to share your work with others as well. This section will help you get your system set up for deploying projects to Heroku.

###Making a Heroku Account

To make an account, go to [https://heroku.com/](https://heroku.com/) and click one of the signup links. It’s free to make an account, and Heroku has a free tier that allows you to test your projects in live deployment.

###Installing the Heroku Toolbelt

To deploy and manage a project on Heroku's servers, you'll need the tools available in the Heroku Toolbelt. To install the latest version, visit [https://toolbelt.heroku.com/](https://toolbelt.heroku.com/) and follow the directions for your operating system. This will involve either a one-line terminal command or an installer you can download and run.

###Installing required packages

You'll also need to install a number of packages that help serve Django projects on a live server. In an active virtual environment, issue these commands:

    (ll_env)learning_log$ pip install dj-database-url
    (ll_env)learning_log$ pip install dj-static
    (ll_env)learning_log$ pip install static3
    (ll_env)learning_log$ pip install gunicorn

Issue the commands one at a time so you know if any package fails to install correctly. (Some of these packages may not install on Windows, so don't be concerned if you get an error message when you try to install some of them. This shouldn't affect your ability to deploy the project to Heroku.)

[top](#)