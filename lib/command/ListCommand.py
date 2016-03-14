import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../helper')
from git_helper import *

class ListCommand:
    def __init__(self, args):
        pass

    def run(self):
        gitConfig = GitConfig()
        list = gitConfig.list()

        for key, val in list.iteritems():
            print key + ': ' + val
