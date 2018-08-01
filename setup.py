from glob import glob
import os

from setuptools import find_packages, setup, Extension

long_description = 'Scout Application Performance Monitoring Agent - https://scoutapp.com'
if os.path.exists('README.md'):
    long_description = open('README.md').read()

setup(name='pyobjtrace',
      version='1.0.0',
      description='Python Object Allocation Tracer',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/scoutapp/pyobjtrace',
      author='Scout',
      author_email='support@scoutapp.com',
      license='MIT',
      zip_safe=False,
      python_requires='>=3.4, <4',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=[os.splitext(os.basename(path))[0] for path in glob('src/*.py')],
      ext_package='pyobjtrace',
      ext_modules=[Extension('objtrace', ['src/pyobjtrace/ext/objtrace.c'])],
      install_requires=[],
      keywords='apm performance monitoring development',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: System :: Monitoring',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
      ])
