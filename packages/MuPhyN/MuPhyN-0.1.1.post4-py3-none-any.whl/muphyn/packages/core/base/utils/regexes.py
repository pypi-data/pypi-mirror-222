import re

from typing import List

class Regex:

    # Boolean regexes
    BooleanRegex = r"^\s*[tT]rue\s*$|^\s*[fF]alse\s*$|^\s*[01]{1}\s*$"
    FalseRegex = r"^\s*[fF]alse\s*$|^\s*0\s*$"
    TrueRegex = r"^\s*[tT]rue\s*$|^\s*1\s*$"
    
    # Integer regex
    IntegerRegex = r"^[-+]?[0-9]*$"

    # Comma float regexes 
    CommaFloatRegex = r"^[-+]?[0-9]*,[0-9]*$"
    CommaScientificNumberRegex = r"^[-+]?[1-9](?:,\d+)?[Ee][-+]?\d+$"

    # Dot float regexes
    DotFloatRegex = r"^[-+]?[0-9]*(?:\.[0-9]*)?$|^inf$"
    DotScientificNumberRegex = r"^[-+]?[1-9](?:\.\d+)?[Ee][-+]?\d+$"

    # String literal regex
    StringLiteralRegex = r"^\".*\"$"

    # Email
    EmailRegex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"

    # ----------
    # Functions
    # ----------

    @staticmethod
    def isBoolean(value: str) -> bool:
        return re.match(Regex.BooleanRegex, value) is not None

    @staticmethod
    def isTrueValue(value: str) -> bool:
        return re.match(Regex.TrueRegex, value) is not None

    @staticmethod
    def isFalseValue(value: str) -> bool:
        return re.match(Regex.FalseRegex, value) is not None

    @staticmethod
    def isInteger(value: str) -> bool:
        return re.match(Regex.IntegerRegex, value) is not None

    @staticmethod
    def isCommaFloat(value: str) -> bool:
        return re.match(Regex.CommaFloatRegex, value) is not None or re.match(Regex.CommaScientificNumberRegex, value) is not None

    @staticmethod
    def isCommaScientificFloat(value: str) -> bool:
        return re.match(Regex.CommaScientificNumberRegex, value) is not None

    @staticmethod
    def isDotFloat(value: str) -> bool:
        return re.match(Regex.DotFloatRegex, value) is not None or re.match(Regex.DotScientificNumberRegex, value)

    @staticmethod
    def isDotScientificFloat(value: str) -> bool:
        return re.match(Regex.DotScientificNumberRegex, value)

    @staticmethod
    def isStringLiteral(value: str) -> bool:
        return re.match(Regex.StringLiteralRegex, value)

    @staticmethod
    def isEmailAddress(value: str):
        return re.match(Regex.EmailRegex, value)
    
    @staticmethod
    def findAll(value: str, pattern: str) -> List[str]:
        return re.findall(pattern, value)