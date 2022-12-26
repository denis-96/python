from jinja2 import Template

cars = [{'model': 'Ауди', 'price': 23000},
        {'model': 'Шкода', 'price': 17300},
        {'model': 'Вольво', 'price': 44300},
        {'model': 'Фольксваген', 'price': 21300}]

# Фильтры

# sum(iterable, attribute=None, start=0)
tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"

# digs = [1, 2, 3, 4, 5]
# tpl = "Сумма {{ digs | sum }}"
# tm = Template(tpl)
# msg = tm.render(digs=digs)

# max
tpl = "Автомобиль: {{ cs | max(attribute='price')  }}"
# tpl = "Автомобиль: {{ (cs | max(attribute='price')).model }}"
    
# min
tpl = "Автомобиль: {{ (cs | min(attribute='price')).model  }}"

# random
tpl = "Автомобиль: {{ cs | random  }}"

# replace
tpl = 'Автомобиль: {{ cs | replace("о", "О") }}'

tm = Template(tpl)
msg = tm.render(cs = cars)
print(msg)


# Блок filter
# {{% filter <название фильтра> %}
# <фрагмент для применения фильтра>
# {% endfilter %}

persons = [{"name": "Алексей", "old": 18, "weight": 78.5},
           {"name": "Николай", "old": 28, "weight": 82.3},
           {"name": "Иван", "old": 33, "weight": 94.0}]
 
tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%}
'''

tm = Template(tpl)
msg = tm.render(users = persons)
print(msg)


# Макроопределения
# похожи на функции в python
html = '''
{%- macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro -%}
 
<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
'''
tm = Template(html)
print(tm.render())


# Вложенные макросы – call

# Модуль Jinja имеет специальное определение:
# {% call[(параметры)] <вызов макроса> %}
# <вложенный шаблон>
# {% endcall %}

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]

html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}
 
{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''
 
tm = Template(html)
msg = tm.render(users = persons)
 
print(msg)