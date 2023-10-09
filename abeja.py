class Abeja():
    name = None
    target = []
    arguments = []

    def __init__(self):
        super().__init__()

    def add_name(self, name):
        self.name = name

    def add_target(self, target):
        self.target = target

    def add_argument_list(self, arguments):
        self.arguments = arguments

    def add_argument(self, argument):
        self.arguments.append(argument)
