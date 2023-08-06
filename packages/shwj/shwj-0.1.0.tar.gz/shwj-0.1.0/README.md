# 如何使用pypi
然后，
# setup.py
classifiers字段是一个元数据字段，用于定义您的Python包的分类信息。这些信息将在您将包上传到PyPI时用于分类和标记您的包。
Development Status:
```
3 - Alpha
4 - Beta
5 - Production/Stable
```
Intended Audience:
```
Developers
Science/Research
Education
```
License:
```
MIT License
Apache Software License
GNU General Public License v3 (GPLv3)
```
Programming Language:
```
Python :: 3
Python :: 3.6
Python :: 3.7
Python :: 3.8
```
# 项目
项目的目录大概为
```
your-package-name/
    package/
        __init__.py
        module1.py
        module2.py
    setup.py
    README.md
```

__init__.py是一个特殊的Python文件，用于标识一个目录是一个Python包。当Python解释器遇到包含__init__.py文件的目录时，它会将该目录视为一个包，并且可以通过包名来访问其中的模块和子包

__init__.py文件可以包含Python代码，用于初始化包的内容。这些代码在导入包时会被执行，并且可以用于设置包的初始状态、导入子模块或定义一些包级别的变量或函数。

# LICENSE
https://choosealicense.com/

# 构建 上传
```
python setup.py sdist bdist_wheel
```
这将在dist文件夹下生成一个.tar.gz源代码包和一个.whl二进制包。

使用twine上传包：
```
twine upload dist/*
```
twine将会提示您输入PyPI账户的用户名和密码。

```
twine upload dist/* --verbose
```
添加了--verbose选项后，twine将输出上传过程中的详细信息，包括上传的进度、服务器响应以及可能发生的错误信息。