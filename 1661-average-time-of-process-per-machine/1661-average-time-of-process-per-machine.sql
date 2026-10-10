
SELECT a1.machine_id, ROUND(AVG(a1.timestamp-a2.timestamp), 3) as processing_time
FROM Activity as a1
JOIN Activity as a2
ON a1.machine_id = a2.machine_id AND a1.process_id = a2.process_id
WHERE a1.activity_type = 'end' AND a2.activity_type = 'start'
GROUP BY a1.machine_id