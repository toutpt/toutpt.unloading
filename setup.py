from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='toutpt.unloading',
      version=version,
      description="Unloading Plone by setup your zope project with technologies like varnish memcache relstorage, ...",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='jeanmichel.francois@makina-corpus.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['toutpt'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.caching',
          'python-memcached',
          'Products.MemcachedManager',
          'RelStorage',
          'psycopg2',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
