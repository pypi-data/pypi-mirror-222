import setuptools


libName="MAZAlib"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=libName,
    version="0.0.1",
    description='TBA',
    long_description=long_description,
    author='Mathieu Gravey, Roman V. Vasilyev, Timofey Sizonenko, Kirill M. Gerke, Marina V. Karsanina',
    author_email='mathieu.gravey@unil.ch',
    license='GPLv3',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: C++',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent'
    ]
)