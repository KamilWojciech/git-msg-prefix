import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../helper')
from git_helper import *

class RemoveCommand:
    def __init__(self, args):
        if (args.branch):
            self.branch = args.branch
        else:
            self.branch = branchName()


    def run(self):
        gitConfig = GitConfig()
        if (gitConfig.unset(self.branch) != None):
            print "Commit messages for \033[92m" + self.branch + "\033[0m branch no longer has prefix"
        else:
            print "Branch \033[92m" + self.branch + "\033[0m does not have prefix!"
