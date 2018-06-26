try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
setup(
    name='pybamer',
    version='0.1',
    author='Danny Antaki',
    author_email='dantaki@ucsd.edu',
    packages=['pybamer'],
    scripts=['pybamer/pybamer'],
    url='https://github.com/dantaki/pybamer',
    license='LICENSE',
    long_description=open('README').read(),
    install_requires=[
	"pysam",
	"numpy"
    ]
)
