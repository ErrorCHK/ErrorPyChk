import asyncio
import sys
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
import PyQt5
import os
import aiohttp
from PyQt5.QtWidgets import QApplication
class Screenshot(QWebEngineView):
    print("ENTRANDO")
    async def capture(self, url, output_file):
        print("ENTRANDO 1")
        self.output_file = output_file
        print("ENTRANDO 1.1")
        URL = QUrl(url)
        print("ENTRANDO 1.1.1")
        #self.load(URL)
        print("ENTRANDO 1.2")
        self.loadFinished.connect(self.on_loaded)
        print("ENTRANDO 1.3")
        self.setAttribute(Qt.WA_DontShowOnScreen)
        print("ENTRANDO 1.4")
        self.page().settings().setAttribute(
            QWebEngineSettings.ShowScrollBars, False)
        self.show()
    def on_loaded(self):
        print("ENTRANDO 2")
        size = PyQt5.QtCore.QSize(1050,600)
        self.resize(size)
        QTimer.singleShot(1000, self.take_screenshot)
    def take_screenshot(self):
        print("ENTRANDO 3")
        self.grab().save(self.output_file, b'PNG')
        self.app.quit()