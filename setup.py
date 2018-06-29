from setuptools import setup


long_desc = """
TODO
"""

setup(name='latex_diff',
      version='0.1dev',
      description='TODO',
      long_description=long_desc,
      long_description_content_type='text/markdown',
      # url='',
      author='Johannes Lange',
      license='GPL-3.0',
      packages=['latex_diff'],
      scripts=['bin/latex_diff'],
      python_requires='>=3',
      install_requires=['simplediff'])
