# Создаем маршрут
route = Bus_route()

# Добавляем остановки
route.add_stop(Bus_Stop('Спортивная', '55.47.55', 15))
route.add_stop(Bus_Stop('Ленина', '55.45.56', 20))
route.add_stop(Bus_Stop('Кинотеатр Современник', '55.47.57', 25))
route.add_stop(Bus_Stop('Имени Николаева', '55.47.58', 0))

print('1. Информация об остановке.')
print(route.stops[0].show_info())
print()

print('2. Общее время маршрута.')
print(f'Общее время: {route.calculate_full_time()} минут.')
print()

print('3. Позиция через n остановок (от Спортивной).')
print(route.bus_position_after_n_stops_from('Спортивная', 2))
print()

print('4. Установка текущей позиции и позиция через n остановок (от текущей).')
route.set_current_stop('Ленина')
print(route.bus_position_after_n_stops(2))
print()

print('5. Поиск остановок по времени (30 минут).')
stops_in_time = route.find_stops_by_time(30)
for stop in stops_in_time:
    print(f"{stop['name']} - {stop['full_time']} минут (позиция {stop['position']})")
print()

print('6. Обратный маршрут.')
reverse = route.reverse_route()
for i, stop in enumerate(reverse.stops):
    print(f'{i+1}. {stop.name} (до следующей: {stop.time_to_next} мин)')
print()

print('7. Генерация отчета.')
route.generate_report('route_report.txt')
print("Отчет сохранен в файл 'route_report.txt'")
print()
