class TaskParseError(Exception):
    """
    Represent an error when parsing a task.
    """
    message: str = ""

    def __init__(self, message):
        self.message = message
