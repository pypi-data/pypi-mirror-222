from setuptools import setup, find_packages

setup(
    name='DdlGeneric',
    version='1.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'DdlGeneric = ddl2pojo.main:main'
        ]
    },
    install_requires=[
        'argparse'
    ],
    author='visonforcoding',
    author_email='visonforcoding@gmail.com',
    description='DDL文件解析程序',
    url='https://gitee.com/visonforcoding/code-template-tools',
    package_data={
        "": ["ddl2pojo.tpl"],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)