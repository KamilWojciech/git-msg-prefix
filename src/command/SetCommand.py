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
        gitConfig = GitConfig()
        gitConfig.set(self.branch, self.prefix)

        print "Commit messages for \033[92m" + self.branch + "\033[0m branch has now prefix: \033[92m" + self.prefix + "\033[0m"
