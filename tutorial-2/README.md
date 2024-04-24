# Tutorial 2: Practice pair programming

## What is pair programming?

> Pair programming essentially means that two people write code together on one machine. It is a very collaborative way of working and involves a lot of communication. While a pair of developers work on a task together, they do not only write code, they also plan and discuss their work. They clarify ideas on the way, discuss approaches and come to better solutions. (Böckeler and Siessegger)

&#10140; Watch from [18:19-23:47 in this Presentation by Paige Watson](https://www.linkedin.com/events/7170722062938849280/comments/)

Benefits of pair programming include:

+ Peer to peer knowledge transfer
+ Increased bus factor (low bus factor represents a risk)
+ Better quality solutions
+ Fewer bugs and mistakes
+ Developers learn communication skills
+ Developers build better relationships

However, pair programming requires mental and social effort. It is a skill that takes time to master. Moreover, there are different pairing techiques you can use.

## Tutorial overview

In this tutorial, you'll experience a gentle introduction to pair programming using the **driver-navigator**  technique.

To accommodate learners who are not co-located, we'll make use of the [Live Share](https://code.visualstudio.com/learn/collaboration/live-share) feature of [Visual Studio Code](https://code.visualstudio.com/download). For those wanting to setup a physical pair programming station, this article showcases some [different configurations](https://www.clearlyagile.com/agile-blog/2016/5/20/pair-programming-configurations).

The task you'll pair on involves producing and parsing some dummy application data in the JSON format. It is a technically simple task, but it involves discussion, since there are design decisions to be made in the process.

## Learning outcomes

+ Gain experience with the driver-navigator approach to pair programming
+ Practice parsing a JSON file in python
+ Reflect on your experiences with pair programming, identifying opportunities for personal development

## Pre-requisites

