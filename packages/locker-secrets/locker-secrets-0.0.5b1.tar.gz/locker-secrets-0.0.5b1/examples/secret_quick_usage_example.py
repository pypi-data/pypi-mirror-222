import os
from dotenv import load_dotenv

import locker


load_dotenv()
access_key = os.getenv("ACCESS_KEY_TEST")
locker.access_key = "10G7DBZTW0PB:ZsoAyq3odFcLWk1GwwH2U2nWF24EBgM7ouc1+6JyS7M="
locker.api_base = "https://13.212.140.120:8080"

# Get list secrets
secrets = locker.list()
for secret in secrets:
    print(secret.key, secret.value, secret.description, secret.environment_name)


# # Get a secret value by secret key. If the Key does not exist, the SDK will return the default_value
# secret_value = locker.get_secret("Key 1", default_value="TheDefaultValue")
# print(secret_value)
#
#
# # Update a secret value by secret key
# secret = locker.modify(key="Key 1", value="NEW_VAL_1", environment_name="Staging")
# print(secret.key, secret.value, secret.description, secret.environment_name)
#
#
# # Create new secret
# new_secret = locker.create(key="GOOGLE_API", value="test", environment_name="Staging")
# print(new_secret.key, new_secret.value, new_secret.description, new_secret.environment_name)
