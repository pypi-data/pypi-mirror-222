from setuptools import setup

setup(
    name='sedi',
    version='0.3',
    py_modules=['sed'],
    install_requires=[
        # list your script's dependencies here
        # for example, 'requests' if your script uses the requests library
    ],
    entry_points='''
        [console_scripts]
        sedi=sed:main
    ''',
)
