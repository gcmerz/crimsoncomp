# Assignment 2: Objects and Polymorphism

This week we're going to mess with how to create objects, define classes, and extend those classes. After you write your classes, you'll load and dump some objects to and from a text file, so keep this in mind when naming your attributes. Our code expects them to be named in a certain way.

Again, if at any point you have an issue, let Gabbi (gabbi.merz@thecrimson.com) or Lydia (lydia.goldberg@thecrimson.com) know! Don't bash your head against the wall. We're here to help.

The distribution code you'll need to complete this assignment is in this repo.

## Get set up
Doing this assignment will require the use of some third-party libraries. Check out our document at [setting up](https://github.com/harvard-crimson/comp/blob/master/general/setting_up.md) to get yourself ready to download some libraries. If you have any questions about it, definitely shoot one of us an email and we'll help you out :).

> __TODO__: do whatever it says to do in [setting up](https://github.com/harvard-crimson/comp/blob/master/general/setting_up.md).

## Content
As a newspaper, the Crimson often produces articles and other content - who would have guessed! In order to model these in Python, we use objects to represent a piece of content, and classes to represent a set of objects that behave similarly.

In `models.py`, we've created a `Content` class that reflects the general idea of what a piece of content should embody.

It should have:

- `contributors`: a list of people (strings) that helped create this content 
- `creation_date`: the date the content was created.  Note: not necessarily the date that the Python object is created. 
- a `show` method: displays the piece of content when called.

`self.contributors` and `self.creation_date` must be set in the `__init__` method.

> __TODO__: `creation_date` is up to you to implement! Take a look at existing documentation for `datetime.date` for more details (google it). 

The `show` method currently raises a `NotImplementedError`, which means we'll have to override it later when extending it to our own custom classes if we don't want the interpreter to yell at us.

## What About Articles?
Some of the content we produce at the Crimson are articles, and some are pictures. Having a `Content` class is all fine and dandy, but we soon realize that it's too general for our needs.

To fix this, we extend `Content` to two different classes that behave slightly differently - `Article` and `Picture`. 

In addition to the regular `Content` attributes, an `Article` object should have:

- `headline`: a headline
- `content`: a string representing the content of the article
- a `show` method that prints all the info to the terminal in a pretty way

In addition to the regular `Content` attributes, a `Picture` object should have:

- `title`: the title of the image
- `caption`: a caption for the image
- `path`: the path to where the image file is located
- a `show` method that displays all the info in a pretty way, and also displays the image using [Pillow's Image module](http://pillow.readthedocs.org/en/latest/reference/Image.html). 

> __TODO__: Write an Article class and a Picture class that have these properties.

_Note: again, make sure that you name your attributes carefully, since the next part requires them to be named in a certain way to work._

## Load me up, Scotty!
Here comes the fun part (and the part that verifies that you did the first parts right).

Inside `loadcontent.py` are two methods, `to_json` and `from_json`. 

- `to_json` dumps all your existing `Content` objects into a document called `dump.txt`.
- `from_json` retrieves all the json strings in `dump.txt` and loads them into `Content.existing_content`.

What is JSON? JSON is a lightweight format that makes storing nested dictionaries and lists very easy. It does this by standardizing the ways dictionaries and lists are dumped into strings. The JSON library in Python have functions like `json.loads` and `json.dumps` for this purpose.

Read through the code and make sure you understand it. Also take a look at `dump.txt` to get a feel for what JSON looks like. If you're feeling really ambitious, try writing some code that parses `dump.txt` (feel free to look to `loadcontent.py` for inspiration). Again, if you have any questions, consult Google or your Tech Managers.

To verify that your code above works well, open terminal in the same folder as `loadcontent.py` and pull up the Python shell by just typing

    python

Import the functions from `loadcontent.py` as well as the classes from `models.py`. Call `from_json`. This should load all the strings from `dump.txt` into `Content.existing_content`.

You can also create new objects of your own and dump them into `dump.txt`, close your Python shell, and then retrieve them later.

Now you can play with these objects - call `show`, modify their contents, go crazy! 

## Feedback?
You're done! Congrats! Just push your code to your Github, and you can wipe your hands of the whole thing.
