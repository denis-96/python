# Общая структура интерфейса

# Вверху каждого окна под заголовком можно размещать меню.
# Для этого сначала создается панель MenuBar, затем идут вкладки меню (Menu) и далее, создаются пункты меню (MenuItem) в каждой из вкладок.

# Под меню можно располагать одну или несколько панелей инструментов. Они создаются с помощью специального метода окна:
# CreateToolBar()

# Затем, в окне располагаются отдельные элементы интерфейса: тексты, поля ввода, кнопки, списки и т.п. Они называются виджетами.
# Располагаться они могут непосредственно в окне, но обычно формируют, так называемый, Layout (схему), в который помещают элементы интерфейса.

# Механизм под общим названием Layout в wxPython реализуется с использованием панелей и сайзеров:
# Panel, Sizers: (BoxSizer, WrapSizer, GridSizer, FlexGridSizer, GridBagSizer)

# Наконец, в самом низу окна можно создавать статусную строку с помощью виджета StatusBar.

# Чтобы мы могли модифицировать класс Frame удобнее создать свой собственный наследуя его от базового Frame, например, вот так:

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        
# Мы здесь объявляем свой конструктор с двумя параметрами: parent и title и, затем, внутри него вызываем конструктор базового класса, используя функцию super().
# Далее, по программе, мы можем использовать наш класс следующим образом:

app = wx.App()
 
wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()

# Конечно, класс Frame – это лишь один из представителей оконных классов. В wxPython их шесть и они следующие:

# PopupWindow – специальный оконный класс для создания popup меню, списков combobox и других вспомогательных виджетов подобного рода;
# ScrolledWindow – используется для создания окна с прокручиваемым содержимым;
# Frame – используется для создания стандартного окна;
# MDIParentFrame (Multiple Document Interface) – класс, содержащий дочерние оконные классы (как пример, Photoshop со множеством открытых документов);
# MDIChildFrame – создает окно внутри класса MDIParentFrame;
# Dialog – создает диалоговое окно.

# Например, заменим стандартное окно Frame на MDIParentFrame:
class MyFrame(wx.MDIParentFrame ):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title)
        
        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)
 
        win = wx.MDIChildFrame(self, -1, "Child Window", size=(200, 150))
        win.Show()
        
# Далее, при создании Layout помимо класса Panel можно использовать еще такие контейнеры для виджетов:

# ScrolledWindow – контейнер с прокручиваемым содержимым;
# SplitterWindow – контейнер с разделительной полосой, которую можно перемещать, изменяя размеры соответствующих содержимых;
# Notebook – используется для создания tab-интерфейса (панель со вкладками).
# Ну а базовый набор виджетов определяется такими классами:

# - для динамических (т.е. их содержимое может меняться):

# Button – обычная кнопка;
# BitmapButton – кнопка с картинкой;
# ToggleButton – кнопка переключатель;
# SpinButton – стрелочки вверх/вниз;
# RadioButton – радио-кнопка (кружочек с точкой);
# CheckBox – чекбокс (флажок);
# TextCtrl – поле ввода текста;
# SpinCtrl – поле ввода со стрелочками вверх/вниз;
# ComboBox – выпадающий список с возможностью ввода значения;
# Choice – выпадающий список только с возможностью выбора;
# Slider – бегунок;
# ScrollBar – скроллинг;
# Grid – таблица (наподобие Excel);
# RadioBox – контейнер для RadioButton;
# ListBox – список.

# - для статических:

# StaticBitmap – для статических изображений;
# StaticBox – квадратная рамка;
# Gauge – прогресс-бар;
# StaticText – простой текст;
# StaticLine – линия.