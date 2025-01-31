import os


def error_message_detail(error, error_detail):
    """
    It takes an error and an error detail and returns a string with the file name, line number, and
    error message

    Returns:
      The error message is being returned.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(file_name,
                                                                                                           exc_tb.tb_lineno,
                                                                                                           str(error))

    return error_message

# It's a custom exception class that takes an error message and an error detail and returns a formatted error message
class TTSException(Exception):
# TTSException(e, sys):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message