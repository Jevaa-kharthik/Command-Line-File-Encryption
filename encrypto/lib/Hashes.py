from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

class Hashes:
    def hash(self, data, en_algo):
        algorithms = {
            "SHA1": hashes.SHA1(),
            "SHA224": hashes.SHA224(),
            "SHA256": hashes.SHA256(),
            "SHA384": hashes.SHA384(),
            "SHA512": hashes.SHA512(),
            "SHA3_224": hashes.SHA3_224(),
            "SHA3_256": hashes.SHA3_256(),
            "SHA3_384": hashes.SHA3_384(),
            "SHA3_512": hashes.SHA3_512(),
            "SHA512_224": hashes.SHA512_224(),
            "SHAKE128": hashes.SHAKE128(length=16),
        }
        
        if en_algo not in algorithms:
            raise ValueError(f"There is no encryption called {en_algo}")

        digest = hashes.Hash(algorithms[en_algo], backend=default_backend())
        digest.update(data.encode() if isinstance(data, str) else data)
        return digest.finalize()
