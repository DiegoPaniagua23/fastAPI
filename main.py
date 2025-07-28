from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException 
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# Pydantic model for Post
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title":"title of post 1", "content": "content of post 1", "id": 1},
            {"title":"favourite meals", "content": "I like pizzas", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

# Request Get method url: "/"
@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI!"}
  
@app.get("/posts")
def get_posts():
    return {"data": my_posts} 

@app.post("/posts", status_code=status.HTTP_201_CREATED) 
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
       #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'message': f"Post with id {id} was not found"}
    return {"post_detail": post}

@app.delete("/posts/{id}")
def delete_post(id: int):
    index = find_index_post(id)
    my_posts.pop(index)
    return {"message": "post was successfully deleted"}
 