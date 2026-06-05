"""Functions to manage and organize queues at Chaitana's roller coaster."""
def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Description goes Here"""
    if ticket_type == 1:
        express_queue.append(person_name) 
        return express_queue
    normal_queue.append(person_name) 
    return normal_queue


def find_my_friend(queue, friend_name):
    """Description goes Here"""
    return queue.index(friend_name)

def add_me_with_my_friends(queue, index, person_name):
    """Description goes Here"""
    queue.insert( index , person_name)
    return queue

def remove_the_mean_person(queue, person_name):
    queue.pop(queue.index(person_name))
    return queue

def how_many_namefellows(queue, person_name):
    """Description goes Here"""
    return queue.count(person_name)

def remove_the_last_person(queue):  
    """Description goes Here"""
    return queue.pop(-1)

def sorted_names(queue):
    """Description goes Here"""
    return sorted(queue)