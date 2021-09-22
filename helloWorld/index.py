#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return """
            <h1><font color="red">PythonとElectronを使ったアプリ</font></h1>
            <h2><font color="blue">表示結果</font></h2>
            <p>この文章は、</p>
            <p>Electronでindex.jsを読み込んだあと、</p>
            <p><pre>「require('child_process').spawn('python',['./index.py']);」</pre></p>
            <p>によって、index.pyファイルを読み込み表示した文章です。</p>


            """

@app.route("/hw")

def hw():
    return """
            <h1><font color="red">PythonとElectronを使ったアプリ</font></h1>
            <h2><font color="blue">Hello World</font></h2>
            <p>この文章は、</p>
            <p>Electronでindex.jsを読み込んだあと、</p>
            <p><pre>「require('child_process').spawn('python',['./index.py']);」</pre></p>
            <p>によって、index.pyファイルを読み込み表示した文章です。</p>


            """

@app.route("/t")

def t():
    return """
            <h1><font color="red">PythonとElectronを使ったアプリ</font></h1>
            <h2><font color="blue">Test-1</font></h2>
            <p>この文章は、</p>
            <p>Electronでindex.jsを読み込んだあと、</p>
            <p><pre>「require('child_process').spawn('python',['./index.py']);」</pre></p>
            <p>によって、index.pyファイルを読み込み表示した文章です。</p>


            """

if __name__ == "__main__":
    app.run(host="localhost", port=5000)