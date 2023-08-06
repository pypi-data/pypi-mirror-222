from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='microjoy',
    version='0.0.2',
    license='MIT License',
    author='Issei momonge',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='mggyggf@gmail.com',
    keywords='joystick micropython',
    description=u'biblioteca para leitura de joystick com micropython',
    packages=['j'],
    install_requires=[],)