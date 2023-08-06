from setuptools import setup #, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Async HTTP Client for Waba360 interacting'
LONG_DESCRIPTION = 'And aiohttp webhook server for receiving updates.'

# Setting up
setup(
    name="waba_360",
    version=VERSION,
    author="Mike Artemiev",
    author_email="<mixartemev@gmail.com>",
    description=DESCRIPTION,
    # packages=find_packages(),
    # package_dir={'': 'src'},
    install_requires=['aiohttp', 'python-dotenv'],
    keywords=['whatsapp', 'http-client', 'api'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
    ]
)