from setuptools import setup, find_packages

setup(
    name='pipedrive-api',
    version="0.1",
    license="BSD",

    install_requires = [
        "requests",
    ],

    description='Minimalistic wrapper around Pipedrive API',
    long_description=open('README.md').read(),

    author='Harshad Sharma',
    author_email='harshad@sharma.io',

    url='http://github.com/hiway/pipedrive-api',
    download_url='http://github.com/hiway/pipedrive-api/downloads',

    include_package_data=True,

    packages=['pipedrive'],

    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
    ]
)