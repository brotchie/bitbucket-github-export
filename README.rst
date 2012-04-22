Simple command line script to migrate a bitbucket.org Mercurial repository to github.

Requires your public key to be installed on both bitbucket and github.

Depends on the hg-git mercurial extensions and the Pygithub3 and
python-bitbucket Python packages.::

    sudo apt-get install python-dev
    sudo pip install hg-git Pygithub3 https://bitbucket.org/jmoiron/python-bitbucket/get/default.tar.bz2

Activate the hg bookmarking extensions and hg-git by adding::

    [extensions]
    hgext.bookmarks =
    hggit =

to your ~/.hgrc.
