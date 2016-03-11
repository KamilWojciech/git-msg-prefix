import subprocess

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

def branchName():
    branchName = subprocess.check_output(['bash','-c', 'git rev-parse --abbrev-ref HEAD '])
    branchName = branchName.strip()

    return branchName