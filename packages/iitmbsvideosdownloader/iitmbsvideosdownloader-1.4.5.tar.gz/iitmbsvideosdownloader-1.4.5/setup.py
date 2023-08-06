from setuptools import find_packages, setup
setup(
    name='iitmbsvideosdownloader',
    packages=find_packages(include=['iitmbsvideosdownloader']),
    version='1.4.5',
    description='Python Bot Library to download IITM BS videos.',
    author='Savi',
    license='MIT',
    install_requires=['selenium==4.10.0'],
    setup_requires=['pytest-runner', 'wheel'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)