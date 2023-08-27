def hello_world_return():
    return "Hello world!"  # requires print when called


def hello_world_print():
    print("Hello World!")  # doesnt require print when called


def args_return(text: str):
    return text

def args_print(text: str):
    print(text)


hello_world_print()
args_print("Hello World!")
print(hello_world_return())
print(
    args_return(
        "Did  you pray today?"
    )
)
