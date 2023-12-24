import uvicorn

if __name__ == "__main__":
    with open("ipconfig.txt") as file:
        address = file.readline()
    uvicorn.run("app.api:app", host=address, port=8000, reload=True)