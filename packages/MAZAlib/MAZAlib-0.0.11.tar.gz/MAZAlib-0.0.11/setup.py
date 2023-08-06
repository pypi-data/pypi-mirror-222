import setuptools
import glob

libName="MAZAlib"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=libName,
    version="0.0.11",
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
    ext_modules=[setuptools.Extension(libName, sources=['./maza_cwrapper/pythoninterface.cpp'],
			language="c++", 
			extra_compile_args=["-std=c++17",'-O3', '-w'],
			extra_link_args=["-std=c++17"],
			include_dirs=['mydist/include/'],
			libraries = ["mydist"],
			library_dirs = ["mydist/build/"]
			)]
)