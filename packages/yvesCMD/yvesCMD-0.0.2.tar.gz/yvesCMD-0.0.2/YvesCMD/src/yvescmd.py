"""
[Fork Description]:::
    This module is a fork of the 'cmd' microframework designed for building console applications. In this fork, certain elements have been removed to streamline the framework and make it more lightweight. The goal was to simplify the process of creating and managing console commands while retaining the core functionality of the original 'cmd' framework.

[Features]:::
    - Removal of unnecessary components from the original 'cmd' framework.
    - Simplified command creation and handling for console applications.
    - Retains core functionalities for creating interactive console-based interfaces.
    - Provides an efficient and straightforward way to define and execute custom console commands.

[Note]:::
    The original 'cmd' microframework is a useful tool for console application development, but it can be enhanced and tailored for specific use cases through forks like this one. The modifications made in this fork aim to make the 'cmd' framework even more user-friendly and straightforward for developers looking to build console-based applications.

[New]:::
    - Introduction of the void command without arguments.
    - Enhancement of the do command structure:
        Previously, in the original module, all command attributes (i.e., text following the command name) were combined into the first argument, excluding 'self.'
        [For Example]:::
        Old:
            def do_command(self, arg): . . .
                [ cmd ] command a b c d
                # In 'arg,' a string with text "a b c d."
        New:
            def do_command(self, a, b, c=None, d=None): . . .
                [ cmd ] command option_a option_b
                # Arguments 'a' and 'b' will contain 'option_a' and 'option_b,' respectively. If an option-arg has no value, the parameter is not mandatory.
    )
"""


import string
from .register import AutoRegisterCommandsMeta

IDENTCHARS = string.ascii_letters + string.digits + '_'

__all__ = ["YveCMD"]

class YveCMD(metaclass=AutoRegisterCommandsMeta):
    identchars = IDENTCHARS
    ruler = '='
    lastcmd = ''
    intro = None
    relative_prompt = '[ cmd ] ' 
    admin = False

    def __init__(self):
        self.cmdqueue = []

    @classmethod
    def register_handler(cls, cmd_handler):
        cls.register_handler_method(cmd_handler)  # Call the class method to register the handler

    def cmdloop(self, intro=None):
        """
        [Goals]
            - Starts the command loop.

        [ForExm]
            - cmdloop
        """
        self.preloop()
        try:
            if intro is not None:
                self.intro = intro
            if self.intro:
                print(str(self.intro))
            stop = None
            while not stop:
                if self.cmdqueue:
                    line = self.cmdqueue.pop(0)
                else:
                    line = input(self.relative_prompt)  # Use input() for simplicity
                line = self.precmd(line)
                stop = self.onecmd(line)
                stop = self.postcmd(stop, line)
            self.postloop()
        except KeyboardInterrupt:
            self.postloop()

    def precmd(self, line):
        """
        [Goals]
            - Preprocesses the command line input before parsing.

        [ForExm]
            - precmd line1
        """
        return line

    def postcmd(self, stop, line):
        """
        [Goals]
            - Postprocesses the command execution result.

        [ForExm]
            - postcmd stop1 line1
        """
        return stop

    def preloop(self):
        """
        [Goals]
            - Runs any setup code before the command loop starts.
        """
        pass

    def postloop(self):
        """
        [Goals]
            - Runs any cleanup code after the command loop ends.
        """
        print("Exiting...")

    def onecmd(self, line):
        """
        [Goals]
            - Parses and executes a single command line input.

        [ForExm]
            - onecmd line1
        """
        cmd, args, line = self.parseline(line)
        if not line:
            return self.emptyline()
        if cmd is None:
            return self.default(line)
        self.lastcmd = line
        if line == 'EOF':
            self.lastcmd = ''
        if cmd == '':
            return self.default(line)
        else:
            try:
                func = getattr(self, 'do_' + cmd)
                func(*args)  # Call the do_ method with arguments
            except AttributeError:
                try:
                    func = getattr(self, 'void_' + cmd)
                    func()  # Call the void_ method without arguments
                except AttributeError:
                    return self.default(line)
            except TypeError as e:
                if not self.admin:
                    print("Error: Invalid number of arguments.")
                    print("Type 'help {}' for more information.".format(cmd))
                else:
                    print(e)
            except Exception as e:
                print("Error:", e)

    def emptyline(self):
        """
        [Goals]
            - Handles an empty input line.
        """
        if self.lastcmd:
            return self.onecmd(self.lastcmd)

    def default(self, line):
        """
        [Goals]
            - Handles an invalid or unknown command.

        [ForExm]
            - default line1
        """
        print('[ e r r o r  > %s' % line)


    def parseline(self, line):
        """
        [Goals]
            - Parses a command line input into a command and its arguments.

        [ForExm]
            - parseline line1
        """
        line = line.strip()
        if not line:
            return None, None, line

        elif line[0] == '?':
            line = 'help ' + line[1:]
        elif line[0] == '!':
            if hasattr(self, 'do_shell'):
                line = 'shell ' + line[1:]
            else:
                return None, None, line

        i, n = 0, len(line)
        while i < n and line[i] in self.identchars:
            i += 1
        cmd, arg = line[:i], line[i:].strip().split()
        return cmd, arg, line