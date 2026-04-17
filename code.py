import base64
import json

class Bus_Stop:
    def __init__(self, name, coordinates, time_to_next):
        self.name = name
        self.coordinates = coordinates
        self.time_to_next = time_to_next

    def show_info(self):
        return f"Остановка {self.name}\nКоординаты: {self.coordinates}\nВремя до следующей: {self.time}"

    def to_dict(self):
            return {
                "name": self.name,
                "coordinates": self.coordinates,
                "time_to_next": self.time_to_next
            }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["coordinates"], data["time_to_next"])
    
    def to_base64(self):
        json_str = json.dumps(self.to_dict())
        return base64.b64encode(json_str.encode()).decode()
    
    @classmethod
    def from_base64(cls, base64_str):
        json_str = base64.b64decode(base64_str).decode()
        data = json.loads(json_str)
        return cls.from_dict(data)

class Bus_route:
    def __init__(self):
        self.stops = []

    def add_stop(self, stop):
        self.stops += stop
        print(f"В маршрут добавлена остановка {stop.name}.")

    def calculate_full_time(self):
        if not self.stops:
            return 0
        full_time = 0
        for stop in self.stops:
            full_time += stop.time_to_next
        return full_time
    
    def bus_position_after_n_stops(self, current_bus_stop_name, n_stops):
        current_position = self.stops.index(current_bus_stop_name)
        if current_bus_stop_name + n_stops >= len(self.stops):
            return f"Автобус проедет все {len(self.stops)} остановок и завершит маршрут."
        return f"Через {n_stops} остановок автобус будет на остановке: {self.stops[current_position + n_stops].name}"
    
    def reverse_route(self):
        re_route = Bus_route()
        for stop in reversed(self.stops):
            reverse_stop = Bus_Stop(stop.name, stop.coordinates, stop.time_to_next)
            re_route.add_stop(reverse_stop)
        return re_route
    
route = Bus_route()
stop = Bus_Stop('jijo','89.80.90','90')
route.add_stop(stop)
