import datetime

from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, Select, EmailInput, ImageField, ClearableFileInput, DateTimeField



class ArticlesForm(ModelForm):
    form = Select()
    name = TextInput()
    email = EmailInput()
    departament = Select()
    data_incident = TextInput()
    locations = Select()
    city = Select()
    company = Select()
    conditions = Select()
    stop_work = Select()
    observation_in = Select()
    description = Textarea()
    corrective = Textarea()
    category = Select()
    control = Select()
    victims = Select()
    incident_class = Select()
    incident_class_fatal = Select()
    image1 = ImageField(required=False)
    image2 = ImageField(required=False)
    image3 = ImageField(required=False)
    image4 = ImageField(required=False)
    image5 = ImageField(required=False)
    


    class Meta:
        form = [  ('Карта наблюдения', 'Карта наблюдения'),
                  ('Происшествие', 'Происшествие'),]
        departament = [
            ('Наклонно-направленного бурения и телеметрии (DRS)', 'Наклонно-направленного бурения и телеметрии (DRS)'),
                  ('Механизированной добычи (ALS)', 'Механизированной добычи (ALS)'),
            ('Породоразрушающего инструмента (DB)', 'Породоразрушающего инструмента (DB)'),
            ('Буровых растворов и жидкостей заканчивания (DCF)', 'Буровых растворов и жидкостей заканчивания (DCF)'),
            ('Внутрискважинные операции (РР)', 'Внутрискважинные операции (РР)'),
            ('Заканчивание скважин и КРС (CWI)', 'Заканчивание скважин и КРС (CWI)'),
            ('Интегрированных сервисов (IWS)', 'Интегрированных сервисов (IWS)'),
            ('Департамент консультирования по технологиям разработки нефтяных залежей (RDS)', 'Департамент консультирования по технологиям разработки нефтяных залежей (RDS)'),
            ('Центр исследований и разработок (NII)', 'Центр исследований и разработок (NII)'),
            ('Департамент технологий и инвестиций (DTI)', 'Департамент технологий и инвестиций (DTI)'),
            ('Вспомогательные функции (HQ)', 'Вспомогательные функции (HQ)'),
            ('Другое', 'Другое'),
        ]
        locations = [
            ('Производственная база (AMO)', 'Производственная база (AMO)'),
            ('Месторождение (FLD)', 'Месторождение (FLD)'),
            ('Завод (MFG)', 'Завод (MFG)'),
            ("Офис (OFF)", "Офис (OFF)"),
            ("Другое", "Другое")]
        city = [
            ('Астрахань', 'Астрахань'),
            ('Губкинский', 'Губкинский'),
            ('Иркутск', 'Иркутск'),
            ('Когалым', 'Когалым'),
            ('Красноярск', 'Красноярск'),
            ('Ленск', 'Ленск'),
            ('Мегион', 'Мегион'),
            ('Москва', 'Москва'),
            ('Нефтеюганск', 'Нефтеюганск'),
            ('Нижневартовск', 'Нижневартовск'),
            ('Новосибирск', 'Новосибирск'),
            ('Новый Уренгой', 'Новый Уренгой'),
            ('Ноябрьск', 'Ноябрьск'),
            ('Нягань', 'Нягань'),
            ('Оренбург', 'Оренбург'),
            ('Пермь', 'Пермь'),
            ('Тарко-Сале', 'Тарко-Сале'),
            ('Тюмень', 'Тюмень'),
            ('Уват', 'Уват'),
            ('Усинск', 'Усинск'),
            ('Южно-Сахалинск', 'Южно-Сахалинск'),
            ('Ванкорский производственный участок', 'Ванкорский производственный участок'),
            ('Кондинский производственный участок', 'Кондинский производственный участок'),
            ('Пайяхский ЛУ КП2', 'Пайяхский ЛУ КП2'),
            ('Пайяхский ЛУ КП6', 'Пайяхский ЛУ КП6'),
            ('Соровский производственный участок', 'Соровский производственный участок'),
            ('Другое', 'Другое')]
        company = [
            ('Группа компаний "Технологии ОФС"', 'Группа компаний "Технологии ОФС"'),
            ('Подрядные организации или иное', 'Подрядные организации или иное'),
            ('Компания Заказчик', 'Компания Заказчик')]
        conditions = [
            ("Опасные действия", "Опасные действия"),
            ("Опасные условия", "Опасные условия"),
            ("Безопасные действия", "Безопасные действия"),
            ("Безопасные условия", "Безопасные условия")
        ]
        stop_work = [
            ('Нет', 'Нет'),
            ('Да', 'Да')
        ]
        observation_in = [
            ('Группа компаний "Технологии ОФС"', 'Группа компаний "Технологии ОФС"'),
            ('Подрядная организация', 'Подрядная организация')
        ]
        category = [
            ("Инструменты и оборудование", "Инструменты и оборудование"),
            ("Погрузо-разгрузочные работы", "Погрузо-разгрузочные работы"),
            ("Средства индивидуальной защиты (СИЗ)", "Средства индивидуальной защиты (СИЗ)"),
            ("Человеческий фактор (прим. темп работы, нахождение в зоне потенциальной опасности)", "Человеческий фактор (прим. темп работы, нахождение в зоне потенциальной опасности)"),
            ("Обмен информацией", "Обмен информацией"),
            ("Внешние условия (прим. погодные, дорожные, шум)", "Внешние условия (прим. погодные, дорожные, шум)"),
            ("Пожарная безопасность", "Пожарная безопасность"),
            ("Радиационная безопасность", "Радиационная безопасность"),
            ("Химические реагенты", "Химические реагенты"),
            ("Транспортная безопасность", "Транспортная безопасность"),
            ("Содержание зданий и сооружений", "Содержание зданий и сооружений"),
            ("Экологическая безопасность", "Экологическая безопасность")
        ]
        victims = [
            ('Нет', 'Нет'),
            ('1', '1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('Более 4', 'Более 4')
        ]
        incident_class = [
            ("Незначительный", "Незначительный"),
            ("Серьезный (Serious)", "Серьезный (Serious)"),
            ("Крупный (Major)", "Крупный (Major)"),
            ("Катастрофический (Catastrophic)", "Катастрофический (Catastrophic)")
        ]
        incident_class_fatal = [
            ("Смертельный несчастный случай (Fatality)", "Смертельный несчастный случай (Fatality)"),
            ("С временной потерей трудоспособности (травма) (Day Away from Work Case)", "С временной потерей трудоспособности (травма) (Day Away from Work Case)"),
            ("Медицинское лечение за пределами первой медицинской помощи (MTBFA)", "Медицинское лечение за пределами первой медицинской помощи (MTBFA)"),
            ("Профессиональное заболевание", "Профессиональное заболевание"),
            ("Экстренная эвакуация (Emergency evacuation)", "Экстренная эвакуация (Emergency evacuation)"),
            ("Оказание первой медицинской помощи (First Aid)", "Оказание первой медицинской помощи (First Aid)"),
            ("Потенциально опасное повторяющееся происшествие (Hi-Po)", "Потенциально опасное повторяющееся происшествие (Hi-Po)"),
            ("Экологическое происшествие", "Экологическое происшествие"),
            ("Пожар/Взрыв", "Пожар/Взрыв"),
            ("Радиация", "Радиация"),
            ("Происшествие без последствий (Near Miss)", "Происшествие без последствий (Near Miss)"),
            ("Нарушение 9 жизненно-важных правил (Life Saving Rules)", "Нарушение 9 жизненно-важных правил (Life Saving Rules)"),
            ("Дорожно-транспортное происшествие", "Дорожно-транспортное происшествие"),
            ("Другое", "Другое")
        ]

        model = Articles
        fields = ['form', 'name', 'email', 'departament', 'data_incident', 'locations', 'city', 'company', 'conditions', 'stop_work', 'observation_in', 'description', 'corrective', 'category', 'control', 'victims', 'incident_class', 'incident_class_fatal', 'image1', 'image2', 'image3', 'image4', 'image5']
        widgets = {

            "form": Select(choices=form, attrs={'class' : 'form-cotrol', 'required': True,}),
            "name": TextInput(attrs= {'class' : 'form-cotrol', 'required': True, 'placeholder': "Ваше ФИО"}),
            "email": EmailInput(attrs={'class': 'form-cotrol', 'required': True, 'placeholder': "Ваш E-mail", }),
            "departament": Select(choices=departament, attrs={'class': 'form-cotrol', 'required': True,}),
            "data_incident": TextInput(attrs={'type':'datetime-local', 'class': 'form-cotrol', 'required': True, 'placeholder': "Дата и время"}),
            "locations": Select(choices=locations, attrs={'class': 'form-cotrol', 'required': True,}),
            "city": Select(choices=city, attrs={'class': 'form-cotrol', 'required': True, }),
            "company": Select(choices=company, attrs={'class': 'form-cotrol', 'required': True, }),
            "conditions": Select(choices=conditions, attrs={'class': 'form-cotrol', 'required': True, }),
            "stop_work": Select(choices=stop_work, attrs={'class': 'form-cotrol', 'required': True, }),
            "observation_in": Select(choices=observation_in, attrs={'class': 'form-cotrol', 'required': True, }),
            "description": Textarea(attrs= {'class' : 'form-cotrol', 'required': True, 'placeholder': "Опишите наблюдение", 'minlength': '20', 'rows': '1'}),
            "corrective": Textarea(attrs= {'class' : 'form-cotrol', 'required': True, 'placeholder': "Корректирующие действия", 'minlength': '20', 'rows': '1'}),
            "category": Select(choices=category, attrs={'class': 'form-cotrol', 'required': True, }),
            "control": Select(choices=stop_work, attrs={'class': 'form-cotrol', 'required': True, }),
            "victims": Select(choices=victims, attrs={'class': 'form-cotrol', 'required': True, }),
            "incident_class": Select(choices=incident_class, attrs={'class': 'form-cotrol', 'required': True, }),
            "incident_class_fatal": Select(choices=incident_class_fatal, attrs={'class': 'form-cotrol', 'required': True, }),
            "image1": ClearableFileInput(attrs={'class': 'form-cotrol', 'required': False}),
            "image2": ClearableFileInput(attrs={'class': 'form-cotrol', 'required': False}),
            "image3": ClearableFileInput(attrs={'class': 'form-cotrol', 'required': False}),
            "image4": ClearableFileInput(attrs={'class': 'form-cotrol', 'required': False}),
            "image5": ClearableFileInput(attrs={'class': 'form-cotrol', 'required': False}),

        }