import subprocess
import re

class GitConfig():
    section = 'msg-prefix'

    def get(self, key):
        try:
            var = subprocess.check_output(['git','config', self.section + '.' +key]).strip()
        except subprocess.CalledProcessError:
            var = None

        return var

    def set(self, key, value):
        subprocess.check_output(['git','config', self.section + '.' +key, value])

    def list(self):
        output = subprocess.check_output(['git','config', '--list'])
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
    branchName = subprocess.check_output(['bash','-c', 'git rev-parse --abbrev-ref HEAD '])
    branchName = branchName.strip()

    return branchName