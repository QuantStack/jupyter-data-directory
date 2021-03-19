import os
from setuptools import find_packages, setup

setup(
    name='jupyter-data-directory',
    version='0.0.1',
    license='3-clause BSD',
    author='Madhur Tandon',
    author_email='madhur.tandon@quantstack.net',
    description='Notebook Server Extension to serve a data directory',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=['tornado'],
    data_files=[
        ('etc/jupyter/jupyter_notebook_config.d', ['etc/jupyter/jupyter_notebook_config.d/jupyter-data-directory.json']),
        ('etc/jupyter/jupyter_server_config.d', ['etc/jupyter/jupyter_server_config.d/jupyter-data-directory.json']),
        ('etc/jupyter', ['etc/jupyter/jupyter-data-directory.json']),
        ('share/jupyter/data-directory', ['share/jupyter/data-directory/example.md', 'share/jupyter/data-directory/jupyter-logo.png'])
    ],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)
