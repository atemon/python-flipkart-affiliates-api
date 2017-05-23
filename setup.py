"""Setup.py file for Atemon.SMS package."""
from distutils.core import setup

setup(
    name='Flipkart-AffiliatesAPI',
    version='0.1.0.0',
    packages=['atemon', 'atemon.flipkart'],
    long_description="Connect to Flipkart Affiliates API with Python",
    author="Varghese Chacko",
    author_email="varghese@atemon.com",
    url="https://github.com/atemon/python-flipkart-affiliates-api",
    install_requires=["requests>=2.14.2"],
    provides=["flipkartaffiliates"],
    license="MIT License (modified)",
)
