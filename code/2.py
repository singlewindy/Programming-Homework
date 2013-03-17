# coding=utf-8
import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

x = []
rst = []
rst_A = []
rst_B = []
A_array = []
B_array = []

def myplot(axes, array, title):
	for i in xrange(len(x)):
		axes.axhline(array[i], xmin = float(x[i]) / len(x), xmax = float(x[i] + 1) / len(x), linewidth = 3)
		if i < len(x) - 1:
			if array[i] != array[i+1]:
				axes.axvline(i + 1, 0, 1, linewidth = 5)

	axes.axis([0, len(x), 0, 1])
	axes.set_title(title)


class CanvasFrame(wx.Frame):
    def __init__(self):
    	global x
        wx.Frame.__init__(self,None,-1,
                         'CanvasFrame',size=(550,350))

        
        figure = Figure()
        x = range(len(rst))
        axes = figure.add_subplot(3,1,1)
        myplot(axes, A_array, 'A')

        axes = figure.add_subplot(3,1,2)
        myplot(axes, B_array, 'B')

        axes = figure.add_subplot(3,1,3)
        myplot(axes, rst, 'OUTPUT')

        self.canvas = FigureCanvas(self, -1, figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

class CanvasFrame_NOT(wx.Frame):
    def __init__(self):
    	global x
        wx.Frame.__init__(self,None,-1,
                         'CanvasFrame',size=(550,350))

        
        figure = Figure()
        x = range(len(rst_A))
        axes = figure.add_subplot(4,1,1)
        myplot(axes, A_array, 'A')

        axes = figure.add_subplot(4,1,2)
        myplot(axes, B_array, 'B')

        axes = figure.add_subplot(4,1,3)
        myplot(axes,rst_A, 'OUTPUT_A')

        axes = figure.add_subplot(4,1,4)
        myplot(axes, rst_B, 'OUTPUT_B')

        self.canvas = FigureCanvas(self, -1, figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

class Calc(wx.Frame):

	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Calculator', size = (300, 200))
		self.panel = wx.Panel(self, -1)

		self.A_lable = wx.StaticText(self.panel, -1, "A:", pos = (70, 10), size = (100, -1))
		self.A_text = wx.TextCtrl(self.panel, -1, "", pos = (100, 10), size=(100, -1))

		self.A_text.SetInsertionPoint(0)

		self.B_lable = wx.StaticText(self.panel, -1, "B:", pos = (70, 70))
		self.B_text = wx.TextCtrl(self.panel, -1, "", pos = (100, 70), size=(100, -1))

		button_add = wx.Button(self.panel, label = u'与', pos = (5, 120), size = (30, 30))
		button_or = wx.Button(self.panel, label = u'或', pos = (65, 120), size = (30, 30))
		button_not = wx.Button(self.panel, label = u'非', pos = (125, 120), size = (30, 30))
		button_add_not = wx.Button(self.panel, label = u'同或', pos = (185, 120), size = (30, 30))
		button_or_not = wx.Button(self.panel, label = u'异或', pos = (245, 120), size = (30, 30))

		self.Bind(wx.EVT_BUTTON, self.add_result, button_add)
		self.Bind(wx.EVT_BUTTON, self.or_result, button_or)
		self.Bind(wx.EVT_BUTTON, self.not_result, button_not)
		self.Bind(wx.EVT_BUTTON, self.add_not_result, button_add_not)
		self.Bind(wx.EVT_BUTTON, self.or_not_result, button_or_not)

	def add_result(self, event):
		global rst, A_array, B_array
		A = self.A_text.GetValue()
		B = self.B_text.GetValue()
		rst = []
		for i in xrange(len(A)):
			if int(A[i]) and int(B[i]):
				rst.append(1)
			else:
				rst.append(0)

			A_array.append(int(A[i]))
			B_array.append(int(B[i]))
		
		frame = CanvasFrame()
		frame.Show(True)


		# self.panel = backend_wxagg.FigureCanvasWxAgg(self, -1, Figure())
		# axes = self.panel.figure.gca()
		# axes.cla()
		# axes.plot(x, rst)

		# self.panel.draw()  

	def or_result(self, event):
		global rst, A_array, B_array
		A = self.A_text.GetValue()
		B = self.B_text.GetValue()
		rst = []
		for i in xrange(len(A)):
			if not int(A[i]) and not int(B[i]):
				rst.append(0)
			else:
				rst.append(1)

			A_array.append(int(A[i]))
			B_array.append(int(B[i]))

		frame = CanvasFrame()
		frame.Show(True)
		# print rst

	def not_result(self, event):
		global rst_A, rst_B, A_array, B_array
		A = self.A_text.GetValue()
		B = self.B_text.GetValue()
		rst_A = []
		rst_B = []
		for i in xrange(len(A)):
			rst_A.append(1 - int(A[i]))
			rst_B.append(1 - int(B[i]))

			A_array.append(int(A[i]))
			B_array.append(int(B[i]))

		print rst_A
		frame = CanvasFrame_NOT()
		frame.Show(True)

	def add_not_result(self, event):
		global rst, A_array, B_array
		A = self.A_text.GetValue()
		B = self.B_text.GetValue()
		rst = []
		for i in xrange(len(A)):
			if int(A[i]) == int(B[i]):
				rst.append(1)
			else:
				rst.append(0)

			A_array.append(int(A[i]))
			B_array.append(int(B[i]))

		frame = CanvasFrame()
		frame.Show(True)
		
		# print rst

	def or_not_result(self, event):
		global rst, A_array, B_array
		A = self.A_text.GetValue()
		B = self.B_text.GetValue()
		rst = []
		for i in xrange(len(A)):
			if int(A[i]) == int(B[i]):
				rst.append(0)
			else:
				rst.append(1)

			A_array.append(int(A[i]))
			B_array.append(int(B[i]))

		frame = CanvasFrame()
		frame.Show(True)


if __name__ == '__main__':
	app = wx.App()
	frame = Calc(parent = None, id = -1)
	frame.Show()
	app.MainLoop()
