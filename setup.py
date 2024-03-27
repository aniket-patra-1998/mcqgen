from setuptools import find_packages,setup

setup(
    name = 'mcqgen',
    version='0.0.1',
    author = 'aniket patra',
    author_email='aniketpatra001@gmail.com',
    install_requires =['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    PACKAGES=find_packages()
)