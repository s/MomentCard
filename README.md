MomentCard
==========

A Flask based Python application that creates card of given Instagram Url

Application first connects to Instagram Api and fetchs matched photo datas.<br/>

Then generates the html file.

##Installation and Run

```
$ pip install Flask
$ git clone git://github.com/s/MomentCard.git ~/MomentCard
$ cd ~/MomentCard
$ python app.py
```
Then open the url in your browser:

<code>http://localhost:1105/generate?access_token=access_token&photo_url=url</code>

Example parameters:<br/>
<code>access_token:	XXXXXXXXX.XXXXXX.XXXXXXXXXXXXXXXXXXXXXX</code><br/>
<code>photo_url:instagram.com/p/gWUeJnn0t3/</code>

All you need to configure is given url above. Just get an access_token from Instagram API and start creating cards.

##Screen Shots

![View Screen Shot](https://raw.github.com/s/MomentCard/master/static/ss.png)