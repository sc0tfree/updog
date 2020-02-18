from setuptools import setup
from os import path
import updog


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='updog',
    version=updog.version,
    url='https://github.com/sc0tfree/updog',
    # GitHub releases in format "updog-X.Y"
    download_url = 'https://github.com/sc0tfree/updog/archive/updog-' + updog.version + '.tar.gz',
    license='MIT',
    author='sc0tfree',
    author_email='henry@sc0tfree.com',
    description='Updog is a replacement for Python\'s SimpleHTTPServer. '
                'It allows uploading and downloading via HTTP/S, can set '
                'ad hoc SSL certificates and use http basic auth.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='HTTP server SimpleHTTPServer directory',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Communications :: File Sharing',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Security'
    ],
    packages=['updog', 'updog.utils'],
    entry_points={
        'console_scripts': 'updog = updog.__main__:main'
    },
    include_package_data=True,
    install_requires=[
        'colorama',
        'flask',
        'flask_httpauth',
        'werkzeug',
        'pyopenssl'
    ],
)
