# -*- coding: utf-8 -*-
'''
@File    :   validate_password.py
@Time    :   2023/08/02 15:16:23
@Author  :   rayzh
@Description:   Indicate whether the given string is a valid email,mobile,etc
                according to the regular expression.
'''
import re


class Validation:
    def __init__(self) -> bool:
        self.valid = True

    def validate_email(self, email: str) -> bool:
        pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'
        if re.match(pattern=pattern, string=email) is not None:
            return self.valid
        else:
            return not self.valid

    def validate_mobile(self, mobile: str) -> bool:
        """
        Available mobile phone numbers in Chinese Mainland.
        """
        pattern = r'^1[35678]\d{9}$'
        if re.match(pattern=pattern, string=mobile) is not None:
            return self.valid
        else:
            return not self.valid

    def validate_password(self, password: str, min=10, max=32) -> bool:
        """
        The password shall contain at least two kinds of numbers, uppercase and lowercase letters, and special characters (excluding Chinese characters and spaces), and the length shall not be less than 10 characters.
        """
        pattern = r'(?!^[0-9]+$)(?!^[a-z]+$)(?!^[A-Z]+$)(?!^[^A-z0-9]+$)^[^\s\u4e00-\u9fa5]{10,32}'
        if 10 <= len(password) <= 32:
            if re.match(pattern=pattern, string=password) is not None:
                return self.valid
        return not self.valid
