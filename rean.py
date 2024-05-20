import queue
import re

not_reserved_word = "OVY"
status = []

def shaping(real_sql = ""):
    shaping_sql = real_sql.replace(";", " ;").replace("(", " ( ").replace(")", " ) ").replace(",", " , ")
    shaping_sql = re.sub("\s+", " ", shaping_sql).lower()
    shaping_sql = re.sub(" +$", "", shaping_sql)
    return shaping_sql

def lower(str = ""):
    return str.lower()

def read_status():
    status = []
    f = open("status/operator", "r")
    status= status + f.read().split('\n')

    f = open("status/reserved", "r")
    status = status + list(map(lower, f.read().split('\n')))

    f = open("status/other", "r")
    status = status + list(map(lower, f.read().split('\n')))
    #status.append(start_status)
    return status

def word2status(word = ""):
    status = read_status()
    if word in status:
        return word
    else:
        return not_reserved_word

def main():
    start_status = "start"

    #ステータスの読み込み
    status = read_status()
    print(status)
    
    f = open("rean_data.sql")
    sqls = f.read().split('\n')

    history = []
    line = 0
    for sql in sqls:
        print("---------startt------------")
        i = 0
        j = 0
        line = line + 1
        now_status = start_status
        past=[start_status, start_status]
        move = ""
        div = shaping(sql).split(" ")
        div = list(map(word2status, div))
        status_stack = queue.LifoQueue()
        status_stack.put(start_status)
        
        print(div)
        for word in div:
            j = j+1
            move = status_stack.queue[-1] + " " + past[0] + "_" + past[1] + " -> " + word
            print(move)
            if move not in history:
                history.append(move)
                i = i+1
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
        print(status_stack.queue)
        if move not in history:
            history.append(move)
            i = i+1
        print(line,":",i,"/",j)

    lean_data = '\n'.join(history)
    f = open("reaned_data.txt", "w")
    f.write(lean_data)
    f.close()

if __name__ == "__main__":
    main()
    not_reserved_word = "OVY"