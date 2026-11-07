from textnode import TextNode, TextType
import os
import shutil
from generate_page import generate_pages_recursive
import sys

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    source_to_dest("static", "public")
    generate_pages_recursive("content","template.html","public", basepath)

def source_to_dest(source="static",dest="public"):
    if not os.path.exists(source):
        raise Exception("source not exist")
    if os.path.exists(dest):
        print(f"Cleaning destination directory: {dest}")
        shutil.rmtree(dest)
    
    os.makedirs(dest)
    rec_copy(source,dest)
    return

def rec_copy(src,dst):
    for item in os.listdir(src):
        src_path = os.path.join(src,item)
        dst_path = os.path.join(dst, item)
        
        if os.path.isdir(src_path):
            os.makedirs(dst_path, exist_ok=True)
            rec_copy(src_path, dst_path)
        else:
            shutil.copy(src_path, dst_path)
            print(f"Copied: {src_path} -> {dst_path}")
main()