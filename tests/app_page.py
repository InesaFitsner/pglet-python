import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import pglet
from pglet import Page, Text, Button, Stack, Textbox, Checkbox

page = pglet.page("index", no_window = True)

page.clean(force=True)

#page.update(Page(title="Counter"))
page.title = "Counter"
page.update()

txtNum = Textbox(value = '0', align = 'right')

def on_click(e):
    try:
        count = int(page.connection.get_value(txtNum))

        #if we get here the number is int
        #page.send('set number errorMessage=""')

        if e.data == '+':
            page.connection.set_value(txtNum, count + 1)

        elif e.data =='-':
            page.connection.set_value(txtNum, count - 1)

    except ValueError:
        page.connection.send('set number errorMessage="Please enter a number"')

stack = Stack(horizontal = True, controls=[
        Button('-', onclick=on_click, data='-'),
        txtNum,
        Button('+', onclick=on_click, data='+'),
    ])

page.add(stack)

chk = Checkbox("Check it!", id="check1")
page.add(chk)

chk.label = "Check it, again!"
page.update()

stack.controls.pop(0)
page.update()

input("Press Enter to exit...")