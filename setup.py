from setuptools import setup

packages = [
    'osxmmkeys',
]

requires = [
    'pyobjc',
]

setup(
    name='osxmmkeys',
    version='0.0.4',
    description='Easily handle media keys on OS X.',
    long_description=open('README.rst').read(),
    author='Justin Li',
    author_email='jli@j-li.net',
    url='https://github.com/pushrax/osxmmkeys',
    license='MIT',
    packages=packages,
    install_requires=requires,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia',
    ]
)

