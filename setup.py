from setuptools import setup, find_packages
from typing import List

INSTALL_REQUIRES = [
    # 'confluent-kafka>=1.2.0',
    'bottle;python_version>"3"',
]  # type: List[str]

TEST_REQUIRES = [
    'boddle',
    'nose'
]

setup(
    name='kafka_selfservice',
    version='0.1',
    packages=find_packages(exclude=("tests", "tests.*")),
    url='',
    license='MIT',
    author='Dheeraj',
    author_email='',
    description='',
    install_requires=INSTALL_REQUIRES,
    test_suite="nose.collector",
    tests_require=TEST_REQUIRES,
    extra_requires={
        'dev': TEST_REQUIRES,
    }
)
