# TODO: Stub

import os

class Config:
    """
    Config Class - Holds functions to read/write App configurations
    """

    @staticmethod
    def get_conf(entry):
        """get_conf(entry) - returns the value of the inputted entry."""

        # Reading and storing the contents of tml_config.txt into conf_lines
        with open(os.path.join(os.getcwd(), "conf", "tml_config.txt"), "r") as conf_file:
            conf_lines = conf_file.readlines()

        # Creating variables
        assignChar = None
        endChar = None
        currentCharInt = 0
        conf_dict = {}

        # loop for every object in conf_lines
        for line in conf_lines:

            # Resetting variables
            current_line = ""
            currentEntry = None
            currentValue = None

            # Loop for every character in the current line
            for char in line:

                # if statements
                if char == ":":
                    assignChar = currentCharInt
                elif char == ";":
                    endChar = currentCharInt

                # Skipping newline characters
                if char == "\n":
                    pass
                else:
                    current_line += char

                # Incrementing currentCharInt by 1
                currentCharInt += 1

            # Analyzing current_line
            currentEntry = current_line[:assignChar]

            # Analyzing currentValue
            currentValue = current_line[assignChar+1:endChar]
            if currentValue == "true":
                currentValue = True
            elif currentValue == "false":
                currentValue = False
            elif currentValue == "None":
                currentValue = None

            # Creating new entry with item and value
            conf_dict[str(currentEntry)] = currentValue

        return conf_dict[entry]

