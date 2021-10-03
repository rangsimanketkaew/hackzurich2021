import setuptools
from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='migarden',
    packages=setuptools.find_packages(),
    version='0.1',
    license='MIT',
    description='MiGarden - Let\'s save our planet from CO2',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Rangsiman Ketkaew',
    author_email='rangsiman1993@gmail.com',
    url='https://github.com/rangsimanketkaew/hackzurich2021',   # Provide either the link to your github or to your website
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',  
    keywords=[
        'migarden',
        'open-source', 
        'opencv', 
        'hackzurich'
        ], 
    install_requires=[
        'numpy',
        'pyzbar',
        'opencv-python',
        'cairosvg'
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': ['migarden=migarden.app:main']
    },
)
