const app = require("express")();
const path = require('path')
const child = require('child_process');

app.get("/",async(req,res)=>{
    res.sendFile(path.join(__dirname,"index.html"))
})

app.get('/run', function (req, res) {
    const subprocess = runScript()
    res.set('Content-Type', 'text/plain');
    subprocess.stdout.pipe(res)
    subprocess.stderr.pipe(res)
  })

app.listen(3000, async()=>{
    console.log("Listening to port 3000")
})

function runScript(){
    return child.spawn('python', [
      "-u", 
      path.join(__dirname, 'main.py'),
      "--foo", "some value for foo",
    ]);
}