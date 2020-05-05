　　Cython是一个快速生成Python扩展模块的工具，从语法层面上来讲是Python语法和C语言语法的混血，当Python性能遇到瓶颈时，Cython直接将C的原生速度植入Python程序，这样使Python程序无需使用C重写，能快速整合原有的Python程序，这样使得开发效率和执行效率都有很大的提高，而这些中间的部分，都是Cython帮我们做了，接下来简单说一下Cython的安装和使用方法

　　一、首先Cython官网地址是：http://cython.org/ 这里有cython的安装和开发文档，关于Cython的下载可以在pypi上直接下载安装包：https://pypi.python.org/pypi/Cython/ 由于是在Linux下安装使用，这里下载的是Cython-0.25.2.tar.gz，上传至linux执行如下步骤安装：

tar -xvzf Cython-0.25.2.tar.gz
cd Cython-0.25.2
python setup.py install
　　这样Cython模块就安装成功了

　　然后我们首先看一下cython的基本使用，首先 mkdir hello_pack && cd hello_pack 建立一个目录并且进入，然后编写一个hello.pyx的脚本，代码如下：

# coding=utf-8
def print_hello(name):
    print "Hello %s!" % name
　　代码很简单，就是一个函数，然后编写一个setup.py，代码如下：

复制代码
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [Extension("hello",["hello.pyx"])]
setup(
    name = "Hello pyx",
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
复制代码
　　这里导入了Cython的模块，其中setup name指定模块的名称，然后执行编译命令：

python setup.py build_ext --inplace
　　编译完之后，看到当前目录下会生成两个文件，一个是hello.c一个是hello.so，hello.c就是转换而成的c代码，而hello.so就是我们需要的python经过Cython编译之后的模块，我们为了当前目录可被调用，建立__init__.py内容如下：

# coding=utf-8
from hello import *
　　然后执行 cd .. 回到上层目录，建立一个hello.py，代码如下：

#!/usr/bin/python
# coding=utf-8
from hello_pack import hello
hello.print_hello("cython")
　　很简单，就是调用我们编译好的hello模块，然后执行里面的方法，现在直接执行hello.py，看到输出结果正常

　　

 

　　那么现在，我们就完成了Cython的基本使用，其实setup.py编译脚本也可以写成如下这样：

from distutils.core import setup
from Cython.Build import cythonize
setup(
    name='Hello pyx',
    ext_modules=cythonize('hello.pyx')
)
　　这种写法更通用，编译的时候直接使用 python setup.py build 就可以了，注意不是install，执行install后会把模块复制到python系统目录下了；

　　执行完之后，会看到当前目录有一个build目录，然后进去会发现有如下两个目录：

　　

　　第二个temp是编译过程中汇编生成的.o文件，第一个lib开头的目录中存放的就是hello.so文件，直接把这个文件拷贝出来就可以使用了，另外为了方便，运行脚本直接和so文件放在一个目录下就可以，直接使用import hello即可导入，也不用建立__init__.py了


https://www.cnblogs.com/freeweb/p/6548208.html