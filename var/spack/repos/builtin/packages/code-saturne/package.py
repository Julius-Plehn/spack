# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install code-saturne
#
# You can edit this file again by typing:
#
#     spack edit code-saturne
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class CodeSaturne(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/code-saturne/code_saturne/archive/refs/tags/v6.2.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('6.3.0', sha256='54a1b1b22e69a9577753a20703dcaa266f3f04be2f8558f9b085b56551f214ef')
    
    variant('gui', default=False, description='Enable GUI')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    
    depends_on('mpi')
    depends_on('hdf5')
    depends_on('zlib')
    depends_on('py-pyqt5', when='+gui')
    # FIXME: Add additional dependencies if required.
    # depends_on('foo')

    def autoreconf(self, spec, prefix):
        # FIXME: Modify the autoreconf method as necessary
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
