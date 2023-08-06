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

```
long_description=open('readme.md', encoding='utf8').read(),
long_description_content_type='text/markdown',
```
指定long_description字段的内容类型，这里是"text/markdown"，表示使用Markdown格式来书写详细描述

`"Programming Language :: Python :: 3"`表示包适用于Python 3.x版本。

`"Operating System :: OS Independent"`表示包适用于任意操作系统
## package_dir = { '': 'src' }
将包的根目录映射到了名为src的目录。这意味着src目录中的包将被视为根目录下的包。find_packages()函数会自动查找src目录中包含__init__.py文件的子目录，并将这些目录作为包打包。

考虑以下目录结构：
```
diffwave/
    src/
        diffwave/
            __init__.py
            module1.py
            module2.py
    setup.py
    README.md
```
在这个例子中，src/diffwave目录是包的根目录，包含了__init__.py文件和其他模块文件。通过将package_dir = { '': 'src' }指定为setup.py中的参数，setuptools会将src/diffwave目录映射到根目录，并将其中的模块打包进diffwave包中。

这种结构的好处是，将包的源代码放在一个名为src的子目录中，可以保持项目的整洁性和可维护性。同时，可以使包的根目录更加简洁，不包含过多的辅助文件。

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
## 更新上传
修改版本号： 在setup.py文件中修改包的版本号，确保新版本号与之前已上传的版本不同。这样，您可以上传一个新版本的包。

删除重复版本： 如果您确实想重新上传之前已存在的版本，可以先删除PyPI上已上传的相同版本。前往PyPI网站，登录您的账户，找到并删除重复的版本，然后再尝试上传。

删除本地dist目录： 在执行`twine upload dist/*`命令之前，可以先删除本地dist目录中的包文件，然后重新运行上传命令。

 如果您确实想上传一个之前已存在的版本，并且不想删除已上传的包，可以尝试添加--skip-existing选项，如下所示：

`twine upload --skip-existing dist/*`twine将跳过已经存在的文件，而不会尝试覆盖它们。
# 安装使用
pip install shwj==0.1.0 -i https://pypi.Python.org/simple/

主版本号为0通常用于标识一个包的测试版（Pre-Alpha或Alpha版）。在软件开发中，版本号中的主版本号为0时，通常表示该软件还处于早期开发阶段，不稳定，可能存在较大的变动和不向后兼容的改变。

主版本号为0时的常见含义是：

0.x.x：测试版（Pre-Alpha或Alpha版）。表示软件仍在开发中，功能可能不完整，API可能会有较大变动，不适合用于生产环境。
一旦软件开发进入到稳定阶段，特别是在API稳定，功能相对完善，并且通过大规模测试的情况下，一般会将主版本号更新为1，然后进入稳定版本发布。

https://pypi.tuna.tsinghua.edu.cn/packages/cf/19/9a46dff65b7622cd70298823e621ebaaffc35fba636c7e81ac26c67459da/