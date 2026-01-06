--Overall failure rate
SELECT
    COUNT(*) AS total_records,
    SUM(target) AS failures,
    ROUND(100.0 * SUM(target) / COUNT(*), 2) AS failure_rate_pct
FROM predictive_maintenance;

--Failure rate by machine type
SELECT
    type,
    COUNT(*) AS total,
    SUM(target) AS failures,
    ROUND(100.0 * SUM(target) / COUNT(*), 2) AS failure_rate_pct
FROM predictive_maintenance
GROUP BY type
ORDER BY failure_rate_pct DESC;

--Compare parameters: Failure VS No Failure
SELECT
    target,
    AVG(air_temperature_k) AS avg_air_temp,
    AVG(process_temperature_k) AS avg_process_temp,
    AVG(rotational_speed_rpm) AS avg_speed,
    AVG(torque_nm) AS avg_torque,
    AVG(tool_wear_min) AS avg_tool_wear
FROM predictive_maintenance
GROUP BY target;
