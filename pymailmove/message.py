"""
Message object
"""
import email


class Message(object):
    """
    Represents a message
    """

    def __init__(self, raw, date=None, flags=None):
        self._raw = raw
        self._message = email.message_from_bytes(raw)
        self._date = date
        self._flags = flags

    def __repr__(self):
        return "<Mail {} >".format(self.subject)

    @property
    def raw(self):
        """
        Content in rfc822 format
        """
        return self._raw

    @property
    def parsed(self):
        """
        Parsed message
        """
        return self._message

    @property
    def date(self):
        """
        Date in the format used in the imap protocol
        """
        return self._date

    @property
    def flags(self):
        """
        Flags as used in the imap protocol
        """
        return self._flags

    @property
    def subject(self):
        """
        Message subject
        """
        return self.parsed.get('Subject')
