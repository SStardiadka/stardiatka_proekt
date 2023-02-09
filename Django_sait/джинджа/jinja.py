from jinja2 import Template
# экранирование символов
class Name:
    def __init__(self, name, age) -> None:   
        self.name = name
        self.age = age
        
tma = Name('<a> dima </a>', 49)      
tm = Template('hi {{tma.name | e}} my {{tma.age}}').render(tma=tma)
print(tm)

# сумма цены
lst =[{'модель':'опель', 'цена':100},
      {'модель':'москвичь', 'цена': 200},
      {'модель':'жигули', 'цена': 300}
]
listt ='сумарная цена автомобилей {{ lst | sum(attribute = "цена")  }}'
sm = Template(listt)
summ = sm.render(lst = lst)
print(summ)

# блок филтр приводит к нужному регистру
persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "иван", "old": 33, "weight": 94.0}
]
 
tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%}
'''
 
tm = Template(tpl)
msg = tm.render(users = persons)
 
print(msg)