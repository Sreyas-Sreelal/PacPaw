from setuptools import setup, find_packages

setup(
    name='pacpaw',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Colorama',
        'BeautifulSoup4',
        'Requests',
    ],
    entry_points='''
        [console_scripts]
        pacpaw=pacpaw:cli
    ''',
)