from fastapi import FastAPI
import uvicorn
import router


app = FastAPI()
app.include_router(router.router)


if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=3216,reload=True)




