from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Tair vector database with Haystack'
LONG_DESCRIPTION = 'An new integration of Tair vector database TairVector with Haystack by deepset.'

# 配置
setup(
    # 名称必须匹配文件名 'tairhaystack'
    name="tairhaystack",
    version=VERSION,
    author="Zhidong Tan",
    author_email="<2741986499@email.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['haystack', 'tair'], # add any additional packages that
    # 需要和你的包一起安装，例如：'caer'

    keywords=['tair', 'haystack'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)