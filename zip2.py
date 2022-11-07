import os
import zipfile
#批量压缩脚本 (当前目录每五个文件压缩为一个压缩包)

print("[*] 欢迎Sword压缩脚本")
print("============功能面板==============")
print("1. 查看当前目录所有压缩文件")
print("2. 开启压缩")



filelist = []
filePath = './'
filenames = os.listdir(filePath)
def zip_files(files, zip_name):
    zip = zipfile.ZipFile( zip_name, 'w', zipfile.ZIP_DEFLATED )
    for file in files:
        print ('compressing', file)
        zip.write( file )
    zip.close()
    print ('compressing finished')
flag = int(input("请输入你的选项:"))

if (flag == 1):
    for fname in filenames:
        if '.zip' in fname and 'baiyun' in fname:
            print(fname)
    exit(1)

l = filenames
n = 5  #大列表中几个数据组成一个小列表
lists = [l[i:i + n] for i in range(0, len(l), n)]
for index,li in enumerate(lists, start=1):
    zip_file = '.\\baiyun%s.zip'%index
    zip_files(li, zip_file)



# files = ['.\\1.py','.\\23007-1662646271.doc']  # 文件的位置，多个文件用“，”隔开
# zip_file = '.\\m66y.zip'           # 压缩包名字
# zip_files(files, zip_file)