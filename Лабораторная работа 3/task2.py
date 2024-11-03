# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, delim=','):
    first_group_set = set(first_group.split(delim))
    second_group_set = set(second_group.split(delim))
    common_elements = list(first_group_set & second_group_set)
    return common_elements

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))