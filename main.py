import win32gui
import win32ui
import win32api
import win32con
import time
import uuid
from PIL import Image
import os
import ocr

hWnd = win32gui.FindWindow(None, 'easycode-javascript')
print(hWnd)
# 将窗口置顶
win32gui.SetForegroundWindow(hWnd)
time.sleep(1)


def screenshot(hWnd, pos):
    """
      截图的工具方法
      Args:
        hWnd: 窗口句柄
        pos: 保存的文件夹地址
      Returns:
        文件的最后位置
    """
    # 获取窗体坐标
    width = 83
    height = 35
    # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(hWnd)
    # 创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    # 创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # 将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    # 保存bitmap到内存设备描述表
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)
    filePos = os.path.abspath(os.path.join(pos, str(uuid.uuid1()) + '.jpg'))
    print(filePos)
    saveBitMap.SaveBitmapFile(saveDC, filePos)
    return filePos


def pil_image_similarity(filepath1, filepath2):
    """
      图片相似度计算
    """


pic = screenshot(hWnd, 'image')
AK = "o2dmI91tLrpKif98uIhzbVfU"  # 官网获取的AK
SK = "t1z52AuDgqCZxB1Il6WaiyVbGr3kRGPT"  # 官网获取的SK
code_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"  # 百度图片识别接口地址
code_obj = ocr.BaiduOCR(
    AK=AK, SK=SK, code_url=code_url, img_path=pic)
res = code_obj.getCode()
print(res)
code = res.get("words_result")[0].get("words")
print(code)
