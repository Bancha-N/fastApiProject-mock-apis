import time

from fastapi import FastAPI

number_of_call_stack = 30

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/check_scheduled_action/{name}")
async def check_run_scheduled_action_complete(name: str):
    time.sleep(1)
    set_number_of_call_stack()
    print(number_of_call_stack)
    if number_of_call_stack <= 0:
        return {
            "name": name,
            "number_of_call_stack": number_of_call_stack,
            "result": "complete"
        }
    else:
        return {
            "name": name,
            "number_of_call_stack": number_of_call_stack,
            "result": "not_complete"
        }


def set_number_of_call_stack():
    global number_of_call_stack
    number_of_call_stack = number_of_call_stack - 1
