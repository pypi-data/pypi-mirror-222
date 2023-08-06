import os
from typing import Union

from PyQt6.QtCore import QUrl, Qt, QDir, pyqtSignal

from muphyn.packages.interface.base.widgets.webviews.WebEngineView import WebEngineView, WebEnginePage
from muphyn.utils.paths import ROOT_DIR

MD_TO_HTML_PARSER = \
"""
<!doctype html>
<html>
    <head>
        <meta charset="utf-8"/>
        <title>Marked in the browser</title>
        <link rel="stylesheet" type="text/css" href="{github-markdown.css}">
    </head>
    <body class="markdown-body">
        <div id="content"></div>
        <script src="{marked.js}"></script>
        <script>
            markdownContent = `{toParse}`
            document.getElementById('content').innerHTML = marked.parse(markdownContent);
        </script>
    </body>
</html>
"""

class MarkdownView(WebEngineView):

    GithubMarkdownCssPath = os.path.join(ROOT_DIR, "docs\\css\\github-markdown.min.css")
    MarkedJsPath = os.path.join(ROOT_DIR, "docs\\js\\marked.min.js")
    DocumentPath = os.path.join(ROOT_DIR, "docs")

    def setContentData(self, markdown: str, baseUrl: QUrl = QUrl(DocumentPath)) -> None:
        # 
        parsedHtml = MD_TO_HTML_PARSER

        # Replace github-markdown.min.css path
        parsedHtml = parsedHtml.replace("{github-markdown.css}", MarkdownView.GithubMarkdownCssPath)

        # Replace marked.js path
        parsedHtml = parsedHtml.replace("{marked.js}", MarkdownView.MarkedJsPath)

        # Replace markdown content
        parsedHtml = parsedHtml.replace("{toParse}", markdown.replace('`', '\`'))

        return self.setHtmlContent(parsedHtml, baseUrl)