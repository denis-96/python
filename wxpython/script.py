import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super().__init__(parent, title=title, size=size)
        
        menubar = wx.MenuBar()
        
        menu1 = wx.Menu()
        menu1.Append(1, 'One', kind=wx.ITEM_RADIO)
        menu1.Append(2, 'Two', kind=wx.ITEM_RADIO)
        menu1.Append(3, 'Three', kind=wx.ITEM_RADIO)
        
        menu2 = wx.Menu()
        menu2.Append(4, 'Four', kind=wx.ITEM_CHECK)
        menu2.Append(5, 'Five', kind=wx.ITEM_CHECK)
        menu2.Append(6, 'Six', kind=wx.ITEM_CHECK)
        
        menu3 = wx.Menu()
        menu3.Append(7, 'Seven')
        menu3.Append(8, 'Eight')
        
        exitMenu = wx.Menu()
        exitMenu.Append(9, 'Exit')
        
                
        menubar.Append(menu1, 'Один')
        menubar.Append(menu2, 'Два')
        menubar.Append(menu3, 'Три')
        menubar.Append(exitMenu, 'Выход')
        
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.onQuit, id=9)
        
    def onQuit(self, event):
        self.Close()
        
        
app = wx.App()

frame = MyFrame(None, title='Тестовое окно', size=(800, 500))
frame.Center()
frame.Show()

app.MainLoop()