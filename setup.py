from setuptools import setup, find_packages
import os

version = open('collective/js/ui/multiselect/version.txt').read().strip()
maintainer = 'Elio Schmutz'

setup(name='collective.js.ui.multiselect',
      version=version,
      description="turning html multiple select inputs into a sexier equivalent",
      long_description=open("README.txt").read() + "\n" +
                    open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='jquery ui multiselect',
      author='%s, 4teamwork GmbH' % maintainer,
      author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
      license='GPL2',
      url='http://www.quasipartikel.at/multiselect/',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js', 'collective.js.ui'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
