# setup.py

from setuptools import setup, find_packages

setup(
    name='pix_qrcode',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'qrcode[pil]',
        'Pillow'
    ],
    description='Biblioteca para gerar QR Codes de pagamentos via PIX',
    author='Jean Pires - JD',
    author_email='jdrpires@gmail.com',
    url='https://github.com/jdrpires/pix_qrcode',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
