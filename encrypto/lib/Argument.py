class Argument:
    def __init__(self, args):
        self.commands = []
        self.options = []
        self.optionValues = {}
        
        for arg in args:
            if "=" in arg:
                pair = arg.split('=')
                self.optionValues[pair[0]] = pair[1]
                self.options.append(pair[0])
            else:
                self.commands.append(arg)

    def hasOptions(self, options):
        return any(option in self.options for option in options)

    def hasOption(self, option):
        return option in self.options

    def hasCommands(self, commands):
        return any(command in self.commands for command in commands)

    def hasCommand(self, command):
        return command in self.commands

    def getOptionValue(self, option, default=None):
        return self.optionValues.get(option, default)

    def hasOptionValue(self, option):
        return option in self.optionValues
