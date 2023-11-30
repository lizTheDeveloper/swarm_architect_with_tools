# Python function to parse markdown files
import markdown
from bs4 import BeautifulSoup

def parse_markdown(file_path):
    with open(file_path, 'r') as md_file:
        md_content = md_file.read()

    html = markdown.markdown(md_content)
    soup = BeautifulSoup(html, 'html.parser')

    # Extract sections and content
    sections = {}
    for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        section = header.get_text()
        content = ''
        for sibling in header.next_siblings:
            if sibling.name and sibling.name.startswith('h'):
                break
            content += str(sibling)
        sections[section] = content

    return sections
