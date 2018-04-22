from setuptools import setup

setup(
    name="CoordinateTranslator",
    version='0.1',
    author='Manoj Pillay',
    author_email='spadejac@gmail.com',
    py_modules=['CoordinateTranslator', 'Cigar', 'CigarTests'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        CoordinateTranslator=CoordinateTranslator:cli
    ''',
    project_urls={
                 	'Source': 'https://gitlab.com/spadejac/U2FsdGVkX19c3IfNjlyyxNyniQpXP.Yp'
		 }
)
