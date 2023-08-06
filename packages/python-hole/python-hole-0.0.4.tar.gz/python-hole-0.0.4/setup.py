from setuptools import setup

setup(
    name='python-hole',
    version='0.0.4',
    packages=['pyhole', 'pyhole.antlr', 'pyhole.visualizer'],
    package_dir={'': 'src'},
    url='https://github.com/JulienLie/python-hole',
    license='MIT',
    author='Julien Lienard',
    author_email='julien.lienard@uclouvain.be',
    description="Python package to build code patterns"
)
