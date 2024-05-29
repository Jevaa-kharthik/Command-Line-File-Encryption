### Prerequisites : 
	Python Modules like:
	- Cryptography
	- Sys
	- Hashes
	 
### On Ubuntu or Debian :
```
sudo apt install encrypto
```
### OR
```
apt install encrypto
```
### On mac : 
```
brew install encrypto
```
### --filepath : 
```
jevaakharthik@Jevaa$ encrypto --filepath=~/Downloads/sample.txt
```
### --secrct :
```
jevaakharthik@Jevaa$ encrypto --filepath=~/Downloads/sample.txt --secret=jevaa@123
```
### --encryption :
```
jevaakharthik@Jevaa$ encrypto --filepath=~/Downloads/sample.txt --secret=jevaa@123 --encryption=<TypeOfEncryption>
```
### Type of Encryption :

- SHA1
- SHA224
- SHA256
- SHA384
- SHA512
- SHA3_224
- SHA3_256
- SHA3_384 
- SHA3_512
- SHA512_224
- SHAKE128

