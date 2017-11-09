# Assignment 5 - learning to read and write (code)
Diving into the codebase. Oh boy.

This week, we're going to ask you to begin to go through our codebase and figure out some of the working parts.

## Questions 
Write down your answers in the file answer_template.txt! Remember to put your name in the provided space. We'll be instructing you to poke through various aspects of the website, like tags, articles, the base template, and searching.

We'll be working with the crimsononline repo that you set up on your computer last week.

Let's get into it!

## Tags
Check out [this tag page](http://www.thecrimson.com/tag/editorials/). Play around a little with the section and type filter, and take a look at `urls.py` in crimsononline. (Here's [Django documentation on urls.py](https://docs.djangoproject.com/en/1.8/topics/http/urls/) if you get confused!) 

**TODO 1:** Briefly explain what a "tag" is. What is the name of the URL pattern that handles requests for the tag page? 

Now check out `views.py` in `crimsononline/content/`. 

**TODO 2:** What view handles the tag page?

**TODO 3:** Say I wanted the page for the just the tag “Editorials.” What parameter(s) would be passed from the url to the view, and what would their value(s) be?

**TODO 4:** Now say I wanted only the articles with the tag “Editorials” in the “Opinion” section. What parameter(s) would be passed from url to view now, and what would their value(s) be? 

## Articles
Check out [this piece](http://www.thecrimson.com/article/2014/2/20/harvard-odyssey-dogecoin/). It’s a standard non-feature article. 

**TODO 5:** What url pattern handles this? What view handles it?      
...having trouble finding it in urls.py? (it’s kind of tricky!) _**Hint:** check out `generic_patterns`, know that “article” is what we call a “content type,” and pay particular attention to the patterns (think regex) in the url of the piece!_

Go to the view you identified in TODO 5.

**TODO 6:** What type of object (i.e. what class / model) is the variable “c” in this view? _**Hint:** Notice the model methods that are called by “c” in the view, particularly the method used to return a rendered page._

Check out the model/class you just identified in TODO 6 in the appropriate`models.py` file.

Notice how complex it is! Take a look at the methods and how they interact and call upon other methods in the class. Keeping in mind what was returned by the view in TODO 6, answer: 

**TODO 7:** Which method is ultimately responsible for rendering the article? 
_**Hint:**  If stuck, this Django documentation on [requests/responses](https://docs.djangoproject.com/en/1.8/ref/request-response/), especially the section about HttpRequest objects, may be helpful._

For a standard non-feature piece like our example, the template is called `page.html`. Find this file.

**TODO 8:** What is its file path? _**Hint:** check the models folder—what type of content is this news piece?_

**TODO 9:** Find the div with the id “article-tags” in the template. Explain what is happening in this div. Also take a look at this div via Inspect element on the actual article. 

## Base Template and Search
Now let's visit something we call the base template, or `__base.html`, which this, as well as many other (read: most) pages extend. 

Find it in the codebase, and using Inspect element to compare divs, ids, etc. on the website to help you figure things out, answer the following:

**TODO 10:** What is the purpose of this particular template? 

**TODO 11:** What are some parts of the website that are defined in `__base.html`? 

Find the search box in `__base.html`. The actual search is powered by Google, and our template simply displays the search results. Read up a little on HTML forms if needed, particularly the action attribute. 

**TODO 12:** What is the url pattern that handles search? _**Hint:** there are two relevant urls.py files._

Notice how Google’s JavaScript handles all of the search functionality, and our template is basically just a shell to display what Google does for us. 

**TODO 13:** Describe at a high level how we might implement our own search functionality, say, that searched specifically just Content with specific Tags. 

### That's all, folks! Stay tuned for next time :D
