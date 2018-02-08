PyMailMove
==========
PyMailMove allows you to backup E-Mails, as well as copying them between
different accounts for the purpose of migrating them.

Installation
------------

PyMailMove is installable via pip

  pip install pymailmove

Source install:

  pip install git+https://github.com/funbaker/pymailmove

Usage
-----

PyMailMove is a command line tool. It uses subcommands to specify different
email storages.

  pymailmove --help

  Usage: pymailmove [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

  Commandline entrypoint

  Options:
    --version  Show the version and exit.
    --help     Show this message and exit.

  Commands:
    from-imap
    from-mbox
    to-imap
    to-mbox

Currently supported server interfaces are IMAP, and the used local file format
is mbox.

Use pymailmove COMMAND --help to see the available options
