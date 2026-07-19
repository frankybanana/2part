SELECT
    c.login,
    COUNT(o.courierId) AS orders_in_delivery
FROM
    Couriers c
LEFT JOIN
    Orders o ON c.id = o.courierId
WHERE
    o.inDelivery = true
GROUP BY
    c.id, c.login
ORDER BY
    orders_in_delivery DESC;