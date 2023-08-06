**SHE Cryptography**
========================
The expansion of SHE is Symmetric Hybrid Encryption. It is a hybrid and lightweight cryptographic system that transforms plaintext into ciphertext so that secret communication is to be ensured.

[![PyPI Version](https://img.shields.io/pypi/v/sheCry.svg)](https://pypi.python.org/legecy/sheCry)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

--------------------
**Preface**
--------------------
SHE is a symmetrical cryptographic concept that ensures faster processing speed along with better security. Theoretically, a hacker needs to go for 2^256 = 1.16e+77 possible ways in terms of finding the correct key to decrypt the ciphertext if the secret key is 256 bits long and secure with a hashing function. It is by far impossible for a regular user device to solve the math. It will be needed a supercomputer to do the computation. However, a low computational powered device (e.g. IOT device) can easily handle it because of its symmetric and stream cipher architecture. Thus, it makes the algorithm faster. Also, SHE is a software and hardware-independent cryptography. Last but not least, as technology is getting revolutionized day by day, it is embracing lightweight and low-powered systems. As a matter of fact, today's cryptography also needs to be lightweight and ensure better security and performance. This is why this new innovation, SHE Cryptography can make a fruitful impact in today’s security epidemic.

----------------------------
**Program Utilization**
----------------------------
* A user inputs the length of private keys and generated shared keys.
* A user inputs message.
* Generates prime number according to Fermat Prime Number Theorem.
* Generates private key.
* Generates public key according to private key.
* Diffie-Hellman key exchange protocol is used for authenticity checking, where a sender locks the message with a receiver's public key and the receiver unlocks it with his private key.
* The message is encrypted and decrypted by ChaCha20 algorithm.
* Poly1305 algorithm has been used for integrity checking.

--------------------------------
**Caution**
--------------------------------
* SHE is absolutely not for unethical motives.
* The message will be deleted automatically if anyone tries to alter the key.
* Anyone can use this cryptography for free only for education, research, and further development purpose.