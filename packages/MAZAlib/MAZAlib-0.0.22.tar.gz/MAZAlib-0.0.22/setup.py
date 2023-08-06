import setuptools
import glob

import os
from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext
from pathlib import Path


class CMakeExtension(Extension):
    def __init__(self, name):
        super().__init__(name, sources=[])


class CMakeBuild(build_ext):
    def run(self):
        ext = self.extensions[0]
        build_temp = Path(self.build_temp)
        build_temp.mkdir(parents=True, exist_ok=True)
        extdir = Path(self.get_ext_fullpath(ext.name))
        extdir.mkdir(parents=True, exist_ok=True)

        cmake_list_dir = os.path.abspath(os.path.dirname(__file__))
        build_dir = os.path.join(cmake_list_dir, 'build')
        library_path = '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + \
            str(extdir.parent.absolute())
        self.spawn(['cmake', cmake_list_dir,
                   library_path, '-B', build_dir])
        self.spawn(['cmake', '--build', build_dir,
                   '--target', 'imaza', '--', '-j', '-Imydist/include/', '-Lmydist/build/','-lmydist'])


libName="MAZAlib"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=libName,
    version="0.0.22",
    description='TODO',
    long_description=long_description,
    author='Mathieu Gravey, Roman V. Vasilyev, Timofey Sizonenko, Kirill M. Gerke, Marina V. Karsanina',
    author_email='mathieu.gravey@unil.ch',
    license='GPLv3',
    packages=setuptools.find_packages() + ["mydist"],
    package_data={'mydist': ['build/*.so', 'include/*.h']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: C++',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent'
    ],
    # ext_modules=[setuptools.Extension(libName, sources=['./MAZAlib/pythoninterface.cpp'],
	# 		language="c++", 
	# 		extra_compile_args=["-std=c++17",'-O3', '-w'],
	# 		extra_link_args=["-std=c++17"],
	# 		include_dirs=['mydist/include/'],
	# 		libraries = ["mydist"],
	# 		library_dirs = ["mydist/build/"]
	# 		)]
    ext_modules=[CMakeExtension('imaza')],
    cmdclass={'build_ext': CMakeBuild}
)