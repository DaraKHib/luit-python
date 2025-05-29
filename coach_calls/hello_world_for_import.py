def hello_world() -> str:
    """
    Returns a simple greeting message.

    Returns:
        str: The greeting "Hello World!"
    """
    return "Hello World!"  # Basic return of a static greeting string


if __name__ == "__main__":
    # Print the result of the hello_world function when the script is run directly
    print(hello_world())