+ Partner to pair with!
+ A user story to work on (see Lecture 5)
+ Basic python (and python installation)
+ [Visual Studio Code](https://code.visualstudio.com/) with [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) extension
+ Headset with microphone (if pairing remotely)
+ Webcam (if pairing remotely)
+ Pen and paper or digital whiteboard for sketching ideas

## Step 1: Get ready

&#10140; Decide on a setup you'll use for this pairing session
- If you are physically co-located, you may sit side by side and use Live Share
- If you are not co-located, use Live Share remotely

&#10140; Make sure you have both completed [Tutorial 1](../tutorial-1/README.md) and have executed `git pull` to ensure your local git repository is in sync with the remote

&#10140; Decide who will drive and who will navigate first
- Whoever is driving will do the Live Sharing first
- The navigator will direct and/or ask questions to encourage the driver to verbalise their thinking
- The navigator should open this tutorial and any other documentation you need on their computer, so they can refer to it while directing the driver 

&#10140; Take a look at these [best practices for pairing](https://dev.to/documatic/pair-programming-best-practices-and-tools-154j#best-practices-for-pair-programming) before you start, and discuss your thoughts

## Step 2: Pair!

+ The goal of this pairing activity will be to work together to start implementing a user story from your product backlog.
+ To start with, you'll be doing a small amount of designing / planning on a digital whiteboard or pen and paper. You should aim to do the minimum amount of planning that will enable you to get started with the code implementation (the design will evolve incrementally as you add functionality and refactor.)
+ The tutorial suggests you begin your code implementation by creating some dummy application data in the form of a JSON file (just enough to be able to implement your first user story.) If your user story doesn't require any object data, you could nip straight to [Tutorial 3](../tutorial-3/). However, if you are not too confident in python, creating and parsing a simple JSON file is a good place to start.
+ You should switch roles every 10 mins or so, or sooner if someone becomes stuck.
+ Each pair in your team will work on a different user story. However, it may be beneficial to all work together for the first part of this tutorial, especially where there is overlap in your stories (i.e. they refer to the same objects).

&#10140; From your user story, identify the objects, properties and verbs - these will form the basis of your class design
- Refer back to Lecture 5 if you run into difficulty with this step
- Here is an example of a user story:
> **As a** user of the 'learn software engineering' application,  
> **I want** to view a list of Topics which are appropriate  
> for someone with my level of experience,  
> **so I can** decide where to focus my learning.
- In the above, I've identified **User**, **Topic** and **TopicList** as objects (classes). **experience_level** will be a property of both a User and a Topic.

&#10140; Open Visual Studio Code and navigate to your working directory

&#10140; Start a Live Share session with your partner (and other team members if you are taking these first few steps together)
- Refer to the [Quick Start section of the website](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare#:~:text=Quickstart)

&#10140; Inside your working directory, create a folder for your application code (for example, `app/`)

&#10140; Inside your app directory, create a JSON file with some dummy object data 
- JSON should be stored in a file with the `.json` extension
- Here is an example of an array of objects in the JSON format:

            [{"topic_title": "Version Control", "difficulty_level": 1},
            {"topic_title": "Continuous Delivery", "difficulty_level": 3}]
- You'll need just enough dummy data to be able to test the functional requirements of the user story have been met. Check out my [example from Tutorial 3](../tutorial-3/app/data/topics.json)

&#10140; Add, commit and push your dummy data to the remote repository:

        git add app/data.json
        git commit -m "adding some dummy data for a topics object"
        git push origin main

**At this point, your team should split into pairs if you have not done so already. A driver from each pair can start a new Live Share session with their partner.**

&#10140; Practice parsing your JSON in python
- You can either do this from the python interactive shell, or from a temporary `.py` file
- You can invoke the python interactive shell from the integrated terminal with: `python3`

        # import the json package
        import json

        # create a file object from your JSON file
        f = open('data.json')

        # load the data into a python object
        data = json.load(f)

- Assuming you have created an array of objects, as I have done, you can explore its properties:

        # return the length of the array
        len(data)

        # return the first object
        data[0]

        # return the 'title' property of all the objects as a list
        for d in data:
            print(d["title"])
- To close the python interactive shell: `Ctrl+D`
- For more operations, refer to the [examples here](https://www.geeksforgeeks.org/read-json-file-using-python/)

&#10140; **If** less than 50 mins have passed, move onto [Tutorial 3](../tutorial-3/) which will get you started on your class implementation using Test Driven Development (TDD) with the pytest framework.

&#10140; **After 50 mins**, irrespective of where you have got up to, procede to Step 3.

## Step 3: Sync your work

&#10140; Make sure the files you've worked on have been **added** to your local git repository, and that the changes you've made have been **committed** and **pushed** to the remote repository (see [Tutorial 1](../tutorial-1/README.md))

&#10140; Make sure each person has **pulled** the changes, so your local repositories are both in sync

## Step 3: Reflect

&#10140; Reflect together on how this pairing session went
    - *What did you learn?*
    - *What felt difficult or challenging?*
    - *How could it have gone better?*

&#10140; Document the work you did today for your group report (a short summary is fine)

## Step 4: Plan

&#10140; Independently, think about what you might do differently another time, to make pairing and collaborating more effective

&#10140; Record your personal reflections for your individual reflective report

&#10140; Plan your next pairing session!
- Rotating pairs is recommended to maximise knowledge transfer
- You should rotate pairs at least once on this coursework so you have had the opportunitity to experience pairing with different people

## Recommended reading

+ [Pair Programming Best Practices and Tools](https://dev.to/documatic/pair-programming-best-practices-and-tools-154j)
+ Böckeler and Siessegger (2020) [On Pair Programming](https://martinfowler.com/articles/on-pair-programming.html)
+ Jason Thomas (2021) [Best Practices for Pair Programming Remotely](https://www.coscreen.co/blog/best-practices-for-pair-programming-remotely/)
+ Sorrel Harriet (2022) [Supporting neurodiversity in paired programming](https://sorrelharriet.medium.com/supporting-neurodiversity-in-paired-programming-8b250d2b5cab)
+ Kent Beck (1999) Extreme Programming Explained (Chapter 7)
+ Jfromtheblock (2021) [How to do pair programming with VS code](https://duckly.com/blog/pair-programming-with-vs-code/)