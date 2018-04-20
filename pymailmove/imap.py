"""
IMAP Storage
"""
import logging
import imaplib

from .message import Message
from . import helpers

__all__ = ['IMAPServer']

logger = logging.getLogger(__name__)


class IMAPServer(object):
    """
    This class represents a mailserver
    """
    def __init__(self, host, port=None, login=None, ssl=True):
        """
        Initializes the object with the given parameters
        """
        self._host = host
        imap_kwargs = {"host": host}

        self._port = port
        if port:
            imap_kwargs["port"] = port

        self._ssl = ssl
        if ssl:
            if port is None:
                port = 993
            self._imap = imaplib.IMAP4_SSL(**imap_kwargs)
        else:
            if port is None:
                port = 143
            self._imap = imaplib.IMAP4(**imap_kwargs)

        if login:
            self._imap.login(*login)

    def iter_messages(self, mailbox=None):
        """
        Iterates over emails in a given mailbox

        Parameters
        ----------
        mailbox : str
            mailbox or directory to iterate over

        Returns
        -------
        sequence
            sequence of :class:`~pymailmove.Message` objects
        """
        if not mailbox:
            mailbox = "INBOX"

        self._imap.select(mailbox)

        _, (ids,) = self._imap.search(None, "ALL")

        for id_ in ids.split():
            _, ((meta, content), _) = self._imap.fetch(
                id_, "(FLAGS INTERNALDATE RFC822)")

            date = helpers.imapmeta2date(meta)
            flags = helpers.imapmeta2flags(meta)

            message = Message(content, date, flags)

            logger.info(
                'Fetched message from %s: %s', self._host, message.subject)

            yield message

    def append_messages(self, messages, mailbox=None):
        """
        Appends mail to mailbox
        """
        if mailbox is None:
            mailbox = "INBOX"

        self._imap.select(mailbox)

        for message in messages:
            assert isinstance(message, Message)

            self._imap.append(
                mailbox, ' '.join(message.flags), message.date, message.raw)

            logger.info(
                'Appended message to %s: %s', self._host, message.subject)
