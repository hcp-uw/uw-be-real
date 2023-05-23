from datetime import datetime

# For Cerberus Validator to accept datetime in YYYY-MM-DD format.
TO_DATE = lambda s: datetime.strptime(s, "%Y-%m-%d")

# Constants for readability
URL = "string"
NETID = "string"

# Regex statements
FULLNAME_REGEX = "^[\S].{0,63},[\S].{0,63}$"
FIRSTNAME_REGEX = "^[\S].{0,63}$"
LASTNAME_REGEX = "^[\S].{0,63}$"
USERNAME_REGEX = "^[\S]{1,64}$"
ACCOUNT_STATUS_REGEX = "^(active|deactivated|banned)$"
UUIDV4_REGEX = "^[0-9(a-f|A-F)]{8}-[0-9(a-f|A-F)]{4}-4[0-9(a-f|A-F)]{3}-[89ab][0-9(a-f|A-F)]{3}-[0-9(a-f|A-F)]{12}$"
PHONE_REGEX = "^\d{10}$|^$"
UW_EMAIL_REGEX = "^\S*@uw.edu$"
UW_CAMPUS_REGEX = "^(seattle|bothell|tacoma)$|^$"
MAJOR_REGEX = "^[\S]{1,64}$|^$"
DATE_REGEX = "^(19|20)\d\d[- \.](0[1-9]|1[012])[- \.](0[1-9]|[12][0-9]|3[01])$|^$"
INTERESTS_REGEX = "^[\S]{1,64}$"
