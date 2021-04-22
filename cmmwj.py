import PySimpleGUI as sg
import os
sg.theme('Dark Brown')
layout = [
    [sg.Text('文件名前缀', size=(15, 1), justification='center'), sg.InputText(key="pre_str")],
    [sg.Text('文件名起始编码', size=(15, 1), justification='center'), sg.InputText(key="no")],
    [sg.Text('文件位置', size=(15, 1), justification='center'), sg.InputText(key="file_path"), sg.FolderBrowse(button_text='浏览..')],
    [sg.Submit(button_text='重命名', key='Submit'), sg.Cancel(button_text='取消', key='Cancel')]]

window = sg.Window('批量修改文件名', layout, default_element_size=(30, 1), font='微软雅黑')

while True:
    event, values = window.read()
    if event == "Submit":
        img_path = values["file_path"]
        list01 = os.listdir(img_path)  # 遍历选择的文件夹
        num = values["no"]  # 文件起始编号
        pre_str = values["pre_str"]  # 文件名前缀

        for fileName in list01:
            imgType = os.path.splitext(fileName)[1]  # 获取文件名后缀，即为文件格式
            os.chdir(img_path)  # 将当前工作目录修改为待修改文件夹的位置
            # os.rename(fileName, (img_path + "\\" + str(num) + imgType))
            new_file_name = pre_str + str(num) + imgType
            os.rename(fileName, new_file_name)  # 命名规则可以根据自己需要组合和扩展
            num = int(num) + 1  # 编号递增
        sg.Popup("完成")

    if event == "Cancel" or event == sg.WIN_CLOSED:
        break