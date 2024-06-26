from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth, post, user, vote

# We don't need this anymore because of alembic
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# You can specify this to only allow your web app to make requests
origins = ["*"]
# Before the request goes to the route it goes to the middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This is how we can break down the code into smaller parts
# It goes into all the routers and looks for the matching path
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# You have to be careful how you structure your API, because order matters,
# fastAPI goes from top to bottom and looks for the first match


# Decorator turns this into path operation
# This is a get method
@app.get("/")
# You can use async def as well
def root():
    """
    Returns a dictionary with a message when the root path is accessed.

    :return: A dictionary with a message.
    """
    return {"message": "Pozdravljeni na mojem api, uspešno deplojano iz CI/CD pipline, ubuntu!"}
