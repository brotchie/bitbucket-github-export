.. image:: https://docs.google.com/drawings/pub?id=1efPWn9IPMn_J4ZMrT2aOhgKq5flgtxpx47l3_aw3DUM&w=456&h=76

Simple command line script to migrate a bitbucket.org Mercurial repository to github. Install using::

    sudo pip install "https://github.com/brotchie/bitbucket-github-export/tarball/master"

Requires your public key to be installed on both bitbucket and github.

Depends on the hg-git mercurial extensions and the Pygithub3 and python-bitbucket Python packages (These are install by the setup.py script). Make sure you have the Python development libraries installed::

    sudo apt-get install python-dev

Activate the hg bookmarking extensions and hg-git by adding::

    [extensions]
    hgext.bookmarks =
    hggit =

to your ~/.hgrc.
