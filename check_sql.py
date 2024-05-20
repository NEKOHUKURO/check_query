from rean import shaping, word2status, read_status
import queue
def check_sql(sql = ""):
    start_status = "start"
    not_reserved_word = "OVY"

    status = read_status()

    status_stack = queue.LifoQueue()
    status_stack.put(start_status)

    now_status = start_status
    past=[start_status, start_status]
    move = ""
    f = open("reaned_data.txt", "r")
    history = f.read().split('\n')
    print(history)
    div = shaping(sql).split(" ")
    div = list(map(word2status, div))
    for word in div:
        move = status_stack.queue[-1] + " " + past[0] + "_" + past[1] + " -> " + word
        if move not in history:
            print(move)
            return False
        if word in status:
            if word == '(':
                status_stack.put(word)
                now_status = word
            if word == ')':
                status_stack.put(word)
                now_status = word
            if word == ",":
                pass
            else:
                if now_status == '(':
                    status_stack.get()
                    status_stack.put(word)
                    now_status = word
                if word == ')':
                    status_stack.get()
                    status_stack.get()
                    now_status = word
                else:
                    status_stack.get()
                    status_stack.put(word)
                    now_status = word

        past[0] = past[1]
        past[1] = word
    move = status_stack.queue[-1] + " " + past[0] + "_" + past[1] + " -> " + word
    if move not in history:
        print(move)
        return False
    return True

if __name__ == "__main__":
    ss = check_sql("SELECT * FROM cars WHERE price = (SELECT MAX(price) FROM cars);")
    print(ss)