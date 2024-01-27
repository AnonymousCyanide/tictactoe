from zero import ZeroClient

zero_client = ZeroClient("localhost", 5559)

def echo():
    resp = zero_client.call("echos", "Hi there!")
    print(resp)

def hello():
    resp = zero_client.call("hello_world", None)
    print(resp)


if __name__ == "__main__":
    echo()
    hello()