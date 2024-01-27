from zero import ZeroClient



zero_client = ZeroClient("localhost", 5559)

def check_for_winner():
    resp = zero_client.call("check_for_winner", None)
    return resp
def make_board(cords):
    resp = zero_client.call("make_board", cords)
    return resp