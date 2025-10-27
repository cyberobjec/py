from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/args/{arg1}")
def args_1(arg1: str, arg2: int = 0,arg3: bool = False):
    return {"message": f"Hello, {arg1}! {arg2} {arg3}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000,reload=True)