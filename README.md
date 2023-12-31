**Версия 0.05 07.01.2024**
1. Добавлены подписки на рассылки о новых материалах в категориях:
    * страница доступна при выборе категории в списке новостей;
    * создан метод subscribe для подписки на категории и unsubscribe для отписки пользователей;
    * просмотр подписок через ссылку категории в списке новостей
    * при публикации новости все подписчики получают сообщение на почту со ссылкой на страницу для прочтения новости (использован сигнал m2m_changed).
2. Реализована отправка списка статей на почту подписчиков категорий каждую неделю на основе той же модели Subscriber:
    * подключено приложение django_apscheduler;
    * добавлена команду запуска периодических задач;
    * настроена периодическую задачу отправки списка статей каждую пятницу в 18:00;
    * составлено сообщение со ссылками на статьи;
    * сообщение содержит только статьи, которые появились с момента предыдущей рассылки.

**Версия 0.04 19.12.2023**
1. Добавлена форма регистрации на сайте с возможностью зарегистрироваться с помощью почты и пароля или через Yandex-аккаунт.
2. Использован пакет django-allauth
3. После того как пользователь вошел, перенаправление на страницу с новостями
4. Настроены проверки у представлений создания и редактирования новостей и статей, также добавлена опция проверки прав в default.html показа/скрытия
 ссылки "Утилиты" в navbar
5. Создана группа authors, выданы ей права на создание и изменение новых записей в разделах «Статьи» и «Новости».
6. Проверена работа прав
7. В приложении news функции переделаны на классы
