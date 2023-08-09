from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import binascii

def generate_keys_and_signatures(M, N):
    keys = [DSA.generate(1024) for _ in range(N)]
    message = b"CSCI301 Contemporary Topics in Security 2023"

    signatures = []
    for i in range(M):
        signer = DSS.new(keys[i], 'fips-186-3')
        hash_obj = SHA256.new(message)
        signature = signer.sign(hash_obj)
        signatures.append(binascii.hexlify(signature).decode())

    return keys, signatures

def generate_scripts(M, N):
    keys, signatures = generate_keys_and_signatures(M, N)

    scriptPubKey = " ".join(binascii.hexlify(key.publickey().export_key(format='DER')).decode() for key in keys)
    scriptSig = " ".join(signatures)

    with open("scriptPubKey.txt", "w") as spk_file:
        spk_file.write(scriptPubKey)

    with open("scriptSig.txt", "w") as ss_file:
        ss_file.write(scriptSig)

generate_scripts(2, 3)
