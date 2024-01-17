-- display top 3 of cities temprature during july

SELECT city, AVG(value) AS avg_temp FROM tempratures
WHERE month = 7 OR month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;