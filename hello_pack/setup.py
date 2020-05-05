# from distutils.core import setup
# from distutils.extension import Extension
# from Cython.Distutils import build_ext
# ext_modules = [Extension("hello",["hello.pyx"])]
# setup(
#     name = "Hello pyx",
#     cmdclass = {'build_ext': build_ext},
#     ext_modules = ext_modules
# )

from distutils.core import setup
from Cython.Build import cythonize
setup(
    name='Hello pyx',
    ext_modules=cythonize('hello.pyx')
)


# 编译
# https://www.cnblogs.com/freeweb/p/6548208.html
# python setup.py build