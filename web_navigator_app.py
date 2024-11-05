from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit, QPushButton, QLineEdit, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys

class WebNavigatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Web Navigation Data Annotation Tool')
        self.setGeometry(100, 100, 1200, 800)  # Set window size

        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Create navigation toolbar
        nav_toolbar = QToolBar("Navigation")
        self.addToolBar(nav_toolbar)

        # Add back, forward, reload, and home buttons
        back_action = QAction("Back", self)
        back_action.triggered.connect(self.browser_back)
        nav_toolbar.addAction(back_action)

        forward_action = QAction("Forward", self)
        forward_action.triggered.connect(self.browser_forward)
        nav_toolbar.addAction(forward_action)

        reload_action = QAction("Refresh", self)
        reload_action.triggered.connect(self.browser_reload)
        nav_toolbar.addAction(reload_action)

        # Add address bar
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)
        nav_toolbar.addWidget(self.address_bar)

        # Embedded web browser
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))  # Load any default URL
        self.browser.urlChanged.connect(self.update_address_bar)
        main_layout.addWidget(self.browser)

        # Chat interface for agent actions and user feedback
        chat_layout = QVBoxLayout()
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        chat_layout.addWidget(self.chat_display)

        # Control buttons for Yes/No
        self.yes_button = QPushButton('Yes')
        self.no_button = QPushButton('No')
        self.yes_button.clicked.connect(self.confirm_action)
        self.no_button.clicked.connect(self.modify_action)
        chat_layout.addWidget(self.yes_button)
        chat_layout.addWidget(self.no_button)

        # Add chat layout to main layout
        main_layout.addLayout(chat_layout)

        # Set the layout and main widget
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def browser_back(self):
        self.browser.back()

    def browser_forward(self):
        self.browser.forward()

    def browser_reload(self):
        self.browser.reload()

    def load_url(self):
        url = self.address_bar.text()
        if not url.startswith("http"):
            url = "http://" + url  # Add http if missing
        self.browser.setUrl(QUrl(url))

    def update_address_bar(self, qurl):
        self.address_bar.setText(qurl.toString())

    def confirm_action(self):
        # Code to confirm agent's action and proceed
        self.chat_display.append("Action confirmed.")

    def modify_action(self):
        # Code to allow user to modify the action
        self.chat_display.append("Action modified by user.")

# Run the app
app = QApplication(sys.argv)
window = WebNavigatorApp()
window.show()
sys.exit(app.exec_())
