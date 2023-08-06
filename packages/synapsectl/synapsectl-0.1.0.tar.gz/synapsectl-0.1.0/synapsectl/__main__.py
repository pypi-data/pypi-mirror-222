import datetime
import getpass
from time import sleep

import synapsectl.config
import synapsectl.api as api
import argparse
import urllib.parse
import tqdm

cli = argparse.ArgumentParser("Synapse control tool")
subparsers = cli.add_subparsers(dest="subcommand")


def argument(*name_or_flags, **kwargs):
    """Convenience function to properly format arguments to pass to the
    subcommand decorator.
    """
    return (list(name_or_flags), kwargs)


def subcommand(args=None, parent=subparsers):
    args = args or []

    def decorator(func):
        parser = parent.add_parser(func.__name__.replace('_', '-'), description=func.__doc__)
        for arg in args:
            parser.add_argument(*arg[0], **arg[1])
        parser.set_defaults(func=func)

    return decorator


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


@subcommand()
def version(args):
    response = api.request('get', '_matrix/federation/v1/version')

    ver = response.json()['server']
    print("{} version: {}".format(ver['name'], ver['version']))


@subcommand()
def media_statistics(args):
    response = api.request('get', '_synapse/admin/v1/statistics/users/media', auth=True)
    users = response.json()['users']
    users_on_size = sorted(users, key=lambda k: k['media_length'], reverse=True)
    for user in users_on_size:
        humansize = sizeof_fmt(user['media_length'])
        print("{: <10} {} ({})".format(humansize, user['user_id'], user['displayname']))


@subcommand([argument('--guests', help="Include guest users", action="store_true"),
             argument('--filter', help="List users containing string"),
             argument('--deactivated', help="Include deactivated users", action="store_true"),
             argument('--order', help="Order by",
                      choices=['name', 'is_guest', 'admin', 'user_type', 'deactivated', 'shadow_banned', 'displayname',
                               'avatar_url'], default='name'),
             argument('--reverse', help="Reverse sort order", default="f", action="store_const", const="r")])
def user_list(args):
    url = '/_synapse/admin/v2/users?'
    q = {
        'from': '0',
        'limit': '100',
        'guests': 'true' if args.guests else 'false',
        'deactivated': 'true' if args.deactivated else 'false',
        'order_by': args.order,
        'dir': args.reverse
    }
    if args.filter:
        q['filter'] = args.filter
    url += urllib.parse.urlencode(q, doseq=False)
    response = api.request('get', url, auth=True)
    for user in response.json()['users']:
        flags = ''
        if user['is_guest']:
            flags += 'g'
        if user['admin']:
            flags += 'A'
        if user['deactivated']:
            flags += 'D'
        print('{: <3} {} ({})'.format(flags, user['name'], user['displayname']))


@subcommand([argument("token", help="Access token from an admin user")])
def set_token(args):
    # Run an request with the token to check its validity
    api.request('get', '/_synapse/admin/v2/users?from=0&limit=1&guests=false', token=args.token)

    config = synapsectl.config.get_config()
    config.set('connection', 'token', args.token)
    synapsectl.config.save_config(config)


@subcommand([argument("username", help="Username to login with")])
def login(args):
    pwd = getpass.getpass("Password: ")
    response = api.request('post', '/_matrix/client/r0/login', payload={
        "type": "m.login.password",
        "user": args.username,
        "password": pwd,
    })
    data = response.json()
    config = synapsectl.config.get_config()
    config.set('connection', 'token', data['access_token'])
    synapsectl.config.save_config(config)


@subcommand([argument('--all', help="Also include local-only data", action="store_true"),
             argument('--age', help="Delete events older than x days (default 365)", type=int, default=365)
             ])
def purge_history(args):
    response = api.request('get', '_synapse/admin/v1/rooms', auth=True)
    rooms = set()
    for row in response.json()['rooms']:
        rooms.add(row['room_id'])

    print(f"Cleaning history of {len(rooms)} rooms...")
    now = datetime.datetime.now()
    last_year = now - datetime.timedelta(days=args.age)
    for room_id in tqdm.tqdm(rooms):
        ret = api.request('post', f'_synapse/admin/v1/purge_history/{room_id}', auth=True, payload={
            "delete_local_events": args.all,
            "purge_up_to_ts": int(last_year.timestamp())
        })
        data = ret.json()
        if 'error' in data and data['errcode'] != 'M_NOT_FOUND':
            print(f"API response: {data['error']}")
            return
        if 'errcode' in data and data['errcode'] == 'M_NOT_FOUND':
            # M_NOT_FOUND is returned when there's no events to be deleted
            continue
        pid = data['purge_id']
        sleep(0.2)
        while True:
            ret = api.request('get', f'_synapse/admin/v1/purge_history_status/{pid}', auth=True, payload={
            })
            if ret.json()['status'] != "active":
                break
            sleep(2.5)
        if ret.json()['status'] != "complete":
            err = ret.json()['error']
            print(f"Failed purge of room {room_id}: {err}")


@subcommand([argument('--age', help="Delete media older than x days (default 365)", type=int, default=365)])
def purge_media_cache(args):
    now = datetime.datetime.now()
    last_year = now - datetime.timedelta(days=args.age)

    before_ts = int(last_year.timestamp()) * 1000
    print("Removing files, this is a slow operation without feedback...")
    ret = api.request('post', f'_synapse/admin/v1/purge_media_cache?before_ts={before_ts}', auth=True)
    data = ret.json()
    if 'error' in data:
        print(data['error'])
        return
    print(f"Removed {data['deleted']} files")


def main():
    args = cli.parse_args()
    if args.subcommand is None:
        cli.print_help()
    else:
        args.func(args)


if __name__ == '__main__':
    main()
