show databases;
use world;
show tables;
show table status;

desc city;
desc country;
desc countrylanguage;

select * from city;  # 애스터리스크(*) : All
select name from city;
select name, population from city;

select name, population
from city
where population > 7000000;

select name, population
from city
where population between 6000000 and 8000000;

select name, population
from city
where population >= 6000000 and population <= 8000000; 

select *
from city
where countrycode = 'KOR';

select *
from city
where countrycode = 'KOR'
and population >= 1000000;

select *
from city
where population >= 6000000 and population <= 8000000; 

select *
from city
where name in('seoul', 'tokyo');

select *
from city
where countrycode in('kor','jpn');

select *
from city
where countrycode like 'ko_';

select *
from city
where name like 'tel %';

select *
from city
where countrycode = ( select countrycode
					from city
                    where name = 'seoul');
                    
select *
from city
where population > any ( select population    -- any 하나만 만족해도 okay  = some도 같음
					                     from city
                                         where district = 'new york');
                    
select *
from city
where population > all ( select population    -- 조건 중 만족이 가장 높은 값이 출력됨
					                  from city
                                       where district = 'new york');
                    
select *
from city
order by Population desc;  -- 인구를 내림차순으로 보여줘!!

select *
from city
order by countrycode asc, population desc;

-- 인구수로 내림차순하여 한국에 있는 도시보기
-- 국가면적 크기로 내림차순하여 나라보기

select *
from city
where countrycode = 'kor'
order by population desc;

desc country;

select *
from country
order by surfacearea desc;

select distinct countrycode from city;      -- distinct 중복제거  

select * from city
order by population desc limit 10;

select countrycode, max(population)       -- max, min, avg : 집계함수
from city
group by countrycode;


select countrycode, min(population)
from city
group by countrycode;

select countrycode, avg(population)
from city
group by countrycode;

select countrycode, avg(population) as 'avg'
from city
group by countrycode;

select count(*)
from city;

select avg(population)
from city;

select countrycode, max(population)
from city
group by countrycode;

select countrycode, max(population)
from city
group by countrycode                                              -- 그룹바이 된 집계함수의 조건을 걸어줄때 having 사용
having max(population) > 8000000;

select countrycode, name, sum(population)
from city
group by countrycode, name with rollup;                   -- with rollup : 위 4개에 대한 중계 합계 값을 보여줌

select *
from city
join country on city.countrycode = country.code;            -- 여러개 테이블 조인할 때 사용

select *
from city
join country on city.countrycode = country.code
join countrylanguage on city.countrycode = countrylanguage.countrycode;                    -- 3개의 테이블이 조인

-- 문자열 길이 반환
select Length('aksjdlskgjldf');

select concat('my', 'sql', 'source');

-- 검색하는 문자가 몇번째에 있다는 것을 알려줌
select locate('abc', 'dasdadasdabcfgadfgfg');


select 
left('mysql is an open source relational database management system', 5),  -- 왼쪽에서 5번째까지
right('my name is KIM', 2);   -- 오른쪽에서 2번째까지

select
lower('mysql is an open source relational database management system'),  -- 소문자 변경
upper('my name is KIM');   -- 대문자 변경

select replace('mssql', 'ms', 'my');   -- 특정 문자를 변경함

select trim('          mysql        ');  -- 공백이 있지만 없앰

select trim('          mysql        '),
trim(leading '#' from '###mysql###'),   -- 앞부분 특정문자를 없앰
trim(trailing '#' from '###mysql###');  -- 뒷부분 특정문자를 없앰


select format(123123123452342134124.124135135134135, 3);
-- 3개씩 끊어서 보여줘라


select floor(10.95), ceil(10.95), round(10.95);
-- floor : 내림, ceil : 올림, round : 반올림

select sqrt(4), pow(2, 3), exp(3), log(3);
-- sqtr : 양의 제곱근
-- pow : 2의 3승이 됨. 즉, 첫번째 인수로는 밑수를 전달하고 두번째 인수로는 지수를 전달하여 거듭제곤 계산
-- exp : 인수로 지수를 전달받아, e의 거듭제곱을 계산
-- log : 자연로그 값을 계산

select sin(pi()/2), cos(pi()), tan(pi()/4);
-- sin : 사인 값, cos : 코사인 값, tan : 탄젠트 값

select abs(-3),
round(rand()*100, 0);
-- abs : 절대값 반환, rand : 0.0보다 크거나 같고 1.0보다 작은 하나의 실수를 무작위 생성

select now(), curdate(), curtime();

select now(), date(now()), month(now()), day(now()), hour(now()), minute(now()), second(now());

select now(), monthname(now()), dayname(now());

select now(), dayofmonth(now()), dayofweek(now()), dayofyear(now());

select date_format(now(), '%D %y %a %d %m %n %j');

create table city2 as select * from city;

select * from city2;

create database kim;

use kim;

select * from test;

create table test2 (
	id int not null primary key,
    col1 int null,
    col2 float null,
    col3 varchar(45) null
);
-- 테이블 생성

select * from test2;

alter table test2
add col4 int null;
-- 컬럼 추가

select * from test2;

desc test2;

alter table test2
modify col4 varchar(20) null;
-- 컬럼 속성 변경

alter table test2
drop col4;
-- 컬럼 삭제

desc test2;

create index Col1Idx
on test (col1);
-- 단순 인덱스 추가

show index from test;

create unique index Col2Idx
on test (col2);
-- unique 형의 인텍스 추가

show index from test;

alter table test
add fulltext Col3Idx(col3);    
-- 일반적인 인덱스와 달리 매우 빠르게 테이블의 모든 텍스트 컬럼을 검색

show index from test;

alter table test
drop index col3idx;
-- 인덱스 삭제

show index from test;

drop index col2idx on test;
-- 인덱스 삭제

show index from test;

create view testview as
select col1, col2
from test;

select * from testview;

alter view testview as
select col1, col2, col3
from test;

drop view testview;

use world;

create view allview as
select city.name, country.surfacearea, city.population, countrylanguage.language
from city
join country on city.CountryCode = country.Code
join countrylanguage on city.CountryCode = countrylanguage.CountryCode
where city.countrycode = 'kor';


select * from allview;

use kim;

insert into test
value(1, 123, 1.1, 'test');

insert into test2 select * from test;   -- 복사

update test
set col1 = 1, col2=1.0, col3='test'
where id = 1;

delete from test2
where id = 1;    -- 테이블에선 지웠지만 용량은 줄지 않는다, 삭제되지 않고 복구 가능

truncate table test;  -- 그냥 삭제됨, 용량도 줄음


drop table test2;

drop database kim;