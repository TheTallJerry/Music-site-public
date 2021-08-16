# Music-site-public

A website where I share my music-related works, and where people can reach out to me

# Link

 https://zyjerryzhang-music-site.herokuapp.com/, might take a few seconds to load due to the limit of the free plan

# About/Background

 I have a relatively active [Musescore.com profile](https://musescore.com/thetalljerry) with a fair amount of followers, and for those of you not familiar with the site, it's essentially a place to share musical arrangements/compositions that are made with the music scripting software Musescore. Because of its _free_ nature, there's a pretty significant userbase. 

 A few months back I started receiving messages (from my potential/exsiting Musescore followers)
*  Asking what I've been working on
*  Expressing interest on working with me in the future
*  Asking about my music-related experiences

 At first it was easy to manage, I would simply respond to each message individually, **but as time went by the quantity started piling up**. As a result I felt the need to create a central place that can satisfy all these needs, for the sake of ease of management. Unfortunately, the Musescore website isn't capable of handling that, hence I decided to write a website myself to solve this problem. 

# Design/Tech-stack

 I made a summary of the features that I need to support and that I might need to support in the future

## For myself
*  Managing the contact requests - ideally through a database - such as closing and deleting. 
*  Analyzing the contact requests such as filtering by day, title, whether it's about a completed or under-development work, etc
*  Uploading my existing and under-development work with additional details as needed without having to rewrite the code (i.e. changes in an admin panel and reflected on the site in real time)
*  Having registered users for future functionalities
## For the website visitors
*  Being able to contact me in a rather simply manner (such as filling out a form)
*  Being able to lookup the status of their contact request
*  Being able to view my work/experiences

 For production, I wanted a beginner-friendly hosting service with a free tier, so I chose Heroku. 

 Having these in mind, I narrowed down to `Django`, a `Python` web framework with builtin admin interface, user authentication, testing environment, and many other useful modules. It's easily scalable, and works flawlessly with `SQL` databases. In addition, it has a strong and active community, and is supported by many hosting services. 

## A full list of the techologies I used
*  `Python`, `Django`
*  `HTML`, `CSS`, `Javascript`, `Bootstrap`
*  `SQLite` and `PostgresSQL` (difference of use cases explained below)
*  Heroku and AWS (usage of AWS explained below)

 I also recommend checking out `requirements.txt` for a full list of `Python` Modules used. It will also help you setting up a virtual environment if you prefer. 

# Problems/Solutions

## During development

*  **Problem**: While `Django` has a builtin form module, with creation and validation capabilities, I found my forms vulnerable to mass-creations (such as using  `requests.post`)
*  **Solution**: I added a Google recaptcha (i.e. _I'm not a robot_) field to my forms and  _voila_, problem solved. 

## During Production

 1.
*  **Problem**: While `SQLite` *can* work during production and is in fact `Django`'s default file storage service, it's not recommended and unfortunatly Heroku doesn't support it. 
*  **Solution**: fortunately, `Django` provides a smooth transition between databases, so I installed the `PostgresSQL` Addon via Heroku, configured the database for `Django`, and problem solved. For this task specifically, I had to install `psycopg2`.

 2.
*  **Problem**: Heorku doesn't support user-uploaded media files' storage (i.e. no place to store admin's uploaded pictures)
*  **Solution**: After some research I decided to use _AWS IAM and S3 buckets_ for this. They're relatively easy to use - although I did have some learning curve on the user/bucket policies - has a free tier, and many security configurations which I love, and problem solved. For this task specifically, I had to install `boto3.`

 3.
*  **Problem**: My localhost domain is different from my deployed domain, plus I might purchase a custom domain in the future. My navigation bar relies on relative links - which involves setting the `<base> HTML` element. Dynamically changing them is too much work and I often ended up forgetting it. 
*  **Solution**: I used javascript to set `<base>` with `window.location.origin`, and problem solved. 

# Source-code

 I will be releasing portions of source code under this repostitory as I finalize each component. For now, please reach out to me if you'd like to view the source code. 

# Conclusion

 While a functional website has been produced, I am still finalizing the details, optimizing the front-end user interface, as well as populating the database.