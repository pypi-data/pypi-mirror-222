from setuptools import setup, find_packages
import textwrap

long_description = textwrap.dedent("""
    Package to send slack messages via databricks notebooks.

    ## Usage

    Here is a simple usage example:

    ```python
    from dbxslackmessage import SlackMessage

    webhook_url = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'
    channel = '#your-channel'
    messages = ['Hello, World!', 'This is a test message from dbxslackmessage package']

    slack_message = SlackMessage(webhook_url, channel)
    slack_message.send_messages(messages)
    ```
    ### Installing  dbxslackmessage

    ``` python -m pip install dbxslackmessage ```

""")

setup(
    name='dbxslackmessage',
    version='0.1.6',
    author='Vaishali Khairnar',
    author_email='vkhairnar@ripple.com',
    description='Package to send slack messages via databricks notebooks',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
