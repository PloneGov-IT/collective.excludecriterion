from setuptools import setup, find_packages
import os

version = '0.1.0'

setup(name='collective.excludecriterion',
      version=version,
      description="An extra criterion for plone.app.collection that exclude results with a list of keywords",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Development Status :: 4 - Beta",
        ],
      keywords='criterion collection subjects keywords',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone>=4.2',
          'plone.app.querystring',
      ],
      extras_require={
          'test': [
              'collective.testcaselayer',
              'Products.PloneTestCase',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
