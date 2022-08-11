import os
import webbrowser
import wx
app = wx.App()
version=1.0
name="Search multiple sites"
description="With this program you can search in multiple sites"
class myapp(wx.Frame):
	def __init__(self):
		super().__init__(None, title=name, name=name)
		self.Center()
		p = wx.Panel(self)
		wx.StaticText(p, -1, "Input/Result")
		self.option = wx.TextCtrl(p, -1, style=wx.TE_MULTILINE + wx.HSCROLL)
		exit = wx.Button(p, -1, "Exit the program")
		exit.Bind(wx.EVT_BUTTON, self.onexit)
		about = wx.Button(p, -1, "about")
		about.Bind(wx.EVT_BUTTON, self.onabout)
		menubar = wx.MenuBar()
		file = wx.Menu()
		searchMenu = wx.Menu()
		bing=searchMenu.Append(-1, "bing 	ctrl+b")
		yahoo=searchMenu.Append(-1, "yahoo 	alt+y")
		google1=searchMenu.Append(-1, "google 	ctrl+g")
		Ecosia=searchMenu.Append(-1, "Ecosia")
		DuckDuckGo=searchMenu.Append(-1, "DuckDuckGo")
		file.AppendSubMenu(searchMenu, "search engines")
		weMenu = wx.Menu()
		ar_w=weMenu.Append(-1, "arabic 	ctrl+w")
		en_w=weMenu.Append(-1, "english 	alt+w")
		fr_w=weMenu.Append(-1, "french 	ctrl+shift+w")
		file.AppendSubMenu(weMenu, "Wikipedia")
		wiMenu = wx.Menu()
		youtube1=wiMenu.Append(-1, "youtube 	ctrl+y")
		open=wiMenu.Append(-1, "open link 	ctrl+o")
		ama=wiMenu.Append(-1, "amazon 	ctrl+shift+a")
		file.AppendSubMenu(wiMenu, "Other")
		s_mMenu= wx.Menu()
		telegramMenu= wx.Menu()
		te_user=telegramMenu.Append(-1, "Open Telegram chat with username typed 	ctrl+t")
		te_num=telegramMenu.Append(-1, "Open a Telegram conversation with the phone number typed 	ctrl+shift+t")
		s_mMenu.AppendSubMenu(telegramMenu, "telegram")
		me_user=s_mMenu.Append(-1, "Opening a conversation in messenger with username typed 	alt+m")
		wha_num=s_mMenu.Append(-1, "Opening a conversation in WhatsApp with the phone number typed 	alt+h")
		twe_user=s_mMenu.Append(-1, "Open Twitter username link 	alt+t")
		fass_user=s_mMenu.Append(-1, "Open Facebook username link 	alt+f")
		file.AppendSubMenu(s_mMenu, "Social Media")

		links = wx.Menu()
		teItem = links.Append(-1, "telegram")
		tweItem = links.Append(-1, "Twitter")
		facebookItem = links.Append(-1, "facebook")
		whatsappItem = links.Append(-1, "whatsapp")

		q_a = wx.Menu()
		smMenu = wx.Menu()
		youtube2=smMenu.Append(-1, "youtube")
		facebook2=smMenu.Append(-1, "facebook")
		twitter2=smMenu.Append(-1, "twitter")
		telegram2=smMenu.Append(-1, "telegram")
		whatsapp2=smMenu.Append(-1, "whatsapp")
		q_a.AppendSubMenu(smMenu, "Social Media")


		txt = wx.Menu()
		openItem = txt.Append(-1, "Open a new file 	ctrl+shift+o")



		analysis = wx.Menu()
		helpItem = analysis.Append(-1, "help file 	f1")
		conMenu = wx.Menu()
		technologyandnewst=conMenu.Append(-1, "Technology and News on Telegram")
		technologyandnewsy=conMenu.Append(-1, "Technology and News on YouTube")
		mesteranas=conMenu.Append(-1, "Mester Anas on Telegram")
		mohammedtechnology=conMenu.Append(-1, "Mohamed Technology on Telegram")

		analysis.AppendSubMenu(conMenu, "contact us")
		aboutItem = analysis.Append(-1, "about 	f3")

		menubar.Append(file, "program") 
		menubar.Append(links, "Create sharing links")
		menubar.Append(q_a, "Quick access")
		menubar.Append(txt, "text files")
		menubar.Append(analysis, "help")
		self.SetMenuBar(menubar)


		self.Bind(wx.EVT_MENU, self.onOpen, openItem)
		self.Bind(wx.EVT_MENU, self.onhelp, helpItem)
		self.Bind(wx.EVT_MENU, self.onabout, aboutItem)

		self.Bind(wx.EVT_CLOSE, self.onexit)
		self.Show()
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.bing.com/search?q=" + self.option.Value), bing)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.yahoo.com/search?q=" + self.option.Value), yahoo)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.google.com/search?q=" + self.option.Value), google1)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.Ecosia.org/search?q=" + self.option.Value), Ecosia )
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://duckduckgo.com/?q=" + self.option.Value), DuckDuckGo)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://ar.wikipedia.org/wiki/" + self.option.Value), ar_w)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://en.wikipedia.org/wiki/" + self.option.Value), en_w)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://fr.wikipedia.org/wiki/" + self.option.Value), fr_w)

		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.youtube.com/results?search_query=" + self.option.Value), youtube1)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new(self.option.Value), open)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.amazon.eg/s?k=" + self.option.Value), ama)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/" + self.option.Value), te_user)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/" + self.option.Value), te_num)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://m.me/" + self.option.Value), me_user)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://wa.me/" + self.option.Value), wha_num)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.twitter.com/" + self.option.Value), twe_user)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.facebook.com/" + self.option.Value), fass_user)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/share/url?url=" + self.option.Value), teItem)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://twitter.com/intent/tweet?text=" + self.option.Value), tweItem)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.facebook.com/sharer/sharer.php?" + self.option.Value), facebookItem)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://wa.me/?text=" + self.option.Value), whatsappItem)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.youtube.com"), youtube2)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://www.facebook.com"), facebook2)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://twitter.com"), twitter2)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://web.telegram.org"), telegram2)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://web.whatsapp.com"), whatsapp2)



		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/technologyandnewsanasmohammed"), technologyandnewst)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://youtube.com/c/technologyandnews"), technologyandnewsy)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/mesteranasm"), mesteranas)
		self.Bind(wx.EVT_MENU, lambda event: webbrowser.open_new("https://t.me/MohamedTechnology"), mohammedtechnology)
	def onOpen(self, event):
		openDialog = wx.FileDialog(self, "Open a new file")
		result = openDialog.ShowModal()
		if result == wx.ID_CANCEL:
			return
		path = openDialog.Path
		filename = openDialog.Filename
		file = open(path, "r", encoding="utf-8")
		self.option.Value = file.read()
		file.close()
		self.Title = f"{filename} - {name}"
		self.activeFile = path
	def onhelp(self, event):
		os.startfile("help_me.html")

	def onexit (self, event):
		message=wx.MessageBox("Do you want to exit the program", "Exit the program", wx.YES_NO)
		if message == wx.YES:
			wx.Exit()
	def onabout (self, event):
		wx.MessageBox(f"""{name} 
{version} 
{description} 
This app is developed by Mohamed Technology and Mesteranas""","About program")




myapp()

app.MainLoop()