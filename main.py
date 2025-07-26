from fastapi import FastAPI 

app = FastAPI()

# Request Get method url: "/"
@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI!"}
  
@app.get("/posts")
def get_posts():
    return {"data": "These are your posts!"}
