'''Write a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)

    It should first delete all the contents of the destination directory (public) to ensure that the copy is clean.
    It should copy all files and subdirectories, nested files, etc.
    I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code.

'''
import os
import shutil

def copy_static_files_to_public():
    PUBLIC_STRING = "public"
    STATIC_STRING = "static"
    def recursive_copy_file(src_path):
        public_path = os.path.join(PUBLIC_STRING, src_path)
        static_path = os.path.join(STATIC_STRING, src_path)
        items = os.listdir(static_path) 
        for item in items:
            static_item_path = os.path.join(static_path, item)
            joined_public_path = os.path.join(public_path, item)
            if os.path.exists(static_item_path):
                if os.path.isfile(static_item_path):
                    shutil.copy(static_item_path, joined_public_path)
                    continue
                
                if os.path.isdir(static_item_path):
                    if not os.path.exists(joined_public_path):
                        
                        os.mkdir(joined_public_path)
                        recursive_copy_file(os.path.join(src_path, item))
                    
    if os.path.exists("public"):
        shutil.rmtree("public")
    src_path = "static"
    if not os.path.exists("public"):
        os.mkdir("public")
    items = os.listdir(src_path)
    for item in items: 
        public_path = os.path.join(PUBLIC_STRING, item)
        static_path = os.path.join(STATIC_STRING, item)
        if not os.path.exists(public_path): 
            if os.path.isfile(static_path):
                shutil.copy(static_path, public_path)
                continue
            elif os.path.isdir(static_path):
                os.mkdir(public_path)
                recursive_copy_file(item)
            
    
copy_static_files_to_public()