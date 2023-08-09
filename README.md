# P2MSAssignment
Implementation of foundational concepts in cryptocurrency &amp; blockchain technology

Files
The code is separated into two scripts:

generate_scripts.py - Generates the scriptPubKey and scriptSig files.
verify_script.py - Verifies the signatures in the P2MS script.

How to run the programs
Generate Scripts
Run generate_scripts.py in your Python environment. It takes two arguments: the number of signatures (M) and the number of public keys (N). Here's an example:

# This will generate scripts with 2 signatures and 3 public keys.
generate_scripts(2, 3)

The script generates N DSA 1024-bit key pairs, and then M signatures of the text "CSCI301 Contemporary Topics in Security 2023", each signed with a different private key.

The script writes the public keys to scriptPubKey.txt and the signatures to scriptSig.txt.
Verify Script
Run verify_script.py in your Python environment. This script reads the public keys from scriptPubKey.txt and the signatures from scriptSig.txt, and verifies each signature using its corresponding public key. It outputs a message to the console indicating whether each signature is authentic.

Expected outcomes
When you run generate_scripts.py, it should generate two files: scriptPubKey.txt and scriptSig.txt. The former will contain N public keys in hexadecimal format, separated by spaces. The latter will contain M signatures in hexadecimal format, also separated by spaces.

When you run verify_script.py, it should output a message for each signature, indicating whether the signature is authentic. If everything is working correctly, all the signatures should be authentic.
