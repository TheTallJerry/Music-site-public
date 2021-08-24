# Music-site-public

A website where I share my music-related works, and where people can reach out to me

# Public Link

 https://zyjerryzhang-music-site.herokuapp.com/, might take a few seconds to load due to the limit of the free plan


# Running Locally

A simplified version of the source code has been uploaded, excluding my data and tests, where the latter is currently being optimized. 

To run locally
1. You'll need at least `Python 3.9.4` accessible via command line - if you have a higher version that's fine too - I haven't tried with lower versions, so those may or may not work. It is also recommended to have `pip` installed. 
2. `requirements.txt` specifies all the `Python` modules used in this project. If you aren't using a virtualenv, run `pip install -r requirements.txt` if you have pip to install all the modules. Other downloading services will have similar commands. 
3. Now moving inside the project. You need to configure a series of settings in `testsite/settings.py`, specifically anything noted with `TODO`. Examples of this include an email account and password used for sending emails in the contact request, as well as google recaptcha public and secret keys. Leaving the email credentials as null will affect sending emails, and leaving recaptcha as null will prevent the recaptcha from displaying; however, the site will still run normally. To experience the full functionalities, add your own values. 
4. Now simply run `python manage.py migrate --run-syncdb` then `python manage.py runserver`. The link to your local server will be displayed in the terminal. To create an admin, run `python manage.py createsuperuser`, then enter your desired credentials. To access the admin panel, add `/admin` to the end of your localhost, so if your localhost is `123.4.5.6`, use `123.4.5.6/admin`. 
# About/Background

 I have a relatively active [Musescore.com profile](https://musescore.com/thetalljerry) with a fair amount of followers. The site is essentially a place to share musical arrangements/compositions that are made with the music scripting software Musescore. Because of its _free_ nature, there's a pretty significant userbase. 

 A few months back I started receiving messages (from my potential/exsiting Musescore followers)
* Asking what I've been working on
* Expressing interest on working with me in the future
* Asking about my music-related experiences

 At first it was easy to manage, I would simply respond to each message individually, **but as time went by the quantity started piling up**. As a result I felt the need to create a central place that can satisfy all these needs, for the sake of ease of management. Unfortunately, the Musescore website isn't capable of handling that, hence I decided to write a website myself to solve this problem. 

# Design and Tech stack

 I made a summary of the features that I need to support and that I might need to support in the future

### For myself
* Managing the contact requests - ideally through a database - such as closing and deleting. 
* Analyzing the contact requests such as filtering by day, title, whether it's about a completed or under-development work, etc
* Uploading my existing and under-development work with additional details as needed without having to rewrite the code (i.e. changes in an admin panel are reflected on the site in real time)
* Having registered users for future functionalities
### For the website visitors
* Being able to contact me in a rather simple manner (such as filling out a form)
* Being able to lookup the status of their contact request(s)
* Being able to view my work/experiences

 For production, I wanted a beginner-friendly hosting service with a free tier, so I chose Heroku. 

 Having these in mind, I narrowed down to `Django`, a `Python` web framework with builtin admin interface, user authentication, testing environment, and many other useful modules. It's easily scalable, and works flawlessly with `SQL` databases. In addition, it has a strong and active community, and is supported by many hosting services. 

# Techologies used
* `Python`, `Django`
* `HTML`, `CSS`, `Javascript`, `Bootstrap`
*  Git
* `SQLite` and `PostgresSQL` (difference of use cases explained below)
* Heroku and AWS (usage of AWS explained below)

 This project uses `Python 3.9.4`. In addition, I recommend checking out `requirements.txt` for a full list of `Python` Modules used. It will also help you set up a virtual environment if you prefer. 

# Problems and Solutions

### During Development

**1.** 
* **Problem**: While `Django` has a builtin form module, with creation and validation capabilities, I found my forms vulnerable to mass-creations (such as using  `requests.post`)
* **Solution**: I added a Google recaptcha (i.e. _I'm not a robot_) field to my forms and  _voila_, problem solved. 

**2.** 
* **Problem**: I wanted to have on my site a selection of Musescore comments from my popular works. However, there isn't a functional API at the moment. 
* **Solution**: I used Google Dev Tools to locate the request-response containing the info I needed, then mannually extracted it myself. **A downside to this** is if the response (in `json`) changes (such as changes in key names), my extraction might fail and could cause a server crash, hence for the time being I'm making this feature optional with a `try-except`. 

### During Production

**1.** 
* **Problem**: While `SQLite` *can* work during production and is in fact `Django`'s default file storage service, it's not recommended and unfortunatly Heroku doesn't support it. 
* **Solution**: Fortunately, `Django` provides a smooth transition between databases, so I installed the `PostgresSQL` Add-on via Heroku, configured the database for `Django`, and problem solved. For this task specifically, I had to install `psycopg2`.

**2.** 
* **Problem**: Heorku doesn't support user-uploaded media files' storage (i.e. no place to store admin's uploaded pictures)
* **Solution**: After some research I decided to use _AWS IAM and S3 buckets_ for this. They're relatively easy to use - although I did have some learning curve on the user/bucket policies - has a free tier, and many security configurations which I love, and problem solved. For this task specifically, I had to install `boto3.`

**3.** 
* **Problem**: My localhost domain is different from my deployed domain, plus I might purchase a custom domain in the future. My navigation bar relies on relative links - which involves setting the `<base> HTML` element. Mannually changing them is too much work and I often ended up forgetting it. 
* **Solution**: I used `Javascript` to set `<base>` with `window.location.origin`, automating this process, and problem solved. 

### Alternate solution for some of the problems above? 

The third problem during production:
* **Alternate solution**: I could've written some code to do a DNS redirect to my IP address, then my program listens in on a specific port. 
* **Reason for not doing this**: I believed changing the base element is of less work. Once there are more than two domains to run the site on, DNS redirect will involve more avoidable code, whereas I will never need to change the `Javascript` code and it'll always work. 

# Conclusion

 While a functional website has been produced, I am still finalizing the details, optimizing the front-end user interface, as well as populating the database.
