# Educadia: Full-Stack Development Milestone Project


This is my final project at the Code Institute Full-Stack Web Developer course. The purpose of the project is to demonstrate my practical skilled that I gined in Django framework and and back-end development. The idea of the project is to serve an actual local school in my home country. Giving them a way to facilitate remote learning in the COVID times.

## Table of contents

* [Live](#Live)
* [User stories](#user-stories)
* [UX](#ux)
  * [Strategy plane](#strategy-plane)
  * [Scope plane](#scope-plane)
  * [Structure plane](#structure-plane)
  * [Skeleton plane](#skeleton-plane)
  * [Surface plane](#surface-plane)
* [Wireframes](#wireframes)
* [Features](#features)
* [Future implementations](#future-implementations)
* [Technologies](#technologies)
* [Challenges](#Challenges)
* [Deployment](#Deployment)
* [Testing](#Testing)
* [Credits](#credits)

## Live

The live educadia project is hosted on Heroku. you can access it [here](https://educadia-test.herokuapp.com/).

The following accounts are available for testing:

* teacher1 (for a teacher user type)
* student1 (for a student user type)


The password is learnonline for both accounts.

## User stories

The following user stories were considered:

* As a user, I want to register an account, so I can log in to the website.
* As a user, I want to reset my password if I forget it, so I can log in to the account.
  * Acceptance criteria: build a an authentication system based on the Django's allauth system

* As a user, I want to be able to add my full name, bio, and picture and edit them if I want to change any.
  * Acceptance criteria: build a user account model with add and edit functionality.

* As a teacher, I want to add/edit/delete classes.
  * Acceptance criteria: build class model and give CRUD access to teachers

* As a teacher, I want to add/edit/delete materials.
  * Acceptance criteria: build materials model and give CRUD access to teachers

* As a student, I want to view available classes to join.
  * Acceptance criteria: build a join class functionality

* As a student, I want to view class materials available in the classes I joined.
  * Acceptance criteria: have an access restriction to view each class materials for students

## UX

### Strategy plane

> What am I aiming to achieve in the first place, and for whom?

The project is for the teachers and the students. It includes one main functionality, everything else is to facilitate that functionality

The funtionality of the project is to give teachers a place online to share class materials with students, and to give the students organized views to access these materials. This function would serve 2 purposes; One, to have one place where all teachers add their classes and materials and for students to access them. Two, to have that virtual space go byond the physical space limitations allowing students from anywhere to join the class of a teacher they are interested in.
 

The initial registration for all users would make the user type a student, for a teacher to be registered a manual tracking from the admin would change the user type for that particular user to a teacher. This will prevent teachers outside of the school to register for this site.

### Scope plane

> What features do I want to include in my design?

The following features were for teachers:

* to be able to edit/update user details.
* to be able to add classes, where teacher can set a customized join code to share with any potential student.
* to be able to edit/delete classes.
* to be able to add/edit/delete materials from classes.

For students:

* to be able to edit/update user details.
* to join classes which I have the join code from the teacher.
* to be able to view and download class materials for the joined classes.


### Structure plane

> How is the information structured?

The landing page lists all the available classes, with teachers name on the top for ease to spot if looking for a particular teacher (if he/she exists on this site). if logged in, there will a join class button on each class. the point of that button is to inform the student of how to join a class, that he first needs to have the join code from the teacher of that class. When logged in (for both teachers and students), the user will be able to access classes and materials associated with that user in the database.

The structure of the database as follows:

* The User model is a built-in Django model coming from allauth.

* The UserAccount model for myaccount application, includes basic info about user:
  * user = OneToOneField(...) with the allauth model
  * first_names = CharField(...)
  * last_name = CharField(...)
  * user_type = CharField(...) auto set to student unless changed by the admin
  * bio = CharField(...)
  * image = ImageField(...)

* The AllClasses model for myclasses application, includes the details about a class:
  * added_by = ForeignKey(...) with the UserAccount model
  * class_name = CharField(...)
  * class_join_code = CharField(...)
  * class_subject = CharField(...)
  * class_university = CharField(...)
  * class_collage = CharField(...)
  * class_department = CharField(...)
  * class_level = CharField(...)
  * class_division = CharField(...)
  * class_year = CharField(...)

* The AllMaterials model for myclasses application, includes details about a material:
  * added_by = ForeignKey(...) with the UserAccount model
  * for_class = ForeignKey(...) with the AllClasses moddel
  * name = CharField(...)
  * doc = FileField(...)
  * link = CharField(...)
  * desc = CharField(...)

* The ClassRegister model for myclasses application, serves as a general register for classes:
  * student_name = ForeignKey(...) with the UserAccount model
  * registered_for = ForeignKey(...) with the AllClasses moddel
  * join_code = CharField(...)


### Skeleton plane

> How is the information implemented, and how will the user navigate through the features?

For the landing page, the navigation bar is is self explanatory to guide the user in the right direction. The mobile view has a simple navigation bar that slides down on click. Only the login, the registration, resources view is available when the user is not logged in. The my classes, my account, and logout becomes visible on the navigation bar after the successful authentication. The views are mostly one level so there was no need to include a button to take the user back a step, since clicking on the navigation links will do similar action.

### Surface plane

> What will the product look like?

The mobile-first approach design was implemented on this website to maintain the user experience from mobile devices to desktop computers. Bootstrap was used to achive the responsiveness.

Each page is divided into three sections: the navbar, the actual page that contains the information, and the footer.

The footer is made to be sticky to the bottom, as in it will remains hidden until the user scrolls down to the bottom of the page. If the contents of the page is short, the footer remains in the bottom of the page. it displays the copyright and the donation link where payments can be taken as a donation to the school

The navbar is simple. The colours are light but separated from each other. There is not much typography on the website yet. The default font was used for this reason. There is an slide down form which opens upon user click for both my account and my classes applications, used to keep the page contents organized and to keep the list of existing classes/materials seperated from the forms.

## Wireframes

* The wireframe was created to show an estimated look and feel of the website on mobile, tablet, and pc.

  * You can see the initial look of the pages as below:
    * Classes/home page:
        ![Classes/home](https://gist.github.com/AwsSG/7791b9d095ae5d7efb8d290f86f5e41d#gistcomment-3725920)
    * Login page:
        ![Login](https://gist.github.com/AwsSG/7791b9d095ae5d7efb8d290f86f5e41d#gistcomment-3725919)
    * Registration page:
        ![Registration](https://gist.github.com/AwsSG/7791b9d095ae5d7efb8d290f86f5e41d#gistcomment-3725921)
    * Student classes page:
        ![Student](https://gist.github.com/AwsSG/7791b9d095ae5d7efb8d290f86f5e41d#gistcomment-3725922)
    * Teacher classes page:
        ![Teacher](https://gist.github.com/AwsSG/7791b9d095ae5d7efb8d290f86f5e41d#gistcomment-3725923)



## Features

There are also a few hidden features in the backend,which is the heart of the project. It gathers all the information for the views and stores all the information that comes from the frontend. It is connected to a free Postgres database hosted by Heroku. The dj-database-url and the psycopg2-binary applications are connecting the database to the backend. The gunicorn application is responsible for running the Django website on the Heroku server. The static files and media content are hosted by the AWS S3 Cloud Storage API. The Stripe application ensures a smooth, secure, and convenient card payment. A short JavaScript code guarantees the real-time connection to [stripe.com](https://stripe.com/ie) for the enhanced user experience and the immediate card data validation.

In addition, because the main users (students in particular) of this project have limited knowledge, the teachers asked to have all verifications to be done by admin to avoid unwaned users. which will be done with the standard django admin panel by the head teacher of the school.

## Future implementations

I am planning to implement the following features in the future:

* to add a second language (Arabic) to the project, Making it easier for the users since it will be in their native language.
* to create webhooks for Stripe to ensure that every payment (donation) is stored in the database and every confirmation email is sent after a successful payment
* to add ability to chat between teachers and students
* to write more code for the backend to strengthen the defensive design
* to add contents for the dashboard and resources in the my account view that is pulled from the database for better UX
* to add ability for students to upload homework and assignemtns if a teacher assigns any.
* to include a new view as a library for small publications by the teachers

## Technologies

### Languages

Required technologies:

* HTML 5
* CSS 3
* JavaScript
* Python
* Django
* Relational database (MySQL or Postgres)
* Stripe payment
* Additional libraries and APIs

Technologies used in the project:

* HTML5
* CSS3
* JavaScript
* Python (3.8)
* Django 3.1
* AWS S3 Storage API

### Libraries and frameworks

* [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) framework for developing responsive websites
* [jQuery (3.5.1)](https://jquery.com/) library to use JavaScript easier on the website
* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) to handle forms in the project
* [dj-database-url](https://pypi.org/project/dj-database-url/) to use database URL in Django applications
* [Pillow](https://pypi.org/project/Pillow/) for Python Imaging/file Library
* [stripe](https://pypi.org/project/stripe/) to handle secure card payments
* [gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX
* [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) Python-PostgreSQL Database Adapter


### Challenges

I faced several challenges during the project, including the tight deadline and dealing with the complexity of django having no prior exposure to anything similar until my enrolment in CI. Few of the most difficult challenges I faced are:

* When I wrote the CRUD functionality for adding the materials, the old files were not deleted when instance is deleted. I looked for a solution a lot and could not find one that I can understand and implement. However, when I expressed this to my mentor he gave me some guidance on a simple way to override the delete functionality to make sure that it also deletes the file.

* allauth, while it offers great ease for the log in system, I found it to be quite comlicated to style, as well as to predict its behaviour. I used dev tools thoroughly and managed to have some styling, but its not the exact way I wanted it to look like. Plus, the model itself is standard, so I initially envisioned my UserAccount model to be part of the basic user model from allauth. But in reality it was too complicated for me to customize the allauth model, which is why I decided to use a secondary user model (UserAccount) to add the fields that suit this project (which is why the user is redirected to profile page right after successful authentication). Lastly, the messages in the allauth was also challenging to place in a toast, this issue I was not able to fix. You can see that when a new user is registered, a message will appear at the ttop of the page (that the confirmation email was sent) instead of it appearing in the toast like the other messages.

* UniqueConstraint for the class register model, because I wanted to prevent joining an already joined class (creating a duplicate instance for the student). I tried to use a unique constraint in the model, however, it proved to be quite complicated. Instead, I created a check in my classes view to perform that function.

* View class details for a student type user. Because the form to join a class will be submitted to class register model, I needed to somehow use the foreign key field with the User Account model to know if that student have already registered for a particular class. The way I was able to soleve that is by relying on the join code field in class register model, so first I created filter to check if the combination of that (student) user with that join code already exists in the database. Then only allow the join functionality if there is no prior registration for this class. This way can be problematic if 2 classes or more have the same join code. 

* Stripe website change. Therefore, I had to rely on code snippets from the CI BA project to move forward with setting up stripe. Plus, in this particular school, the donations will be handeled by the finance department which will have no access to this site. The solution to this was to give the financial department the backend of stripe to handle the payments receipts.

### Deployment

#### Running Code Locally


1. Follow this link to my [Repository on Github](https://github.com/AwsSG/educadia) and open it.

2. Click `Clone or Download`.

3. In the Clone with HTTPs section, click the `copy` icon.

4. In your local IDE open Git Bash.

5. Change the current working directory to where you want the cloned directory to be made.

6. Type `git clone`, and then paste the URL you copied earlier.

7. Press enter and your local clone will be ready.

8. Create and start a new environment:  
`python -m .venv venv`  
`source env/bin/activate`

9. Install the project dependencies:  
pip install -r requirements.txt

10. Create a new file, called `env.py` and add your environment variables:

`import os`  
`os.environ.setdefault("STRIPE_PUBLISHABLE", "secret key here")`\
`os.environ.setdefault("STRIPE_SECRET", "secret key here")`\
`os.environ.setdefault("DATABASE_URL", "secret key here")`\
`os.environ.setdefault("SECRET_KEY", "secret key here")`\
`os.environ.setdefault("AWS_ACCESS_KEY_ID", "secret key here")`\
`os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "secret key here")`

11. Go to `settings.py` file and add your environment variables.

12. Add `env.py` to .gitignore file

13. Go to terminal and run the following: `python3 manage.py makemigrations`, then `python3 manage.py migrate` to migrate all existing migrations to postgres database.

14. Create a superuser: `python3 manage.py createsuperuser`

15. Run it with the following command:  
`python manage.py runserver`

16. Open `localhost:8000` on your browser

17.  Add `/admin` to the end of the url address and login with your superuser account and create new products.

#### Deployment to Heroku

The following steps were taken in order to deploy this site to Heroku:

1. Created a new app in `Heroku` with a unique name, chose my region

2. Went to `Resources`, within Add-ons searched `Heroku Postgres`, chose Hobby Dev - Free version, then clicked `Provision` button.

3. In `Settings` clicked on `Reveal Config Vars` button, and copied the value of `DATABASE_URL`

4. Returned to terminal window and run `sudo pip3 install dj_database_url`

5. Also run `sudo pip3 install psycopg2`. Created a requirements.txt file using the terminal command `pip3 freeze > requirements.txt`

6. Went to `settings.py` and added `import dj_database_url` and updated `DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}` also updated `env.py` with `os.environ.setdefault("DATABASE_URL", "postgres://postgres key - copied earlier from Heroku")`

7. I run `python3 manage.py makemigrations`, then `python3 manage.py migrate` to migrate all existing migrations to postgres database.

8. I created a superuser: `python3 manage.py createsuperuser`

9. Logged in to `Amazon AWS`, went to `S3` and created a new `S3` bucket.

10. Returned to terminal window and run `sudo pip3 install django-storages` and `sudo pip3 install boto3`. Went to `settings.py` and added `storages` to `INSTALLED_APPS`.

11. Also in `settings.py` the following lines are added:

`AWS_STORAGE_BUCKET_NAME = 'educadia-test'`\
`AWS_S3_REGION_NAME = 'eu-west-1'`\
`AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")`  
`AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")`  
`AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME`

12. Updated `env.py` with `AWS` keys (these keys are from `S3`).

13. Created `custom_storages.py` at the top level:

`from django.conf import settings`  
`from storages.backends.s3boto3 import S3Boto3Storage`


`class StaticStorage(S3Boto3Storage):`  
`&nbsp;&nbsp;&nbsp;location = settings.STATICFILES_LOCATION`

`class MediaStorage(S3Boto3Storage):`  
`&nbsp;&nbsp;&nbsp;location = settings.MEDIAFILES_LOCATION`

14. Went to `settings.py` and added:

`STATICFILES_LOCATION = 'static'`  
`STATICFILES_STORAGE = 'custom_storages.StaticStorage'`

`MEDIAFILES_LOCATION = 'media'`  
`DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'`

15. Returned to terminal window and run `python3 manage.py collectstatic`

16. Returned to `Heroku`. In `Settings` clicked on `Reveal Config Vars` button, and added all the following config vars from `env.py`:

| Key         | Value | 
|:-------------:| :----: | 
|  AWS_ACCESS_KEY_ID | secret key here  |
|  AWS_SECRET_ACCESS_KEY | secret key here |
|  DATABASE_URL | secret key here |
|  DISABLE_COLLECTSTATIC| 1 |
|  SECRET_KEY | secret key here |
|  STRIPE_PUBLISHABLE | secret key here |
|  STRIPE_SECRET| secret key here |

17. Clicked to `Deploy`, then `GitHub`, searched for my repository and clicked to `Connect` button.

18. Returned to terminal window and run `sudo pip3 install gunicorn` and added to `requirements.txt`

19. Created a `Procfile` using the following command: `echo web: gunicorn ms4.wsgi:application`

20. Ran `git add .`, `git commit -m "my commit message"` and `git push` commands to push all changes to my GitHub repository.

20. Returned to `Heroku` and hit `Deploy Branch`

21. Once the build is complete, click on `Open app`

22. Went to `settings.py` and added `educadia-test.herokuapp.com` to `ALLOWED_HOSTS`

23. Ran `git add .`, `git commit -m "my commit message"` and `git push` commands to push all changes to my GitHub repository.

24. Returned to `Heroku` and hit `Deploy Branch` again.

### Testing

* During the development of the project I carried out testing, I used Google Chrome Developer Tools consistently to check each changes.

* I have tested the site on Google Chrome, Safari and Firefox. And on the following mobile devices: Samsung note20, iPhone11 and iPhone6. And on iPad tablet.

* Testing was done to ensure that all available (clickable) button are working properly and the links are liked correctly.

* A sample of teachers (3 teachers) and students (5 students) from the school were asked to review the site and documentation to point out any bugs and/or user experience issues. the following was found:

* Below is the detailed manual (logical) testing of all elements and functionality on every page:

| Action         | Expected result | Outcome | 
|:------------- | :---- | :----: | 
|  open landing/home page | home page loads with available classes cards and basic navigation  | SUCCESS |
|  attemt to sign up by navigating to sign up | sign up page loads and accepts user inputs / user gets email for confirmation  | SUCCESS |
|  attemt to login by navigating to login | login page loads and accepts user input / user is logged in only if both username and password are correct  | SUCCESS  |
|  attemt to signup / login from the inline link on login / sign up page | user can sign up / log in successfully exactly like the previous two tests  | SUCCESS  |
|  attemt to recover passowrd by clicking on forgot password | user can recover password by entering the account associated email  | SUCCESS  |
|  attemt to navigate as a logged in user | user have access to my classes & profile & log out in the navigation  | SUCCESS  |
|  attemt to fill profile details | user input is accepted in the profile page and the view reflects the changes after save | SUCCESS  |
|  attemt to update profile details | user input is accepted in the profile page and the view reflects the changes after save | SUCCESS  |
|  attemt to log in as a teacher | user can add classes by navigating to myclasses  | SUCCESS  |
|  attemt to add a class as a teacher | user can add classes successfully and the added class show up on home page  | SUCCESS  |
|  attemt to edit a class as a teacher | user can edit only a class that was added by the user successfully and the edited class details reflect on myclasses & home views  | SUCCESS  |
|  attemt to delete a class as a teacher | user can delete only a class that was added by the user successfully and the deleted class no longer show on myclasses & home views  | SUCCESS  |
|  attemt to add material to a class as a teacher | user can add material and attach a file to a class that was added by the user successfully and the added materials show on class view  | SUCCESS  |
|  attemt to edit material to a class as a teacher | user can edit material and attach a new file to a class that was added by the user successfully and the updated materials show on class view  | SUCCESS  |
|  attemt to delete material from a class as a teacher | user can delete material from a class nd the deleted material no longer show on class view  | SUCCESS  |
|  attemt to log in as a student | user can join classes  | SUCCESS  |
|  attemt to join a class as a student | user can join a class with the correct join code and the joined class show on my classes view  | SUCCESS  |
|  attemt to join same class again as a student | a message show up iforming user that this class is already joined / prevent duplicate join classes | SUCCESS  |
|  attemt to view materials in a class as a student | user can view materials in classes | SUCCESS  |
|  attemt to download a material as a student | user can download the selected material by clicking the download button | SUCCESS |
|  attemt to join a class from home page as a student | user redirected to my classes view where the user can join a class | SUCCESS |
|  attemt to join a class from home page as a student | user redirected to my classes view where the user can join a class | SUCCESS |
|  attemt to unjoin a class | cannot be done by normal user / only admin user can perform this action | SUCCESS |
|  attemt to donate any amount with valid card number | user input is accepted when clicking pay if card details are valid | SUCCESS |
|  attemt to donate any amount with invalid card number | user input is not accepted and a message show underneath the card number field to inform user of invalid card number | SUCCESS |

* Tested the site using Chrome Lighthouse (for both desktop and mobile) and below are the scores:
  * Mobile
    * Performance: 87
    * Accessibility: 100
    * Best Practices: 87
    * SEO: 90
  * Desktop
    * Performance: 91
    * Accessibility: 100
    * Best Practices: 87
    * SEO: 92

#### Known issues found by users

* When a user logges in he/she is directed to the my account page (originally to fill the user details). However, users prefer if it only directed them to my account when loggin in for the first time.

* After paying a donation, the is no redirection to any other page.

* Teachers want the class join code to be visable on home and my classes views.


## Credits

### Content

The project was inspired by websites like google classroom and by the need of the school for a custom online solution.

### Acknowledgements

I'd like to thank

* Teachers of the school for their support and understanding of the long development process, especially the head teacher.
* Code Institute for the tutorials all the help I got to progress and finish the website, and
* Mentor Brian Macharia for his advice and guiding me through this project.