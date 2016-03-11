import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../helper')
from git_helper import *

class SetCommand:
    def __init__(self, args):
        self.prefix = args.prefix

        if (args.branch):
            self.branch = args.branch
        else:
            self.branch = branchName()


    def run(self):
        print self.prefix
        print self.branch
        print 'set command!'
