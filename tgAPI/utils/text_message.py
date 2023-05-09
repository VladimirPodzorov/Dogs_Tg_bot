from typing import Dict


def back_message(item: Dict):
    return (
        f"{item['image_link']}\n<b>Порода: {item['name']}\nМинимальный вес(сучка): {item['min_weight_female']} фунтов\n"
        f"Максимальный вес(кобель): {item['max_weight_male']} фунтов\nМинимальный рост(сучка): {item['min_height_female']}"
        f" дюйма\nМаксимальный рост(кабель): {item['max_height_male']} дюйма\nЛиняет: {item['shedding']} из 5\n"
        f"Дрессируемость: {item['trainability']} из 5\nНасколько вокальной является порода(лай): {item['barking']} из 5\n"
        f"Способность к охране: {item['protectiveness']} из 5\n"
        f"Дружелюбность с детьми: {item['good_with_children']} из 5\n"
        f"Дружелюбность с другими собаками: {item['good_with_other_dogs']} из 5\n"
        f"Энергичность: {item['energy']} из 5\nПродолжительность жизни: {int(item['min_life_expectancy'])} - "
        f"{int(item['max_life_expectancy'])} лет</b>"
    )
