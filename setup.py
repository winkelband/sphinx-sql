from setuptools import setup, find_packages
from sphinx_sql import __version__, __release__

cmdclass = {}
try:
    from sphinx.setup_command import BuildDoc
    cmdclass['build_sphinx'] = BuildDoc
except ImportError:
    print("Warning: sphinx is not available, not building docs.")

with open('README.rst') as file:
    long_description = file.read()

version = __version__
release = __release__
name = 'sphinx-sql'

setup(
    name=name,
    version=release,
    packages=find_packages(),
    url='https://github.com/winkelband/sphinx-sql',
    license='MIT',
    author=[
        'Marcus Robb',
        'David Berthel'
    ],
    description="Sphinx extension for autodoc of SQL files by Marcus Robb. Forked and extended by David Berthel.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    install_requires=[
        'ddlparse',
        'sphinx',
        'sphinx_rtd_theme'
    ],
    dependency_links=[
        'git://github.com/winkelband/ddlparse.git#egg=ddlparse',
    ],
    include_package_data=True,
    cmdclass=cmdclass,
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', release),
            'source_dir': ('setup.py', 'docs/source'),
            'build_dir': ('setup.py', 'docs/build')
        }
    }
)
