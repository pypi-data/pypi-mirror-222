import os
import configparser

configfile = None


def get_config():
    global configfile
    confdir = os.path.expanduser('~/.config')
    if os.getenv('XDG_CONFIG_HOME'):
        confdir = os.path.expanduser(os.getenv('XDG_CONFIG_HOME'))
    confdir = os.path.join(confdir, 'synapsectl')
    if not os.path.isdir(confdir):
        os.makedirs(confdir)
    configfile = os.path.join(confdir, 'synapsectl.ini')
    parser = configparser.ConfigParser()
    parser.add_section('connection')
    parser.set('connection', 'url', 'http://127.0.0.1:8008')

    if os.path.isfile(configfile):
        parser.read(configfile)

    return parser


def save_config(config):
    with open(configfile, 'w') as handle:
        config.write(handle)
