from setuptools import setup

setup(
    name='sedi',
    version='0.11',
    py_modules=['provision', 'sed'],
    install_requires=[
        # list your script's dependencies here
        # for example, 'requests' if your script uses the requests library
    ],
    entry_points='''
        [console_scripts]
        sedi=provision:main
    ''',
)

# Certainly! Here's a step-by-step guide on how you can package your Python script and make it available for users to install via pip:
# 
# 1. **Create a setup.py file:** This file is used by setuptools to package your script. It should be in the same directory as your script file (`sed.py`), and it should look something like this:
# 
#     ```python
#     from setuptools import setup
# 
#     setup(
#         name='sedi',
#         version='0.1',
#         py_modules=['sed'],
#         install_requires=[
#             # list your script's dependencies here
#             # for example, 'requests' if your script uses the requests library
#         ],
#         entry_points='''
#             [console_scripts]
#             sedi=sed:main
#         ''',
#     )
#     ```
# 
#     This setup file declares that there is a console script named `sedi` that should run the `main` function in the `sed` module (i.e., `sed.py`). Replace `main` with the name of the function you want to run when the `sedi` command is invoked.
# 
# 2. **Package your script:** You can now create a distribution package for your script. First, install setuptools and wheel (if you haven't already) with the following command:
# 
#     ```shell
#     pip install setuptools wheel
#     ```
# 
#     Then, run this command to create a source distribution and a wheel distribution of your script:
# 
#     ```shell
#     python setup.py sdist bdist_wheel
#     ```
# 
#     This will create two files in a new `dist` directory: a .tar.gz file (the source distribution) and a .whl file (the wheel distribution).
# 
# 3. **Test your package locally:** Before you publish your package to PyPI, you might want to test it locally to make sure it works. You can do this with pip's `--find-links` option, which tells pip to look for packages in the local filesystem. Run this command to install your package locally:
# 
#     ```shell
#     pip install --find-links=dist sedi
#     ```
# 
#     After running this command, you should be able to use the `sedi` command in your terminal.
# 
# 4. **Publish your package to PyPI:** Once you're satisfied that your package works as expected, you can publish it to PyPI. First, install twine (if you haven't already):
# 
#     ```shell
#     pip install twine
#     ```
# 
#     Then, run this command to upload your distributions to PyPI:
# 
#     ```shell
#     twine upload dist/*
#     ```
# 
#     You'll be prompted to enter your PyPI username and password. If you don't have a PyPI account, you can create one at https://pypi.org/account/register/.
# 
# 5. **Install your package:** Your package is now available on PyPI! Anyone can install it with pip:
# 
#     ```shell
#     pip install sedi
#     ```
# 
# And they will be able to run your script using the `sedi` command.
# 
# Remember, you will need to replace 'main' in the setup.py file with the name of the function you want to run when your script is invoked. If your script is just a bunch of statements and doesn't define a function to be run, you might want to wrap your script's code in a function so that it can be invoked by setuptools. For example:
# 
# ```python
# def main():
#     # your script's code here
# 
# if __name__ == '__main__':
#     main()
# ```
# 
# This way, your script can be run both as a standalone script and as a console script installed by pip.
# Aleksa21
# WZn-ZK7,VANf4-S