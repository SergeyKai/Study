import random

case = ['🔪', "⚔", '🔫']

inventory = []

print('Добро пожаловать в Симулятор открытия кейсов!!!')
print('[1] Открыть кейс')
print('[2] Открыть инвентарь')
print('[0] Выхлод')

action = input('Выбирите действие:')

if action == '1':
    item = random.choice(case)
    inventory.append(item)
    print(f'Поздравляем тебе выпал {item}')
