"""
Main Purpose:
	Understand documenation of PyQt5 library and WebEngineWidgets module
	Learn inheritance, super(), *args, and **kwargs
	Note: This is just sample code since some sites block how module gets information

Idea stolen from:
	https://pythongeeks.org/create-web-browser-python-pyqt/

Level: Advanced
What I learned:
	PyQt5: https://pypi.org/project/PyQt5/
	PyQt5 Documentation: https://docs.pypi.org/
	Qt WebEngine Widgets Documentation: https://doc.qt.io/qt-6/qtwebenginewidgets-index.html

Created by HackerDu

# Important: Master this to understand inheritance concept with super() ⭐⭐⭐⭐⭐❤️❤️❤️❤️❤️
class Rectangle:								# Parent/Super class
	def __init__(self, length, width):			# Construction: Rectangle(length=3,width=3)
		self.length = length
		self.width = width
	def area(self):
		return self.length * self.width

class Square(Rectangle):						# Child class
	def __init__(self, length):					# Construction: Square(length=3)
		super().__init__(length, length)		# Rectangle.__init__(self, length, length)
												# self.length = length
												# self.width = length
class Cube(Square):								# Grandchild Class, Construction: Cube(length=3)
	def surface_area(self):
		return super().area() * 6				# Uses super().area() method
	def volume(self):
		return super().area() * self.length

cube = Cube(3)
print(cube.surface_area()) 						# 54
print(cube.volume()) 							# 27
"""

import sys
try:
	from PyQt5.QtCore import QUrl
	from PyQt5.QtWidgets import *
except ImportError:
	print("pip3 install PyQt5")							# Note: Had to google https://pypi.org/project/PyQtWebEngine/
try:
	from PyQt5.QtWebEngineWidgets import QWebEngineView
except ImportError:
	print("pip3 install PyQtWebEngine")

class Window(QMainWindow):								# PyQt5.QtWidgets.QMainWindow, learn inheritance
	def __init__(self, *args, **kwargs):				# learn *args and **kwargs
		super(Window, self).__init__(*args, **kwargs)	# learn super()
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl('https://www.google.com'))
		self.browser.urlChanged.connect(self.update_AddressBar)
		self.setCentralWidget(self.browser)
		self.status_bar = QStatusBar()
		self.setStatusBar(self.status_bar)

		self.navigation_bar = QToolBar('Navigation Toolbar')
		self.addToolBar(self.navigation_bar)

		back_button = QAction("Back", self)
		back_button.setStatusTip('Go to previous page you visited')
		back_button.triggered.connect(self.browser.back)
		self.navigation_bar.addAction(back_button)

		refresh_button = QAction("Refresh", self)
		refresh_button.setStatusTip('Refresh this page')
		refresh_button.triggered.connect(self.browser.reload)
		self.navigation_bar.addAction(refresh_button)

		next_button = QAction("Next", self)
		next_button.setStatusTip('Go to next page')
		next_button.triggered.connect(self.browser.forward)
		self.navigation_bar.addAction(next_button)

		home_button = QAction("Home", self)
		home_button.setStatusTip('Go to home page (Google page)')
		home_button.triggered.connect(self.go_to_home)
		self.navigation_bar.addAction(home_button)

		self.navigation_bar.addSeparator()

		self.URLBar = QLineEdit()
		# This specifies what to do when enter is pressed in the Entry field
		self.URLBar.returnPressed.connect(lambda: self.go_to_URL(QUrl(self.URLBar.text())))
		self.navigation_bar.addWidget(self.URLBar)

		self.addToolBarBreak()

		# Adding another toolbar which contains the bookmarks
		bookmarks_toolbar = QToolBar('Bookmarks', self)
		self.addToolBar(bookmarks_toolbar)

		leetcode = QAction("Leetcode", self)
		leetcode.setStatusTip("Go to Leetcode website")
		leetcode.triggered.connect(lambda: self.go_to_URL(QUrl("https://leetcode.com")))
		bookmarks_toolbar.addAction(leetcode)

		youtube = QAction("Youtube", self)
		youtube.setStatusTip("Go to Youtube website")
		youtube.triggered.connect(lambda: self.go_to_URL(QUrl("https://youtube.com")))
		bookmarks_toolbar.addAction(youtube)

		pythongeeks = QAction("PythonGeeks", self)
		pythongeeks.setStatusTip("Go to PythonGeeks website")
		pythongeeks.triggered.connect(lambda: self.go_to_URL(QUrl("https://pythongeeks.org")))
		bookmarks_toolbar.addAction(pythongeeks)

		facebook = QAction("Facebook", self)
		facebook.setStatusTip("Go to Facebook")
		facebook.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.facebook.com")))
		bookmarks_toolbar.addAction(facebook)

		linkedin = QAction("LinkedIn", self)
		linkedin.setStatusTip("Go to LinkedIn")
		linkedin.triggered.connect(lambda: self.go_to_URL(QUrl("https://in.linkedin.com")))
		bookmarks_toolbar.addAction(linkedin)

		instagram = QAction("Instagram", self)
		instagram.setStatusTip("Go to Instagram")
		instagram.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.instagram.com")))
		bookmarks_toolbar.addAction(instagram)

		twitter = QAction("Twitter", self)
		twitter.setStatusTip('Go to Twitter')
		twitter.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.twitter.com")))
		bookmarks_toolbar.addAction(twitter)

		self.browser.maximumSize()
		self.show()

	def go_to_home(self):
		self.browser.setUrl(QUrl('https://www.google.com/'))

	def go_to_URL(self, url: QUrl):
		if url.scheme() == '':
			url.setScheme('https://')
		self.browser.setUrl(url)
		self.update_AddressBar(url)

	def update_AddressBar(self, url):
		self.URLBar.setText(url.toString())
		self.URLBar.setCursorPosition(0)

def main():
   app = QApplication(sys.argv)
   app.setApplicationName('Hackers Web Browser')

   window = Window()
   app.exec_()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()