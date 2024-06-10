import requests
import fitz  # 导入PyMuPDF
import os
import fnmatch

def download_pdf_from_url(url):
    """
    从指定的URL下载PDF文件并保存到指定路径。
    
    参数:
    url (str): PDF文件的在线URL。
    save_path (str): 下载后保存的本地路径。
    """

    save_path="./tmp.pdf"
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"PDF downloaded successfully from {url}.")
    else:
        print(f"Failed to download PDF from {url}.")
    get_first_line_and_rename(save_path)

def get_first_line_and_rename(pdf_path):
    """
    从指定路径的PDF文件中读取第一页的第一行文本。
    
    参数:
    pdf_path (str): PDF文件的路径。
    
    返回:
    str: 第一页的第一行文本，如果找不到，则返回None。
    """
    try:
        doc = fitz.open(pdf_path)  # 打开PDF文件
        page = doc[0]  # 获取第一页
        
        # 初始化变量用于存储第一行的文本
        first_line = ""
        
        # 遍历页面上的所有文本块
        for block in page.get_text("blocks"):
            x0, y0, x1, y1, text, block_type, block_no = block
            
            # 如果这是一个新的段落或文本块，更新第一行的开始位置
            if block_type == 0:  # 0表示新的一段文字开始
                first_line = text
                break  # 找到了第一行，就跳出循环
        rename_file(first_line,pdf_path)
    except Exception as e:
        print(f"Error reading PDF: {e}")

def rename_file(first_line,pdf_path):
    new_filename = f"{first_line}.pdf"
    # 构建新文件的路径
    new_file_path = pdf_path.replace(pdf_path.split('/')[-1], new_filename)
    os.rename(pdf_path,new_file_path)
    print(f"Renamed '{pdf_path}' to '{new_file_path}'.")

def find_pdfs(directory):
    """
    查找指定目录及其子目录下的所有PDF文件。
    
    参数:
    directory (str): 要搜索的目录路径。
    
    返回:
    list: 包含所有PDF文件的路径列表。
    """
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, '*.pdf'):
                filename = os.path.join(root, basename)
                pdf_files.append(filename)
    return pdf_files
# 测试使用
# pdf_url = "https://arxiv.org/pdf/2403.02183"
# pdf_path = "./tmp.pdf"
# download_pdf_from_url(pdf_url, pdf_path)
# first_line = get_first_line(pdf_path)
# if first_line:
#    print(f"The first line of the document is: {first_line}")
# else:
#    print("Could not find the first line in the document.")
# rename_file(first_line)

