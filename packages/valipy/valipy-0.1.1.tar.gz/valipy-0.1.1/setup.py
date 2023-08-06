from setuptools import find_packages, setup
setup(
    name='valipy',
    packages=find_packages(),
    version='0.1.1',
    description='A chainable, fluent Python library for validating data',
    author='Joaquin Jose Von Chong',
    license='MIT',
    author_email = 'jjvonchong@outlook.com',      # Type in your E-Mail
    url = 'https://github.com/pimepan/valipy',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
    keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
    readme='README.md',
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)