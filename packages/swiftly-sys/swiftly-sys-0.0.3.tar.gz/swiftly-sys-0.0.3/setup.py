from setuptools import setup, find_packages

setup(
    name='swiftly-sys',
    version='0.0.3',
    license='Apache2',
    packages=find_packages(),
    scripts=['scripts/swiftly', 'scripts/swiftly.bat'],
    description = 'Do what you\'re good at; writing code. Swiftly handle the rest',
    long_description='''
    Swiftly let's you focus on building amazing products. Swiftly makes sure your entire code scales, while keeping the code so maintainable. No spaghetti code, ever!\n
    Read the docs at: https://docs.swiftly-sys.tech
    ''',
    author = 'Shubham Gupta',
    author_email = 'shubhastro2@gmail.com',
    url = 'https://github.com/brainspoof/swiftly-sys',
    keywords = ['python project', 'project management', 'code management', 'project building', 'python project managment', 'organized project'],
    install_requires=[],
)