# """
# Main entry point for the Telco application.
# """
# pass

from database.models import DatabaseClass

DatabaseClass.insert_users("grant", "0902345689")
DatabaseClass.insert_users("grant", "0902345589")
DatabaseClass.insert_users("grant", "0902345789")