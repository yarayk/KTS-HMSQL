# Done
# Топ 5 самых коротких перелетов по длительности
# Колонки: [flight_no, duration]
TASK_1_QUERY = """
SELECT
    flight_no,
    scheduled_arrival - scheduled_departure AS duration
FROM flights
ORDER BY duration ASC
LIMIT 5;
"""

# Топ 3 рейса по числу упоминаний (меньше 50)
# Колонки: [flight_no, count]
TASK_2_QUERY = """
SELECT
    flight_no,
    COUNT(*) AS count
FROM flights
GROUP BY flight_no
HAVING COUNT(*) < 50
ORDER BY count DESC
LIMIT 3;
"""

# Число перелетов внутри одной таймзоны
# Колонка: [count]
TASK_3_QUERY = """
SELECT
    COUNT(*) AS count
FROM flights f
JOIN airports_data a_dep ON f.departure_airport = a_dep.airport_code
JOIN airports_data a_arr ON f.arrival_airport = a_arr.airport_code
WHERE a_dep.timezone = a_arr.timezone;
"""
