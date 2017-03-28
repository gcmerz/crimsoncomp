# Assignment 4 - Django (TURNED UP)

\#turnup<br>
\#turnup<br>
\#turnip


So, so far, we've basically walked you through all the things you need to know. This week, we're doing something a little bit different and letting you wade through some documentation.

NOBODY PANIC. It's really not that terrible - ~~documentation is generally pretty good for Django~~ there's a lot of Django documentation, and if that fails, Google is an excellent resource. Also don't forget your tech managers (that's us!),Gabbi and Lydia (gabbi.merz@thecrimson.com and lydia.goldberg@thecrimson.com)!

## Plan of Attack
The things you'll have to do, building off of the newspaper project we started last week:

1. Use the admin interface.
2. Make pages for Articles (html and views).
3. Make a homepage (html).
4. Edit the admin form for Articles to, instead of having a textField, to have a TinyMCE field.
5. Make a migration :o.

Not too bad right?

You might be asking, what is TinyMCE? TinyMCE is a widget that you can use in the Django admin interface that takes text (including lots of paragraphs and line breaks) and turns it into valid HTML. That is, it wraps the paragraphs in `<p> </p>` tags, as well as inserts hyperlinks when needed.

But we'll get to that later! First... remember how there's an actual Django tutorial that we referenced (but didn't actually use) last time? Well this time, we're making you use it. (Hurrah!) However, you only need to worry about the sections that we reference explicitly here

## Use the Admin Interface

Please refer to the link [here](https://docs.djangoproject.com/en/1.8/intro/tutorial02/#creating-an-admin-user) to create a Django admin user. They're referring to a different website structure, but hopefully you can generalize to our newspaper setup. Remember our "app" is named "content"; they have a "polls" app. Last time we wrote Article and Contributor models; the tutorial has a Question model. 

>__TODO__ Follow along with the sections, and stop right before the header "Customize the admin form."

Again, the link: [https://docs.djangoproject.com/en/1.8/intro/tutorial02/#creating-an-admin-user](https://docs.djangoproject.com/en/1.8/intro/tutorial02/#creating-an-admin-user)

## Make article pages
Let's see if you can synthesize what you've learned so far, and try a TODO without a step-by-step guide :D

Remember [regexes](https://github.com/harvard-crimson/comp/blob/master/general/regexes.md) and MVT? Now's the time to put your knowledge to the test. 

>__TODO__ Make a template for articles, displaying all the information you see fit. Make sure you wire in a proper url in `urls.py` and a function in `views.py`! If you're having problems remembering, pull up [our presentation - Django part 1](https://www.dropbox.com/s/nv6xhekvqzt27t7/presentation3_django1.pdf?dl=0), or ask Google!

Don't worry if it looks ~~somewhat~~ totally shitty. The important part is that you can make the Django part of it work.

## Make a Homepage
Make the homepage displaying some collection of articles with links to the article pages! Be sure to take advantage of template inheritance to avoid repeating too much HTML. 

## Save
You're done for now! Now since you did lots of things that we may not know the location of, please, in a `README.txt` file detail

- the url of the homepage
- the urls of the articles

Then, push it to your Github!

## Customize the Article Admin
This part is tricky because it involves reading documentation (gasp!). The idea is to figure out how to plug in TinyMCE into the admin interface so that users can input formatted content (bolding, italicizing, and underlining - OH MY.)

Resources:

- A helpful page on how to change the elements on the admin interface is located [here](https://docs.djangoproject.com/en/1.8/intro/tutorial02/#customize-the-admin-form).
- TinyMCE installation instructions here (be sure to `workon` your virtual environment!).
- ... and documentation on how to use it is [here](http://django-tinymce.readthedocs.org/en/latest/usage.html). Go nuts!

Don't worry if it seems nebulous - it may be helpful to work with another tech comper on this, so refer to the facecard wall, or ask us if you hit a wall.

## Make a Migration
Add one field of your choice to any of the `content` models, and make a migration! To do this, we must execute four steps.

1. Make a change to your models! Like add a field or something. Migrations are boring if there's nothing to migrate :D
2. Create the migration file "automagically" (bleh!) via Django's built-in migration system.

        ./manage.py makemigrations <app_name>
3. Optional: Check to see the migration is there in the migrations folder. Maybe take a peek inside to see what Django actually did.

        ls <app_name>/migrations
4. Run the migration.

        ./manage.py migrate <app_name>

Let us know what field you added in the `README.txt` from before.

## Make it beautiful
Flex those HTML/CSS/JS muscles and make your website (or at least one page of it) beautiful. Or terrible. Just write some HTML, CSS, and maybe some JavaScript.

## Huzzah!
Congrats! Now you know how to Django. (If you say it fast enough, people might even think you know how to dance!) Push your changes and rejoice!
