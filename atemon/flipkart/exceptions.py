"""Exception handlers."""


class ProductNotLoadedException(Exception):
    """Exception class to raise when products are not loaded already."""

    def __init__(self, expression=None, message="Products are not loaded yet."):
        """initialize."""
        self.expression = expression
        self.message = message
