import re
from yt_dlp import YoutubeDL

class DataValidation:
    def __init__(self):
        self.yt = YoutubeDL()

    def validate_input(self, input):
        """
        Validates if the input is a valid YouTube link or short code.
        Args:
            input (str): The input to be validated.
        Returns:
            bool: True if the input is valid, False otherwise.
        """
        if self.validate_url(input):
            return True
        elif self.validate_short_code(input):
            return True
        else:
            return False

    def validate_url(self, url):
        """
        Validates if the input YouTube link is valid.
        Args:
            url (str): The URL to be validated.
        Returns:
            bool: True if the URL is valid, False otherwise.
        """

        # Check if the URL contains 'youtube.com'
        if re.search(r"^https?:\/\/(?:www\.)?youtube\.com\/", url):
            try:
                self.yt.extract_info(url=url)
                return True
            except Exception as e:
                print(f"Error validating URL: {e}")
                return False
        else:
            return False

    def validate_short_code(self, code):
        """
        Validates if the input YouTube short code is valid.
        Args:
            code (str): The short code to be validated.
        Returns:
            bool: True if the code is valid, False otherwise.
        """
        # Check if the code contains 'youtu.be'
        if re.search(r"^https?:\/\/(?:www\.)?youtu\.be\/", code):
            try:
                self.yt.extract_info(url=code)
                return True
            except Exception as e:
                print(f"Error validating short code: {e}")
                return False
        else:
            return False

class OptionsSelector:
    pass

class Downloader:
    pass