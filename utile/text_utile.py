# 定位到标签后面的文本编辑框，传入控件
def set_text(control, input_text):
    siblings = control.parent().children()
    for i, sibling in enumerate(siblings):
        if sibling == control and i < len(siblings) - 1:
            sibling_edit = siblings[i + 1].set_text(input_text)
            return sibling_edit
    return None
