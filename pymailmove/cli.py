# -*- coding: utf-8 -*-
"""
Commandline functionallity
"""
import click

from . import __version__
from .imap import IMAPServer
from .mbox import MboxStorage


@click.group(chain=True)
@click.version_option(__version__)
@click.pass_context
def main(context):
    """
    Commandline entrypoint
    """
    context.obj = {
        'messages': list(),
        'to': list()
    }


@main.command(name='from-imap')
@click.option('--host')
@click.option('--port', default=None)
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
@click.option('--ssl/--no-ssl', is_flag=True, default=True)
@click.pass_obj
def from_imap(obj, host, port, username, password, ssl):
    imap = IMAPServer(host, port=port, login=(username, password), ssl=ssl)

    for message in imap.iter_messages():
        obj['messages'].append(message)


@main.command(name='to-imap')
@click.option('--host')
@click.option('--port', default=None)
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
@click.option('--ssl/--no-ssl', is_flag=True, default=True)
@click.pass_obj
def to_imap(obj, host, port, username, password, ssl):
    imap = IMAPServer(host, port=port, login=(username, password), ssl=ssl)
    obj['to'].append(imap)


@main.command(name='from-mbox')
@click.option('--path', required=True)
@click.pass_obj
def from_mbox(obj, path):
    mbox = MboxStorage(path)

    for message in mbox.iter_messages():
        obj['messages'].append(message)


@main.command(name='to-mbox')
@click.option('--path', required=True)
@click.pass_obj
def to_mbox(obj, path):
    mbox = MboxStorage(path)
    obj['to'].append(mbox)


@main.resultcallback()
@click.pass_obj
def gruntwork(obj, result):
    for to in obj['to']:
        to.append_messages(obj['messages'])


if __name__ == '__main__':
    main()
