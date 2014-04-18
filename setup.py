from distutils.core import setup

setup(
    name='socialanalytics',
    version='0.2.0',
    author='Michael Stitt',
    author_email='michaelstitt10@hotmail.com',
    packages=['socialanalytics'],
    url='https://github.com/Abundnce10/socialanalytics',
    license='LICENSE.txt',
    description='Insight into how a specific URL performs on a variety of social networks.',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 2.0.0",
    ],
)
