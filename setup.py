from setuptools import setup

from distutils.command.sdist import sdist
from subprocess import Popen, PIPE
import os


class sdist_git(sdist):
    user_options = sdist.user_options + [
            ('dev', None, "Add a dev marker")
            ]

    def initialize_options(self):
        sdist.initialize_options(self)
        self.dev = 0

    def run(self):
        if self.dev:
            suffix = '.dev%s' % self.get_revision()
            self.distribution.metadata.version += suffix
        sdist.run(self)

    def get_revision(self):
        try:
            p = Popen('git log -n 1 --pretty=format:%H'.split(), stdout=PIPE)
            rev = p.stdout.read().strip()
        except:
            print("Could not determine git revision.")
            rev = "deadbeef"
        return rev


# prevent metis_dll check at setup time
os.environ['METIS_DLL'] = 'SKIP'

import torch_metis

setup(
    name='torch_metis',
    version=torch_metis.__version__,
    author="Tim Kaler",
    author_email="tfk@mit.edu, timkaler@gmail.com",
    url="https://github.com/kw/metis-python",
    py_modules=['torch_metis'],
    license='MIT',
    description="Modified version of the METIS wrapper using ctypes originally written by Ken Watford (kwatford@gmail.com). Original repository https://github.com/kw/metis-python. This package is primarily intended to be used with SALIENT++",
    long_description= open('README.rst').read(),
    cmdclass={'sdist': sdist_git},
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
        ],
)
