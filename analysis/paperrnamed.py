import argparse
import analysis
from itertools import groupby

def main():
    parser = argparse.ArgumentParser(description='This is a sample tool to rename your paper.')
    
    # 添加可选的参数
    parser.add_argument('-f', '--filename', type=str, default=None,help='Input file name')
    parser.add_argument('-d', '--dirname', type=str, default=None, help='Input dir name')
    parser.add_argument('-u', '--url', type=str, default=None, help='Input url')
    # 解析命令行参数
    args = parser.parse_args()
    # 检查参数是否为空
    if args.filename == None and args.dirname == None and args.url == None:
        print("Please provide one parameter. Using -h to see the help")
        return
    #开始解析
    if(args.filename != None):
        analysis.get_first_line_and_rename(args.filename)
        return
    if(args.dirname != None):
        pdf_files = analysis.find_pdfs(args.dirname)
        for pdf in pdf_files:
            analysis.get_first_line_and_rename(pdf)
        return
    if(args.url != None):
        analysis.download_pdf_from_url(args.url)
        return


if __name__ == "__main__":
    main()
