"""
Eases porting of bitbucket.org Mercurial
repositories to github.

Requires:
        public key on bitbucket and github
        apt-get install python-dev
        ./pip install ~/contrib/python-bitbucket
        ./pip install Pygithub3                                                             ./pip install hg-git
        Add to ~/.hgrc
        [extensions]
        hgext.bookmarks =
        hggit = 
"""

from __future__ import print_function

import os
import sys
import argparse
import operator
import tempfile

from bitbucket import BitBucket
from pygithub3 import Github

def list_bitbucket(args):
    assert len(args.args) == 1

    username, = args.args

    bb = BitBucket()
    user = bb.user(username)
    for repo in sorted(user.repositories(), key=operator.itemgetter('name')):
        print('{0} ({1}) - {2}'.format(repo['name'], repo['slug'], repo['description']))

def list_github(args):
    assert len(args.args) == 1

    username, = args.args

    gh = Github()

    for repo in gh.repos.list(username).all():
        print('{0} - {1}'.format(repo.name, repo.description))

def port(args):
    assert len(args.args) == 5

    bbslug, bbusername, ghrepo, ghusername, ghpassword = args.args

    # Fetch repository description.
    bb = BitBucket()
    bbrepo = bb.repository(bbusername, bbslug)
    bbrepo_info = bbrepo.get()
    description = bbrepo_info.get('description')

    # Checkout repository.
    temppath = tempfile.mkdtemp()
    checkoutpath = os.path.join(temppath, bbslug)
    hgreposrc = 'ssh://hg@bitbucket.org/{0}/{1}'.format(bbusername, bbslug)

    rc = os.system('hg clone {0} {1}'.format(hgreposrc, checkoutpath))
    assert rc == 0

    # Create github repository.
    gh = Github(login=ghusername, password=ghpassword, user=ghusername)
    ghrepo_info = gh.repos.create(dict(name=ghrepo, description=description))
    ghrepodst = 'git+ssh://' + ghrepo_info.ssh_url.replace(':', '/')

    rc = os.system('hg -R {0} bookmark -r default master'.format(checkoutpath))
    assert rc == 0

    rc = os.system('hg -R {0} push {1}'.format(checkoutpath, ghrepodst))
    assert rc == 0

COMMANDS = {
    'list-bitbucket' : ('List all bitbucket repositories.', list_bitbucket),    
    'list-github' : ('List all github repositories.', list_github),
    'port' : ('Port a bitbucket repository to github.', port),
}

def main():
    parser = argparse.ArgumentParser(description='Port bitbucket hg repos to github.')
    parser.add_argument('command', help='Command to perform.')
    parser.add_argument('args', nargs='*')

    args = parser.parse_args()

    if args.command in COMMANDS:
        _, fcn = COMMANDS[args.command]
        fcn(args)
    else:
        print('Invalid command "{0}".'.format(args.command), file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
