from fastapi import Body, FastAPI 

app = FastAPI()

# Request Get method url: "/"
@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI!"}
  
@app.get("/posts")
def get_posts():
    return {"data": "These are your posts!"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}
