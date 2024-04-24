# Tutorial 3: TDD with python and pytest

## Overview

This tutorial will aim to walk you through the first stages of developing a python application using a Test Driven Development (TDD) approach. You should be pairing with another member of your team for this tutorial.

Since your application will have different requirements to the one used in the examples, you will need to think carefully, and communicate frequently with your pairing partner and team.

## Learning outcomes

+ Gain experience with the TDD approach to software development
+ Reflect on the benefits and challenges with this approach

## Important things to note before getting started...

+ It is recommended that your team uses python to develop its software project. This will make it easier to adopt the collaborative development practices documented in these tutorials. If you do use another language, you will need to look for an equivalent test framework. Failure to implement tests (an important mark of software quality) will affect your mark.
+ You should develop the habit of using [virtual environments](https://docs.python.org/3/tutorial/venv.html) when building python applications. These are isolated python environments that can be consistently replicated across different machines. We don't want a situation where one team member is using a different version of python, or a different version of a python package from other team members! We also need it to be easy for those reviewing your code to run your application. 

## Pre-requisites

### Complete tutorials 1 and 2
+ You'll need to complete tutorials [1](../tutorial-1/) and [2](../tutorial-2/) before attempting this tutorial.
+ The pre-requisites for Tutorial 2 apply here too (such as having a well defined user story to work on.)

### Install Visual Studio Code with WSL
+ This tutorial assumes you will use **Visual Studio code with the WSL extension** to develop and execute your python code. 
+ WSL refers to the Windows Subsystem for Linux, which allows you to run a Linux environment on your Windows machine.
+ Many python developers prefer to develop on Linux as some packages will not work properly on Windows, and code may execute faster on Linux-based operating systems.
+ The commands in this tutorial will be slightly different if you're using Windows without WSL. Where applicable, I have tried to link you to some resources that may help.

&#10140; [Follow these instructions to install WSL2](https://learn.microsoft.com/en-gb/windows/wsl/install)

&#10140; [Follow these instructions to install VS code with the WSL extension](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode).

### Install Python 3.12
+ The tutorial assumes you'll use the latest stable version of python which is currently 3.12.

&#10140; From the integrated terminal, check you have python 3.12 installed:

        python --version

+ If you haven't got it, you should install it. 

### Install the `venv` package
+ If you're on a Mac, Linux or WSL, you may need to install the [`venv`](https://docs.python.org/3/library/venv.html) package for python.
+ On Windows, it should already be installed.

**Once you have done all of the above, you're ready to start!**

## Step 1: Create a virtual environment for your python project

&#10140; From the integrated terminal, initiate a virtual environment:

        python3.12 -m venv ./appname

+ In the above, replace 'appname' with the name of your application.

## Step 2: Activate the virtual environment

&#10140; From the integrated terminal, activate the virutal environment:

        source /appname/bin/activate

+ At this point you should see the command line prompt changes, indicating you are now in the virtual environment.
+ To deactivate it, you can simply do:

        deactivate

## Step 3: Install the pytest library

We'll use the [pytest framework](https://docs.pytest.org/en/8.0.x/) to write unit tests for our code.

**Make sure your virtual environment is activated before completing this step.**

&#10140; Install the pytest package with pip, which is a package manager for python:

        pip install python

**Note:** this installs the package in the virtual environment only - not on your system-wide python installation, which is really handy as it means we can have many python projects using different versions of python or its packages while avoiding package conflicts.

## Step 4: Create a structure for your application

**You are advised to consult your team here, or work together on it, so as to avoid conflicts when you commit your code to github.**

&#10140; Create a skeleton structure for your application as follows:

                app/
                        models/
                                __init__.py
                        tests/
                                __init__.py
+ The `__init__.py` files are needed for the models and tests directories to be recognised as packages.
+ **Tip:** From the terminal with WSL, you can easily create new files with the `touch` command:

                touch app/models/__init__.py

## Step 5: Write a failing test

The basic workflow for TDD is illustrated below. We'll try to follow this as closely as possible, though what you're able to implement in practice without mocking frameworks or databases etc may be minimal. That's OK, we're here to learn best practices, not to make fully functional software!

![TDD Workflow](images/TDD-workflow.png)

&#10140; Inside `tests/`, create a file, `test_mymodel.py`
- In the above, replace 'mymodel' with the name of the class you are planning to implement. For example, I am about to implement a TopicList class, hence I will call my python file, `test_topiclist.py`.

&#10140; Open the test file you just created

&#10140; Identify a method of the class you intend to write, which is needed for your story to meet its acceptance criteria
- For example, TopicList needs a `get_topics()` method, which will return the topics data
- Your method should have a name that describes what it does, and it should use the python naming convention for functions and methods (lowercase, words separated by underscores)

&#10140; Identify one or more criteria that will allow us to know if this method is behaving correctly
- For example, `get_topics()` should return a list, and its length should be greater than 0
- We may need to add to this list of pass criteria later, so keep it simple for now!

&#10140; Write a single test for your method
- Use `assert` statements to evaluate your test criteria
- Here is an example:

                def test_get_topics_is_list():
                        tl = TopicList()
                        assert isinstance(tl.get_topics(), list)
- In the above, I define a function, `test_get_topics_is_list()` (in pytest, all tests should be prefixed with `test_`, followed by the name of the method or function they are testing.)
- The name of the test function should describe the thing it is testing (it essentially tests a single requirement)
- I then create an instance of my `TopicList` class (which I haven't written yet!)
- I then include a single assert statement to evaluate whether the `get_topics()` method returns a list

&#10140; Run the test from the integrated terminal:

                pytest tests/
- Of course it will FAIL with a NameError because we haven't written the class yet!

&#10140; Create a file called `mymodel.py` in your models directory (replacing mymodel with the name of the class)
- For example, I have created a `topiclist.py` file

&#10140; In the new file, define the class, but without any code in it. For example,

                class TopicList:
                        pass
&#10140; Import the class into the top of your test script. For example,

                from models.topiclist import TopicList

&#10140; Run pytest again
- This time you should receive an AttributeError, because we haven't defined the method we're trying to test yet.

## Step 6: Write the minimum code to pass the test

&#10140; Implement the minimum amount of code in your class definition to make the test pass.
- Here's my example:

                class TopicList:
    
                        # Instance method
                        def get_topics(self):
                                return [1,2,3,4]

&#10140; Re-run your test. Eventually you should see a satisfying green pass!

![Passing Tests](images/tests-pass.png)

Clearly my code is not finished yet, but I have satisfied my first requirement!
Next I need to repeat this process, until all the acceptance criteria for the story have been met.

## Step 7: Write more tests before writing more code!

&#10140; Write another test to test another critera.
- **Remember:** Each new test you write should test a different requirement.
- For example, in my case, another test might be, `test_get_topics_by_difficulty`. This would check that the topics returned by the `get_topics` method returned only topics of a certain difficulty. This might lead to a bit of code refactoring!

&#10140; Run the new test - which will most likely fail the first time you run them!

&#10140; Add just enough new code to pass the new test

&#10140; Repeat... (for a maximum of 30-50 mins!)
- It's important to take regular breaks when pairing

## Step 8: Commit your work

&#10140; At this stage you should add, commit, push your work to the remote repository on GitHub
+ **Don't** add or commit any files related to your python virtual environment!
+ **Only** add the files in your `data`, `models` and `tests` directories!

## Step 9: Create a requirements file

In order for others to be able to recreate your virtual environment, we need to make a `requirements.txt` file which will be stored along with our source code. We can do this with `pip freeze`.

&#10140; Generate a `requirements.txt` file:

                pip freeze > requirements.txt

&#10140; Add, commit and push the requirements file to the remote repository on GitHub

## Step 10: Create a README file for your application

Every code project needs a README file! This should include instructions for others on how to run and use your application. To start with, we'll keep ours very lightweight, with a simple set of instructions for recreating the virtual environment and running the tests.

&#10140; Create a `README.md` file in the base of your local repository

&#10140; Add some text to your README file, which should include something like the following:

        From a terminal, clone this repository:

                git clone 
        Navigate into the app directory:

                cd app/
        Initialise a python virtual environment running python 3.12:

                python3.12 -m venv .
        Activate the virtual environment:

                source bin/activate
        Install the dependencies required for this application to run:

                pip install -r requirements.txt
        Run the tests:

                pytest tests/

&#10140; Add, commit, push your README file to the remote repository on GitHub.

## Extension exercise

&#10140; Reflect on your experiences with TDD...
- *What are the benefits of this approach?*
- *How can TDD support the design of good quality software?*

&#10140; Consider, *what other steps did we take to help ensure the quality of the software?*
- **Tip:** Go back over the different steps and ask yourself, *why did we do it like this?*

&#10140; Document the actions and insights you have taken today for your group and individual reports.

## Further reading

+ Martin Fowler (2023) [Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)
+ Jacob Schmitt (2024) [Test Driven Develoment Explained](https://circleci.com/blog/test-driven-development-tdd/)
+ Kent Beck (2002) [Test Driven Development By Example](https://www.amazon.co.uk/Test-Driven-Development-Addison-Wesley-Signature/dp/0321146530)
+ [Virtual Environment Documentation](https://docs.python.org/3/library/venv.html)
+ [Pytest documentation](https://docs.pytest.org/en/7.1.x/contents.html)
+ Reitz & Schluzzer (online) [Hitchhiker's Guide to Python: Structuring the repository](https://docs.python-guide.org/writing/structure/#structure-of-the-repository)