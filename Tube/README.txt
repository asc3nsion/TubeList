			TubeList v0.000

Descriptiion:
-------------

An experiment loading content using the youtube api.
From the an array of video ids I get data from an
api query for each video.  This data is sorted in 
server.py, and passed to tubelist.py to be rendered.


Requirements
------------
Python 2.7+
Web Browser

Installation and Use
--------------------
Copy folder "Tube" to a local directory.
With python installed, Open command prompt
and cd into the "Tube"directory:

python server.py

The page will be opened and dislayed in your
default browser.


To do:
----------
It would be cool to make a chrome extension
that saves the video id of an open youtube
video to json.  That way multiple video
lists could be saved and loaded.

It would also make sense to then extend
tubelist.py to load a list of the available
video lists so the videos could be changed.

Then add a play fuction so the videos could
be played in succession on the page.

