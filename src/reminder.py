class PrefixedReminder:
    """This class acts as a base class for other types of reminders.
    Classes that subclass it should override the `self.text` property
    """
    def __init__(self, prefix="Hey, don't forget to "):
        self.prefix = prefix
        self.text = prefix + '<placeholder_text>'

class PoliteReminder(PrefixedReminder):
    """This class politely reminds you of your tasks"""
    
    def __init__(self, text):
        prefix = "Would you please "
        super(PoliteReminder, self).__init__(prefix)
        self.text = self.prefix + text