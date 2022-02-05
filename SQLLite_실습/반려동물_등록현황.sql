SELECT count(*) from 반려동물_등록현황;

SELECT DISTINCT 등록품종수 FROM 반려동물_등록현황;

SELECT DISTINCT [등록주체(시군구)] FROM 반려동물_등록현황;

SELECT DISTINCT [읍면동(법정동)] FROM 반려동물_등록현황;

SELECT [읍면동(법정동)], [등록주체(시군구)], 동물소유자당동물등록수
FROM 반려동물_등록현황
WHERE [등록주체(시군구)] = '72';

SELECT [읍면동(법정동)], [등록주체(시군구)], 동물소유자수, 동물소유자당동물등록수
FROM 반려동물_등록현황
ORDER BY 동물소유자수 ASC;