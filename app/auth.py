from fastapi import HTTPException, Header

def get_current_user(api_key: str = Header(None)):
    if api_key != "your_secret_api_key":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return api_key
