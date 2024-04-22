# Demo Application

This is the beginnings of an application that seeks to educate students about modern software engineering practices.

The first user story included in this implementation is:

> **As a** user of the 'learn software engineering' application,  
> **I want** to view a list of Topics which are appropriate  
> for someone with my level of experience,  
> **so I can** decide where to focus my learning.

The **acceptance criteria** for this user story is:

> **Given** a user has opened the application  
> **And** the user has input their experience level  
> **When** the user clicks on 'Learn About Modern Software Engineering',  
> **Then** display a list of topics  
> **And** display only topics matching the user's experience level  
> **And** list topics alphabetically (a-z)

There is currently a single class: `TopicList`, which has a single method, `get_topics()`

## Install the application

+ From a terminal, clone this repository:

        git clone 
+ Navigate into the app directory:

        cd app/
+ Initialise a python virtual environment running python 3.12:

        python3.12 -m venv .
+ Activate the virtual environment:

        source bin/activate
+ Install the dependencies required for this application to run:

        pip install -r requirements.txt
+ Run the tests:

        pytest tests/
