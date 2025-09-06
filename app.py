from fastapi import FastAPI, Body, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

# Test data
books = []