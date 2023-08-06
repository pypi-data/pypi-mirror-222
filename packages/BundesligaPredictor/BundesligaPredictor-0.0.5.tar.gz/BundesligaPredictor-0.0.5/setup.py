from setuptools import setup, find_packages

setup(
    name='BundesligaPredictor',
    version='0.0.5',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'flask',
        'bs4',
        'requests',
        'hyperopt'
    ],
    package_data={
    '': ['*'],
    'scripts': ['*'],
    'tests': ['*'],
    'data': ['*']
}

)
