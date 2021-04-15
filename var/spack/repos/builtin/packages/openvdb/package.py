# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Openvdb(CMakePackage):
    """OpenVDB is an open source C++ library comprising a novel hierarchical
    data structure and a large suite of tools for the efficient storage and
    manipulation of sparse volumetric data discretized on three-dimensional
    grids. It was developed by DreamWorks Animation for use in volumetric applications
    typically encountered in feature film production."""

    homepage = "https://www.openvdb.org"
    url      = "https://github.com/AcademySoftwareFoundation/openvdb/archive/refs/tags/v7.2.3.tar.gz"

    version('8.0.1', sha256='a6845da7c604d2c72e4141c898930ac8a2375521e535f696c2cd92bebbe43c4f')
    version('8.0.0', sha256='04a28dc24a744f8ac8bbc5636a949628edb02b7c84db24ad795429c8c739a9ee')
    version('7.2.3', sha256='3087f4f31c844a6e8c7d7c93d396998cd052b1ef196e3510c0e33eaccbf5af0b')

    variant('print', default=True, description='Command line binary for displaying information about OpenVDB files')
    variant('lod', default=True, description='Command line binary for generating volume mipmaps from an OpenVDB grid')
    variant('render', default=True, description='Command line binary for ray-tracing OpenVDB grids')
    variant('view', default=True, description='Command line binary for displaying OpenVDB grids in a GL viewport')
    variant('python', default=False, description='Python module for OpenVDB C++ Python bindings')
    variant('jemalloc', default=True, description='Follow recommendation to use Jemalloc, otherwise TBB malloc')

    depends_on('cmake@:3.13.5', type='build', when='+python')

    depends_on('boost +system +iostreams')
    depends_on('boost +numpy +python', when='+python')
    depends_on('python', when='+python')
    depends_on('py-numpy', when='+python')
    depends_on('intel-tbb')
    depends_on('openexr')
    depends_on('c-blosc')
    depends_on('zlib')
    depends_on('glfw', when='+view')
    depends_on('jemalloc', when='+jemalloc')

    def cmake_args(self):
        args = [
            self.define('OPENVDB_BUILD_CORE', True),
            self.define_from_variant('OPENVDB_BUILD_VDB_PRINT', 'print'),
            self.define_from_variant('OPENVDB_BUILD_VDB_LOD', 'lod'),
            self.define_from_variant('OPENVDB_BUILD_VDB_RENDER', 'render'),
            self.define_from_variant('OPENVDB_BUILD_VDB_VIEW', 'view'),
            self.define_from_variant('OPENVDB_BUILD_PYTHON_MODULE', 'python'),
        ]
        return args
