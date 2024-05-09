SELECT c.login AS login, COUNT(o.id)
FROM Couriers c
LEFT JOIN Orders o ON o.courierId = c.id
WHERE o.inDelivery = true OR o.inDelivery IS NULL
GROUP BY login;
