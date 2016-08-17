def letter_queue(commands):
    queue = []

    for command in commands:
        if "PUSH" in command:
            queue.append(command[-1])
        else:
            if "POP" in command:
                if len(queue) == 0:
                    pass
                else:
                    queue.pop(0)
    print("".join(queue))
    return "".join(queue)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"