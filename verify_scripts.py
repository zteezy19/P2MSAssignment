from Crypto.PublicKey import DSA

from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import binascii

def verify_script():
    with open("scriptPubKey.txt", "r") as spk_file:
        public_keys_hex = spk_file.read().split()
    with open("scriptSig.txt", "r") as ss_file:
        signatures_hex = ss_file.read().split()

    public_keys = [DSA.import_key(binascii.unhexlify(pk_hex)) for pk_hex in public_keys_hex]
    signatures = [binascii.unhexlify(sig_hex) for sig_hex in signatures_hex]

    message = b"CSCI301 Contemporary Topics in Security 2023"

    for i, signature in enumerate(signatures):
        verifier = DSS.new(public_keys[i], 'fips-186-3')
        hash_obj = SHA256.new(message)
        try:
            verifier.verify(hash_obj, signature)
            print(f"The signature {i+1} is authentic.")
        except ValueError:
            print(f"The signature {i+1} is not authentic.")

verify_script()
