from setuptools import setup

abinito_packages = ['abinitostudio',
                    'abinitostudio.calculation',
                    'abinitostudio.io', 
                    'abinitostudio.plot', 
                    'abinitostudio.structure', 
                    'abinitostudio.ui']
abinito_scripts = ['scripts/cal_vasp_single.py']

setup(name="abinitostudio",
    # pypi中的名称，pip或者easy_install安装时使用的名称，或生成egg文件的名称
    version="1.0.1",
    description="A studio for first-principles calculations.",
    long_description="This is a long description.",
    author="Pan Zhou, Xin Lu and Li Zhongsun",
    author_email="zhoupan71234@xtu.edu.cn",
    classifiers=["Development Status :: 3 - Alpha",'Programming Language :: Python',],
    # 需要打包的目录列表
    packages=['abinitostudio',
			  'abinitostudio.calculation',
              'abinitostudio.io', 
              'abinitostudio.plot', 
              'abinitostudio.structure', 
              'abinitostudio.ui'],
    scripts = ['scripts/cal_vasp_single.py'],
    # 需要打包的单文件模块
    py_modules=['appMain','install'],
    # 需要安装的依赖
    install_requires=[
		'paramiko==2.7.1',
		'jumpssh==1.6.5',
		'pyxtal==0.3.0',
		'ase==3.19.1',
		'pymatgen==2020.4.2',
		'traits==6.0.0',
		'traitsui==7.0.0',
		'PyQt5==5.11.2',
		'pyface==6.1.2',
		'envisage==4.9.2',
		'vtk==8.1.2',
		'mayavi==4.7.1',
    ]
    # # 安装过程中，需要安装的静态文件，如配置文件、service文件、图片等
    # data_files=[
    #     ('', ['conf/*.conf']),
    #     ('/usr/lib/systemd/system/', ['bin/*.service']),
    # ],
    # # 希望被打包的文件
    # package_data={
    #     '': ['*.txt']
    # },
    # # 该文件入口指向 foo/main.py 的main 函数
    # entry_points={
    #     'console_scripts': ['foo = foo.main:main']
    # }
)
