import subprocess
import re
import sys

class GitConfig():
    def __init__(self):
        pass

    section = 'msg-prefix'

    def get(self, key):
        try:
            var = subprocess.check_output(['git', 'config', self.section + '.' + key]).strip()
        except subprocess.CalledProcessError:
            var = None

        return var

    def set(self, key, value):
        subprocess.check_output(['git', 'config', self.section + '.' + key, value])

    def unset(self, key):
        try:
            var = subprocess.check_output(['git', 'config', '--unset', self.section + '.' + key]).strip()
        except subprocess.CalledProcessError:
            var = None

        return var

    def list(self):
        output = subprocess.check_output(['git', 'config', '--list'])
        fullList = output.split('\n')

        list = {}
        for row in fullList:
            if (row):
                matches = re.match('^([^.^=]+)\.([^=]+)\=(.*)$', row)
                section = matches.group(1)
                branch = matches.group(2)
                value = matches.group(3)
                if (section == self.section):
                    list[branch] = value

        return list


def branchName():
    try:
        branchName = subprocess.check_output(['bash', '-c', 'git rev-parse --abbrev-ref HEAD 2>/dev/null '])
        branchName = branchName.strip()
    except:
        branchName = None
    return branchName
