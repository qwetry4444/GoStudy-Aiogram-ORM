from src import messages


def change_group_successful(group_number):
    return f"{messages.CHANGE_GROUP_NUMBER_SUCCESSFUL} {group_number}"

def welcome_message(user_name):
    return messages.WELCOME_MESSAGE.format(user_name)

def lecturer_of_subject(subject: str) -> str:
    return f"{subject}"
# return f"{subject} {messages.lecturer_of_subject}"