class ProjectFolderError(Exception):
    """
    Represent an error when parsing the project folder.
    """
    message: str = ""

    def __init__(self, message):
        self.message = message
