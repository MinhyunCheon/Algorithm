문제 설명
CART_PRODUCTS 테이블은 장바구니에 담긴 상품 정보를 담은 테이블입니다. CART_PRODUCTS 테이블의 구조는 다음과 같으며,
ID, CART_ID, NAME, PRICE는 각각 테이블의 아이디, 장바구니의 아이디, 상품 종류, 가격을 나타냅니다.

NAME	TYPE
ID	INT
CART_ID	INT
NAME	VARCHAR
PRICE	INT

데이터 분석 팀에서는 우유(Milk)와 요거트(Yogurt)를 동시에 구입한 장바구니가 있는지 알아보려 합니다.
우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회하는 SQL 문을 작성해주세요.이때 결과는 장바구니의 아이디 순으로 나와야 합니다.

예시
예를 들어 CART_PRODUCTS 테이블이 다음과 같다면

CART_PRODUCTS 테이블

ID	CART_ID	NAME	PRICE
1630	83	Cereal	3980
1631	83	Multipurpose Supply	3900
5491	286	Yogurt	2980
5504	286	Milk	1880
8435	448	Milk	1880
8437	448	Yogurt	2980
8438	448	Tea	11000
20236	1034	Yogurt	2980
20237	1034	Butter	4890
83번 장바구니에는 Milk와 Yogurt가 모두 없습니다.
286번 장바구니에는 Milk와 Yogurt가 모두 있습니다.
448번 장바구니에는 Milk와 Yogurt가 모두 있습니다.
1034번 장바구니에는 Milk는 없고 Yogurt만 있습니다.

따라서 SQL 문을 실행하면 다음과 같이 나와야 합니다.

CART_ID
286
448



SELECT
    A.CART_ID
    FROM (SELECT
        ID
        , CART_ID
        , GROUP_CONCAT(NAME) PRODUCTS
        FROM CART_PRODUCTS
        GROUP BY CART_ID) A
    WHERE A.PRODUCTS LIKE ('%Milk%')
      AND A.PRODUCTS LIKE ('%Yogurt%')
    ORDER BY A.ID ASC
