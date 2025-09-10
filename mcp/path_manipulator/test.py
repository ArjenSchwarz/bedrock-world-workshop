import utils

user_pool_id = "ap-southeast-2_BMF8LKUZ2"
client_id = "nfah83tili3qtcnpevfr2bhiq"
client_secret = "ribae8d4nrrcoig1a4ar7nfc0jnejmpv4ro1i5napova7q4c7hh"
RESOURCE_SERVER_ID = "pathmanipulator-ezqyo2z4b9"
scopeString = f"{RESOURCE_SERVER_ID}/gateway:read {RESOURCE_SERVER_ID}/gateway:write"
REGION = "ap-southeast-2"

token_response = utils.get_token(
    user_pool_id, client_id, client_secret, scopeString, REGION
)
token = token_response["access_token"]
