# coding=utf-8
import wx

class Calc(wx.Frame):

	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Sumulator', size = (800, 600))
		self.panel = wx.Panel(self, -1)

		sampleList = ['0', '1']

# ---------------------------------  RS  -------------------------------------------------------------

		self.RS = wx.StaticText(self.panel, -1, u"RS触发器(R、S不能同时为1)", pos = (50, 13), size = (100, -1))
		font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL)
		self.RS.SetFont(font)

		self.S_lable = wx.StaticText(self.panel, -1, "S:", pos = (50, 53), size = (100, -1))
		self.S_value = wx.Choice(self.panel, -1, pos = (70, 50), choices = sampleList)

		self.R_lable = wx.StaticText(self.panel, -1, "R:", pos = (50, 83), size = (100, -1))
		self.R_value = wx.Choice(self.panel, -1, pos = (70, 80), choices = sampleList)

		# self.Q1_lable = wx.StaticText(self.panel, -1, "Q:", pos = (50, 113), size = (100, -1))
		# self.Q1_value = wx.Choice(self.panel, -1, pos = (70, 110), choices = sampleList)

		self.Q1_lable = wx.StaticText(self.panel, -1, u"Q (输入,数据间以逗号隔开):", pos = (50, 113))
		self.Q1_value = wx.TextCtrl(self.panel, -1, "", pos = (70, 143), size=(150, -1))

		self.Q1_output_lable = wx.StaticText(self.panel, -1, "Output:", pos = (50, 178))
		self.Q1_output_value = wx.TextCtrl(self.panel, -1, "", pos = (70, 205), size=(150, -1))

		button_simulate1_one = wx.Button(self.panel, label = u'模拟', pos = (100, 240), size = (80, 30))
		# button_simulate1_many = wx.Button(self.panel, label = u'多指模拟', pos = (155, 240), size = (80, 30))
		
# ---------------------------------  JK  -------------------------------------------------------------

		self.JK = wx.StaticText(self.panel, -1, u"JK触发器", pos = (310, 13), size = (100, -1))
		font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL)
		self.JK.SetFont(font)

		self.J_lable = wx.StaticText(self.panel, -1, "J:", pos = (310, 53), size = (100, -1))
		self.J_value = wx.Choice(self.panel, -1, pos = (330, 50), choices = sampleList)

		self.K_lable = wx.StaticText(self.panel, -1, "K:", pos = (310, 83), size = (100, -1))
		self.K_value = wx.Choice(self.panel, -1, pos = (330, 80), choices = sampleList)

		# self.Q2_lable = wx.StaticText(self.panel, -1, "Q:", pos = (450, 113), size = (100, -1))
		# self.Q2_value = wx.Choice(self.panel, -1, pos = (470, 110), choices = sampleList)

		self.Q2_lable = wx.StaticText(self.panel, -1, u"Q (输入,数据间以逗号隔开):", pos = (310, 113))
		self.Q2_value = wx.TextCtrl(self.panel, -1, "", pos = (330, 143), size=(150, -1))

		self.Q2_output_lable = wx.StaticText(self.panel, -1, "Output:", pos = (310, 178))
		self.Q2_output_value = wx.TextCtrl(self.panel, -1, "", pos = (330, 205), size=(150, -1))

		button_simulate2_one = wx.Button(self.panel, label = u'模拟', pos = (360, 240), size = (80, 30))
		# button_simulate2_many = wx.Button(self.panel, label = u'多指模拟', pos = (555, 240), size = (80, 30))

