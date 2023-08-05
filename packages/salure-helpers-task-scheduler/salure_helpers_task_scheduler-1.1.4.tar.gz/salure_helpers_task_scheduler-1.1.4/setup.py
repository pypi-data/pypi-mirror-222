from setuptools import setup


setup(
    name='salure_helpers_task_scheduler',
    version='1.1.4',
    description='Task Scheduler from Salure',
    long_description='Task Schedule from Salure',
    author='D&A Salure',
    author_email='support@salureconnnect.com',
    packages=["salure_helpers.task_scheduler"],
    license='Salure License',
    install_requires=[
        'salure-helpers-mysql>=1',
        'salure-helpers-salureconnect>=1',
        'salure-helpers-mandrill>=0',
        'salure-helpers-salure_functions>=0',
        'salure-helpers-elastic>=0',
        'pandas>=1,<=1.35',
        'requests>=2,<=3'
    ],
    zip_safe=False,
)