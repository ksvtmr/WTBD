exec(open('gen2.py').read().split('# ---------- ')[0])
def li(xs,fs=19): return '<ul>'+''.join(f"<li style='font-size:{fs}px;margin-bottom:5px'>{x}</li>" for x in xs)+'</ul>'
A=[('Д1','Оборудование ≈ 60% статьи 35 млрд ₸ (≈21 млрд)','3+ предложения поставщиков, 02.12'),
('Д2','Извлечение вторсырья 30–50% от теоретического','пилот сбора и морфология, S2–S3'),
('Д3','Сети и дороги площадки B ≤ 6 млрд ₸','изыскания A и B, 15.01'),
('Д4','ОВОС и госэкспертиза 5–6 месяцев','консультации с регуляторами, S1'),
('Д5','Рост города ~2%/год → ~390 тыс. т к 2030','данные акимата, S1')]
arows=''.join(f"<tr><td style='font-size:18px;padding:6px 8px'><b style='color:{AC2}'>{a}</b></td><td style='font-size:18px;padding:6px 8px'>{b}</td><td style='font-size:17px;padding:6px 8px;color:{MU}'>{c}</td></tr>" for a,b,c in A)
body=f"""<div class='row' style='flex:1;align-items:stretch;min-height:0'>
<div class='dk' style='flex:0 0 520px;display:flex;flex-direction:column;gap:10px'>
<h3>Проект и цели (SMART)</h3>
<p style='font-size:19px'><b>Спонсор:</b> аким / заместитель · <b>РП:</b> команда WTBD · <b>Упр. комитет:</b> зам. акима, финслужба, ЖКХ/экология, маслихат (наблюдатель)</p>
<p style='font-size:19px'><b>Стадия 0:</b> 04.11.2026 – 02.02.2027, ≤ 750 млн ₸ · проект: 70 млрд ₸, 26 мес.</p>
{li(['Захоронение −25–35% за первый полный год работы','Товарные фракции 45–75 тыс. т/год, ≥ 70% под договоры сбыта до пуска','Засорённость раздельного сбора ≤ 15% к концу 2027','Публичная панель KPI ежемесячно с 2027','Бюджет ≤ 70 млрд ₸, резерв ≥ 5% до EPC','Пуск: план 31.08.2028, прогноз 08–10.2028'],19)}
<h3 style='margin-top:8px'>Управление</h3><p style='font-size:18px'>Гибрид PMBOK 7: стадия-гейт на капитальные решения + спринты по 2 недели. Изменения &gt; 1% бюджета или &gt; 1 мес. — только через Упр. комитет. Отчёт раз в 2 недели, публикация ≤ 10 дней после решения.</p>
</div>
<div style='flex:1 1 0;min-width:0;display:flex;flex-direction:column;gap:14px'>
<div class='card'><h3 style='font-size:22px'>Входит</h3><p style='font-size:18px'>Изыскания и проект, площадка, сортировка + компостирование, контейнеры раздельного сбора, схема вывоза с оператором, ИС учёта, работа с жителями, пилот возврата тары</p></div>
<div class='card'><h3 style='font-size:22px'>Не входит</h3><p style='font-size:18px'>Новый полигон, переработка фракций в продукцию, сжигание, пересмотр контрактов оператора без юр. анализа</p></div>
<div class='card'><h3 style='font-size:22px'>Ограничения</h3><p style='font-size:18px'>Нет доп. ассигнований · ≤ 750 млн ₸ за 90 дней · ОВОС, слушания, санитарные нормы, госзакупки, экспертиза обязательны</p></div>
<div class='card' style='flex:1'><h3 style='font-size:22px'>Результат стадии 0</h3><p style='font-size:18px'>Пакет решения на 02.02.2027: площадка, конфигурация модулей, базовые бюджет и график, договорённости с покупателями</p>
<h3 style='font-size:22px;margin-top:12px'>Контрольные точки</h3><table><tr><td style='font-size:17px;padding:5px 8px;width:130px'><b>11.11.2026</b></td><td style='font-size:17px;padding:5px 8px'>Мораторий, утверждение Устава</td></tr><tr><td style='font-size:17px;padding:5px 8px;width:130px'><b>18.11.2026</b></td><td style='font-size:17px;padding:5px 8px'>Ответ маслихату, встреча с жителями</td></tr><tr><td style='font-size:17px;padding:5px 8px;width:130px'><b>02.12.2026</b></td><td style='font-size:17px;padding:5px 8px'>Требования 3+ поставщикам</td></tr><tr><td style='font-size:17px;padding:5px 8px;width:130px'><b>15.01.2027</b></td><td style='font-size:17px;padding:5px 8px'>Итоги изысканий A и B</td></tr><tr><td style='font-size:17px;padding:5px 8px;width:130px'><b>02.02.2027</b></td><td style='font-size:17px;padding:5px 8px'>Точка решения (go / no-go)</td></tr><tr><td style='font-size:17px;padding:5px 8px;width:130px'><b>~09.2027</b></td><td style='font-size:17px;padding:5px 8px'>EPC / договор на оборудование</td></tr></table></div>
</div>
<div style='flex:0 0 560px;display:flex;flex-direction:column;gap:14px'>
<div class='card' style='padding:14px 14px'><h3 style='font-size:22px'>Допущения (проверяем за 90 дней)</h3>
<table><tr><th style='font-size:17px;padding:6px 8px'>№</th><th style='font-size:17px;padding:6px 8px'>Допущение</th><th style='font-size:17px;padding:6px 8px'>Как и когда</th></tr>{arows}</table></div>
<div class='card' style='flex:1;border-left:8px solid {AC}'><h3 style='font-size:22px'>Сценарии</h3>
<p style='font-size:18px'><b>Основной:</b> площадка B, модули по мере трёх доказательств</p>
<p style='font-size:18px'><b>Опция:</b> получены обе земли A и B → B под комплекс, A под компост / резерв 2-й очереди</p>
<p style='font-size:18px'><b>Стресс:</b> +15% к оборудованию → резерв 2,85 млрд ₸ (худший 0,75)</p>
<h3 style='font-size:22px;margin-top:12px'>Критерии успеха</h3><p style='font-size:18px'>Цели 1–4 достигнуты, комплекс введён, нет судебных остановок</p>
<h3 style='font-size:22px;margin-top:12px'>Главные риски</h3><p style='font-size:18px'>Уход эксперта 09.11 · протест · рост цены оборудования · нет покупателя — слайды 12–13</p></div>
</div></div>"""
page('15_ustav','Устав проекта · Project Charter','Устав стадии 0: цели, рамки, допущения',body,'План на 90 дней — слайд 9 · график реализации — слайд 10 · все допущения помечены Д1–Д5, у каждого есть способ и срок проверки')
