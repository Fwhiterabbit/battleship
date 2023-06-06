const { spawn } = require('child_process');
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

battleship.get('/', (req, res) => {
    const pythonProcess = spawn('python', ['index.py']);
  
    pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
    });
  
    pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
    });
  
    pythonProcess.on('close', (code) => {
      console.log(`child process exited with code ${code}`);
      res.send('Application executed successfully.');
    });
  });
  