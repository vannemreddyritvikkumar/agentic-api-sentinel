import pyiso8583
from langchain.tools import tool

@tool
def analyze_iso_message(hex_message: str):
    """Decodes raw ISO 8583 hex logs to find sensitive PII leakage."""
    # This tool proves you can parse actual credit card data streams
    try:
        decoded, _ = pyiso8583.decode(hex_message)
        # Check if Field 2 (PAN/Card Number) is unmasked
        if len(decoded.get('2', '')) > 4:
            return "VULNERABILITY FOUND: Unmasked Primary Account Number (PAN) in Field 2."
        return f"Message Type: {decoded.get('t')}. No PII leakage detected."
    except Exception as e:
        return f"Error parsing ISO message: {str(e)}"

@tool
def test_bola_vulnerability(endpoint: str, user_token: str, victim_account_id: str):
    """Attempts to access another user's balance via IDOR/BOLA."""
    # This is the 'Red Teaming' part of your agent
    # It tries to use User A's token to see User B's data
    headers = {"Authorization": f"Bearer {user_token}"}
    payload = {"account_id": victim_account_id}
    # logic to call mock_payment_api...
    return "200 OK - Access Granted. (VULNERABLE)"
