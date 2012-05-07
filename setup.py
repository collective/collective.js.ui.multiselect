from setuptools import setup, find_packages
import os

version = '1.0'
maintainer = 'Elio Schmutz'

setup(name='collective.js.ui.multiselect',
      version=version,
      description='Integrates the multiselect widget into plone.',
      long_description=open('README.rst').read() + '\n' + \
          open(os.path.join('docs', 'HISTORY.txt')).read(),

      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.0',
        'Framework :: Plone :: 4.1',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        ],

      keywords='jquery ui multiselect plone',
      author='4teamwork GmbH',
      author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
      url='https://github.com/4teamwork/collective.js.ui.multiselect',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js', 'collective.js.ui'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',
        ],

      entry_points='''
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      ''',
      )
