Solana_Storage.py
from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.system_program import CreateAccountParams, create_account
from solana.transaction import Transaction
import json
import os

def store_data_on_solana(data):
    solana_client = Client(os.getenv('RPC_URL'))
    payer = PublicKey(os.getenv('SOLANA_PAYER_KEYPAIR'))  # User's wallet address
    
    # This is a very basic example. In reality, you'd use a program to handle data storage
    new_account = PublicKey("NEW_ACCOUNT_PUBLIC_KEY")  # This would be generated dynamically
    lamports = solana_client.get_minimum_balance_for_rent_exemption(len(json.dumps(data)))
    
    transaction = Transaction().add(
        create_account(CreateAccountParams(
            from_pubkey=payer,
            new_account_pubkey=new_account,
            lamports=lamports,
            space=len(json.dumps(data)),
            program_id=PublicKey("SYSTEM_PROGRAM_ID")
        ))
    )
    
    # Here you would sign and send the transaction
    # solana_client.send_transaction(transaction, payer)

if __name__ == "__main__":
    data = {"example": "data"}
    store_data_on_solana(data)
    
 insight-container {
    margin: 20px;
}

.insight-item {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    margin-bottom: 10px;
}

.insight-header {
    color: #333;
}

.tweet-content {
    font-style: italic;
    color: #555;
}

.insight-details {
    color: #777;
    font-size: 0.9em;
}

.sentiment-scores {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
}

.additional-info {
    margin-top: 10px;
    font-size: 0.9em;
    color: #888;
}
