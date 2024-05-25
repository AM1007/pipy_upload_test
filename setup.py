from setuptools import setup, find_packages

setup(
    name='pipy_upload_test',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'prompt_toolkit'
    ],
    entry_points={
        "console_scripts": [
            "pipy_upload_test = project.main:main"
        ]
    }
)
