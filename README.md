Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.

запрос:

           SELECT track,
    CASE
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS status
    FROM
    "Orders";

Скриншот результата запроса 2_sql.png (директория \practicum_diplom)
# 2. Автоматизация теста.

Для запуска теста необходимо в файл configuration скопировить URLстенда вида 
: https://e2988140-1cf1-4a60-b32a-7e73cfa72281.serverhub.praktikum-services.ru/

В файле sendor_stand_request нажать кнопку Run 

Скриншот автоматизации  Autotest.png (директория \practicum_diplom)