# ---------------------------------  D  -------------------------------------------------------------
		self.D = wx.StaticText(self.panel, -1, u"D触发器", pos = (50, 313), size = (100, -1))
		font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL)
		self.D.SetFont(font)

		self.D_lable = wx.StaticText(self.panel, -1, "D:", pos = (50, 353), size = (100, -1))
		self.D_value = wx.Choice(self.panel, -1, pos = (70, 350), choices = sampleList)

		# self.Q3_lable = wx.StaticText(self.panel, -1, "Q:", pos = (50, 383), size = (100, -1))
		# self.Q3_value = wx.Choice(self.panel, -1, pos = (70, 380), choices = sampleList)

		self.Q3_lable = wx.StaticText(self.panel, -1, u"Q (输入,数据间以逗号隔开):", pos = (50, 383))
		self.Q3_value = wx.TextCtrl(self.panel, -1, "", pos = (70, 413), size=(150, -1))

		self.Q3_output_lable = wx.StaticText(self.panel, -1, "Output:", pos = (50, 448))
		self.Q3_output_value = wx.TextCtrl(self.panel, -1, "", pos = (70, 475), size=(150, -1))

		button_simulate3_one = wx.Button(self.panel, label = u'模拟', pos = (100, 510), size = (80, 30))
		# button_simulate3_many = wx.Button(self.panel, label = u'多指模拟', pos = (155, 510), size = (80, 30))

# ---------------------------------  T  -------------------------------------------------------------
		self.T = wx.StaticText(self.panel, -1, u"T触发器", pos = (310, 313), size = (100, -1))
		font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL)
		self.T.SetFont(font)

		self.T_lable = wx.StaticText(self.panel, -1, "T:", pos = (310, 353), size = (100, -1))
		self.T_value = wx.Choice(self.panel, -1, pos = (330, 350), choices = sampleList)

		# self.Q4_lable = wx.StaticText(self.panel, -1, "Q:", pos = (450, 383), size = (100, -1))
		# self.Q4_value = wx.Choice(self.panel, -1, pos = (470, 380), choices = sampleList)

		self.Q4_lable = wx.StaticText(self.panel, -1, u"Q (输入,数据间以逗号隔开):", pos = (310, 383))
		self.Q4_value = wx.TextCtrl(self.panel, -1, "", pos = (330, 413), size=(150, -1))

		self.Q4_output_lable = wx.StaticText(self.panel, -1, "Output:", pos = (310, 448))
		self.Q4_output_value = wx.TextCtrl(self.panel, -1, "", pos = (330, 475), size=(150, -1))

		button_simulate4_one = wx.Button(self.panel, label = u'模拟', pos = (310, 510), size = (80, 30))
		# button_simulate4_many = wx.Button(self.panel, label = u'多指模拟', pos = (555, 510), size = (80, 30))

# ---------------------------------  cascade  -------------------------------------------------------------
		self.cascade = wx.StaticText(self.panel, -1, u"级联(各触发器的栏中设置参数)", pos = (560, 13), size = (100, -1))
		font = wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL)
		self.cascade.SetFont(font)

		cascadeList = ['None', 'RS', 'JK', 'D', 'T']

		self.First_lable = wx.StaticText(self.panel, -1, u"第一级:", pos = (560, 53), size = (100, -1))
		self.First_value = wx.Choice(self.panel, -1, pos = (620, 50), choices = cascadeList)

		self.Second_lable = wx.StaticText(self.panel, -1, u"第二级:", pos = (560, 83), size = (100, -1))
		self.Second_value = wx.Choice(self.panel, -1, pos = (620, 80), choices = cascadeList)

		self.Third_lable = wx.StaticText(self.panel, -1, u"第三级:", pos = (560, 113), size = (100, -1))
		self.Third_value = wx.Choice(self.panel, -1, pos = (620, 110), choices = cascadeList)

		self.Forth_lable = wx.StaticText(self.panel, -1, u"第四级:", pos = (560, 143), size = (100, -1))
		self.Forth_value = wx.Choice(self.panel, -1, pos = (620, 140), choices = cascadeList)

		# self.Q2_lable = wx.StaticText(self.panel, -1, "Q:", pos = (450, 113), size = (100, -1))
		# self.Q2_value = wx.Choice(self.panel, -1, pos = (470, 110), choices = sampleList)

		self.Q5_lable = wx.StaticText(self.panel, -1, u"Q (输入,数据间以逗号隔开):", pos = (560, 173))
		self.Q5_value = wx.TextCtrl(self.panel, -1, "", pos = (580, 203), size=(150, -1))

		self.Q5_output_lable = wx.StaticText(self.panel, -1, "Output:", pos = (560, 238))
		self.Q5_output_value = wx.TextCtrl(self.panel, -1, "", pos = (580, 265), size=(150, -1))

		button_simulate5_one = wx.Button(self.panel, label = u'模拟', pos = (610, 290), size = (80, 30))
		


