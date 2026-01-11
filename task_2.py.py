def find_common_participants(first_group,second_group,separator=','):
    first_group = first_group.split(separator)
    second_group = second_group.split(separator)
    one_group = list(set(first_group).intersection(second_group))
    one_group.sort()
    return one_group

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(f"Общие участники: {find_common_participants(participants_first_group,participants_second_group,separator='|')}")