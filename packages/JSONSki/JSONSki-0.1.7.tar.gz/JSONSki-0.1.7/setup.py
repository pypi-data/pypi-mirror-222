from setuptools import setup, Extension

# Extension module
JSONSKi_module = Extension(
    'JSONSki',
    sources=['./example_python/example1.cpp','/example_python',],
    include_dirs=['./example_python/pybind11-master/include','./src','../src', '../src/..','/src','src','example_python','/example_python'],
     extra_compile_args=['-mavx', '-mavx2', '-mpclmul','-std=c++11']  
)

# JSONSKi_module = Extension(
#     'JSONSki',
#     sources=['example1.cpp'],
#     include_dirs=['../example_python/pybind11-master/include','../src', '../src/..'],
#      extra_compile_args=['-mavx', '-mavx2', '-mpclmul','-std=c++11']  
# )

AUTHOR = 'AutomataLab'

AUTHOR_EMAILS = 'zhijia@cs.ucr.edu'


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Package information
setup(
    name='JSONSki',
    version='0.1.07',
    author= AUTHOR,
    author_email= AUTHOR_EMAILS,
    description='JSONSki_Python is the Python binding port for JSONSki',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/your_repository',
    ext_modules=[JSONSKi_module],
    zip_safe=False,
)