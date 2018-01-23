
import os
import string 

def alter(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w") as f:
        f.write(file_data)
def rename(pi, pt):
    images = os.listdir(pi)
    i = 9007
    for image in images:
        path = os.path.join(pi, image)
        newname = str(i).zfill(6) + ".jpg"
        newpath = os.path.join(pi, newname)
        os.renames(path, newpath)
        alter(pt, image, newname)
        i += 1
if __name__ == '__main__':
    #图像重命名
    ImagePath = './ExpandedImages'
    FilteredImagePath = './ExpandedImagesFiltered'
    TXTPath = './TXT/output.txt'
    FilteredTXTPath = './TXTFiltered/output.txt'
    # rename(ImagePath, TXTPath)
    rename(FilteredImagePath, FilteredTXTPath)
