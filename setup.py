import sys

# Borrowing a trick from nibabel to enable some functionality coming
# from setuptools.
# For some commands, use setuptools
if len(set(('test', 'easy_install')).intersection(sys.argv)) > 0:
    import setuptools

from distutils.core import setup

extra_setuptools_args = {}
if 'setuptools' in sys.modules:
    extra_setuptools_args = dict(
        tests_require=['nose'],
        test_suite='nose.collector',
        extras_require = dict(
            test='nose>=0.10.1')
    )

files = ['../resources/*']
setup(name = "neurosynth",
      version = "0.2.dev",
      maintainer='Tal Yarkoni',
      maintainer_email='tyarkoni@gmail.com',
      url='http://github.com/neurosynth/core',
      packages = ["neurosynth", "neurosynth.base", "neurosynth.analysis", "tests"],
      package_data = {'neurosynth' : ['../resources/*'],
                      'tests' : ['data/*']
                      },
      **extra_setuptools_args
      )
