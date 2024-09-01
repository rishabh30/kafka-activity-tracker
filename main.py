import uvicorn

from app.db.config import Constants


def main():
    uvicorn.run(
        app="app.server:app",
        host=Constants.APP_HOST,
        port=Constants.APP_PORT,
        reload=True,
        workers=1,
    )


if __name__ == "__main__":
    main()
