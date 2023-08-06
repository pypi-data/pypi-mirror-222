from __future__ import print_function

import setuptools
import sys

# Convert README.md to reStructuredText.
if {'bdist_wheel', 'sdist'}.intersection(sys.argv):
    try:
        import pypandoc
    except ImportError:
        print('WARNING: You should install `pypandoc` to convert `README.md` '
              'to reStructuredText to use as long description.',
              file=sys.stderr)
    else:
        print('Converting `README.md` to reStructuredText to use as long '
              'description.')
        long_description = pypandoc.convert('README.md', 'rst')

setuptools.setup(
    name='chattr-django-master-password',
    version='1.1.3',
    author='Interaction Consortium',
    author_email='studio@interaction.net.au',
    url='https://github.com/ixc/django-master-password',
    description='Login as any user with a master password. Add master '
                'password support to your custom authentication backend.',
    long_description=locals().get('long_description', ''),
    license='MIT',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
    ],
    extras_require={
        'dev': [
            'ipdb',
            'ipython',
        ],
        'test': [
            'coverage',
            'coveralls',
            'django-dynamic-fixture',
            'django-nose',
            'django-webtest',
            'nose-progressive',
            'WebTest',
        ],
    },
    setup_requires=['setuptools_scm'],
)
