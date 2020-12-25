from selenium import webdriver
# 内网本地测试环境
Intranet_url = "https://httpswww.msyk.cn/"
Local_filepaths = [r'D:\BAK_JF\WP\素材\picture\jpg\01.jpg', r'D:\BAK_JF\WP\素材\音频\different\林俊杰 - 将故事写成我们.mp3',
                   r'D:\BAK_JF\WP\素材\视频\NASA打造太空GPS导航_标清.mp4', r'D:\BAK_JF\WP\素材\PDF\真\P0209C-数学理(1).pdf',
                   r'D:\BAK_JF\WP\素材\题目\综合5-单、多、填、解.docx', r'D:\BAK_JF\WP\素材\ppt\模板19.pptx',
                   r'D:\BAK_JF\WP\素材\视频\666.mp4']
Local_sck_filepaths = [r'D:\BAK_JF\WP\素材\picture\jpg\01.jpg', r'D:\BAK_JF\WP\素材\音频\different\林俊杰 - 将故事写成我们.mp3',
                       r'D:\BAK_JF\WP\素材\视频\NASA打造太空GPS导航_标清.mp4', r'D:\BAK_JF\WP\素材\PDF\真\P0209C-数学理(1).pdf',
                       r'D:\BAK_JF\WP\素材\ppt\模板19.pptx', r'D:\BAK_JF\WP\素材\ppt\模板27.pptx',
                       r'D:\BAK_JF\WP\素材\ppt\各种字体.pptx', r'D:\BAK_JF\WP\素材\ppt\优质.pptx',
                       r'D:\BAK_JF\WP\素材\题目\综合5-单、多、填、解.docx', r'D:\BAK_JF\WP\素材\文档\2017年高中物理：电学实验.docx']
Local_bk_filepaths = [r'D:\BAK_JF\WP\素材\picture\jpg\01.jpg', r'D:\BAK_JF\WP\素材\BUG编写规范.txt',
                      r'D:\BAK_JF\WP\素材\PDF\真\P0209C-数学理(1).pdf']
# 外网非本地测试环境
Extranet_url = "https://www.msyk.cn/"
UN_filepaths = [r'C:\Users\test\Desktop\素材\01.jpg', r'C:\Users\test\Desktop\素材\林俊杰 - 将故事写成我们.mp3',
                r'C:\Users\test\Desktop\素材\NASA打造太空GPS导航_标清.mp4', r'C:\Users\test\Desktop\素材\P0209C-数学理(1).pdf',
                r'C:\Users\test\Desktop\素材\综合5-单、多、填、解.docx', r'C:\Users\test\Desktop\素材\模板19.pptx',
                r'C:\Users\test\Desktop\素材\666.mp4']
UN_sck_filepaths = [r'C:\Users\test\Desktop\素材\01.jpg', r'C:\Users\test\Desktop\素材\林俊杰 - 将故事写成我们.mp3',
                    r'C:\Users\test\Desktop\素材\NASA打造太空GPS导航_标清.mp4', r'C:\Users\test\Desktop\素材\P0209C-数学理(1).pdf',
                    r'C:\Users\test\Desktop\素材\模板19.pptx', r'C:\Users\test\Desktop\素材\模板27.pptx',
                    r'C:\Users\test\Desktop\素材\各种字体.pptx', r'C:\Users\test\Desktop\素材\优质.pptx',
                    r'C:\Users\test\Desktop\素材\综合5-单、多、填、解.docx', r'C:\Users\test\Desktop\素材\2017年高中物理：电学实验.docx']
UN_bk_filepaths = [r'C:\Users\test\Desktop\素材\01.jpg', r'C:\Users\test\Desktop\素材\BUG编写规范.txt',
                   r'C:\Users\test\Desktop\素材\P0209C-数学理(1).pdf']