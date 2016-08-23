# Loadshedding

GUI interface for fetching and displaying routine for loadshedding routine

  - Fetch routine automatically
  - Update manually
  - highlight current day

### Tech

It uses following library to work properly to work properly:

* [wx] - GUI library
* [httplib] - retrieve requests to specified url
* [datetime] - datetime
* [os] - for path related task

### Installation

It requires [python](http://python.org/doc) 2 or 3+ to run.

Download and extract the [latest pre-built release](https://github.com/joemccann/dillinger/releases).

Install the python and start the terminal.

```sh
$ cd <directory where you extracted>
$ python main.py
```

or launch compiled version.
```sh
$ cd <directory where you extracted>
$ cd dist
$ ./main
```
on linux or simply open loadshedding.exe on dist

### Todos

 - Add more movies information

License
----

MIT




[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [wx]: <http://wxpython.org>
   [httplib]: <https://docs.python.org/2/library/httplib.html>
   [datetime]: <http://python.org/doc>
   [os]: <https://docs.python.org/2/library/os.html>
