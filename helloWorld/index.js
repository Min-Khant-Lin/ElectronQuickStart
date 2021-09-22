const electron = require('electron');
const techacademy = electron.app;
const BrowserWindow = electron.BrowserWindow;
let mainWindow;

techacademy.on('ready', function() {
  let subpy = require('child_process').spawn('python',['./index.py']);
  let URL = 'http://localhost:5000/t';

  let openWindow = function() {
  mainWindow = new BrowserWindow({width: 1000, height: 500 });
  mainWindow.loadURL(URL);
  };
  openWindow();
});