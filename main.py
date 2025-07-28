from typing import Optional
from fastapi import Body, FastAPI 
from pydantic import BaseModel

# Pydantic model for Post
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

app = FastAPI()

# Request Get method url: "/"
@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI!"}
  
@app.get("/posts")
def get_posts():
    return {"data": "These are your posts!"}

@app.post("/createposts") 
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post.dict()}
