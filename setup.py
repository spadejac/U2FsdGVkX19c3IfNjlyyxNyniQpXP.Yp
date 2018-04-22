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
		 },
    classifiers=[
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',

    # Pick your license as you wish (should match "license" above)
     'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2.7',
   ],
)
