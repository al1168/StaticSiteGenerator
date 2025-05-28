# import generate_page
from generate_page import generate_page_recursive, generate_html_page
from generate_public import copy_static_files_to_public
# from textnode import TextNode, TextType
def main():
    # generate_page()
    copy_static_files_to_public()
    # generate_html_page("content/index.md", "template.html","public/index.html")
    # a = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    generate_page_recursive("content","template.html", "public")
main()