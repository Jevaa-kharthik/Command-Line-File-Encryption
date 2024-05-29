from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.hashes import SHA1
from cryptography.hazmat.primitives.hashes import SHA224
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.hashes import SHA384
from cryptography.hazmat.primitives.hashes import SHA512
from cryptography.hazmat.primitives.hashes import SHA3_224
from cryptography.hazmat.primitives.hashes import SHA3_256
from cryptography.hazmat.primitives.hashes import SHA3_384
from cryptography.hazmat.primitives.hashes import SHA3_512
from cryptography.hazmat.primitives.hashes import SHA512_224
from cryptography.hazmat.primitives.hashes import SHAKE128
from lib.Argument import Argument
import sys

class Hashes:
    def hash(en_algo):
        a = Argument(sys.argv)
        if a.hasOptions("--encryption"):
            # en_algo = a.getOptionValue("--encryption")
            try :
                if(en_algo == "SHA1"):
                    encrypted = SHA1()
                elif(en_algo == "SHA224"):
                    encrypted = SHA224()
                elif(en_algo == "SHA256"):
                    encrypted = SHA256()
                elif(en_algo == "SHA3844"):
                    encrypted = SHA384()
                elif(en_algo == "SHA512"):
                    encrypted = SHA512()
                elif(en_algo == "SHA3_224"):
                    encrypted = SHA3_224()
                elif(en_algo == "SHA3_256"):
                    encrypted = SHA3_256()
                elif(en_algo == "SHA3_384"):
                    encrypted = SHA3_384()
                elif(en_algo == "SHA3_512"):
                    encrypted = SHA3_512()
                elif(en_algo == "SHA512_224"):
                    encrypted = SHA512_224()
                elif(en_algo == "SHAKE128"):
                    encrypted = SHAKE128()
                else :
                    print("USAGE : There is no encryption called {}".format())
                    
            except Exception as e:
                print("USAGE : There is no encryption called {}".format())