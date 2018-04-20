.. _api:

Usage
=====
To copy messages from different sources you need to have at least two storage
objects.

Those storage objects include:

* :py:class:`pymailmove.imap.IMAPServer`
* :py:class:`pymailmove.mbox.MboxStorage`

Each of those objects have a ``iter_messages`` and a ``append_messages``
method.


>>> from pymailmove.imap import IMAPServer
>>> from pymailmove.mbox import MboxStorage
>>>
>>> src = IMAPServer('localhost')
>>> dst = MboxStorage('backup.mbox')
>>>
>>> for msg in src.iter_messages():
>>>   dst.append_message(msg)

Server object's ``iter_messages`` and ``append_message`` methods may have a
``mailbox`` parameter.

>>> src = IMAPServer('localhost')
>>> dst = MboxStorage('remotehost')
>>>
>>> for msg in src.iter_messages(mailbox='submailbox'):
>>>   dst.append_message(msg, mailbox='submailbox')

API
===

.. automodapi:: pymailmove.message
.. automodapi:: pymailmove.imap
.. automodapi:: pymailmove.mbox
