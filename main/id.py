import uuid


# def create_id():
#     file = open('random.txt', mode='w', newline='')
#     id = uuid.uuid4()
#     file.write(str(id)+'\n')
#     file.close()
#     return id


def create_id():
    id = uuid.uuid4()
    print(id)
    file = open("id.txt", mode="a", newline='', encoding='UTF-8')
    print(file)
    # check = open("random.txt", mode="r", newline='')
    file.write(str(id)+'\n')
    file.close()
    return id
