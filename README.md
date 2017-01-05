# create-icon-for-ios
1 依赖模块安装

命令行可以直接输入pip验证是否已经安装。
 
若是pip没有安装，可以使用命令sudo easy_install pip

安装pip之后， 先把multiprocessing模块安装好，sudo pip install multiprocessing即可正常安装，非常小的一个模块

执行sudo pip install Pillow

2 工具使用
将需要处理的应用图标文件拷贝至image目录下，并命名为icon.png
执行python文件（用命令python iconSize.py）完成后，ios发布应用所需要的各种尺寸的图标将输出到imag目录下
如果需要修改或增删应用图标尺寸，请修改size.json文件
