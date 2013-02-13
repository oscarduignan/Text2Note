Text2Note
=========

Using an old nokia because my android died and I can't replace it at the moment, so wrote a lightweight flask app to turn text messages to twilio into evernote notes because the phone can't actually store notes itself and has limited text capacity, hosted on heroku.

Below is typed from memory so steps ~~may~~ will need tweaking!

Getting it running in Vagrant
-----------------------------

Well I used the python that ships with ubuntu, so I just ```vagrant up``` then I to bootstrap the server with virtualenv and pip I ran

```wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py && python virtualenv.py venv```

Then to activate the python environment (when I want to install something using pip or start the server I just run

```source ~/venv/bin/activate```

For dev / debugging I ran if off the built in server with ```app.config['DEBUG'] = True``` (should probably be an environment variable, for the moment you'll need to edit ```app.py``` and drop it in just after app is instantiated).

```python /vagrant/app.py```

(Or you can use foreman but you'll have to install that separately.)

And the last note is that it needs the ```EVERNOTE_AUTH_TOKEN``` to be set to run, get your evernote auth token here (this is to get a production one not a sandbox one!) https://www.evernote.com/api/DeveloperToken.action

Getting it running on Heroku
----------------------------

Just make sure you

```heroku config:add EVERNOTE_AUTH_KEY='<YOUR AUTH KEY HERE>'```

Configuring Twilio
------------------

Just ```heroku open``` and copy paste the URL into the sms handler field of the phone number you setup and make sure that the method is set to POST.
