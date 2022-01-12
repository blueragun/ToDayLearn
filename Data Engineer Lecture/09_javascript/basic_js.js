// 자바스크립트의 한줄 주석
/* 
멀티라인 주석
*/

// 자바는 변수의 정의와 선언이 따로 있음.

// 변수의 선언
var var1;   // 이런 var 선언은 잘안씀, 2번째 방법으로 많이 함
let var2;

// 변수의 정의
var2 = 10;
console.log(var2);

// 자료의 타입
console.log( typeof 10);
console.log( typeof 10.0);
console.log( typeof 'Hello');  //  문자열 타입
console.log( typeof true);  // 불리언 타입 

// 파이썬에서는 없는 타입
console.log( typeof null );
console.log( typeof undefined );
console.log( typeof NaN );   // not a number
console.log( typeof Infinity );

// 연산자
// 몫 연산은 없다
console.log( 2+3 );
console.log( 2-3 );
console.log( 2*3 );
console.log( 2/3 );
console.log( 2%3 );
console.log( 2**3 );

//증감연산자, 파이썬에는 없음
let number = 2;
console.log( ++number );   // 파이썬 : number += 1
console.log( --number );

// 전위식, 후위식이 있음
number = 2;
console.log( number++ ); // 후위식
console.log( number );
console.log( ++number ); //전위식

// 비교 연산자
console.log( 1 == '1' );   // 파이썬에서는 False
console.log( 1 === '1' );  // 타입까지 고려 후 비교

// 논리연산자 : &&(and), ||(or), !(not)
console.log( true && false );
console.log( true || false );
console.log( !true );

// 윤년 구하기
let year = 2000;

if(( year%4 == 0 ) && ( year%100 != 0) || (year%400 == 0)) {
    console.log('윤년입니다.')
} else {
    console.log('평년입니다.')
}

// if의 형태
/* 
    if (명제) {

    } else if(명제) {

    } else {

    }
*/

// 블록의 시작과 끝은 {}로 감쌈

// 몫 구하기
let q;
q = 3/2;
q = parseInt(q);  // 몫을 구하기 위해 소수점 이하자리를 버리려 int 타입으로 변형
console.log(q);

// 배열과 반복
// js는 배열이라는 타입(파이썬의 리스트와 동일)

let array = [];

array = [10, 20, 30, 40];
console.log( array );
console.log( array[0] );
console.log( array[2] );


// 객체 생성방법 3가지 
// 1. let array = []; // 빈 배열 객체 생성
// 2. let array1 = Array();  // Array 클래스의 생성자를 이용해서 객체 생성
// 3.let array = new Array(); //new 연산자를 이용한 Array 객체 생성

// 파이썬 append 와 같은 기능  : push
array.push(50);
console.log( array );

// 인덱스 범위를 넘어사는 경우 index error 가 아닌 undefined 오류남
console.log( array[10] );


// js는 배열의 원소를 이렇게도 추가가 된다
array[10] = 100;
console.log( array );

// 연관배열이라고 한다
// 파이썬의 dict 과 같은 map을 지원한다

let = arr = [];

arr['first'] = 10;
console.log( arr );

// for, while, for each

// 파이썬의  for와는 완전 다름
// for는 while의 또다른 표현

// 1부터 10까지 반복
let i = 1;
while( i<= 10 ) {
    console.log(i);
    i++;
}

let j = 1;   // 초기값
while( j<= 10 ) {   // 조건
    console.log(j); 
    ++j;    // 증감
}

// 자바스크립트의 for는 초기값, 조건, 증감; 한줄체 표현
// for(초기값, 조건; 증감)
// 표현만 다르고 동작은 while과 똑같이 동작
for( let i = 1; i <= 10; i++) {
    console.log(i);
}


// 파이썬의 for loop와 동일한 동작을 하는 for each
console.log(array); 
for( let x of array ) {
    console.log(x);
}

// 1부터 n까지의 총합을 구하자
let n =20;
let total = 0;
for( let i = 0; i <= n; i++ ) {
    total += i;
}
console.log( total );

