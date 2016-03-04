from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Allowable extensions
allowed_ext = {'jpg', 'jpeg'}


def allowed_file(filename):
    """
    Determines if filename is allowed
    Args:
        filename: filename of uploaded file

    Returns:
        True if filename is allowed
        False otherwise

    """
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_ext
