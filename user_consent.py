USER_CONSENT.py
from solana.rpc.api import Client
from solana.publickey import PublicKey
import os

def check_user_consent(user_id):
    solana_client = Client(os.getenv('RPC_URL'))
    # This is a placeholder for how consent might be checked on-chain
    consent_account = PublicKey("CONSENT_ACCOUNT_ADDRESS")  # This would be a PDA for the user's consent
    consent_data = solana_client.get_account_info(consent_account)
    
    if consent_data and consent_data['result']['value']:
        # Decode the consent data here
        return True  # Consent is granted
    return False  # Consent is not granted or account not found

# Example usage
if __name__ == "__main__":
    user_id = 'example_user'
    if check_user_consent(user_id):
        print("User has consented to data analysis.")
    else:
        print("User has not consented to data analysis.")
