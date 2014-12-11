"""
Custom Exceptions
"""

class SubjectExists(Exception):
    """
    Raised when subject already exists
    """
    pass

class SubjectError(Exception):
    """
    Raised when problem with the subject file
    """
    pass

class UnknownTag(Exception):
    """
    Raised when tag is not recognised 
    """
    pass