# ---------------------------------  Button Bind  -------------------------------------------------------------
		self.Bind(wx.EVT_BUTTON, self.RS_simulate, button_simulate1_one)
		# self.Bind(wx.EVT_BUTTON, self.RS_many, button_simulate1_many)
		self.Bind(wx.EVT_BUTTON, self.JK_simulate, button_simulate2_one)
		# self.Bind(wx.EVT_BUTTON, self.JK_many, button_simulate2_many)
		self.Bind(wx.EVT_BUTTON, self.D_simulate, button_simulate3_one)
		# self.Bind(wx.EVT_BUTTON, self.D_many, button_simulate3_many)
		self.Bind(wx.EVT_BUTTON, self.T_simulate, button_simulate4_one)
		# self.Bind(wx.EVT_BUTTON, self.T_many, button_simulate4_many)
		self.Bind(wx.EVT_BUTTON, self.cascade_simulate, button_simulate5_one)

# ---------------------------------  Button Function  -------------------------------------------------------------
	def RS_simulate(self, event, Q = []):
		R = int(self.R_value.GetCurrentSelection())
		S = int(self.S_value.GetCurrentSelection())
		Q_raw = self.Q1_value.GetValue()
		if Q == []:
			Q = Q_raw.split(',')
		Q_output = []
		for i in xrange(len(Q)):
			if R == 1 and S == 1:
				ans = 0.5
			else:
				ans = int(S or (not(R) and int(Q[i])))
			Q_output.append(ans)
		self.Q1_output_value.SetValue(str(Q_output))
		return Q_output

	def JK_simulate(self, event, Q = []):
		J = int(self.J_value.GetCurrentSelection())
		K = int(self.K_value.GetCurrentSelection())
		Q_raw = self.Q2_value.GetValue()
		if Q == []:
			Q = Q_raw.split(',')
		Q_output = []
		for i in xrange(len(Q)):
			ans = int((J and not(int(Q[i])) or (not(K) and int(Q[i]))))
			Q_output.append(ans)
		self.Q2_output_value.SetValue(str(Q_output))
		return Q_output

	def D_simulate(self, event, Q = []):
		D = int(self.D_value.GetCurrentSelection())
		Q_raw = self.Q3_value.GetValue()
		if Q == []:
			Q = Q_raw.split(',')
		Q_output = []
		for i in xrange(len(Q)):
			ans = D
			Q_output.append(ans)
		self.Q3_output_value.SetValue(str(Q_output))
		return Q_output

	def T_simulate(self, event, Q = []):
		T = int(self.T_value.GetCurrentSelection())
		Q_raw = self.Q4_value.GetValue()
		if Q == []:
			Q = Q_raw.split(',')
		Q_output = []
		for i in xrange(len(Q)):
			ans = int((T and not(int(Q[i])) or (not(T) and int(Q[i]))))
			Q_output.append(ans)
		self.Q4_output_value.SetValue(str(Q_output))
		return Q_output

	def cascade_simulate(self, event):
		first = self.First_value.GetCurrentSelection()
		second = self.Second_value.GetCurrentSelection()
		third = self.Third_value.GetCurrentSelection()
		forth = self.Forth_value.GetCurrentSelection()
		all = [first, second, third, forth]
		Q_raw = self.Q5_value.GetValue()
		Q = Q_raw.split(',')
		for i in xrange(len(Q)):
			for j in xrange(len(all)):
				if all[j] == 1:
					Q = self.RS_simulate(event, Q)
				elif all[j] == 2:
					Q = self.JK_simulate(event, Q)
				elif all[j] == 3:
					Q = self.D_simulate(event, Q)
				elif all[j] == 4:
					Q = self.T_simulate(event, Q)

		Q_output = [int(x) for x in Q]
		self.Q5_output_value.SetValue(str(Q_output))

if __name__ == '__main__':
	app = wx.App()
	frame = Calc(parent = None, id = -1)
	frame.Show()
	app.MainLoop()
