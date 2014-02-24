Trove Guestagent
--------

Trove Guestagent is a in-VM agent for the Database as a Service of OpenStack.


To run all tests and PEP8, run tox, like so:
$ tox

To quickly run the tests for Python 2.7, run:
$ tox -epy27

To quickly run PEP8, run:
$ tox -epep8

To generate a coverage report,run:
$ tox -ecover
(note: on some boxes, the results may not be accurate unless you run it twice)
