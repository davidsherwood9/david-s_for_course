def find_common_participants(first_group, second_group, sep=","):
    common_participants = set(first_group.split("|")).intersection(set(second_group.split("|")))
    answer = list(sep.join(common_participants).split())
    return answer.sort()    # не получается вернуть сортированный список. Если убрать в этой строке .sort(), то все норм



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print("Общие участники:", find_common_participants(participants_first_group, participants_second_group, sep=","))
