class Command:
    def __init__(self, args):
        self.className = args.which
        self.args = args

    def run(self):
        __import__(self.className)
        module = __import__(self.className)
        command = getattr(module, self.className)(self.args)
        command.run()
