from jinja2 import Template

# Экранирование и блоки raw, for, if

# Экранирование с помощья raw
data = '''{% raw %}Модуль Jinja вместо
определения {{ name }}
подставляет соответсвующее значение{% endraw %}'''

# tm = Template(data)
# msg = tm.render()
# print(msg)


link = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a>'''

# tm = Template("{{link | e}}")
# msg = tm.render(link=link)


# Блок for и if
cities = [{'id':1, 'city': 'Москва'},
          {'id':5, 'city': 'Тверь'},
          {'id':7, 'city': 'Минск'},
          {'id':8, 'city': 'Смоленск'},
          {'id':11, 'city': 'Калуга'}]

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == "Москва" -%}
    <option>{{c['city']}}</option>
{% else -%}
    {{c.city}}
{% endif -%}
{% endfor -%}
</select>'''
# {% -%} минус убирает перенос строки

tm = Template(link)
msg = tm.render(cities=cities)



print(msg)

