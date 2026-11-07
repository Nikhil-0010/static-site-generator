from markdown_blocks import markdown_to_html_node, extract_title
import os

def generate_page(from_path, template_path, dest_path, basepath='/'):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    md_content =""
    with open(from_path, 'r') as file:
        md_content = file.read()
    template_content  = ""
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    html_content = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)
    
    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    full_html = full_html.replace('href="/"',f'href="{basepath}"')
    full_html = full_html.replace('src="/"',f'src="{basepath}"')
    
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, 'w', encoding="utf-8") as file:
        file.write(full_html)
    
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        
        if os.path.isdir(src_path):
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(src_path, template_path, dest_path, basepath)
        elif os.path.isfile(src_path) and dest_path.endswith(".md"):
            dest_html_path = dest_path.replace(".md",".html")
            generate_page(src_path, template_path, dest_html_path, basepath)