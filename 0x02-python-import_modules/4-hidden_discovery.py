#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    defined_names = dir(hidden_4)
    for i in range(len(defined_names)):
        if defined_names[i][0] != "_":
                print("{}".format(define_names[i]))
