# Создание меню и подменю

# MenuBar – для создания панели меню;
# Menu – для создания вкладки меню;
# MenuItem – для создания отдельного пункта.

import wx

APP_EXIT = 1
VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_SRGB = 4

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        
        menubar = wx.MenuBar()
        
        fileMenu = wx.Menu()
        
        # 1
        item = wx.MenuItem(fileMenu, APP_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        fileMenu.Append(item)
        
        # 2
        # fileMenu.Append(APP_EXIT, "Выход", "Выход из приложения")
        
        # item.SetBitmap(wx.Bitmap('картинка.png'))
        
        expMenu = wx.Menu()
        expMenu.Append(wx.ID_ANY, 'Экспорт изображения')
        expMenu.Append(wx.ID_ANY, "Экспорт видео")
        expMenu.Append(wx.ID_ANY, "Экспорт данных")
        
        fileMenu.AppendSeparator()
        fileMenu.Append(wx.ID_NEW, 'Новый\tCtrl+N')
        fileMenu.Append(wx.ID_OPEN, 'Открыть\tCtrl+O')
        fileMenu.Append(wx.ID_SAVE, 'Сохранить\tCtrl+S')
        fileMenu.AppendSubMenu(expMenu, 'Экспорт')
        
        # Модуль wxPython поддерживает четыре типа пуктов:
        # ITEM_NORMAL – обычный текст;
        # ITEM_SEPARATOR – разделитель (сепаратор);
        # ITEM_CHECK – пункт с флажком;
        # ITEM_RADIO – пункт с возможностью перебора.
        viewMenu = wx.Menu()
        self.vStatus = viewMenu.Append(VIEW_STATUS, 'Статусная строка', kind=wx.ITEM_CHECK)
        self.vRgb = viewMenu.Append(VIEW_RGB, 'Тип RGB', kind=wx.ITEM_RADIO)
        self.vSrgb = viewMenu.Append(VIEW_SRGB, 'Тип sRGB', kind=wx.ITEM_RADIO)
        
        
        menubar.Append(fileMenu, '&File')
        menubar.Append(viewMenu, '&View')

        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)
        self.Bind(wx.EVT_MENU, self.onStatus, id=VIEW_STATUS)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_RGB)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_SRGB)
        
    def onStatus(self, event):
        # Используем метод IsChecked(), чтобы определить выбран ли данный пункт. 
        if self.vStatus.IsChecked():
            print('Показать статусную строку')
        else:
            print('Скрыть статусную строку')
            
    def onImageType(self, event):
        if self.vRgb.IsChecked():
            print('Режим RGB')
        elif self.vSrgb.IsChecked():
            print('Режим sRGB')        
        
    def onQuit(self, event):
        self.Close()
        
    
# Bind(event, handler, source=None)

# event – тип события, связанный с определенным интерфейсным объектом;
# handler – ссылка на функцию-обработчик;
# source – источник, генерирующий событие.
# В нашем случае этот метод можно записать так:

# self.Bind(wx.EVT_MENU, self.onQuit, item)
# Мы здесь указали тип события – EVT_MENU, далее, ссылка на метод onQuit, и, наконец, источник – наш пункт меню item. Все, теперь при запуске программы сработает метод onQuit и окно будет закрыто.
        

app = wx.App()

frame = MyFrame(None, title='Урок 4', size=(700, 500))

frame.Show()

app.MainLoop()


        
        