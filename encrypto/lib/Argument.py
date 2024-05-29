class Argument:
    def __init__(self, args):
        self.commands = []  # --pathname=<FilePath>  --secret=<Password> --encryption=<WhatKindOfEncryption>
        self.options = []  # <--pathname>   <--secret>  <--encryption>
        self.optionValues = {}
        # Dict/Set here... Unique Index/No Repeating Value
        # <FilePath>  <Password>  <WhatKindOfEncryption>
        self.args = args

        for arg in self.args:
            if "=" in arg:
                if "=" in arg:
                    pair = arg.split()
                    self.optionValues[pair[0]] = pair[1]
                    # --pathname='I/Am/The/Path'
                    # pair[0] = --pathname
                    # pair[1] = 'I/Am/The/Path'
                    self.options.append(pair[0])
                else:
                    self.options.append(arg) # pair[0] = --pathname
            else:
                self.commands.append(arg)

    def hasOptions(self, options: list):
        userOptions = set(self.options)
        reqOptions = set(options)
        return len(list(userOptions & reqOptions)) >= 1 # userOptions Union Of reqOptions shold be greater than 1 to print the function

    def hasOption(self, option):
        return option in self.hasOptions([option]) # This loops to the hasOptions(self, options: list)

    def hasCommands(self, commands):
        userCommands = set(self.commands)
        reqCommands = set(commands)
        return list(userCommands & reqCommands) # This hasCommands(self, commands) will check wheather the command satisfies

    def hasCommand(self, command):
        return command in self.hasCommands([command]) # This loops to the hasCommands(self, commands)

    def getOptionValue(self, option, defalut=None):
        if option in self.optionValues:
            return self.optionVallues[option] # It will get the vaule of option from hasOptions(self,options)
        else:
            return defalut # else it returns default to the options value

    def hasOptionvalue(self, option):
        return option in self.optionValues # if it has the option value it will send to the self.optionvalues