// js 함수는 파이선과 동일
// js는 'function' 키워드로 함수를 정의

function func(a, b) {
    return a + b;
}

console.log( func(10, 20) );

// 가변인자
function add() {
    // 가변인자 객체가 따로 존재
    let sum = 0;
    for(let i = 0; i < arguments.length; i++ ) {
        sum += arguments[i];
    }
    return sum;
}

ret = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
console.log( ret );

// 지역변수, 전역변수

let mem = 10;
function func1() {
    let mem = 20;
}

func1();
console.log( mem );

//디폴트 파라미터
function func2(a, b=2) {
    console.log(a, b);
}

func2();


// class

class Test {
    constructor() {
        console.log('생성자');

    }
}

obj = new Test();

// 자바스크립트의 은닉성, 지원함
class Person {
    //클래스변수는 아님
    // 필드 선언(public과 private)
    // 속성 앞에 '#'을 붙여서 private 설정을 할 수 있음
    #name;
    #age;

    // 파이선의 class변수와 같은 기능
    static nation = 'korea';

    // 생성자
    constructor(name, age) {
        //this는 파이썬의 self와 같음
        //따로 파라미터로 정의하지 않아도 항상정의되어 있음
        this.#name = name;
        this.#age = age;
    };


    // 정적메소드
    static staticMethod() {
        console.log( Person.nation );
    }
    // class 내에서 메소드를 정의할 때는 'function' 생략
    info() {
        console.log(this.#name, this.#age);
    }
}
// 객체 생성
object = new Person('장동건', 20)
object.info()

//은닉성
//object.#name = '원빈';
//object.info();   // 외부에서는 접근 불가

console.log( Person.nation );
Person.staticMethod();

//getter, setter는 파이선과 동일
object.name = '원빈'
console.log( object.name );
object.info();

/* DOM : Document Object Model

- 현재 브라우저에서 보여지는 문서는 하나의 document객체로 표현되어 집니다.
- 자바스크립트는 document를 통해서 웹의 모든 내용을 전부 제어
- 모든 요소에 대한 정의와 접근 방법들이 전부 명시되어 있습니다.
- 요소를 추가, 수정, 삭제
- 요소에 대한 속성도 추가, 수정, 삭제
- 이벤트에 대한 제어도 가능합니다

- js 'document' 객체 내의 요소들을 다룰 수 있는 API를 제공
  1. document.getElementsByTagName('태그이름')
  2. document.getElementsById('Id 속성')
  3. document.getElementsByClassName('클래스 속성')
  4. document.querySelectorAll('CSS 선택자')

  5. 접근 예시
  ex) document.querySelectorAll('li.nav_item a[data-clk="svc.cafe"]')[0].innerText = 
      '자바스크립트를 통해서 바꿔줄 수 있다는 거죠';

- 계층구조를 이용한 접근
  1. DOM 구조에서는 각 요소들이 전부 하나의 객체임
    - DOM 구조 : document.요소이름
  2. DOM에서 각 노드와의 관계는 다음과 같습니다.
    가. parentNode: 현재 노드의 상위 노드(부모 노드)
    나. childNodes: 자식 노드들의 배열
    다. firstChild: 첫 번째 자식 노드
    라. lastChild: 마지막 자식 노드
    마. nextSibling: 다음 형제 노드
    바. previousSibling: 이전 형제 노드

  3. 계층구조를 이용한 요소 접근 예시
  ex) document.body.childNodes[3].childNodes[5].childNodes[5].c~~
*/



/* BOM : Browser Object Model / window.객체이름

- 브라우저 또한 객체로서 관리
- window 객체
  1. history : 방문한 페이지에 대한 정보
  2. location : 현재 열려있는 페이지에 대한 정보

- 접근 예시
  ex) window.history.back()  : 히스토리상 이전 페이지로 이동
  ex) window.history.forward() : 히스토리상 다음 페이지로 이동
  ex) window.location.href : 현재 열려있는 페이지의 URL