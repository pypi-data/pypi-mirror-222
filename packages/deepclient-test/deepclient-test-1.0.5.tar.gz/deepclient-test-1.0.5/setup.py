from setuptools import setup, find_packages

setup(
    name="deepclient-test",
    version="1.0.5",
    packages=find_packages(),
    install_requires=[
        "aiohttp==3.8.4",
        "aiosignal==1.3.1",
        "async-timeout==4.0.2",
        "backoff==2.2.1",
        "botocore==1.29.129",
        "frozenlist==1.3.3",
        "gql==3.4.1",
        "graphql-core==3.2.3",
        "jmespath==1.0.1",
        "multidict==6.0.4",
        "websockets==10.4",
        "yarl==1.9.2",
        "yarl==1.9.2"
    ],
    description="Deep Client - a way to connect your favorite language with Deep",
    long_description="Deep Client - a way to connect your favorite language with Deep",
    license="Unlicense",
    url="https://github.com/Lotos2021/deepclient-test",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
