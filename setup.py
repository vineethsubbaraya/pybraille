from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3.5',
  'Programming Language :: Python :: 3.6',
  'Programming Language :: Python :: 3.7',
  'Programming Language :: Python :: 3.8',
]
 
setup(
  name='pybraille',
  version='0.0.1',
  description='A library to conver text to 6-dot braille pattern(Grade 1)',
  #long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  #url='',  
  author='Vineeth Subbaraya',
  author_email='josh@edublocks.org',
  license='MIT', 
  #classifiers=classifiers,
  keywords=['python', 'braille', 'text to braille'], 
  packages=find_packages(),
  install_requires=['']
)