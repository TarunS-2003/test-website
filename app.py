from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def hello_world():
  details=[
    {"id":1,
      "name":"seneca",
      "address":"15,SF,USA"
    },
    {"id":1,
      "name":"seneca",
      "address":"15,SF,USA"
    },
    {"id":1,
      "name":"seneca",
      "address":"15,SF,USA"
    }
  ]
  return render_template('index.html',det=details)
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)