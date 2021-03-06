from distutils.core import setup

setup(name='stdeb',
      # Keep version in sync with stdeb/__init__.py, Install section
      # of README.rst, and USER_AGENT in scripts/pypi-install.
      version='0.5.1',
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      description='Python to Debian source package conversion utility',
      long_description=open('README.rst').read(),
      license='MIT',
      url='http://github.com/astraw/stdeb',
      packages=['stdeb','stdeb.command'],
      scripts=['scripts/py2dsc',
               'scripts/pypi-install',
               ],
)
