"""向网页内注入css,js和button中的data-snippets属性
"""
from bs4 import BeautifulSoup
import os

def embed_resources(html_file, outfilename):
    # 读取HTML文件
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')

    # 查找并处理CSS链接
    for link in soup.find_all('link', rel='stylesheet'):
        css_path = link['href']
        if not css_path.startswith(('http:', 'https:')):
            with open(os.path.join(os.path.dirname(html_file), css_path), 'r',
                      encoding='utf-8') as css_file:
                css_content = css_file.read()
                style_tag = soup.new_tag('style', type='text/css')
                style_tag.string = css_content
                link.replace_with(style_tag)

    # 查找并处理JS脚本
    for script in soup.find_all('script', src=True):
        js_path = script['src']
        if not js_path.startswith(('http:', 'https:')):
            with open(os.path.join(os.path.dirname(html_file), js_path), 'r',
                      encoding='utf-8') as js_file:
                js_content = js_file.read()
                new_script_tag = soup.new_tag('script', type='text/javascript')
                new_script_tag.string = js_content
                script.replace_with(new_script_tag)

    # 在按钮嵌入代码      
    for button in soup.find_all('button', attrs={'dir': True}):
        # 提取文件路径
        file_path = button['dir'] + "/" + button['id'] + ".txt"
        with open(os.path.join(os.path.dirname(html_file), file_path), 'r',
                  encoding='utf-8') as file:
            file_content = file.read()
            button['data-snippets'] = file_content 
            button['data-comment'] = file_content
            print(f"\tOK: {button['id']}")

        try:
            file_path = button['dir'] + "/" + button['id'] + ".comment.txt"
            with open(os.path.join(os.path.dirname(html_file), file_path), 'r',
                      encoding='utf-8') as file:
                file_content = file.read()
                button['data-comment'] = file_content
        except FileExistsError:
            pass
        except FileNotFoundError:
            pass

    # 写回修改后的HTML
    with open(outfilename, 'w', encoding='utf-8') as file:
        file.write(str(soup.prettify()))


inputfilename = './snippets.html'
outfilename = './snippets_embed.html'
embed_resources(inputfilename, outfilename)
print(f"DONE:\t\t\t{inputfilename} -> {outfilename}")


