-- this displays max temprature of each state
SELECT state, MAX(value) as max_temp FROM tempratures
GROUP BY state ORDER BY state;
