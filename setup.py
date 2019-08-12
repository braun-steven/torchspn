from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='torchspn',
      version='0.1.0',
      description='PyTorch Layerwise Sum-Product Network Library',
      long_description=readme(),
      url='http://github.com/steven-lang/torchspn',
      author='Steven Lang',
      author_email='steven.lang.mz@gmail.com',
      license='MIT',
      packages=['torchspn'],
      zip_safe=False,
      keywords='pytorch spn torch cuda',
      install_requires=['torch'],
      include_package_data=True,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Artificial Intelligence'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      )
