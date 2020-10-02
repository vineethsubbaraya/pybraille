from setuptools import setup, find_packages

with open("README.md", "r") as rd:
  long_description = rd.read()
 
setup(
  name='pybraille',
  version='0.1.0',
  description='A library to conver text to 6-dot braille pattern(Grade 1)',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/vineethsubbaraya/pybraille',  
  author='Vineeth Subbaraya',
  author_email='vsubbaraya033@gmail.com',
  license='MIT', 
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  keywords=['python', 'braille', 'text to braille'],
  packages=find_packages(),
  install_requires=['']
)