from setuptools import setup, find_packages
from setuptools import  find_namespace_packages
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='antibp3',
    version='1.3',
    description='A tool to predict anti-bacterial peptides',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license_files = ('LICENSE.txt',),
    url='https://github.com/raghavagps/AntiBP3', 
    packages=find_namespace_packages(where="src"),
    package_dir={'':'src'},
    package_data={'antibp3.blast_binaries':['**/*'], 
    'antibp3.blast_db':['**/*'],
    'antibp3.model':['*'],
    'antibp3.motif':['*'],
    'antibp3.perl_scripts':['*']},
    entry_points={ 'console_scripts' : ['antibp3 = antibp3.python_scripts.antibp3:main']},
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'numpy', 'pandas',  'argparse'# Add any Python dependencies here
    ]
)
