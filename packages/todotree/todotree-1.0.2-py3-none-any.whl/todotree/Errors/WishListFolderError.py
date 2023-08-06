class WishListFolderError(Exception):
    """
    Represents an error when parsing the wishlist folder
    """
    message: str = ""

    def __init__(self, message):
        self.message = message
