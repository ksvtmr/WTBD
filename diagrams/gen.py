import os
OUT=os.path.join(os.path.dirname(__file__),'bare' if os.environ.get('BARE') else 'html')
DK='#14302B'; LT='#F6F4EE'; BG2='#E9EEE9'; AC='#D9822B'; AC2='#A3561A'; TX='#3F4B46'; MU='#6B746F'; CARD='#FFFDF8'; BR='#DCD7CB'; GR='#7A8F86'
CSS=f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1920px;height:1080px;background:{LT};font-family:'Liberation Sans',Arial,sans-serif;color:{TX};padding:80px 96px;display:flex;flex-direction:column;gap:36px;overflow:hidden}}
.ey{{font-size:24px;letter-spacing:3px;text-transform:uppercase;color:{AC2};font-weight:700}}
h1{{font-family:'Liberation Serif',Georgia,serif;font-size:56px;color:{DK};line-height:1.1}}
.card{{background:{CARD};border:2px solid {BR};border-radius:16px;padding:22px}}
.dk{{background:{DK};color:{LT};border-radius:16px;padding:22px}}
.ft{{position:absolute;left:96px;bottom:40px;font-size:22px;color:{MU}}}
h3{{font-size:28px;color:{DK};margin-bottom:8px}}
.dk h3{{color:#F2B36F}}
p,li{{font-size:23px;line-height:1.35}}
ul{{padding-left:28px}}
.row{{display:flex;gap:20px}}
.arr{{font-size:44px;color:{AC};align-self:center;font-weight:700}}
.tag{{display:inline-block;background:{BG2};border-radius:999px;padding:4px 14px;font-size:20px;color:{DK};margin:3px 4px 0 0}}
"""
BARE=os.environ.get('BARE')
def page(name,ey,title,body,foot=''):
    if BARE:
        css=CSS.replace("width:1920px;height:1080px","width:1664px;height:700px").replace("padding:80px 96px;display:flex;flex-direction:column;gap:36px","padding:0;display:flex;flex-direction:column;gap:24px")
        h=f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
        open(os.path.join(OUT,name+'.html'),'w').write(h); return
    h=f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div><p class='ey'>{ey}</p><h1>{title}</h1></div>{body}<p class='ft'>{foot}</p></body></html>"
    open(os.path.join(OUT,name+'.html'),'w').write(h)

# 01 Architecture
page('01_arhitektura','Архитектура','Городская платформа ресурсного оборота: 4 продукта на одном слое данных',f"""
<div style='display:flex;flex-direction:column;gap:{10 if BARE else 18}px;flex:1'>
<div class='row'>
 {''.join(f"<div class='card' style='flex:1;border-top:8px solid {c}'><h3>{t}</h3><p>{d}</p><div style='margin-top:10px'>{''.join(f'<span class=tag>{x}</span>' for x in tags)}</div></div>" for t,d,tags,c in [
 ('Житель','Удобный раздельный сбор у дома',['4 фракции','QR на площадке','итоги района'],AC),
 ('Оператор вывоза','Маршруты и контроль качества',['аудит маршрутов','весы на машинах','засорённость'],GR),
 ('Переработчик','Стабильные фракции',['прогноз объёмов','стандарты','образцы'],GR),
 ('Акимат и жители','Управление и доверие',['публичная панель','KPI','бюджет'],DK)])}
</div>
<div class='arr' style='font-size:30px;line-height:1'>↑ данные ↓ решения</div>
<div class='dk' style='display:flex;gap:24px;align-items:center'>
 <div style='flex:1'><h3>ИС учёта материальных потоков (статья 1,5 млрд ₸)</h3><p style='color:#E7EEEA'>Реестр контейнерных площадок · весовой учёт · маршруты · засорённость · сбыт фракций · освоение бюджета</p></div>
 <div style='display:flex;gap:10px;flex-wrap:wrap;width:620px'>{''.join(f"<span class=tag style='background:#24463F;color:#F6F4EE'>{x}</span>" for x in ['QR-коды площадок','весы на мусоровозах','GPS маршрутов','лаборатория качества','открытые данные'])}</div>
</div>
<div class='arr' style='font-size:30px;line-height:1'>↑ поток ↓</div>
<div class='row'>
 {''.join(f"<div class='card' style='flex:1;background:{BG2}'><h3>{t}</h3><p>{d}</p></div>" for t,d in [
 ('Контейнерная сеть','8,0 млрд ₸ · раздельный сбор'),('Транспорт и логистика','6,0 млрд ₸ · с оператором'),('Комплекс сортировки + компост','35,0 млрд ₸ · модульно'),('Площадка и сети','9,0 млрд ₸ · по итогам изысканий')])}
</div></div>""",'Концепция операционной модели, не ИТ-прототип. Суммы — статьи базового бюджета кейса.')

# 02 Material flow
page('02_potok_othodov','Процесс','Путь отходов: от двора до вторичного сырья',f"""
<div class='row' style='align-items:stretch;height:300px'>
{('<div class=arr>→</div>').join(f"<div class='{k}' style='flex:1;display:flex;flex-direction:column;gap:8px'><h3>{t}</h3><p>{d}</p></div>" for k,t,d in [
 ('card','1. Домохозяйство','360 тыс. т/год. Органика 38%, бумага 15%, пластик 14%, стекло 9%, металл 4%, прочее 20%'),
 ('card','2. Контейнерная площадка','4 фракции + смешанные. QR, засорённость сейчас до 25%'),
 ('card','3. Вывоз','Оператор, маршруты по фракциям, весы и GPS'),
 ('dk','4. Комплекс','Приёмка и контроль качества → сортировка → компостирование органики'),
])}
</div>
<div class='row'>
 <div class='card' style='flex:1;border-left:8px solid {GR}'><h3>Товарные фракции</h3><p>45–75 тыс. т/год → переработчики по договорам</p></div>
 <div class='card' style='flex:1;border-left:8px solid {GR}'><h3>Компост / стабилизат</h3><p>Из ~137 тыс. т органики (доля выхода — допущение, проверить)</p></div>
 <div class='card' style='flex:1;border-left:8px solid {AC}'><h3>Полигон</h3><p>Остаток. Цель: −25–35% к захоронению 2026 года</p></div>
</div>""",'Объёмы по кейсу; выход фракций и компоста — допущения команды для проверки морфологией и пилотом.')

# 03 Value tree
br=[('Уменьшить смешанный поток',['Раздельный сбор 4 фракций','Контейнеры у дома','PAYT-пилот (2027)']),
    ('Повысить качество вторсырья',['Контроль засорённости','Обучение и подсказки','Обратная связь УК']),
    ('Создать устойчивый сбыт',['Меморандумы с переработчиками','Стандарты фракций','Прогноз объёмов']),
    ('Снизить риски проекта',['Площадка по данным изысканий','Публичное обсуждение и слушания','Поэтапные закупки'])]
page('03_derevo_cennosti','Бизнес-анализ','Дерево ценности проекта',f"""
<div style='display:flex;flex-direction:column;align-items:center;gap:0;flex:1'>
<div class='dk' style='width:900px;text-align:center'><h3 style='margin:0'>Сократить захоронение и вернуть материалы в оборот</h3></div>
<div style='width:3px;height:30px;background:{DK}'></div>
<div style='width:1350px;height:3px;background:{DK}'></div>
<div class='row' style='width:100%;gap:24px'>
{''.join(f"<div style='flex:1;display:flex;flex-direction:column;align-items:center'><div style='width:3px;height:30px;background:{DK}'></div><div class='card' style='width:100%;border-top:8px solid {AC};text-align:center'><h3 style='margin:0'>{t}</h3></div>{''.join(f'<div style=\"width:3px;height:18px;background:{GR}\"></div><div style=\"width:88%;background:{BG2};border-radius:12px;padding:14px;text-align:center\"><p>{x}</p></div>' for x in xs)}</div>" for t,xs in br)}
</div></div>""",'Каждая ветка имеет KPI на публичной панели.')

# 04 Resident journey
st=[('Узнал о проекте','Страхи, слухи, недоверие','Открытая карта площадок, публикации, общественный совет'),
    ('Решил сортировать','Не понятно, что куда','Одна инструкция: органика / бумага / пластик-металл / стекло'),
    ('Вынес отходы','Контейнер далеко или полон','Контейнер рядом с обычным, вывоз по графику'),
    ('Ошибся','Нет обратной связи','Подсказка на контейнере, сигнал управляющей компании'),
    ('Увидел результат','Не верит, что работает','Итоги района по QR и на публичной панели')]
page('04_put_zhitelya','Продуктовый подход','Путь жителя: сделать правильную сортировку проще, чем неправильную',f"""
<div class='row' style='flex:1'>
{''.join(f"<div style='flex:1;display:flex;flex-direction:column;gap:14px'><div class='dk' style='text-align:center;padding:18px'><p style='font-size:20px;color:#F2B36F'>Шаг {i+1}</p><h3 style='margin:0;color:{LT}'>{a}</h3></div><div class='card' style='border-left:8px solid {AC};flex:1'><p style='font-size:20px;color:{AC2};font-weight:700'>БАРЬЕР</p><p>{b}</p></div><div class='card' style='border-left:8px solid {GR};flex:1.3'><p style='font-size:20px;color:{GR};font-weight:700'>РЕШЕНИЕ</p><p>{c}</p></div></div>" for i,(a,b,c) in enumerate(st))}
</div>""",'Пилот в 2 районах (многоэтажный и частный сектор) проверяет каждый шаг.')

# 05 Dual track
page('05_dve_dorozhki','Проектное управление','Две дорожки сходятся в точке решения 2 февраля 2027',f"""
<div style='display:flex;gap:24px;flex:1;align-items:center'>
<div style='flex:1;display:flex;flex-direction:column;gap:28px'>
 <div class='card' style='border-left:10px solid {AC}'><h3>Проверка (discovery): что сработает в Армане?</h3><div class='row' style='gap:10px'>{''.join(f'<span class=tag>{x}</span>' for x in ['морфология отходов','пилот сбора в 2 районах','интервью и опрос жителей','модель PAYT','меморандумы о сбыте','аудит маршрутов'])}</div></div>
 <div class='card' style='border-left:10px solid {GR}'><h3>Подготовка (delivery): что готовим уже сейчас?</h3><div class='row' style='gap:10px'>{''.join(f'<span class=tag>{x}</span>' for x in ['изыскания A и B','ТЗ конфигурации','цены от 3+ поставщиков','прогноз бюджета','пакет для слушаний','закупочная документация'])}</div></div>
</div>
<div class='arr' style='font-size:80px'>⟩</div>
<div class='dk' style='width:420px'><h3>Точка решения</h3><p style='color:#E7EEEA'>Delivery переходит к закупке и стройке, только когда discovery подтвердил поток, качество и приёмлемость площадки</p></div>
</div>""",'Главная ошибка, от которой защищает модель: начать стройку до проверки.')

# 06 Gantt 90 days
weeks=13
tasks=[('Этап 1. Стабилизация',0,2,DK),('Мораторий, Устав, комитет',0,1,AC),('Ответ маслихату, встреча с жителями',0,2,AC),
('Этап 2. Сбор фактов',2,8,DK),('Прогноз бюджета для финслужбы',2,4,GR),('Запрос цен у 3+ поставщиков',2,4,GR),('Изыскания площадок A и B',4,10,GR),('Морфология и весовой учёт',4,8,GR),('Пилот раздельного сбора',4,12,GR),('Аудит маршрутов с оператором',2,7,GR),
('Этап 3. Варианты и обсуждение',8,12,DK),('Сравнение 3 конфигураций',9,11,GR),('Публичное обсуждение 20.01',10,11,AC),('Модель PAYT, меморандумы о сбыте',9,12,GR),
('Этап 4. Точка решения 02.02',12,13,AC)]
labels=['4 ноя','11','18','25','2 дек','9','16','23','30','6 янв','13','20','27']
rows=''.join(f"<div style='display:flex;align-items:center;height:44px'><div style='width:520px;font-size:22px;{'font-weight:700;color:'+DK if c==DK else ''}'>{t}</div><div style='flex:1;position:relative;height:30px'><div style='position:absolute;left:{s/weeks*100}%;width:{(e-s)/weeks*100}%;height:30px;background:{c};border-radius:8px'></div></div></div>" for t,s,e,c in tasks)
page('06_gantt_90_dney','План на 90 дней','Дорожная карта 4 ноября 2026 – 2 февраля 2027',f"""
<div style='display:flex;flex-direction:column'>
<div style='display:flex;margin-bottom:6px'><div style='width:520px'></div><div style='flex:1;display:flex'>{''.join(f"<div style='flex:1;font-size:19px;color:{MU};border-left:1px solid {BR};padding-left:4px'>{l}</div>" for l in labels)}</div></div>
{rows}</div>""",'Недели с понедельника; оранжевые — вехи и коммуникации, тёмные — этапы.')

# 07 Stakeholders 2x2
pts=[('Акимат (заказчик)',90,88),('Финслужба',85,70),('Маслихат',80,78),('Жители (6 800 подп.)',78,95),('Минэкологии / экспертиза',92,45),('Поставщик оборудования',45,80),('Оператор вывоза',60,72),('Переработчик',40,62),('Техническая группа',50,55),('СМИ',55,40)]
dots=''.join(f"<div style='position:absolute;left:{x*0.72}%;bottom:{y*0.92}%;transform:translate(-8px,8px);display:flex;align-items:center;gap:8px'><div style='width:18px;height:18px;border-radius:50%;background:{AC if y>75 and x>70 else DK}'></div><span style='font-size:21px;color:{DK};background:{LT};white-space:nowrap'>{n}</span></div>" for n,x,y in pts)
page('07_steikholdery','Заинтересованные стороны','Карта стейкхолдеров: влияние × интерес',f"""
<div style='display:flex;gap:30px;flex:1'>
<div style='position:relative;width:1050px;height:{640 if BARE else 760}px'>
 <div style='position:absolute;inset:0 0 40px 50px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;border:2px solid {BR}'>
  <div style='background:{BG2};padding:12px;font-size:20px;color:{MU}'>Информировать регулярно</div><div style='background:#F3E4D2;padding:12px;font-size:20px;color:{AC2};font-weight:700;text-align:right'>Управлять плотно</div>
  <div style='padding:12px;font-size:20px;color:{MU};align-self:end'>Наблюдать</div><div style='background:{BG2};padding:12px;font-size:20px;color:{MU};text-align:right;align-self:end'>Держать удовлетворёнными</div>
 </div>
 <div style='position:absolute;left:50px;right:0;top:0;bottom:40px'>{dots}</div>
 <p style='position:absolute;bottom:0;left:50px;right:0;text-align:center;font-size:22px'>Влияние →</p>
 <p style='position:absolute;left:-20px;top:300px;transform:rotate(-90deg);font-size:22px'>Интерес →</p>
</div>
<div style='flex:1;display:flex;flex-direction:column;gap:14px'>
 <div class='card'><h3>Жители</h3><p>Встреча до 18.11, совет, обсуждение 20.01</p></div>
 <div class='card'><h3>Маслихат</h3><p>Ответ до 18.11, график раскрытия</p></div>
 <div class='card'><h3>Финслужба</h3><p>Прогноз 30.11, далее ежемесячно</p></div>
 <div class='card'><h3>Поставщик</h3><p>Требования 02.12, без обязательств</p></div>
</div></div>""",'Положение точек — экспертная оценка команды.')

# 08 Risk heatmap
risks=[('R1',4,5),('R2',4,4),('R3',4,3),('R4',4,3),('R5',3,4),('R6',3,4),('R7',3,4),('R8',3,3),('R9',3,4),('R10',3,4),('R11',3,3),('R12',4,2),('R13',2,5)]
def col(s): return '#C9653A' if s>=15 else ('#E8B27A' if s>=10 else ('#E9E2C8' if s>=5 else BG2))
cells=''
for imp in range(5,0,-1):
    for pr in range(1,6):
        ids=[r for r,p,i in risks if p==pr and i==imp]
        cells+=f"<div style='background:{col(pr*imp)};border-radius:8px;display:flex;flex-wrap:wrap;align-content:center;justify-content:center;gap:6px;padding:6px'>{''.join(f'<span style=\"background:{DK};color:{LT};border-radius:999px;padding:3px 10px;font-size:20px\">{x}</span>' for x in ids)}</div>"
legend=[('R1','Протест при площадке A'),('R2','Рост цены оборудования'),('R3','Срыв срока'),('R4','Засорённость сбора'),('R5','Нет сбыта фракций'),('R6','Проблемы на B'),('R7','Затягивание ОВОС'),('R9','Исчерпание резерва'),('R10','Давление ускорить закупку'),('R13','Нарушение госзакупок')]
page('08_matrica_riskov','Риски','Тепловая карта рисков: вероятность × влияние',f"""
<div style='display:flex;gap:40px;flex:1'>
<div style='display:flex;gap:12px'>
 <div style='display:flex;flex-direction:column;justify-content:space-around;font-size:22px;width:130px;text-align:right;height:664px'>{''.join(f'<span>Влияние {i}</span>' for i in range(5,0,-1))}</div>
 <div><div style='display:grid;grid-template-columns:repeat(5,150px);grid-template-rows:repeat(5,128px);gap:6px'>{cells}</div>
 <div style='display:grid;grid-template-columns:repeat(5,150px);gap:6px;font-size:22px;text-align:center;margin-top:8px'>{''.join(f'<span>Вер. {i}</span>' for i in range(1,6))}</div></div>
</div>
<div style='flex:1;display:flex;flex-direction:column;gap:8px'>{''.join(f"<p><b style='color:{DK}'>{a}</b> {b}</p>" for a,b in legend)}<p style='color:{MU};margin-top:10px'>Тёмно-оранжевая зона ≥ 15 баллов, оранжевая 10–14.</p></div>
</div>""",'Полный реестр: 13 рисков с мерами и триггерами.')

# 09 Sites
crit=[('Соц.-эколог. риск',35,[1,4,5]),('Срок',20,[5,4,1]),('Стоимость',15,[5,4,2]),('Логистика',15,[5,3,1]),('Инфраструктура',15,[5,3,1])]
cols=[AC,DK,GR]
bars=''
for si,s in enumerate('ABC'):
    segs=''.join(f"<div style='width:{w*v/5*14}px;background:{['#C9653A','#14302B','#7A8F86','#B9C7C0','#E8B27A'][ci]};height:56px;display:flex;align-items:center;justify-content:center;color:{LT if ci<3 else DK};font-size:18px'>{(f'{w*v/100:.2f}'.replace('.',',') if w*v>=70 else '')}</div>" for ci,(n,w,vals) in enumerate(crit) for v in [vals[si]])
    tot=sum(w*vals[si]/100 for n,w,vals in crit)
    bars+=f"<div style='display:flex;align-items:center;gap:16px'><div style='width:240px;font-size:30px;font-weight:700;color:{DK}'>Площадка {s}</div><div style='display:flex'>{segs}</div><div style='font-size:32px;font-weight:700;color:{DK}'>{f'{tot:.2f}'.replace('.',',')}</div></div>"
leg=''.join(f"<span style='display:flex;align-items:center;gap:8px;font-size:22px'><span style='width:22px;height:22px;background:{c};display:inline-block'></span>{n} ({w}%)</span>" for (n,w,v),c in zip(crit,['#C9653A','#14302B','#7A8F86','#B9C7C0','#E8B27A']))
page('09_matrica_ploshadok','Площадки','Многокритериальная оценка: A и B почти равны, решает социальный риск',f"""
<div style='display:flex;flex-direction:column;gap:30px'>{bars}</div>
<div style='display:flex;gap:28px;flex-wrap:wrap'>{leg}</div>
<div class='row'><div class='card' style='flex:1'><h3>Фильтр да/нет до баллов</h3><p>Санитарно-защитная зона и экологическая оценка. Для A (0,8 км до жилья) — под вопросом.</p></div><div class='card' style='flex:1'><h3>Чувствительность</h3><p>Если вес социального риска &lt; 30%, лидирует A. Поэтому решаем по изысканиям, а не по мнениям.</p></div></div>""",'Баллы 1–5 и веса — оценка команды; итог из 5.')

# 10 Budget
b90=[('Изыскания A и B',320),('Техконсультант',150),('Пилот сбора',70),('Морфология',60),('Резерв',60),('Информирование',50),('Юристы',40)]
mx=320
bb=''.join(f"<div style='display:flex;align-items:center;gap:14px;height:52px'><div style='width:260px;font-size:23px;text-align:right'>{n}</div><div style='width:{v/mx*(420 if BARE else 560)}px;height:38px;background:{DK if n!='Резерв' else GR};border-radius:6px'></div><div style='font-size:23px;font-weight:700;color:{DK}'>{v}</div></div>" for n,v in b90)
wf=[('Резерв базы',6.0,0,6.0,DK),('+15% оборуд. (60% статьи)',-3.15,2.85,6.0,'#C9653A'),('Информирование',-0.5,2.35,2.85,'#E8B27A'),('Остаток',2.35,0,2.35,GR)]
sc=62 if BARE else 80
wfh=''.join(f"<div style='display:flex;flex-direction:column;align-items:center;width:{125 if BARE else 170}px'><div style='height:{(6.6-hi)*sc}px'></div><div style='font-size:22px;font-weight:700;color:{DK}'>{f'{v:+.2f}'.replace('.',',')}</div><div style='height:{(hi-lo)*sc}px;width:{80 if BARE else 110}px;background:{c};border-radius:6px'></div><div style='height:{lo*sc}px'></div><p style='font-size:20px;text-align:center;margin-top:8px'>{n}</p></div>" for n,v,lo,hi,c in wf).replace('+6,00','6,00').replace('+2,35','2,35')
page('10_budzhet','Деньги','750 млн ₸ на 90 дней и стресс-тест резерва 70 млрд ₸',f"""
<div style='display:flex;gap:60px;flex:1'>
<div class='card' style='flex:1'><h3>90 дней, млн ₸ (итого 750)</h3>{bb}</div>
<div class='card' style='flex:1'><h3>Резерв проекта, млрд ₸</h3><div style='display:flex;align-items:flex-end;gap:10px;margin-top:10px'>{wfh}</div><p style='color:{MU}'>Худший случай (+15% на всю статью 35 млрд): −5,25 → резерв ≈ 0,25</p></div>
</div>""",'Доля оборудования 60% — допущение; поставщик не расшифровал статью.')

# 11 Go/no-go
crits=['1. Площадка прошла санитарный и экологический фильтр','2. Цена подтверждена 2+ предложениями, резерв ≥ 5%','3. Меморандумы о сбыте ≥ 50% фракций','4. Схема вывоза согласована с оператором','5. Перепланированный срок принят заказчиком']
page('11_go_no_go','Точка решения','Логика решения 2 февраля 2027',f"""
<div style='display:flex;gap:24px;align-items:center;flex:1'>
<div class='dk' style='width:360px'><h3>Пакет решения</h3><p style='color:#E7EEEA'>Изыскания, цены, пилот, обсуждение, прогноз бюджета и срока</p></div>
<div class='arr'>→</div>
<div class='card' style='flex:1'>{''.join(f'<p style="padding:8px 0;border-bottom:1px solid {BR}">{c}</p>' for c in crits)}</div>
<div class='arr'>→</div>
<div style='width:420px;display:flex;flex-direction:column;gap:16px'>
 <div class='card' style='border-left:10px solid {GR}'><h3>Все 5 выполнены</h3><p>GO: закупка оборудования / EPC</p></div>
 <div class='card' style='border-left:10px solid #E8B27A'><h3>Не выполнены 3–5</h3><p>GO с мерами в плане</p></div>
 <div class='card' style='border-left:10px solid #C9653A'><h3>Не выполнены 1 или 2</h3><p>+60 дней проверки, крупных обязательств нет</p></div>
</div></div>""",'Критерии утверждаются вместе с Уставом.')

# 12 Governance
page('12_upravlenie','Управление проектом','Кто принимает решения',f"""
<div style='display:flex;flex-direction:column;align-items:center;gap:0;flex:1'>
<div class='dk' style='width:640px;text-align:center'><h3 style='margin:0'>Спонсор: аким / заместитель</h3><p style='color:#E7EEEA'>Устав, точка решения, изменение срока</p></div>
<div style='width:3px;height:30px;background:{DK}'></div>
<div class='row' style='align-items:center'>
 <div class='card' style='width:430px;background:{BG2}'><h3>Общественный совет</h3><p>Жители, эксперты, НКО: рассматривает материалы до решений по площадке</p></div>
 <div style='width:40px;height:3px;background:{GR}'></div>
 <div class='card' style='width:620px;border-top:8px solid {AC}'><h3>Управляющий комитет</h3><p>Зам. акима, финслужба, ЖКХ и экология, депутат маслихата (наблюдатель). Изменения &gt; 1% бюджета или 1 мес., резерв</p></div>
 <div style='width:40px;height:3px;background:{GR}'></div>
 <div class='card' style='width:430px;background:{BG2}'><h3>Финслужба</h3><p>Ежемесячный прогноз и обязательства</p></div>
</div>
<div style='width:3px;height:30px;background:{DK}'></div>
<div class='card' style='width:640px;text-align:center'><h3 style='margin:0'>Руководитель проекта и PMO</h3><p>Ежедневное управление, отчёт раз в 2 недели, журнал изменений</p></div>
<div style='width:3px;height:30px;background:{DK}'></div>
<div class='row'>{''.join(f"<div class='card' style='width:330px;text-align:center'><p>{x}</p></div>" for x in ['Техконсультант','Изыскатели','Рабочая группа с оператором','Юристы и закупки'])}</div>
</div>""",'Публикация ключевых материалов не позднее 10 дней после утверждения.')

# 13 Roadmap to 2028
ph=[('Стадия 0: проверка','ноя 2026 – фев 2027',0,3.1,AC),('Контейнеры, сбор, ИС учёта','2027',3,14,GR),('Подготовка площадки','фев – июн 2027',3.1,8,DK),('Проект и экспертиза','фев – июл 2027',3.1,9,DK),('Закупка / EPC','июн – сен 2027',7,11,DK),('Строительство и поставка','авг 2027 – июл 2028',9,21,DK),('Пусконаладка','июл – дек 2028',20,26,'#C9653A')]
T=26
months=['ноя 26','фев 27','май 27','авг 27','ноя 27','фев 28','май 28','авг 28','ноя 28']
rr=''.join(f"<div style='display:flex;align-items:center;height:70px'><div style='width:440px'><p style='font-weight:700;color:{DK}'>{n}</p><p style='font-size:19px;color:{MU}'>{d}</p></div><div style='flex:1;position:relative;height:40px'><div style='position:absolute;left:{s/T*100}%;width:{(e-s)/T*100}%;height:40px;background:{c};border-radius:8px'></div></div></div>" for n,d,s,e,c in ph)
page('13_doroznaya_karta','Сроки','Дорожная карта до ввода комплекса',f"""
<div style='display:flex;flex-direction:column;position:relative'>
<div style='display:flex'><div style='width:440px'></div><div style='flex:1;display:flex'>{''.join(f"<div style='flex:1;font-size:19px;color:{MU};border-left:1px solid {BR};padding-left:4px'>{m}</div>" for m in months)}</div></div>
{rr}
<div style='position:absolute;left:calc(440px + (100% - 440px) * {21.9/T});top:30px;bottom:0;border-left:3px dashed #C9653A'></div>
<p style='position:absolute;left:calc(440px + (100% - 440px) * {21.9/T} + 10px);top:24px;font-size:20px;color:#A3561A;font-weight:700'>план 31.08.2028</p>
</div>""",'Реалистичный ввод: октябрь–декабрь 2028 (+2–4 мес.). Длительности — оценки команды.')
print('ok')

# ===== v3 overrides =====
# 02 flow with compost/stabilisate split
page('02_potok_othodov','Процесс','Путь отходов: от двора до подтверждённого покупателя',f"""
<div class='row' style='align-items:stretch;height:{250 if BARE else 300}px'>
{('<div class=arr>→</div>').join(f"<div class='{k}' style='flex:1;display:flex;flex-direction:column;gap:8px'><h3>{t}</h3><p>{d}</p></div>" for k,t,d in [
 ('card','1. Источник','360 тыс. т/год (оценка). Органика 38%, бумага 15%, пластик 14%, стекло 9%, металл 4%, прочее 20%'),
 ('card','2. Сбор','Дворы: 4 фракции + остаток. Крупные источники: магазины, рынки, столовые. Тара: 5–10 магазинов'),
 ('card','3. Вывоз','Оператор: маршруты по фракциям, весы и GPS'),
 ('dk','4. Обработка','Приёмка и контроль качества → модульная сортировка → биологическая обработка органики'),
])}
</div>
<div class='row'>
 <div class='card' style='flex:1;border-left:8px solid {GR}'><h3>Товарные фракции</h3><p>45–75 тыс. т/год (допущение) → только покупателю с согласованными условиями</p></div>
 <div class='card' style='flex:1;border-left:8px solid {GR}'><h3>Компост</h3><p>Из чистой органики, если есть покупатель и качество подтверждено</p></div>
 <div class='card' style='flex:1;border-left:8px solid #B9C7C0'><h3>Стабилизат</h3><p>Из смешанного остатка; не товар, отдельный показатель</p></div>
 <div class='card' style='flex:1;border-left:8px solid {AC}'><h3>Полигон</h3><p>Остаток. Цель −25–35% от базы, измеренной весовым учётом</p></div>
</div>""",'Объёмы — экстраполяция выборки кейса; выходы — допущения, проверяются пилотами и испытаниями.')

# 03b three proofs
mods=[('Сухие фракции','бумага, пластик, металл, стекло','объём и засорённость по пилоту','тест сортировки, образцы','договор с ценой и объёмом'),
('Органика','рынки, столовые, дворы','чистота потока у крупных источников','компост: испытание качества','покупатель компоста'),
('Тара (Pfand-пилот)','бутылки и банки в 5–10 магазинах','число возвратов и цена одного возврата','чистый ПЭТ и алюминий','переработчик берёт партию'),
('Остаток','то, что не стало товаром','объём после сортировки','стабилизация','законный маршрут на полигон')]
hdr=''.join(f"<div class='dk' style='text-align:center;padding:14px'><h3 style='margin:0'>{t}</h3></div>" for t in ['Модуль','1. Сырьё подтверждено','2. Обработка испытана','3. Покупатель согласован'])
rows=''.join(f"<div class='card' style='padding:14px'><h3 style='margin:0;font-size:26px'>{a}</h3><p style='font-size:20px;color:{MU}'>{b}</p></div>"+''.join(f"<div style='background:{BG2};border-radius:12px;padding:14px;display:flex;align-items:center'><p>{x}</p></div>" for x in (c,d,e)) for a,b,c,d,e in mods)
page('03_tri_dokazatelstva','Наша идея','Сначала покупатель — затем инвестиции: каждый модуль проходит три доказательства',f"""
<div style='display:grid;grid-template-columns:1.1fr 1fr 1fr 1fr;gap:12px'>{hdr}{rows}</div>
<div class='row' style='align-items:center'><div class='card' style='flex:1;border-left:10px solid {AC};padding:16px'><p><b style='color:{DK}'>Правило:</b> капитальные деньги на модуль открываются, только когда все три доказательства есть. Город покупает результат (качество фракций, остаток, надёжность), а не «линию на 400 тыс. т».</p></div></div>""",'Pfand-пилот — бонусная модель без залога; обязательный залог не в полномочиях акимата.')

# 06 sprints gantt
weeks=13
spr=[('S0',0,1),('S1 Стейкхолдеры',1,3),('S2 Цены, ТЗ',3,5),('S3 Пилоты',5,7),('S4 Данные, образцы',7,10),('S5 Варианты',10,12),('Гейт',12,13)]
tasks=[('Устав, мораторий, комитет, бэклог',0,1,AC),('Ответ маслихату, встреча с жителями',1,2,AC),('Аудит обязательств и 450 млн',1,3,GR),('Прогноз бюджета 30.11',3,4,GR),('Требования 3+ поставщикам 02.12',3,4,GR),('Изыскания площадок A и B',4,10,GR),('Морфология, весовой учёт',5,8,GR),('Пилот сбора в 2 районах',5,12,GR),('Пилот возврата тары, 5–10 магазинов',5,11,GR),('Образцы фракций переработчикам',7,11,GR),('Модель эксплуатации и опекса',8,11,GR),('3 конфигурации, оценка площадок',10,12,GR),('Публичное обсуждение 20.01',11,12,AC),('Пакет решения 26.01 → гейт 02.02',12,13,DK)]
labels=['4 ноя','11','18','25','2 дек','9','16','23','30','6 янв','13','20','27']
band=''.join(f"<div style='position:absolute;left:{s/weeks*100}%;width:{(e-s)/weeks*100}%;top:0;bottom:0;background:{'#E9EEE9' if i%2==0 else LT};border-left:1px solid {BR}'><p style='font-size:18px;font-weight:700;color:{DK};padding:6px;white-space:nowrap;overflow:hidden'>{n}</p></div>" for i,(n,s,e) in enumerate(spr))
rows=''.join(f"<div style='display:flex;align-items:center;height:{36 if BARE else 44}px'><div style='width:470px;font-size:21px'>{t}</div><div style='flex:1;position:relative;height:24px'><div style='position:absolute;left:{s/weeks*100}%;width:{(e-s)/weeks*100}%;height:24px;background:{c};border-radius:6px'></div></div></div>" for t,s,e,c in tasks)
page('06_gantt_90_dney','План на 90 дней','6 спринтов по 2 недели и гейт: 4 ноября 2026 – 2 февраля 2027',f"""
<div style='display:flex;flex-direction:column;position:relative'>
<div style='display:flex'><div style='width:470px'></div><div style='flex:1;position:relative;height:40px'>{band.replace('top:0;bottom:0','top:0;height:40px')}</div></div>
<div style='display:flex;margin:4px 0'><div style='width:470px'></div><div style='flex:1;display:flex'>{''.join(f"<div style='flex:1;font-size:18px;color:{MU};border-left:1px solid {BR};padding-left:4px'>{l}</div>" for l in labels)}</div></div>
{rows}</div>""",'S4 — 3 недели из-за праздников. Каждый спринт: планирование в понедельник, обзор со стейкхолдерами, ретроспектива.')

# 10 budget consistent
b90=[('Изыскания A и B',270),('Техконсультант + опекс',150),('Пилот сбора',70),('Морфология',60),('Резерв этапа',50),('Информирование',50),('Юристы',40),('Пилот тары',30),('Испытания образцов',30)]
mx=270
bb=''.join(f"<div style='display:flex;align-items:center;gap:14px;height:{42 if BARE else 50}px'><div style='width:270px;font-size:22px;text-align:right'>{n}</div><div style='width:{v/mx*(400 if BARE else 520)}px;height:32px;background:{DK if 'Резерв' not in n else GR};border-radius:6px'></div><div style='font-size:22px;font-weight:700;color:{DK}'>{v}</div></div>" for n,v in b90)
sc=62 if BARE else 80
wf=[('Резерв базы',6.0,0,6.0,DK),('+15% на оборуд. (≈21 млрд)',-3.15,2.85,6.0,'#C9653A'),('Остаток: базовый стресс',2.85,0,2.85,GR),('Худший: вся статья 35 млрд',0.75,0,0.75,'#E8B27A')]
wfh=''.join(f"<div style='display:flex;flex-direction:column;align-items:center;width:{125 if BARE else 170}px'><div style='height:{(6.6-hi)*sc}px'></div><div style='font-size:22px;font-weight:700;color:{DK}'>{(f'{v:+.2f}' if v<0 else f'{v:.2f}').replace('.',',')}</div><div style='height:{(hi-lo)*sc}px;width:{80 if BARE else 110}px;background:{c};border-radius:6px'></div><div style='height:{lo*sc}px'></div><p style='font-size:19px;text-align:center;margin-top:8px'>{n}</p></div>" for n,v,lo,hi,c in wf)
page('10_budzhet','Деньги','750 млн ₸ на проверку и стресс-тест резерва 6 млрд ₸',f"""
<div style='display:flex;gap:40px;flex:1'>
<div class='card' style='flex:1.1'><h3>90 дней, млн ₸ (итого 750, потолки)</h3>{bb}</div>
<div class='card' style='flex:1'><h3>Резерв проекта, млрд ₸</h3><div style='display:flex;align-items:flex-end;gap:10px;margin-top:6px'>{wfh}</div></div>
</div>""",'Доля оборудования ≈ 60% статьи 35 млрд — допущение; поставщик не расшифровал статью.')

# 11 go/no-go fixed
crits=['1. Площадка: путь разрешений понятен, СЗЗ и экология без запретов','2. Цена: 2+ предложения, прогноз ≤ 70 млрд, резерв ≥ 5%','3. Сбыт: договоры или соглашения с ценой на ≥ 50% массы товарных фракций модуля','4. Логистика: схема вывоза согласована с оператором','5. Эксплуатация: опекс посчитан, источник покрытия дефицита есть','6. Срок и ответы жителям: график с зависимостями, замечания отработаны']
page('11_go_no_go','Точка решения','Гейт 2 февраля: решение по каждому модулю отдельно',f"""
<div style='display:flex;gap:20px;align-items:center;flex:1'>
<div class='dk' style='width:300px'><h3>Пакет решения</h3><p style='color:#E7EEEA'>Три доказательства по каждому модулю + цена, площадка, опекс, график</p></div>
<div class='arr'>→</div>
<div class='card' style='flex:1'>{''.join(f'<p style="padding:6px 0;border-bottom:1px solid {BR};font-size:22px">{c}</p>' for c in crits)}</div>
<div class='arr'>→</div>
<div style='width:440px;display:flex;flex-direction:column;gap:12px'>
 <div class='card' style='border-left:10px solid {GR}'><h3>Всё выполнено</h3><p>GO: закупка модуля</p></div>
 <div class='card' style='border-left:10px solid #C9653A'><h3>Нет сбыта или логистики</h3><p>Закупки модуля нет: испытания или меньшая конфигурация</p></div>
 <div class='card' style='border-left:10px solid #E8B27A'><h3>Нет площадки или цены</h3><p>+60 дней проверки без крупных обязательств</p></div>
</div></div>""",'Некритичные замечания — GO с владельцем и сроком устранения.')

# 13 roadmap consistent
ph=[('Стадия 0: 6 спринтов + гейт','ноя 2026 – фев 2027',0,3.1,AC,None),('Сбор, контейнеры, ИС учёта','2027',3,14,GR,None),('Подготовка площадки B','фев – июн 2027',3.1,8,DK,None),('Проект и госэкспертиза','фев – июл 2027',3.1,9,DK,None),('Закупка модулей (после гейтов)','июн – сен 2027',7,11,DK,None),('Строительство и поставка','авг 2027 – июл 2028',9,21,DK,None),('Пусконаладка 2–3 мес.','авг – окт 2028, риск до дек',21,23.5,'#C9653A',26)]
T=26
months=['ноя 26','фев 27','май 27','авг 27','ноя 27','фев 28','май 28','авг 28','ноя 28']
rr=''.join(f"<div style='display:flex;align-items:center;height:{66 if BARE else 74}px'><div style='width:440px;line-height:1.15'><p style='font-weight:700;color:{DK}'>{n}</p><p style='font-size:19px;color:{MU}'>{d}</p></div><div style='flex:1;position:relative;height:36px'><div style='position:absolute;left:{s/T*100}%;width:{(e-s)/T*100}%;height:36px;background:{c};border-radius:8px'></div>{f'<div style=\"position:absolute;left:{e/T*100}%;width:{(r-e)/T*100}%;height:36px;background:repeating-linear-gradient(45deg,#E8B27A 0 8px,#F6F4EE 8px 16px);border-radius:0 8px 8px 0\"></div>' if r else ''}</div></div>" for n,d,s,e,c,r in ph)
page('13_doroznaya_karta','Сроки','Единый график: гибко на проверке, по плану на стройке',f"""
<div style='display:flex;flex-direction:column;position:relative'>
<div style='display:flex'><div style='width:440px'></div><div style='flex:1;display:flex'>{''.join(f"<div style='flex:1;font-size:19px;color:{MU};border-left:1px solid {BR};padding-left:4px'>{m}</div>" for m in months)}</div></div>
{rr}
<div style='position:absolute;left:calc(440px + (100% - 440px) * {21.9/T});top:30px;bottom:0;border-left:3px dashed #C9653A'></div>
<p style='position:absolute;left:calc(440px + (100% - 440px) * {21.9/T} + 10px);top:24px;font-size:20px;color:#A3561A;font-weight:700'>план 31.08.2028</p>
</div>""",'Штриховка — риск переноса ввода до декабря 2028; итоговый срок подтверждаем на гейте.')

# 14 world
cty=[('Германия','Pfand: залог ≥ 0,25 € на одноразовую тару, возврат в магазине; ответственность производителей за упаковку; с 2005 г. запрет захоронения необработанных отходов','Пилот возврата тары в 5–10 магазинах (бонус без залога); производители и импортёры — в финансирование'),
('Южная Корея','Пищевые отходы собираются отдельно, оплата по весу','Начать органику с рынков, столовых, ресторанов'),
('Италия, Contarina','Плата зависит от объёма остаточного мусора','Модель PAYT за 90 дней, пилот в 2027 после решения маслихата'),
('Словения, Любляна','Центр повторного использования: ремонт и перепродажа','Небольшой модуль, социальные рабочие места'),
('Швейцария','Остаток — на энергетическую утилизацию, отдельно от вторсырья','Остаток считаем отдельным потоком; новый МСЗ в базу не включаем')]
page('14_mirovoy_opyt','Мировой опыт','Что берём у Германии и других стран — и как адаптируем для Армана',f"""
<div style='display:flex;flex-direction:column;gap:12px'>
<div style='display:grid;grid-template-columns:260px 1fr 1fr;gap:12px'><div class='dk' style='padding:12px'><h3 style='margin:0'>Страна</h3></div><div class='dk' style='padding:12px'><h3 style='margin:0'>Практика</h3></div><div class='dk' style='padding:12px'><h3 style='margin:0'>Для Армана</h3></div>
{''.join(f"<div class='card' style='padding:14px'><h3 style='margin:0'>{a}</h3></div><div class='card' style='padding:14px'><p>{b}</p></div><div style='background:{BG2};border-radius:16px;padding:14px'><p>{c}</p></div>" for a,b,c in cty)}
</div>
<div class='card' style='border-left:10px solid {AC};padding:14px'><p><b style='color:{DK}'>Главный урок Германии шире Pfand:</b> у каждого потока свой маршрут, ответственный и источник денег. Низкое захоронение там держится и на сжигании, и на обработке остатка, а не только на переработке.</p></div>
</div>""",'Источники: DPG (Pfand), BMUV (упаковка, запрет 2005), EEA 2023, K-eco, Contarina, RCERO Ljubljana, BAFU.')

# 15 PM practices
pr=[('Stage-Gate','гейт 2 фев + гейт на каждый модуль'),('Гибрид: agile + predictive','спринты на проверке, план на стройке'),('Scrum-ритм','спринт 2 нед., планирование, обзор, ретро'),('Kanban-доска','бэклог доказательств по модулям'),('WBS и RACI','кто отвечает за каждый результат'),('Реестр рисков','13 рисков, триггеры, владельцы'),('Контроль изменений','> 1% бюджета или 1 мес. — комитет'),('План/факт освоения','EVM-light: 750 млн по статьям'),('Реестр стейкхолдеров','ответ каждому из 6 писем с датой'),('Benefits realization','KPI с базой и периодом'),('Lessons learned','после каждого спринта'),('Tailoring PMBOK 7','процессы под масштаб проекта')]
page('15_pm_praktiki','Проектное управление','PM-практики, которыми мы управляем проектом',f"""
<div style='display:grid;grid-template-columns:repeat(4,1fr);gap:14px'>{''.join(f"<div class='card' style='border-top:6px solid {AC if i<4 else GR};padding:18px'><h3 style='font-size:26px'>{a}</h3><p style='font-size:21px'>{b}</p></div>" for i,(a,b) in enumerate(pr))}</div>""",'PMI (2021) PMBOK Guide 7th ed.: принципы ценности, стейкхолдеров, рисков и адаптации.')
print('v3 ok')
