import wx
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

def myplot(axes, array, title):
	for i in xrange(len(array)):
		axes.axvline(i, 0, array[i]/max(array), linewidth = 3)

	axes.axis([0, len(array), 0, max(array)])
	axes.set_title(title)

class CanvasFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,
                         'CanvasFrame',size=(550,350))

		N = 10
		M = 20
		x = [1 for n in xrange(N)]
		x_extend = x + [0 for n in xrange(M + 1)]
		h = [0.5 * n for n in xrange(M)]
		h_extend = h + [0 for n in xrange(N + 1)]
		y = [0 for n in xrange(N + M)]
		print x,h,y

		for n in xrange(N + M):
			for m in xrange(n + 1):
				y[n] = y[n] + x_extend[m] * h_extend[n - m]

		figure = Figure()
		axes = figure.add_subplot(3,1,1)
		myplot(axes, x, 'x')

		axes = figure.add_subplot(3,1,2)
		myplot(axes, h, 'h')

		axes = figure.add_subplot(3,1,3)
		myplot(axes, y, 'y')

		self.canvas = FigureCanvas(self, -1, figure)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
		self.SetSizer(self.sizer)
		self.Fit()

if __name__ == '__main__':
	app = wx.App()
	frame = CanvasFrame()
	frame.Show()
	app.MainLoop()


