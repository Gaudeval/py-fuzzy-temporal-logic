from setuptools import setup, find_packages

setup(name='py-stl',
      version='0.11',
      description='TODO',
      url='http://github.com/mvcisback/py-stl',
      author='Marcell Vazquez-Chanlatte',
      author_email='marcell.vc@eecs.berkeley.edu',
      license='MIT',
      install_requires=[
          'funcy',
          'parsimonious', 
          'lenses',
          'sympy',
          'bitarray',
      ],
      extras_require = {
          'robustness': ['numpy', 'pandas']
      },
      packages=find_packages(),
)
