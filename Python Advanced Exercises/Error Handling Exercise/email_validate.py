import re


class NameTooShortError(Exception):
    """Name must be more than 4 characters"""


class MustContainAtSymbolError(Exception):
    """Email must contain @"""


class TooManyAtSymbolsError(Exception):
    """Email must contain only one @"""


class InvalidNameError(Exception):
    """Email input is invalid"""


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""


MIN_LEN = 4
VALID_DOMAINS = [".com", ".bg", ".org", ".net"]

email_pattern = r"^(\w+)@([a-z]+)\.([a-z]+)$"

while True:
    email_input = input().strip()

    if email_input == "End":
        break

    if "@" not in email_input:
        raise MustContainAtSymbolError("Email must contain @")
    if email_input.count("@") > 1:
        raise TooManyAtSymbolsError("Email must contain only one @")

    match = re.fullmatch(email_pattern, email_input)
    if not match:
        raise InvalidNameError("Email input is invalid")

    if len(match.group(1)) <= MIN_LEN:
        raise NameTooShortError("Name must be more than 4 characters")
    if match.group(3) not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
