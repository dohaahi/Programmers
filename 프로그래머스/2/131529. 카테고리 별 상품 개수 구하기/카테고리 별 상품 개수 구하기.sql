-- 코드를 입력하세요
SELECT LEFT (PRODUCT_CODE,2) AS CATEGORY, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY
ORDER BY CATEGORY