
#!/usr/bin/python3
'''LockBoxes'''

def canUnlockAll(boxes):
    ''' checks if all boxes are opened and accessd by the keys on the
    previos box.
    '''
    length = len(boxes)
    keys = set()
    opened_boxes = []
    a = 0

    while a < length:
        oldi = a
        opened_boxes.append(a)
        keys.update(boxes[a])
        for key in keys:
            if key != 0 and key < length and key not in opened_boxes:
                a = key
                break
        if oldi != a:
            continue
        else:
            break

    for a in range(length):
        if a not in opened_boxes and a != 0:
            return False
    return True

