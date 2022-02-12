# ch03장 스파크 애플리케이션 



### 1. 데이터 집계

- GroupBy : 푸시를 사용자 이름으로 그룹핑하면서 각 그룹별 로우 개수를 집계(즉, 각 사용자별 푸시 횟수)

  ```spark
  val grouped = pushes.groupBy("actor.login").count
  ```

- orderBy : 데이터 셋을 정렬  // dec(내림차순), asc(오름차순)

  ```spark
  val ordered = grouped.orderBy(grouped("count").dec
  ```



### 2. spark-submit  사용

- 스파크 애플리케이션을 제출하는 헬퍼 스크립트, 애플리케이션을 스파크 클러스터에서 실행하는데 사용
- 스파크 루트 디렉터리 아래 bin 폴더 안에 있음

# ch04장 스파크 API 



### 1. Pair RDD  : 키-값쌍의 RDD

- 키-값 쌍은 간단하고 범용적이고 확장성이 뛰어난 데이터 모델
- 새로운 타입의 키와 값을 손쉽게 추가할 수 있고 독립적으로 저장할 수 있음
- 캐싱 시스템, No-SQL DB가 키-값 저장소에 해당
- 키-값 쌍은 전통적으로 ''연관 배열' 자료구조 사용해 표현 --> 파이썬에서는 '딕셔너리(형태 : {???} )' 라고 함'
  - 스칼라와 자바에서는 '맵(map)' 이라고 함
- 키-값 쌍 또는 키-값 튜플로 구성된 RDD

```
spark-shell  // scala로 들어감
```

```
val aaa = sc.textFile("first-eidtion/ch04/" + "aaaa.txt")  // 데이터 로드
```

```
val bbb = aaa.map(_.split("#"))  // (#)로 구분된 것을 string 타입으로 저장 --- 데이터 파싱  
```

```
var ccc = bbb.map(a => (a(2).toInt, a))  // PairRDD 생성

# 파싱한 데이터(a)를 튜플로 매핑해 ccc PairRDD로 만든다 
# a(2)는 파싱한 데이터 중 변환하려는 인덱스의 위치이고 toInt는 이값을 정수형으로 변환한 것
# 마지막 tran은 첫번째 요소로 지정하는 것이다
# val(값), var(변수)로 ccc는 변수로 갱신 가능
```



### 2. 키값 가져오기

- PairRDD의 키 또는 값으로 구성된  새로운 RDD를 가져오려면 keys, values 변환 연산자를 사용

  ```
  ccc.keys.distinct().count()
  
  # 중복을 제거하고 데이터의 고유 개수를 계산
  ```



### 3. 키별 개수 세기

```
ccc.countByKey()

# ccc에 있는 키의 출현 횟수를 스칼라 map 형태로 반환
```

```
ccc.countByKey().values.sum

# values, sum은 API매서드가 아닌 표준 매서드
```



### 4. 단일 키로 값 찾기

```
ccc.lookup(00)

# 00의 모든 것을 가져온다
```



### 5. mapValues 변환 연산자로 PairRDD 값 바꾸기

- mapValues는 키를 변경하지 않고 PairRDD에 포함된 값만 변경할 수 있다

```
ccc = ccc.mapValues(a => {
     if(a(3).toInt == 25 && a(4).toDouble > 1)  
         a(5) = (a(5).toDouble * 0.95).toString
     a })

# toDouble : 두번이상
```



### 6. flatMapValues 변환 연산자로 키에 값 추가

- flatMapValues는 변환 함수가 반환한 컬렉션 값들을 원래 키와 합쳐 새로운 키-값 결과 PairRDD에서 제외

```
ccc = ccc.flatMapValues(a => {
    if(a(3).toInt == 81 && a(4).toInt >= 5) {
       val cloned = a.clone()    ## a 배열을 복제
       cloned(5) = "0.00"; cloned(3) = "70"; cloned(4) = "1";
       List(a, cloned)  ## 원래 요소와 추가한 요소 반환
    }
    else
       List(a)   ## 원래 요소만 반환
    })
```



### 7. foldByKey 사용

- 형식 : foldByKey( zeroValue: V )( func: (V, V) => V ): RDD[ ( K, V ) ]

  - zeroValue는 덧셈연산에서는 0, 곱셈에서는 1인 항등원이어야 한다.
  - zeroValue는 가장 먼저 func 함수로 전달해 키의 첫 번째 값과 병합 후 결과를 다시 키의 두번째 값과 병합

- foldByKey는 RDD 파티션 갯수만큼 더하기에 원치 않는 결과가 나올 수 있다.

  ```
  val totals = amounts.foldByKey(0)((p1, p2) => p1 + p2).collect()
  ```

  ```
  amounts.foldByKey(100000)((p1, p2) => p1 + p2).collect()
  ```


### 8. aggregateByKey 사용

- aggregateByKey는 zeroValue를 받아 RDD값을 병합한다는 점에서 foldByKey, reduceByKey와 유사하지만 값의 타입을 바꿀 수 있다.

- 두가지 함수를 전달해야함 1. [(U, V) =>U ] 변환함수, 2.[(U, U) => U] 하는 병합함수

  ```
  val prods = transByCust.aggregateByKey(List[String]())( ## zeroValue에 빈 리스트를 지정
  (prods, tran) => prods ::: List(tran(3)), ## 변환함수(파티션별로 요소를 병합), 제품에 리스트 추가
  (prods1, prods2) => prods1 ::: prods2)   ## 병합함수(최종 결과를 병합), 키가 같은 두 리스트를 이어붙인다
  ```



## 데이터 파티셔닝

- 스파크 데이터 파티셔닝 : Data를 여러 클러스터 노드로 분할하는 것
- 스파크 성능, 리소스 점유량에 영향을 줄 수 있는 RDD 기본 개념
- 스파크 클러스터 : 병렬 연산이 가능하고 네트워크로 연결된 노드의 집합
- RDD 파티션 : RDD 데이터의 일부(조각, 슬라이스)
- ex)
  - 15줄 짜리 text를 여러 파티션으로 분할해 클러스터 노드에 분산, 이렇게 분산된 파티션이 모여 RDD 형성
    - 15 text -> | 노드(1) : 파티션(3text) | 노드(2) : 파티션(3text) | 노드(3) : 파티션(3text) | 노드(4) : 파티션(3text) | 노드(5) : 파티션(3text) |, 각 노드는 네트워크로 연결됨, 파티션이 모여 하나의 RDD 형성

- 셔플링 : 파티션 간의 물리적인 데이터 이동, 새로운 RDD의 파티션을 만들려고 여러 파티션의 데이터를 합칠 떄 발생
  - aggregateByKey 함수 사용시 발생



## 데이터 조인

- 내부조인(Join)
- 왼쪽 외부조인(leftOuterJoin)
- 오른쪽 외부조인(rightOuterJoin)
- 외부조인(fullOuterJoin)



## 데이터 정렬

- repartitionAndSortWithinPartition : 리파티셔닝과 정렬작업을 동시에 수행, 성능이 좋음

- sortByKey

  ```
  val sortedProds = totalsAndProds.sortBy(_._2._2(1))
  ## _._2 : pairRDD 값임
  ## _._2._2(1) : 해당 데이터의 튜플 중 상품정보 배열의 두번째 요소 참조
  ```

- sorkBy



## 데이터 그루핑

- aggregateByKey
- groupByKey
- combineByKey