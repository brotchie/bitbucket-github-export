import bitbucket
import bitbucket_github_export

from argparse import Namespace

TEST_BB_USERNAME = 'bbuser'
TEST_BB_PASSWORD = 'bbpassword'

TEST_GH_USERNAME = 'ghuser'
TEST_GH_PASSWORD = 'ghpassword'

def test_list_bitbucket(monkeypatch):
    class UserStub(object):
        def repositories(self):
            return {}

    class BitBucketStub(object):
        def user(self, username):
            assert username == TEST_BB_USERNAME
            return UserStub()

    monkeypatch.setattr(bitbucket, 'BitBucket', BitBucketStub)
    bitbucket_github_export.list_bitbucket(Namespace(args=[TEST_BB_USERNAME]))
