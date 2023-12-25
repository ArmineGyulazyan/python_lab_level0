class EmptyNoteList(Exception):
    pass

class NoteDoesNotExist(Exception):
    pass

def create_note(note_list):
    note = input('Enter your note: ')
    preview = input('Enter preview: ')
    iden = str(len(note_list)+1)
    note_list[iden] = [preview,note]
    print(note_list)
    return note_list


def note_listing(note_list):
    try:
        if not note_list:
            raise EmptyNoteList('The notes are empty')

        for iden in note_list:
            print(iden,'->',note_list[iden][0])
    except EmptyNoteList as e:
        print(e)

def note_retrieval(note_list):
    inp = input('Enter the identifier to retrieve: ')
    try:
        if inp not in note_list:
            raise NoteDoesNotExist("Note with that Id does'not exist")

        print(inp,'->',note_list[inp][1])

    except NoteDoesNotExist as e:
        print(e)

    return note_list
def note_deletion(note_list):
    inp = input('Enter the identifier to delete: ')
    try:
        if inp not in note_list:
            raise NoteDoesNotExist("Note with that Id does'not exist")
        note_list.pop(inp)

    except NoteDoesNotExist as e:
        print(e)

    return note_list

def search_note(note_list):
    kword = input('Enter the keyword to search: ')
    for iden in note_list:
        if kword in note_list[iden][1]:
            print(iden,'->',note_list[iden])

    return note_list

note_list = {}
while True:
    print("\nMenu for Note-Taking\n1.Create Note\n2.List Notes\n3.Note Retrieval\n4.Note Deletion\n5.Search Notes\n6.Exit\n")
    inp = input('Choose an option: ')
    if inp == '1':
        create_note(note_list)
    elif inp == '2':
        note_listing(note_list)
    elif inp == '3':
        note_retrieval(note_list)
    elif inp == '4':
        note_deletion(note_list)
    elif inp == '5':
        search_note(note_list)
    elif inp == '6':
        break
    else:
        print('Invalid input,Choose again')