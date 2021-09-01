import time , sys
indent = 0
indentIncreasing = True
try:
    while True:
        print(' '*indent,end='')
        print("********")
        time.sleep(0.1)
                     # Increase the number of spaces:
        if indentIncreasing:
            indent=indent+1
            if indent==20:                  # Change direction:
                indentIncreasing=False
                             # Decrease the number of spaces:
        else:
            indent = indent -1
            if indent == 0 :
                indentIncreasing = True      # Change direction:
except KeyboardInterrupt:
    sys.exit()
