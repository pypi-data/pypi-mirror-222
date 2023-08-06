from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Momos Helper Package'
LONG_DESCRIPTION = 'This package is to help increase standardisation & speed of development for Momos internal teams'

# Setting up
setup(
       # the name must match the folder name
        name="momos_py",
        version=VERSION,
        author="Shaun Chew",
        author_email="shaun@momos.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['psycopg2-binary==2.8.6','pandas==2.0.3','gspread==4.0.1','oauth2client==4.1.3'], # add any additional packages that needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'momos','internal','postgres','googlesheet'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)