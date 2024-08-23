--- Thisis used to define a view calld eneed meeting
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80 and (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
