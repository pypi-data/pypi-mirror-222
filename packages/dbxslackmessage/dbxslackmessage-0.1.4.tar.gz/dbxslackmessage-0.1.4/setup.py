from setuptools import setup, find_packages

setup(
    name='dbxslackmessage',
    version='0.1.4',
    author='Vaishali',
    author_email='vkhairnar@ripple.com',
    description='Package to send slack messages via databricks notebooks',
    long_description = 'Package to send slack messages via databricks notebooks',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
