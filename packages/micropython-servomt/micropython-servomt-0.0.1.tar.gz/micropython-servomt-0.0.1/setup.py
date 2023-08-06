from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='micropython-servomt',
    version='0.0.1',
    license='MIT License',
    author='Issei momonge',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='mggyggf@gmail.com',
    keywords='micropython servo motor',
    description=u'uma biblioteca para controle de servo motor com micropython',
    packages=['se'],
    install_requires=[],)