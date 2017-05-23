"""Setup.py file for Atemon.SMS package."""
from setuptools import setup

setup(
    name='Flipkart-AffiliatesAPI',
    version='0.0.1.0',
    packages=['atemon', 'atemon.flipkart'],
    long_description="Connect to Flipkart Affiliates API with Python",
    author="Varghese Chacko",
    author_email="varghese@atemon.com",
    url="https://github.com/atemon/python-flipkart-affiliates-api",
    install_requires=["requests>=2.14.2"],
    provides=["flipkartaffiliates"],
    license="MIT License",
    keywords=["flipkart", "affiliate", "python", "api", "atemon"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 0.0.1 Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
