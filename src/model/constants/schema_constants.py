from datetime import datetime

# For Cerberus Validator to accept datetime in YYYY-MM-DD format.
TO_DATE = lambda s: datetime.strptime(s, "%Y-%m-%d")

# Constants for readability
URL = "string"
NETID = "string"

# Regex statements
FULLNAME_REGEX = "^\S*,(\S*|\S* \S.)$"
UUIDV4_REGEX = "^[0-9(a-f|A-F)]{8}-[0-9(a-f|A-F)]{4}-4[0-9(a-f|A-F)]{3}-[89ab][0-9(a-f|A-F)]{3}-[0-9(a-f|A-F)]{12}$"
PHONE_REGEX = "^\d{10}$"
UW_EMAIL_REGEX = "^\S*@uw.edu$"
UW_CAMPUS_REGEX = "^(seattle|bothell|tacoma)$"
