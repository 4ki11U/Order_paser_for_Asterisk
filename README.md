# Python lxml-parser shop order for the Asterisk
<i>Скрипт написанный на языке Python для сервера телефонии Asterisk.</i>

---
Суть скрипта :
1. обратиться к интернет-магазину по его API
2. получить результат в формате lxml
3. распарсить результат, "убрав лишнее" и привести к единому формату
4. отобразить результат и проиграть результат Asterisk'ом
---
Данный функционал инициализируется при звонке, и проверяет есть ли по номеру звонящего информация : 
* Если обратившись по API была найдена информация по номеру телефона - получаем результат, расспарсиваем и проигрываем его. 
* В ином случае звонящему ничего не проигрывается.
