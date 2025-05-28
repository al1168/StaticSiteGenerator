from markdown_blocks import markdown_to_html_node
import os

def extract_title(markdown: str):
    if not markdown.startswith("# "):
        raise Exception("This is not a h1 tag")
    lines = markdown.split("\n")
    heading_text = lines[0].lstrip("# ").strip()
    return heading_text


def generate_html_page(from_path, template_path, dest_path):
    dest_path = dest_path.replace(".md", ".html")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open (from_path) as file:
        content = file.read()
    # print(content)
    with open(template_path) as file:
        template_content = file.read()

    html_node = markdown_to_html_node(content)
    title = extract_title(content)
    html_string = html_node.to_html()
    final_html = template_content.replace("{{ Content }}", html_string)
    final_html = final_html.replace("{{ Title }}",title)
    a = dest_path.split("/")[:-1]
    curr = ""
    for part in a:
        curr += part + "/"
        if not os.path.exists(curr):
            os.mkdir(curr)
    with open(dest_path, "w") as file:
        file.write(final_html)
# generate_page("content/index.md", "template.html", "outer/inner/inner2/final.html")

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):

    items = os.listdir(dir_path_content)
    SRC_BASE_FOLDER = dir_path_content
    DEST_BASE_FOLDER = dest_dir_path
    for item in items:
        src_curr_item_path = os.path.join(SRC_BASE_FOLDER, item)
        dest_curr_item_path = os.path.join(DEST_BASE_FOLDER,item)
        if os.path.isfile(src_curr_item_path):
            generate_html_page(src_curr_item_path, template_path, dest_curr_item_path)
        elif os.path.isdir(src_curr_item_path):
            generate_page_recursive(src_curr_item_path, template_path, dest_curr_item_path)
    
        
