from setuptools import setup, find_packages

with open('/Users/jevaakharthik/Documents/SNA/pythoncli/Assignment_1/encrypto/requirements.txt', 'r') as f:
    requirments = f.read().splitlines()

setup(

    name='encrypto',
    version='0.1.0',
    packages=find_packages(),
    author='Jevaa Kharthik N',
    author_email='jevaasureka@gmail.com',
    description='encrypto can encrypt any type of file using different algorithm and it is done by cryptography',
    url= 'https://git.selfmade.ninja/jevaa_kharthik/Assignment_1',
    install_requires=[
            requirments
    ],
    entry_points={
        'console_scripts': [
            'encrypto = encrypto.encrypto:main'
        ],
    },
    
)
