from xml.etree import ElementTree as ET

class TextToHTMLConvert:
    def __init__(self, txt_file, html_file):
        self.txt_file = txt_file
        self.html_file = html_file

    def txt_to_html(self):
    # Read text file content
        with open(self.txt_file, 'r', encoding='utf-8') as f:
            print("reading file")
            content = f.read()
            print(content)
        articles = content.strip().split("\n\n")

    # Extract header and paragraph, since you will be having multiple articles the logic will
    # change for the code given below. 
    # Create root element for HTML, try to remember the structure of a HTML file
        root = ET.Element("html")
    # Create head and body elements, try to understand how subElements works
        head = ET.SubElement(root, "head")
        title = ET.SubElement(head, "title")
        title.text = "My News Aggregation Site"
        body = ET.SubElement(root, "body")

        for article in articles:
            lines = article.strip().split("\n")
            if len(lines) < 2:
                continue
            header = lines[0]
            paragraph = "\n".join(lines[1:])
                # Create header and paragraph elements in body
            article_elem = ET.SubElement(body, "div")
            h1 = ET.SubElement(article_elem, "h1")
            h1.text = header
            p = ET.SubElement(article_elem, "p")
            p.text = paragraph

            # Write HTML tree to file
        with open(self.html_file, 'wb') as f:
            tree = ET.ElementTree(root)
            tree.write(f, encoding='utf-8')
        
        print(f"Converted text file '{self.txt_file}' to HTML file '{self.html_file}'.")