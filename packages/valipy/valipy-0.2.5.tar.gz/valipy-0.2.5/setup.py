from setuptools import find_packages, setup
import os

description = "A chainable, fluent Python library for validating data"
def read_file(filename):
    try:
        with open(os.path.join(os.path.dirname(__file__), filename)) as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return description
try:
    long_description = read_file('readme.md') 
except Exception as e:
    long_description = description
setup(
    name='valipy',
    packages=find_packages(),
    version='0.2.5',
    description='A chainable, fluent Python library for validating data',
    long_description_content_type='text/markdown',
    long_description=long_description,

    author='Joaquin Jose Von Chong',
    license='MIT',
    author_email='jjvonchong@outlook.com',
    url='https://github.com/pimepan/valipy',
    keywords=['validation', 'data', 'schema', 'schema validation', 'regex', 'pattern matching'],
    install_requires=["twine", "wheel", "setuptools"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
