from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_BasicAuth(username, password, required_scopes):
    return {'test_key': 'test_value'}

def check_JwtAuthToken(token):
    return {'test_key': 'test_value'}


