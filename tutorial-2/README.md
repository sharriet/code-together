# Tutorial 2: Practice pair programming

    Pair programming essentially means that two people write code together on one machine. It is a very collaborative way of working and involves a lot of communication. While a pair of developers work on a task together, they do not only write code, they also plan and discuss their work. They clarify ideas on the way, discuss approaches and come to better solutions. (Böckeler and Siessegger)

Benefits of pair programming include:

+ Peer to peer knowledge transfer
+ Increased bus factor (low bus factor represents a risk)
+ Better quality solutions
+ Fewer bugs and mistakes
+ Developers learn communication skills
+ Developers build better relationships

However, pair programming requires mental and social effort. It is a skill that takes time to master. Moreover, there are different techniques 

In this tutorial, you'll experience a gentle introduction to pair programming using the driver navigator technique. For other techniques, refer to the further reading section at the end of the tutorial.

To accommodate learners who are not co-located, we'll make use of the [Live Share](https://code.visualstudio.com/learn/collaboration/live-share) feature of [Visual Studio Code](https://code.visualstudio.com/download). For those wanting to setup a physical pair programming station, this article showcases some [different configurations](https://www.clearlyagile.com/agile-blog/2016/5/20/pair-programming-configurations).

## Learning outcomes

+ Gain experience with the driver-navigator approach to pair programming
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

+ Decide on a setup you'll use for this pairing session
    - If you are physically co-located, you may sit side by side and use Live Share
    - If you are not co-located, use Live Share remotely

+ Make sure you have both completed [Tutorial 1](../tutorial-1/README.md) and have executed `git pull` to ensure your local git repository is in sync with the remote

+ Decide who will drive and who will navigate first
    - Whoever is driving will do the Live Sharing first
    - The navigator will direct and/or ask questions to encourage the driver to verbalise their thinking
    - The navigator should open this tutorial and any other documentation you need on their computer, so they can refer to it while directing the driver 

+ Take a look at these [best practices for pairing](https://dev.to/documatic/pair-programming-best-practices-and-tools-154j#best-practices-for-pair-programming) before you start, and discuss your thoughts

## Step 2: Pair

In this pairing activity you'll work together to start implementing a user story from your product backlog.
To start with, you'll be doing a small amount of designing / planning on a digital whiteboard or pen and paper. You should aim to do the minimum amount of planning that will enable you to get started with the code implementation.

You should switch roles every 10 mins or so, or sooner if someone becomes stuck.

Each pair in your team should work on a different user story. It may be beneficial to all work together on the first couple of steps, especially where there is overlap in your stories (i.e. they refer to the same objects).

+ From your story, identify objects, properties and verbs - these will form the basis of your class design
    - Refer back to Lecture 5 if you run into difficulty with this part.
+ Produce a JSON file with some dummy object data (you might not need this step, depending on your story). 
    - JSON should be stored in a file with the `.json` extension
    - Here are a couple of examples of objects in the JSON format:

            {"topic_title": "Version Control", "difficulty_level": 1}
            {"topic_title": "Continuous Delivery", "difficulty_level": 3}
+ Practice parsing your JSON in python
    - Refer to the [top 2 examples here](https://www.w3schools.com/python/python_json.asp)
+ If less than 50 mins have passed, move onto [Tutorial 3](../tutorial-3/) which will get you started on your class implementation using the Test Driven Development (TDD) with the pytest framework
+ After **50 mins**, irrespective of where you get up to, return here and complete Steps 3-5

## Step 3: Sync your work

+ Make sure the files you've worked on have been **added** to your local git repository, and that the changes you've made have been **committed** and **pushed** to the remote repository (see [Tutorial 1](../tutorial-1/README.md))
+ Make sure each person has **pulled** the changes, so your local repositories are both in sync

## Step 3: Reflect

+ Reflect together on how this pairing session went
    - *What did you learn?*
    - *What felt difficult or challenging?*
    - *How could it have gone better?*
+ Document the work you did today for your group report (a short summary is fine)

## Step 4: Plan

+ Independently, think about what you might do differently another time, to make pairing and collaborating more effective
+ Record your personal reflections for your individual reflective report
+ Plan our next pairing session!
    - If you still have work to do on this user story, you might want to pair with the same person, or you could rotate pairs
    - You should rotate pairs at least once on this coursework so you have had the opportunitity to experience pairing with different people

## Recommended reading

+ [Pair Programming Best Practices and Tools](https://dev.to/documatic/pair-programming-best-practices-and-tools-154j)
+ Böckeler and Siessegger (2020) [On Pair Programming](https://martinfowler.com/articles/on-pair-programming.html)
+ Jason Thomas (2021) [Best Practices for Pair Programming Remotely](https://www.coscreen.co/blog/best-practices-for-pair-programming-remotely/)
+ Sorrel Harriet (2022) [Supporting neurodiversity in paired programming](https://sorrelharriet.medium.com/supporting-neurodiversity-in-paired-programming-8b250d2b5cab)
+ Kent Beck (1999) Extreme Programming Explained (Chapter 7)
+ Jfromtheblock (2021) [How to do pair programming with VS code](https://duckly.com/blog/pair-programming-with-vs-code/)