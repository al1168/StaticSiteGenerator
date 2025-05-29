from generate_page import generate_page_recursive, generate_html_page
from generate_public import copy_static_files_to_public
import sys
def main():
    BASEPATH = sys.argv[1] if len(sys.argv) >= 2 else "/"
    print(BASEPATH)
    copy_static_files_to_public("static", "docs")
    # generate_html_page("content/index.md", "template.html","public/index.html")
    generate_page_recursive("content","template.html", "docs", BASEPATH)
main()