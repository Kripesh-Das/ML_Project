import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Generate a detailed error message including file name, line number, and error description.
    
    Args:
        error: The error message or exception object.
        error_detail: The sys module, used to extract traceback information.
    
    Returns:
        str: A formatted error message with file name, line number, and error description.
    """
    _, _, exc_tb = error_detail.exc_info()  # Get exception traceback
    file_name = exc_tb.tb_frame.f_code.co_filename  # Extract file name from traceback
    
    # Format the error message with file name, line number, and error description
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    
    return error_message

class CustomException(Exception):
    """
    Custom exception class to provide more detailed error information.
    Inherits from the built-in Exception class.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initialize the CustomException.

        Args:
            error_message: The basic error message.
            error_detail: The sys module, passed to error_message_detail for traceback info.
        """
        super().__init__(error_message)  # Initialize parent Exception class
        # Generate detailed error message using error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        """
        Return the error message when the exception is converted to a string.
        This method is called when you print the exception or convert it to a string.

        Returns:
            str: The detailed error message.
        """
        return self.error_message

# Note: The 'logging' import from src.logger is not used in this code snippet.
# It might be used elsewhere in the project for logging purposes.