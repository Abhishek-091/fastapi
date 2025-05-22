from fastapi import FastAPI, Query, Header
from pydantic import BaseModel, Field
from router_api import router as router_api
from typing import Annotated, Literal
from fastapi import Query
from pydantic import AfterValidator

app = FastAPI()




app = FastAPI()
app.include_router(router_api, prefix="/router")



class User(BaseModel):
    name: str
    email: str | None = None
    age: int
    salary: float | None = None

    def set_user(self, name: str, email: str | None, age: int, salary: float | None):
        self.name = name
        self.email = email
        self.age = age
        self.salary = salary

    def get_user(self):
        return {
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "salary": self.salary
        }



#Get request
@app.get("/demo")
async def root():
    return {"message": "Hello World"}

#Get request with path parameter
@app.get("/item/{item_no}/{item_name}")
async def get_item(item_no: int, item_name: str):
    return {"item_no": item_no, "item_name": item_name}





#Get request with query parameter
# http://127.0.0.1:8000/items/?skip=0&limit=10
# If you have a group of query parameters that are related, you can create a Pydantic model to declare them.

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_item(filter_query: Annotated[FilterParams, Query()],
                    user_agent: Annotated[str | None, Header()] = None):
    return fake_items_db[filter_query.skip : filter_query.skip + filter_query.limit]







#Required Query parameter
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item





#Optional Query parameter with Validations
# Here we are using Query() because this is a query parameter. 
# Later we will see others like Path(), Body(), Header(), and Cookie(), 
# that also accept the same arguments as Query().

# @ q: str | None = Query(default=None, max_length=50)  --> OLD WAY
# @ q: Annotated[str | None, Query(max_length=50)] = None  --> NEW WAY
# hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None it will not be included in the schema/openapi docs

# Custom Validation

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


@app.get("/items/{item_id}")
async def read_item(item_id: int,
                    q: Annotated[
                        str | None, 
                        Query(max_length=5), 
                        AfterValidator(check_valid_id)] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}



#Post request
@app.post("/user")
async def create_user(user: User):
    return {
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "salary": user.salary
    }






if __name__ == "__main__":
    from uvicorn import run
    run(
        "main:app", 
        host="127.0.0.1", 
        port=8000,
        workers=4
    )