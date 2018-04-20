"""
mbox storage
"""
from pathlib import Path
from mailbox import mbox, mboxMessage
from email.utils import parsedate

from .message import Message
from . import helpers

__all__ = ['MboxStorage']

conv_to = {
    '\Seen': 'R',
    '\Answered': 'A',
    '\Flagged': 'F',
    '\Deleted': 'D',
}
conv_from = {value: key for key, value in conv_to.items()}


def _convert_flags_to(flags):
    return ''.join(conv_to[flag] for flag in flags if flag in conv_to)


def _convert_flags_from(flags):
    flags = set(flags)
    flags = (conv_from[flag] for flag in flags if flag in conv_from)
    flags = tuple(flags)
    return flags


class MboxStorage:
    """
    This class represents a mbox file
    """
    def __init__(self, path):
        self._path = Path(path)
        self._mbox = mbox(path)

    def iter_messages(self, mailbox=None):
        if mailbox is None:
            mailbox = 'INBOX'

        ori = self._mbox

        try:
            ori.lock()

            for message in ori:
                message = Message(
                    bytes(message),
                    parsedate(helpers.ensure_string(message.get('Date'))),
                    _convert_flags_from(message.get_flags())
                )
                yield message
        except Exception:
            ori.unlock()
            raise
        finally:
            ori.flush()
            ori.unlock()

    def append_messages(self, messages):
        mailbox = None  # noqa: F841: there is no spoon

        dest = self._mbox
        path = self._path

        try:
            dest.lock()

            for message in messages:
                assert isinstance(message, Message)

                mboxmsg = mboxMessage(message.raw)
                mboxmsg.set_flags(_convert_flags_to(message.flags))
                mboxmsg.set_from(
                    helpers.ensure_string(message.parsed.get('From').encode()),
                    message.date
                )

                dest.add(mboxmsg)
        except Exception:
            dest.unlock()
            path.unlink()
            raise
        finally:
            dest.flush()
            dest.unlock()
