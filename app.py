from flask import Flask
app=Flask("/info")
def myinfo():
  return "my name is shivam sharma,proud to be the student of lw,learning under the mentorship of the legendary vimal daga sir."
@app.route("/phone")
def myphone():
return "8091381203"
app.run(host="0.0.0.0")