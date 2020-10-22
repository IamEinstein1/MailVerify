import uuid
file = open('id.txt', mode='a')


def create_id():
    file.write('YY')
    id = uuid.uuid4()
    file.write(str(id)+'\n')
    return id
