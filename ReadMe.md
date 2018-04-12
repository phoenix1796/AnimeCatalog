# AnimeCatalog

A place to catalog any and all anime you watch !

## Features

* CSRF protection
* GooglePlus Login
* JSON Api
* Login Deep linking

## Setup

Tested on Python 3.6.3

To run on windows clone the VM,<br>
https://github.com/udacity/fullstack-nanodegree-vm <br>

Or,

Use pip3 ,

> pip3 install --user flask sqlalchemy

## Steps to Run

First setup the catalog.db using ,

> python3 database_setup.py

Then populate the Database with,

> python3 database_populate.py

Start the project using,

> python3 finalProject.py

> Access server by localhost:5000 \*

\*(127.0.0.1 not allowed in the google dashboard)

## JSON endpoints

|                 Endpoint                  |           Function           |
| :---------------------------------------: | :--------------------------: |
|                /api/json/                 | view all Categoryies & Items |
|        /api/json/\<category_name\>        |    view Category details     |
| /api/json/\<category_name\>/\<item_name\> |      view Item details       |

## Miscellaneous

To disable flask debug mode,

> finalProject.py(153:16)

To change webserver port ,

> finalProject.py(154:33)

## Screenshots

![Home page](/screenshots/ss1.png?raw=true "Catalog Overview")
![Anime page](/screenshots/ss2.png?raw=true "Anime Overview")

## References

controllers/authController.py - > Used code from the Oauth course @ udacity

'Started this for my udacity Fullstack nanodegree , continuing it because it seemed like an interesting excuse to watch anime in my free time :P '
