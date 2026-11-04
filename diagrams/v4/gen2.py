import os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'html')
DK='#14302B'; LT='#F6F4EE'; BG2='#E9EEE9'; AC='#D9822B'; AC2='#A3561A'; TX='#3F4B46'; MU='#6B746F'; CARD='#FFFDF8'; BR='#DCD7CB'; GR='#7A8F86'; RD='#C8663B'; GN='#3F7D5E'
CSS=f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1920px;height:1080px;background:{LT};font-family:'Liberation Sans',Arial,sans-serif;color:{TX};padding:64px 96px 90px;display:flex;flex-direction:column;gap:26px;overflow:hidden;position:relative}}
.ey{{font-size:22px;letter-spacing:3px;text-transform:uppercase;color:{AC2};font-weight:700}}
h1{{font-family:'Liberation Serif',Georgia,serif;font-size:50px;color:{DK};line-height:1.1;margin-top:6px}}
.card{{background:{CARD};border:2px solid {BR};border-radius:14px;padding:18px 20px}}
.dk{{background:{DK};color:{LT};border-radius:14px;padding:18px 20px}}
.ft{{position:absolute;left:96px;right:96px;bottom:34px;font-size:20px;color:{MU}}}
h3{{font-size:25px;color:{DK};margin-bottom:6px}}
.dk h3{{color:#F2B36F}}
p,li,td,th{{font-size:21px;line-height:1.3}}
ul{{padding-left:24px}}
.row{{display:flex;gap:18px}}
table{{border-collapse:collapse;width:100%}}
th{{background:{DK};color:{LT};text-align:left;padding:9px 12px;font-size:20px}}
td{{border-bottom:1px solid {BR};padding:8px 12px;vertical-align:top;background:{CARD}}}
.tag{{display:inline-block;background:{BG2};border-radius:999px;padding:3px 12px;font-size:18px;color:{DK};margin:2px 4px 0 0}}
svg text{{font-family:'Liberation Sans',Arial,sans-serif}}
"""
def page(name,ey,title,body,foot=''):
    h=f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div><p class='ey'>{ey}</p><h1>{title}</h1></div>{body}<p class='ft'>{foot}</p></body></html>"
    open(os.path.join(OUT,name+'.html'),'w').write(h)

def tbl(head,rows,widths=None):
    w=''.join(f"<col style='width:{x}'>" for x in widths) if widths else ''
    return "<table>"+w+"<tr>"+''.join(f"<th>{h}</th>" for h in head)+"</tr>"+''.join("<tr>"+''.join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)+"</table>"

# ---------- 01 Что начинаем сейчас
cols=[('Сегодня – 9 ноября','Сохранить знания',RD,['Интервью с уходящим экспертом (3 сессии по 2 ч, запись)','Технологический паспорт: переписка, расчёты, контакты, статус каждого поставщика','Временный владелец техн. направления','Договор с экспертом на консультации после ухода']),
 ('До 11 ноября','Остановить риск',AC,['Мораторий на закупку оборудования и выбор площадки','Утвердить Устав и Управляющий комитет','Реестр достоверности: факт / оценка / заявление','Письмо поставщику: продлить цену, расшифровать 35 млрд ₸']),
 ('До 18 ноября','Открыть диалог',GN,['Ответ маслихату и график раскрытия данных','Встреча с жителями, общественный совет','Рабочая группа с оператором вывоза','Закупки: изыскания A и B, консультант, аудит отходов']),
 ('До 2 декабря','Получить цифры',DK,['Прогноз бюджета финслужбе (30.11)','Техтребования 3+ поставщикам (02.12)','Старт аудита отходов и пилота сбора','Запрос требований к качеству у переработчиков'])]
page('01_nachinaem_seychas','Что делаем прямо сейчас','Первые 4 недели: сохранить знания, остановить риск, открыть диалог, получить цифры',
"<div class='row' style='flex:1'>"+''.join(f"<div class='card' style='flex:1;border-top:10px solid {c};display:flex;flex-direction:column;gap:10px'><p style='color:{MU};font-weight:700'>{d}</p><h3>{t}</h3><ul>{''.join(f'<li style=\"margin-bottom:14px;font-size:24px\">{x}</li>' for x in xs)}</ul></div>" for d,t,c,xs in cols)+"</div>"
+f"<div class='dk' style='padding:16px 22px'><p style='font-size:24px'><b style='color:#F2B36F'>Решение заказчика сегодня:</b> утвердить стадию 0 на 90 дней и 750 млн ₸ на проверку. Не утверждать сегодня площадку и закупку оборудования.</p></div>",
'Все расходы в пределах лимита 750 млн ₸ · устные договорённости эксперта не считаем обязательствами до проверки')

# ---------- 02 Архитектура завода
st=[('Весовая и приёмка','Взвешиваем каждую машину, фото, контроль опасных отходов','чтобы знать реальный поток и платить за тонны'),
 ('Предсортировка','Ручной отбор крупногабарита, плёнки, батареек','защищаем оборудование и людей'),
 ('Барабанный грохот','Отделяем мелкую фракцию (<80 мм), в основном органику','органика 38% потока уходит на компост'),
 ('Баллистический сепаратор','Делим на плоское (бумага, плёнка) и объёмное (бутылки, банки)','упрощает работу оптики'),
 ('Оптика + магнит + вихретоковый','ПЭТ, ПНД, картон; чёрный металл; алюминий','чистые товарные фракции'),
 ('Ручная доочистка и прессы','Контроль качества, тюки по стандарту покупателя','продаём продукт, а не «отходы»')]
arrow=f"<div style='font-size:34px;color:{AC};font-weight:700;align-self:center'>→</div>"
boxes=arrow.join(f"<div class='card' style='flex:1;display:flex;flex-direction:column;gap:6px;padding:14px'><p style='color:{AC2};font-weight:700;font-size:19px'>{i+1}</p><h3 style='font-size:22px'>{t}</h3><p style='font-size:19px'>{d}</p><p style='font-size:18px;color:{GN}'><b>Зачем:</b> {z}</p></div>" for i,(t,d,z) in enumerate(st))
page('02_arhitektura_zavoda','Архитектура комплекса','Откуда, куда и зачем: модульный комплекс на площадке B',
f"""<div class='row' style='align-items:stretch'>
<div class='dk' style='width:260px;display:flex;flex-direction:column;gap:8px'><h3>Откуда</h3><p style='font-size:19px'>Дворы и контейнеры города: 360 тыс. т/год</p><p style='font-size:19px'>Смешанные отходы + раздельный сбор (4 потока)</p><p style='font-size:19px'>Оператор вывоза, маршруты с GPS и весами</p></div>
{arrow}<div style='flex:1;display:flex;flex-direction:column;gap:10px'>
<p style='font-weight:700;color:{DK};font-size:22px'>Модуль 1 · сортировка сухих фракций и смешанных отходов</p>
<div class='row' style='gap:8px'>{boxes}</div>
<div class='row' style='gap:12px'>
<div class='card' style='flex:1;border-left:8px solid {GN}'><h3 style='font-size:22px'>Модуль 2 · органика</h3><p style='font-size:19px'>Мелкая фракция и пищевые отходы → туннельное компостирование 6–8 недель → компост для озеленения города</p></div>
<div class='card' style='flex:1;border-left:8px solid {GR}'><h3 style='font-size:22px'>Модуль 3 · тара</h3><p style='font-size:19px'>Чистый ПЭТ и алюминий из возврата тары и раздельного сбора → прямой путь к переработчику</p></div>
<div class='card' style='flex:1;border-left:8px solid {RD}'><h3 style='font-size:22px'>Модуль 4 · остаток</h3><p style='font-size:19px'>То, что не продаётся → на полигон по договору; цель: −25–35% к захоронению</p></div>
</div></div>{arrow}
<div class='dk' style='width:260px;display:flex;flex-direction:column;gap:8px'><h3>Куда</h3><p style='font-size:19px'>Переработчики: 45–75 тыс. т/год фракций по договорам</p><p style='font-size:19px'>Город и фермеры: компост</p><p style='font-size:19px'>Полигон: только остаток</p><p style='font-size:19px'>ИС учёта: данные о каждой тонне</p></div>
</div>
<div class='row'>
<div class='card' style='flex:1;background:{BG2}'><p><b>Почему модули:</b> каждый модуль получает деньги только после трёх доказательств: сырьё подтверждено, обработка испытана, покупатель согласован.</p></div>
<div class='card' style='flex:1;background:{BG2}'><p><b>Почему не одна линия на 400 тыс. т:</b> поток 360 тыс. т, рециклинг-потенциал ниже; первая очередь под реальный поток + резерв площади под расширение.</p></div>
</div>""",'Состав оборудования — типовая схема MRF; окончательная конфигурация утверждается на гейте 02.02.2027 по данным аудита и предложениям 3+ поставщиков')

# ---------- 03 Gantt
months=['Н','Д','Я','Ф','М','А','М','И','И','А','С','О','Н','Д','Я','Ф','М','А','М','И','И','А','С','О','Н','Д']
X0,W=470,1250; mw=W/26
def x(m): return X0+m*mw
rows=[('Стадия 0: спринты S0–S5 + гейт',0.1,3.05,AC,'проверка'),
('Передача знаний эксперта, консультант',0.1,3.05,RD,'до 9.11 + далее'),
('Изыскания и аудит отходов (A и B)',1.0,2.5,AC,''),
('Пилот раздельного сбора → весь город',1.0,13.9,GN,'контейнеры к 12.2027'),
('ИС учёта и публичная панель',1.0,8.0,GN,''),
('ОВОС и общественные слушания',3.1,7.5,GR,''),
('Проектирование и госэкспертиза',3.1,8.9,GR,''),
('Подготовка площадки B',3.1,7.9,GR,'5 мес.'),
('Закупка модулей (гейт на каждый)',7.0,10.9,DK,''),
('Изготовление и поставка оборудования',11.0,19.9,DK,''),
('Строительство',9.0,20.9,DK,''),
('Пусконаладка (риск до декабря)',20.0,23.0,AC2,'')]
rh=62; y0=60
svg=f"<svg width='1728' height='{y0+len(rows)*rh+40}'>"
for i,mo in enumerate(months):
    svg+=f"<rect x='{x(i)}' y='0' width='{mw-2}' height='34' fill='{BG2 if i%2 else CARD}'/><text x='{x(i)+mw/2-1}' y='24' font-size='18' text-anchor='middle' fill='{DK}'>{mo}</text>"
for yr,a,b in [('2026',0,2),('2027',2,14),('2028',14,26)]:
    svg+=f"<text x='{x(a)+4}' y='54' font-size='17' fill='{AC2}' font-weight='700'>{yr}</text><line x1='{x(a)}' y1='0' x2='{x(a)}' y2='{y0+len(rows)*rh}' stroke='{BR}' stroke-width='2'/>"
for i,(n,a,b,c,l) in enumerate(rows):
    y=y0+i*rh
    svg+=f"<text x='0' y='{y+32}' font-size='21' fill='{DK}'>{n}</text><rect x='{x(a)}' y='{y+10}' width='{(b-a)*mw}' height='32' rx='8' fill='{c}'/>"
    if l: svg+=f"<text x='{x(b)+8}' y='{y+32}' font-size='17' fill='{MU}'>{l}</text>"
for m,lab,c in [(3.0,'Гейт 02.02.2027',RD),(21.9,'План 31.08.2028',DK)]:
    svg+=f"<line x1='{x(m)}' y1='36' x2='{x(m)}' y2='{y0+len(rows)*rh}' stroke='{c}' stroke-width='3' stroke-dasharray='8 5'/><text x='{x(m)+6}' y='{y0+len(rows)*rh+28}' font-size='19' fill='{c}' font-weight='700'>◆ {lab}</text>"
svg+="</svg>"
page('03_gantt_realizacii','План реализации','Диаграмма Ганта: ноябрь 2026 – декабрь 2028',svg,
'Город видит результат в 2027 (контейнеры, сбор, учёт) · ввод комплекса: прогноз август–октябрь 2028, риск до декабря · закупка только после гейта модуля')

# ---------- 04 План исследований / аудита
page('04_plan_issledovaniy','План исследований и аудита','Что проверяем за 90 дней, чтобы решение 2 февраля опиралось на факты',
tbl(['Что проверяем','Метод','Где и когда','Кто','Результат для гейта'],[
['<b>Площадки A и B</b>','Инженерные и экологические изыскания, СЗЗ, сети, транспорт, шум','05.12 – 15.01','Подрядчик по конкурсу, рук. проекта','Рейтинг площадок по 5 критериям'],
['<b>Состав и объём отходов</b>','Морфология (зимний замер), весовой учёт на въезде полигона','2 района, 01.12 – 31.12','Консультант, оператор','Реальный поток по фракциям, ±10%'],
['<b>Качество раздельного сбора</b>','Пилот 4 потоков, выборочный досмотр контейнеров','Многоэтажки + частный сектор, 01.12 – 25.01','Оператор, УК, общ. совет','Засорённость по типам жилья (цель ≤15%)'],
['<b>Цена оборудования</b>','Расшифровка 35 млрд ₸, запрос 3+ предложений, стресс 5 / 10 / 15%','02.12 – 15.01','Техконсультант, закупки','Диапазон цены и сроков поставки'],
['<b>Сбыт</b>','Образцы фракций и компоста, испытания у переработчиков','до 25.01','Рук. проекта, переработчики','Соглашения с ценой и объёмом'],
['<b>Знания эксперта</b>','Аудит договорённостей: что обещано, кому, письменно ли','04.11 – 30.11','Временный владелец, юрист','Реестр: подтверждено / нет'],
['<b>Экономика эксплуатации</b>','Модель: эксплуатация + долг + остаток − продажи','до 20.01','Финслужба, консультант','Годовой дефицит и источник покрытия'],
],['14%','28%','20%','17%','21%']),'Каждое утверждение получает статус в реестре достоверности: подтверждено · требует проверки · оценка · заявление стороны · не подтверждено')

# ---------- 05 Опции развития
def node(t,d,c,w=360):
    return f"<div class='card' style='width:{w}px;border-top:8px solid {c};padding:14px'><h3 style='font-size:22px'>{t}</h3><p style='font-size:19px'>{d}</p></div>"
page('05_opcii_razvitiya','План будущего развития','Основной сценарий и опции: что делаем, если получили две площадки',
f"""<div class='row' style='align-items:center;flex:1'>
<div class='dk' style='width:300px'><h3>Гейт 02.02.2027</h3><p>Выбор по данным изысканий, аудита и слушаний</p></div>
<div style='font-size:40px;color:{AC}'>→</div>
<div style='display:flex;flex-direction:column;gap:14px;flex:1'>
<div class='row' style='align-items:center'>{node('Основной сценарий · одна площадка B','Комплекс 4 модулей на B, резерв площади под вторую очередь. Ввод август–октябрь 2028.',GN,560)}<div style='font-size:30px;color:{AC}'>→</div>{node('2029–2030','Вторая очередь на резервной площади B, если поток и сбыт подтверждены',GN,520)}</div>
<div class='row' style='align-items:center'>{node('Опция 1 · две площадки: B + A','B — сортировка и компост; A (7 км от центра) — перегрузочная станция и эко-центр: приём крупногабарита, ремонт, повторное использование. Без переработки рядом с жильём.',AC,560)}<div style='font-size:30px;color:{AC}'>→</div>{node('Эффект','Короче плечо вывоза: B дальше A на 12 км; меньше грузовиков у жилья; виден результат жителям',AC,520)}</div>
<div class='row' style='align-items:center'>{node('Опция 2 · две площадки: B + C','B — первая очередь; C (12 км от жилья) — земля под вторую очередь и остаток. Готовим C медленно, 8 мес., без влияния на срок.',GR,560)}<div style='font-size:30px;color:{AC}'>→</div>{node('Эффект','Масштабирование без нового конфликта с жителями; C не тормозит первую очередь',GR,520)}</div>
<div class='row' style='align-items:center'>{node('Запасной · B не прошла изыскания','Грунты или сети на B плохие → A при положительной ОВОС и итогах слушаний, иначе C со сдвигом срока',RD,560)}<div style='font-size:30px;color:{AC}'>→</div>{node('Решает комитет','Изменение срока > 1 мес. — через Управляющий комитет и спонсора',RD,520)}</div>
</div></div>""",'Вторую площадку резервируем только из базового бюджета (статья «Подготовка территории» 9 млрд ₸) и только после решения комитета · дополнительных ассигнований нет')

# ---------- 06 Матрица рисков
risks={(5,4):['R14'],(4,5):['R1'],(4,4):['R2'],(4,3):['R3','R4'],(3,4):['R5','R6','R7','R9','R10'],(3,3):['R8','R11'],(4,2):['R12'],(2,5):['R13']}
def col(p,i):
    s=p*i
    return '#C8663B' if s>=15 else ('#E6B36A' if s>=8 else '#BFD3C7')
grid=''
for p in range(5,0,-1):
    grid+=f"<div style='display:flex;align-items:center;justify-content:center;font-size:20px;color:{MU}'>{p}</div>"
    for i in range(1,6):
        t=' '.join(risks.get((p,i),[]))
        grid+=f"<div style='background:{col(p,i)};border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:21px;font-weight:700;color:{DK};text-align:center;padding:4px'>{t}</div>"
grid+="<div></div>"+''.join(f"<div style='text-align:center;font-size:20px;color:{MU}'>{i}</div>" for i in range(1,6))
legend=[('R14','Уход ключевого эксперта 9.11','20'),('R1','Протест по площадке A','20'),('R2','Цена оборудования +15%','16'),('R3','Срыв срока 31.08.2028','12'),('R4','Засорённость сбора 25%','12'),('R5','Нет устойчивого сбыта','12'),('R6','Проблемы на площадке B','12'),('R7','Затягивание ОВОС и экспертизы','12'),('R9','Исчерпание резерва','12'),('R10','Давление «ускорить закупку»','12'),('R13','Нарушение госзакупок','10')]
page('06_matrica_riskov','Риски','Матрица рисков: вероятность × влияние (14 рисков в реестре)',
f"""<div class='row' style='flex:1'>
<div style='display:flex;flex-direction:column;gap:6px'><p style='font-size:20px;color:{MU}'>Вероятность ↑</p>
<div style='display:grid;grid-template-columns:40px repeat(5,170px);grid-template-rows:repeat(5,120px) 30px;gap:6px'>{grid}</div><p style='font-size:20px;color:{MU};margin-left:300px'>Влияние →</p></div>
<div style='flex:1;display:flex;flex-direction:column;gap:6px'>{''.join(f"<div style='display:flex;gap:12px;align-items:center;background:{CARD};border:1px solid {BR};border-radius:10px;padding:7px 14px'><b style='width:60px;color:{DK};font-size:21px'>{a}</b><p style='flex:1'>{b}</p><b style='color:{RD if int(c)>=15 else AC2}'>{c}</b></div>" for a,b,c in legend)}</div>
</div>""",'Красная зона (≥15) — еженедельный контроль Управляющим комитетом · у каждого риска есть владелец, триггер и ответ · полный реестр в приложении к Уставу')

# ---------- 07 Скрытые риски
page('07_skrytye_riski','Скрытые риски','Чего нет на первой странице кейса, но может остановить проект',
tbl(['Скрытый риск','Почему он скрыт','Сигнал (триггер)','Митигация'],[
['<b>Устные обещания эксперта поставщикам</b>','Договорённости были только в голове одного человека','Поставщик ссылается на «согласованные» условия','Реестр договорённостей; ничего не считаем обязательством до проверки юристом'],
['<b>Дефицит на эксплуатации</b>','Все считают стоимость стройки, никто — годовую работу завода','Модель опекса > продаж фракций','До закупки модуля: утверждённый источник покрытия дефицита'],
['<b>Уже потраченные 450 млн ₸</b>','Неясно, какие обязательства за ними стоят','Найдены договоры без результата','Аудит обязательств в спринте S1'],
['<b>Один покупатель на фракцию</b>','Переработчик «готов обсуждать», но может уйти','Меньше 2 соглашений с ценой к 25.01','Минимум 2 покупателя; город — покупатель компоста'],
['<b>Контракты оператора</b>','Многолетние договоры могут запрещать смену маршрутов','Отказ менять маршруты','Юр. анализ, оператор в рабочей группе, поэтапный переход'],
['<b>Сезонность отходов</b>','Зимний замер не равен летнему (органика)','Расхождение > 10% с базой','Повторная морфология летом 2027, модульная мощность'],
['<b>Обжалование закупок</b>','Жалоба участника тендера останавливает его на месяцы','Жалоба в уполномоченный орган','Юр. сопровождение, прозрачные ТЗ, запас 1 мес. в графике'],
['<b>Электросети и вода на B</b>','«Частично есть» ≠ хватает мощности на линию','Техусловия не выданы к 15.01','Запрос техусловий в S2, изыскания сетей'],
],['20%','27%','23%','30%']),'Каждый скрытый риск занесён в реестр с владельцем и проверяется на каждом спринт-обзоре')

# ---------- 08 Карта стейкхолдеров (связи)
N={'akim':(860,110,'Акимат / спонсор',DK),'masl':(260,90,'Маслихат',GR),'fin':(1460,90,'Финслужба',GR),
'zhit':(220,400,'Жители и общ. совет',AC),'oper':(560,560,'Оператор вывоза',GR),'kompl':(1060,720,'Комплекс (проект)',DK),
'pererab':(1560,720,'Переработчики',GN),'post':(1540,420,'Поставщики оборудования',GR),'reg':(220,740,'Экология, санэпид, экспертиза',GR),'eksp':(1060,420,'Уходящий эксперт → консультант',RD)}
E=[('masl','akim','бюджет, тариф PAYT'),('akim','masl','отчёты, данные'),('akim','fin','прогноз'),('fin','akim','деньги, лимит'),
('zhit','akim','обратная связь, протест'),('akim','zhit','данные, панель KPI'),('zhit','oper','отходы по фракциям'),
('oper','kompl','потоки, вес'),('akim','oper','контракт, оплата'),('kompl','pererab','фракции по стандарту'),('pererab','kompl','деньги, требования'),
('post','kompl','оборудование'),('akim','post','ТЗ, 3+ предложения'),('reg','akim','ОВОС, заключения'),('eksp','kompl','знания, паспорт'),('eksp','post','реестр договорённостей')]
s="<svg width='1728' height='790'><defs><marker id='a' markerWidth='10' markerHeight='10' refX='9' refY='3' orient='auto'><path d='M0,0 L9,3 L0,6 z' fill='#A3561A'/></marker></defs>"
import math
for a,b,l in E:
    x1,y1=N[a][0],N[a][1]; x2,y2=N[b][0],N[b][1]
    # offset for bidirectional
    dx,dy=x2-x1,y2-y1; L=math.hypot(dx,dy); ox,oy=-dy/L*14,dx/L*14
    sx,sy=x1+dx*0.22+ox,y1+dy*0.22+oy; ex,ey=x1+dx*0.78+ox,y1+dy*0.78+oy
    s+=f"<line x1='{sx:.0f}' y1='{sy:.0f}' x2='{ex:.0f}' y2='{ey:.0f}' stroke='#A3561A' stroke-width='2.5' marker-end='url(#a)'/>"
    mx,my=(sx+ex)/2+ox*1.6,(sy+ey)/2+oy*1.6
    s+=f"<text x='{mx:.0f}' y='{my+6:.0f}' font-size='17' text-anchor='middle' fill='{TX}' paint-order='stroke' stroke='{LT}' stroke-width='6'>{l}</text>"
for k,(cx,cy,t,c) in N.items():
    w=max(190,len(t)*12+30)
    s+=f"<rect x='{cx-w/2}' y='{cy-30}' width='{w}' height='60' rx='14' fill='{c}'/><text x='{cx}' y='{cy+7}' font-size='20' text-anchor='middle' fill='#F6F4EE' font-weight='700'>{t}</text>"
s+="</svg>"
page('08_karta_steikholderov','Стейкхолдеры','Карта связей: кто что кому передаёт',s,'Стрелка = что передаётся · двусторонние связи показаны парой стрелок · центр управления — акимат и Управляющий комитет')

# ---------- 09 Интерес × влияние
q=[('Управлять плотно','высокое влияние · высокий интерес',DK,['Акимат / спонсор','Маслихат','Жители у площадки A','Управляющий комитет']),
('Держать удовлетворёнными','высокое влияние · низкий интерес',GR,['Экология и санэпид','Госэкспертиза','Финслужба','Министерство (РОП)']),
('Держать в курсе','низкое влияние · высокий интерес',AC,['Жители города, НКО','СМИ','Переработчики','Уходящий эксперт (до 9.11)']),
('Мониторить','низкое влияние · низкий интерес',BG2,['Магазины (возврат тары)','Управляющие компании','Вузы, волонтёры'])]
cells=''.join(f"<div style='background:{c};border-radius:14px;padding:20px;display:flex;flex-direction:column;gap:10px'><h3 style='color:{LT if c in (DK,GR) else DK};font-size:26px;margin:0'>{t}</h3><p style='color:{LT if c in (DK,GR) else MU};font-size:19px'>{sub}</p><div>{''.join(f'<span class=tag style=\"font-size:21px;padding:6px 14px;margin:4px\">{x}</span>' for x in xs)}</div></div>" for t,sub,c,xs in [q[1],q[0],q[3],q[2]])
page('09_matrica_interes_vliyanie','Стейкхолдеры','Матрица «интерес × влияние»',
f"""<div class='row' style='flex:1;align-items:stretch'>
<div style='writing-mode:vertical-rl;transform:rotate(180deg);font-size:22px;color:{MU};text-align:center'>Влияние →</div>
<div style='flex:1;display:flex;flex-direction:column;gap:8px'>
<div style='flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px'>{cells}</div>
<p style='text-align:center;font-size:22px;color:{MU}'>Интерес →</p></div>
<div class='card' style='width:460px;display:flex;flex-direction:column;gap:10px'><h3>Как работаем</h3>
<p><b>Жители:</b> встреча 18.11, общественный совет, QR на площадках, публичные ответы</p>
<p><b>Маслихат:</b> ответ 18.11, график раскрытия, отчёт 20.01</p>
<p><b>Переработчики:</b> рабочая группа раз в 2 недели, образцы, стандарты</p>
<p><b>Регуляторы:</b> ранние консультации, полный пакет с первой подачи</p>
<p><b>Эксперт:</b> перевод в «держать в курсе» через договор консультаций</p></div>
</div>""",'Реестр стейкхолдеров обновляется на каждом спринт-обзоре')

# ---------- 10 Бюджет
b90=[('Изыскания площадок A и B',270,AC),('Техконсультант (вкл. замену эксперта)',150,RD),('Пилот раздельного сбора',70,GN),('Аудит отходов и весовой учёт',60,GN),('Публичное обсуждение, опрос',50,AC2),('Юр. сопровождение, закупки',40,GR),('Пилот возврата тары',30,GN),('Испытания образцов',30,GR),('Резерв этапа',50,BR)]
bars=''.join(f"<div style='display:flex;align-items:center;gap:12px'><p style='width:420px'>{n}</p><div style='height:30px;width:{v*2.0}px;background:{c};border-radius:6px'></div><b style='color:{DK};font-size:21px'>{v}</b></div>" for n,v,c in b90)
b70=[('Строительство и технология',35,DK),('Подготовка территории и сети',9,GR),('Контейнеры и раздельный сбор',8,GN),('Транспорт и логистика',6,GR),('Изыскания, проект, экспертизы',3,AC),('Информирование',1.5,AC2),('ИС учёта',1.5,GN),('Резерв',6,RD)]
stack=''.join(f"<div style='width:{v/70*100}%;background:{c};height:70px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:19px'>{str(v).replace('.',',') if v>=3 else ''}</div>" for n,v,c in b70)
leg=''.join(f"<span style='display:inline-flex;align-items:center;gap:6px;margin-right:18px;font-size:19px'><i style='width:16px;height:16px;background:{c};display:inline-block;border-radius:3px'></i>{n} {str(v).replace('.',',')}</span>" for n,v,c in b70)
page('10_raspredelenie_byudzheta','Бюджет','750 млн ₸ на проверку и 70 млрд ₸ без новых ассигнований',
f"""<div class='row' style='flex:1'>
<div class='card' style='flex:1.15;display:flex;flex-direction:column;gap:9px'><h3>Ближайшие 90 дней · 750 млн ₸</h3>{bars}</div>
<div style='flex:1;display:flex;flex-direction:column;gap:14px'>
<div class='card'><h3>Весь проект · 70 млрд ₸</h3><div style='display:flex;border-radius:10px;overflow:hidden;margin:10px 0'>{stack}</div><div>{leg}</div></div>
<div class='dk'><h3>Стресс-тест резерва 6 млрд ₸</h3><p>+15% к оборудованию (≈21 млрд ₸): резерв 2,85 млрд ₸</p><p>+15% ко всей статье 35 млрд ₸: +5,25 млрд ₸, резерв 0,75 млрд ₸</p><p style='color:#F2B36F;margin-top:8px'>Покрываем мерами: модули, 3+ предложения, потолок индексации, а не резервом</p></div>
</div></div>""",'Сначала тратим немного на проверку, чтобы не потерять много на ошибке · использование резерва — только через Управляющий комитет')

# ---------- 11 BPMN to-be
lanes=['Эксперт (уходит)','Врем. владелец','Рук. проекта','Упр. комитет','Спонсор (аким)']
LH=138; LX=230
s=f"<svg width='1728' height='{LH*len(lanes)+10}'><defs><marker id='b' markerWidth='10' markerHeight='10' refX='9' refY='3' orient='auto'><path d='M0,0 L9,3 L0,6 z' fill='{DK}'/></marker></defs>"
for i,l in enumerate(lanes):
    s+=f"<rect x='0' y='{i*LH}' width='1728' height='{LH}' fill='{CARD if i%2 else BG2}' stroke='{BR}'/><rect x='0' y='{i*LH}' width='{LX-20}' height='{LH}' fill='{DK}'/>"
    words=l.split(' + ') if '+' in l else [l]
    for j,wd in enumerate(words):
        s+=f"<text x='{(LX-20)/2}' y='{i*LH+LH/2+8-(len(words)-1)*13+j*26}' font-size='19' fill='{LT}' text-anchor='middle' font-weight='700'>{wd}{' +' if len(words)>1 and j==0 else ''}</text>"
def lc(i): return i*LH+LH/2
def task(x,lane,t,w=200,c=CARD):
    y=lc(lane); lines=t.split('|'); r=f"<rect x='{x}' y='{y-40}' width='{w}' height='80' rx='12' fill='{c}' stroke='{DK}' stroke-width='2'/>"
    for j,ln in enumerate(lines): r+=f"<text x='{x+w/2}' y='{y+7-(len(lines)-1)*11+j*22}' font-size='17' text-anchor='middle' fill='{DK}'>{ln}</text>"
    return r
def gw(x,lane,t):
    y=lc(lane); return f"<polygon points='{x},{y-34} {x+34},{y} {x},{y+34} {x-34},{y}' fill='#F2B36F' stroke='{DK}' stroke-width='2'/><text x='{x}' y='{y+7}' font-size='22' text-anchor='middle' font-weight='700'>×</text><text x='{x}' y='{y-44}' font-size='16' text-anchor='middle' fill='{DK}'>{t}</text>"
def ar(x1,y1,x2,y2,l=''):
    r=f"<path d='M{x1},{y1} L{x2},{y2}' stroke='{DK}' stroke-width='2' fill='none' marker-end='url(#b)'/>"
    if l: r+=f"<text x='{(x1+x2)/2+6}' y='{(y1+y2)/2-6}' font-size='16' fill='{AC2}' font-weight='700'>{l}</text>"
    return r
s+=f"<circle cx='{LX+20}' cy='{lc(0)}' r='18' fill='{GN}'/><text x='{LX+20}' y='{lc(0)+45}' font-size='15' text-anchor='middle'>04.11</text>"
s+=ar(LX+38,lc(0),LX+70,lc(0))+task(LX+70,0,'Интервью 3×2 ч|переписка, расчёты|в общую папку',210)
s+=ar(LX+280,lc(0),LX+320,lc(0))+task(LX+320,0,'Договор|консультаций|после 9.11',170)
s+=ar(LX+175,lc(0)+40,LX+175,lc(1)-40)+task(LX+70,1,'Технологический|паспорт проекта',210)
s+=ar(LX+280,lc(1),LX+330,lc(1))+task(LX+330,1,'Аудит договорённостей|с поставщиками',210)
s+=ar(LX+540,lc(1),LX+600,lc(1))+gw(LX+634,1,'Подтверждено письменно?')
s+=ar(LX+668,lc(1),LX+730,lc(1),'да')+task(LX+730,1,'В реестр|обязательств',170)
s+=ar(LX+634,lc(1)+34,LX+634,lc(2)-40,'нет')+task(LX+540,2,'Повторный запрос|3+ предложений',190)
s+=ar(LX+900,lc(1),LX+960,lc(1))+task(LX+960,1,'Техтребования|и конфигурации',190)
s+=ar(LX+1055,lc(1)+40,LX+1055,lc(2)-40)+task(LX+960,2,'Пакет решения|изыскания, аудит,|цены, сбыт',190)
s+=ar(LX+730,lc(2),LX+960,lc(2))
s+=ar(LX+1055,lc(2)+40,LX+1055,lc(3)-34)+gw(LX+1055,3,'6 критериев GO?')
s+=ar(LX+1089,lc(3),LX+1180,lc(3),'GO')+task(LX+1180,3,'Закупка модуля|через госзакупки',190)
s+=ar(LX+1021,lc(3),LX+880,lc(3),'NO-GO')+task(LX+680,3,'Доработка: спринт,|новый срок',200)
s+=ar(LX+780,lc(3)-40,LX+1000,lc(2)+40)
s+=ar(LX+1275,lc(3)+40,LX+1275,lc(4)-40)+task(LX+1180,4,'Утверждение|срока и базового плана',190,'#F2E3CF')
s+=ar(LX+1370,lc(4),LX+1430,lc(4))+f"<circle cx='{LX+1450}' cy='{lc(4)}' r='18' fill='{CARD}' stroke='{RD}' stroke-width='6'/><text x='{LX+1450}' y='{lc(4)+48}' font-size='15' text-anchor='middle'>02.02.2027</text>"
s+="</svg>"
page('11_bpmn_to_be','BPMN to-be','Сначала документируем знания эксперта, потом решаем',s,
'Изменения > 1% бюджета или 1 мес. — только Управляющий комитет · срок и базовый план — спонсор · устная договорённость без письменного подтверждения = повторный запрос цен')

# ---------- 12 Кто принимает решения
page('12_kto_reshaet','Управление','Кто принимает решения и кто отвечает (RACI)',
tbl(['Решение','Спонсор (аким)','Упр. комитет','Рук. проекта','Техконсультант','Финслужба','Общ. совет'],[
['Утвердить Устав и мораторий','<b>A</b>','R','R','—','C','I'],
['Передача знаний эксперта, тех. паспорт','I','I','<b>A</b>','R','—','—'],
['Техтребования поставщикам','I','C','<b>A</b>','R','C','—'],
['Выбор площадки','<b>A</b>','R','R','C','C','C'],
['GO / NO-GO модуля на гейте','<b>A</b>','R','R','C','C','I'],
['Изменение > 1% бюджета или 1 мес.','I','<b>A</b>','R','C','C','I'],
['Использование резерва','I','<b>A</b>','R','—','C','I'],
['Публикация данных, панель KPI','I','I','<b>A</b>','—','—','C'],
],['30%','12%','12%','12%','12%','11%','11%'])+
f"<div class='row'><div class='card' style='flex:1'><p><b>Управляющий комитет:</b> заместитель акима, финслужба, управление ЖКХ и экологии, депутат маслихата (наблюдатель). Собирается раз в 2 недели.</p></div><div class='card' style='flex:1'><p><b>Технический консультант</b> заменяет уходящего эксперта: по конкурсу, 150 млн ₸, до найма — временный владелец и консультации эксперта по договору.</p></div></div>",
'R — исполняет · A — утверждает и отвечает · C — консультирует · I — информируется')

# ---------- 13 Спринты и участники
page('13_sprinty','План по спринтам','6 спринтов по 2 недели: цель, участники, результат',
tbl(['Спринт','Даты','Цель','Участники','Результат на обзоре'],[
['<b>S0</b>','04.11–10.11','Запуск и спасение знаний','Рук. проекта, уходящий эксперт, временный владелец, юрист','Устав, мораторий, тех. паспорт, реестр достоверности'],
['<b>S1</b>','11.11–24.11','Стейкхолдеры','Рук. проекта, акимат, жители, маслихат, оператор','Ответ маслихату, общ. совет, аудит 450 млн ₸'],
['<b>S2</b>','25.11–08.12','Цены и ТЗ','Техконсультант, закупки, финслужба, поставщики','Прогноз бюджета 30.11, требования 3+ поставщикам'],
['<b>S3</b>','09.12–22.12','Пилоты','Оператор, УК, жители, магазины','Пилот сбора в 2 районах, возврат тары, аудит отходов'],
['<b>S4</b>','23.12–12.01','Данные и образцы','Переработчики, лаборатория, финслужба','Испытания фракций, модель эксплуатации'],
['<b>S5</b>','13.01–26.01','Варианты','Техконсультант, изыскатели, общ. совет','3 конфигурации, рейтинг площадок, обсуждение 20.01'],
['<b>Гейт</b>','27.01–02.02','Решение','Упр. комитет, спонсор','GO / NO-GO по 6 критериям'],
],['8%','12%','17%','31%','32%']).replace('<td>','<td style="font-size:24px;padding:18px 12px">'),
'Каждый спринт: планирование → ежедневные 15 мин → обзор с заказчиком → ретроспектива · Kanban-доска и бэклог в общей папке')

# ---------- 14 Дорожная карта
ph=[('2026 · ноябрь–январь','Стадия 0 · доказать',AC,['Знания эксперта сохранены','Изыскания, аудит, пилот','Гейт 02.02.2027']),
('2027','Город видит результат',GN,['Контейнеры во всех районах','ИС учёта и публичная панель','Проект, ОВОС, экспертиза','Площадка B, закупка модулей']),
('2028','Комплекс',DK,['Строительство и поставка','Пусконаладка август–октябрь','Договоры сбыта на 70% объёма']),
('2029–2030','Масштабирование',GR,['−25–35% захоронения','Вторая очередь или вторая площадка','PAYT по городу, предложение по РОП'])]
page('14_doroznaya_karta','Дорожная карта','От проверки к результату: 2026 → 2030',
"<div class='row' style='flex:1;align-items:stretch'>"+f"<div style='font-size:40px;color:{AC};align-self:center'>→</div>".join(f"<div class='card' style='flex:1;border-top:12px solid {c};display:flex;flex-direction:column;gap:10px'><p style='color:{MU};font-weight:700'>{d}</p><h3 style='font-size:28px'>{t}</h3><ul>{''.join(f'<li style=\"margin-bottom:18px;font-size:27px\">{x}</li>' for x in xs)}</ul></div>" for d,t,c,xs in ph)+"</div>"
+f"<div class='dk' style='padding:16px 22px'><p style='font-size:24px'><b style='color:#F2B36F'>Главная мысль:</b> мы не отказываемся от проекта. За 90 дней мы превращаем 70 млрд ₸ из надежды в управляемую инвестицию.</p></div>",
'Сроки после гейта перепланируются обоснованно · план 31.08.2028, прогноз август–октябрь 2028, риск до декабря 2028')
print('ok')
