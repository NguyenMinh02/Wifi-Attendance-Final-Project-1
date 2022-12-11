
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, devices, courses, lectures, users, sessions

app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(devices.router)
app.include_router(courses.router)
app.include_router(lectures.router)
app.include_router(users.router)
app.include_router(sessions.router)
@app.on_event("startup")
async def startup():
    print("Hello")

