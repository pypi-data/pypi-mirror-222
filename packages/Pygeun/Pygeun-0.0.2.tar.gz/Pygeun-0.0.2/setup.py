from setuptools import setup, find_packages



setup(
    name='Pygeun',
    version='0.0.2',
    description='Pygeun is for convenience',
    author='Daegeun02',
    author_email='redhawkdg02@gmail.com',
    url='https://github.com/Daegeun02/Pygeun.git',
    install_requires=[],
    packages=find_packages( exclude=[] ),
    keywords=['Pygeun', 'by daegeun', 'for convenience'],
    python_requires='>=3.7',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)