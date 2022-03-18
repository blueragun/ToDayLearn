# Flutter

## 설치방법

1. https://docs.flutter.dev/get-started/install/windows (윈도우)를 통해 Flutter SDK를 다운받는다
2. 설치경로는 C:/user/<user-name>/이 좋다
3. 시스템 - 고급 시스템 설정에서 환경변수를 편집해준다. path - flutter 경로 추가
4. cmd 를 열고 flutter doctor를 입력해 설치되어 있는지 확인한다. 아마 android studio가 설치되어 있지 않다고 뜰것이다.
5. 그 후 flutter 홈페이지 에서 android studio를 받아 설치해준다.

##  Flutter의 특징

1. Flutter란.

   - Google에서 발표한 크로스플랫폼 SDK.
   - 안드로이드, IOS, 웹까지 동시 개발 가능
   - 구글이 만들어 신뢰도와 발전가능성이 높음
   - 컴파일적인 특징덕에 다른 플랫폼보다 속도가 빠름

2. 네이티브 ARM 코드로 미리 컴파일 됨

   ![img](https://blog.kakaocdn.net/dn/cryLMt/btq97OjPeYh/xHvvrZmx7jnaBwJpe1rXJk/img.png)

   - React는 JS bridge를 통해 컴파일을 하였지만 Flutter는 브릿지가 존재하지 않으며 Native 코드로 미리 컴파일 됨

3. Flutter의 장점

   - 개발비용 절감 : OS에 따라 여러번 개발할 필요가 없고 유지보수가 간단함. 비용을 절감할 수 있음
   - 리로드가 빠름 : 컴파일 과정없이 개발과정을 빠르게 UI를 휴대폰에서 확인할 수 있음
   - UI 안정성이 높다

4. Flutter의 단점

   - 플러그인이 적다 : 개발된지 얼마 되지 않아 충분하지 않음
   - 아키텍처와 같은 레퍼런스가 적다. 아키텍처가 정해진게 없다. 개발 규칙들 또한 미약
   - 코드가 아직은 아름답지 않다.

##  Flutter UI

1. 모든 것이 위젯

![img](https://blog.kakaocdn.net/dn/dtpcRt/btqF1AGWkSX/fY7aFWkGjKzK6yaVEJU9KK/img.png)

- UI선언 및 구성방식과 관련된 모든 것은 위젯으로 이루어짐. Java에서는 모든 객체가 Object라는 Class를 상속받는다. 이와 마찬가지로 Flutter에서 UI선언 및 구성 방식에 관련된 모든것들이 위젯을 상속받는다.

- 기존에 Android, IOS에서는 명령형 UI 방식을 통해 UI를 작성. 하지만 Flutter에서는 React Native와 같은 선언적 UI 방식채택.

  선언적 UI 방식이란 UI 객체를 직접 만드는 것이 아니라, UI의 설명만 작성하는 방식. 그러면 프레임워크가 Render Object를 통해 UI객체 생성과 유지를 뒤에서 관리함. 즉 UI 객체가 생성되고 유지되는 세세한 작업을 몰라도 됨. 

  그냥 UI에 대한 설명을 잘 작성하면 프레임워크가 나머지는 함. 하지만 프레임워크가 UI객체 생성과 유지를 관리를 해주기 때문에, UI 객체를 직접 변경해야함. (불변) UI 객체를 변경하려면 UI에 대한 설명을 변경한 후 다시 UI 객체를 생성해야 합니다.

2. Stateless, StateFul 위젯

   - 위젯은 크게 두 가지 Stateful, Stateless Widget으로 나뉨. 

   - UI 객체는 변경할 수 없으며 Widget을 변경 후 재생성해야함. 그리고 이에 관한 개념이 Stateless, Stateful Widget 입니다.

   - Stateless, Stateful로 개념이 나누어졌다고 해서 내부동작이 다르게 이루어지는 것은 아님. 둘은 똑같이 Widget을 상속받았고 동일하게 작동함. 하지만 Stateful Widget은 State라는 서브클래스를 가짐. 그리고 이것이 Stateless Widget과 Stateful Widget간의 유일한 차이 

   - Stateless Widget에 대해 먼저 말해보자면 말그대로 상태정보가 없는 Widget. 즉 변경이 일어나지 않는 Widget이라는 것. 변경이 일어나지 않기 때문에 상태를 굳이 관찰할 필요가 없다. 앱 화면의 로고(AssetImageWidget)를 대표적인 예시.  앱이 실행되는 동안 앱 화면의 로고가 변경되는 일은 없다.

   - Stateful Widget은 Stateless Widget과 다르게 상태정보를 가지고 있는 Widget. Stateful Widgte은 State라는 서브 클래스를 통해 상태정보를 저장. 만약 변경이 일어날 시에는 setState() 함수를 호출하여 State 정보를 변경시킴. 그러면 프레임워크가 변경을 감지하여 해당 UI 객체를 재생성하게 된다. 버튼을 누르면 Text가 바뀌는 등의 동작을 대표적인 예시로 들 수 있다.

     ```
     import 'package:flutter/material.dart';
     void main() {
       runApp(SampleApp());
     }
     class SampleApp extends StatelessWidget {  // 최상위 Widget은 변경이 없음으로 Stateless Widget
       @override
       Widget build(BuildContext context) {
         return MaterialApp(
           title: 'Sample App',
           theme: ThemeData(
             primarySwatch: Colors.blue,
           ),
           home: SampleAppPage(),
         );
       }
     }
     class SampleAppPage extends StatefulWidget {
       SampleAppPage({Key key}) : super(key: key);
       @override
       _SampleAppPageState createState() => _SampleAppPageState();
     }
     class _SampleAppPageState extends State<SampleAppPage> {
       // Default placeholder text
       String textToShow = "I Like Flutter";
       void _updateText() {
         setState(() {  // State 변경
           textToShow = "Flutter is Awesome!";
         });
       }
       @override
       Widget build(BuildContext context) {
         return Scaffold(
           appBar: AppBar(
             title: Text("Sample App"),
           ),
           body: Center(child: Text(textToShow)),
           floatingActionButton: FloatingActionButton(
             onPressed: _updateText,
             tooltip: 'Update Text',
             child: Icon(Icons.update),
           ),
         );
       }
     }
     ```

     

## 화면전환(네비게이터, 루트)

- 하나의 화면으로 동작되는 앱은 정말 거의 없다. 그렇기에 화면을 전환할 수 있는 것은 앱의 기본중에 기본이다. 그리고 Flutter에서는 Navigator와 Route를 통해 화면전환을 수행. Route는 화면에 대한 추상화이며 Navigator는 Rotue를 관리하는 위젯.

- Route는 이름 그대로 화면을 파일 경로처럼 추상화한 것 . 보통 ‘/login’, ‘/home’ 과 같이 경로를 설정. 그리고 Map을 통해서 경로와 해당 화면을 매칭.

- Map을 이용하여 Route를 선언하는 예시.

  ```
  void main() {
   runApp(MaterialApp(
     home: MyAppHome(), // becomes the route named '/'
     routes: <String, WidgetBuilder> {
       '/a': (BuildContext context) => MyPage(title: 'page A'),
       '/b': (BuildContext context) => MyPage(title: 'page B'),
       '/c': (BuildContext context) => MyPage(title: 'page C'),
     },
   ));
  }
  ```

- Navigator는 스택으로 Route를 관리.push(), pop()을 통해 화면 경로를 조절. push(route)를 하면 해당 Route로 화면을 이동할 수 있고, pop()을 하면 이전 Route로 돌아갈 수 있다. 다음은 Navigator를 통해 화면을 이동하는 예시

  ```
  Navigator.of(context).pushNamed('/b');
  ```



## Stateful 위젯의 생명주기

- Lifecycle은 말그대로 생명주기. 인간으로 따지면 (아기 -> 청년 -> 중년 -> 노인 -> 죽음)을 Lifecycle이라고 할 수 있다. Lifecycle이 필요한 이유는 위의 인간의 예시를 들면 쉽게 이해할 수 있다.

  - 아기때는 지식을 습득

  - 청년때는 꿈을 이루기 위해 노력

  - 중년때는 안정을 갖추고 남에게 도움이 되고자 노력

  - 노인때는 죽음을 준비

- Lifecycle이 있으면 각각의 주기마다 할 행동을 지정할 수 있음. Stateless Widget은 이런 Lifecycle에 신경쓸 필요없다. 어차피 변경이 일어나지 않기 때문에 Framework에게 100% 맡기면 되기 때문. 하지만 변경이 일어나는 Stateful Widget에게는 Lifecyle이 필요.

  - createState() : State 객체가 최초로 생성되는 시점 BuildContext가 State에 할당된다.

  - mounted == true : BuildContext가 State에 할당됐는지 확인한다.
  할당됐으면 State가 마운트된 것으로 보고 true를 반환한다.

  - initState() : 이 Lifecycle때 Widget 혹은 BuildContext 초기화하면 된다.

  - didChangeDependencies() : 상속한 Widget이 업데이트될때 호출된다.

  - build() : Widget을 리턴하며 이를 바탕으로 Framework가 UI를 그린다.

  - didUpdateWidget() : Widget에 변경이 있을때 호출된다.

  - setState() : 위에서도 봤던 함수로 프레임워크에 변경사항을 알린다.

  - deactivatie() : state 객체가 삭제된다. 삭제되는 애니메이션 프레임이 끝나기 전에 재사용이 가능하다.

  - dispose() : State 객체가 트리에서 영구적으로 삭제된다.

  - mounted == false : State의 마운트가 완전히 해제됐다.



## 레이아웃 배치 배치방법

이외에 기타로 UI를 배치는  Flutter에서는 Widget Tree를 이용해서 배치

```
@override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Sample App"),
      ),
      body: Center( // 여기에 집중
        child: MaterialButton(
          onPressed: () {}, // 이런식의 Tree 방식으로 UI를 구성함
          child: Text('Hello'),
          padding: EdgeInsets.only(left: 10.0, right: 10.0),
        ),
      ),
    );
  }
```



## Flutter 상태관리

### Ephemeral(임시) State

- Ephemeral State(UI State, Local State)는 단일 위젯에 깔끔하게 포함할 수 있는 상태입니다. 정의가 굉장히 추상적이고 모호한데 이것은 일부로 이렇게 정의한 것이라고 합니다. 아마 정확히 한 가지로 정의하기 어려웠던 것 같습니다. 그렇기에 이해를 돕기위해 몇 가지의 예시를 들겠습니다.
  - 현재페이지에 PageView
  - 복잡한 애니메이션의 현재 진행 상황
  - 현재 선택된 BottomNavigationBar

### App state

- App State(Application State, Shared State)는 Ephemeral State 와는 다르게 앱의 여러부분에서 공유하고 사용자 세션간에 유지되어야하는 상태입니다. 설명이 난해한데 아래의 예시를 보시면 이해가 쉬우실 것 입니다.
  - 사용자 환경설정
  - 로그인 정보
  - 전자 상거래 앱(쿠팡)의 장바구니
  - 뉴스 앱의 Read/Unread State

### Ephemeral(임시) State, App State 사용 규칙



### Provider를 이용한 App State 관리

1. ChangeNotifier

   - 말그대로 변경사항을 알릴 수 있는 클래스입니다. notifyListener()를 사용하면 ChangeNotifier를 구독하고 있는 **Listener**에게 변경사항이 전달됩니다. 지금은 잘 이해가 안되실 수 있으나, 나머지(ChangeNotifierProvider, Consumer)를 살펴보고 난 후에는 이해하시는게 보다 쉬우실 것 입니다. 만약 Reactive Porgramming 혹은 Observer Pattern에 대해서 알고계신 분들은 익숙하신 개념이라 이해하기 쉬우실 것 입니다. 아래는 이해를 돕기위한 예제 코드입니다.

   ```
   class CartModel extends ChangeNotifier { // ChangeNotifier를 상속함
     CatalogModel _catalog;
   
     final List<int> _itemIds = [];
   
     CatalogModel get catalog => _catalog;
   
     set catalog(CatalogModel newCatalog) {
       _catalog = newCatalog;
       notifyListeners(); // 변경사항을 구독하고 있는 리스너에게 전달함
     }
   
     List<Item> get items => _itemIds.map((id) => _catalog.getById(id)).toList();
   
     int get totalPrice =>
         items.fold(0, (total, current) => total + current.price);
   
     void add(Item item) {
       _itemIds.add(item.id);
       notifyListeners();
     }
   }
   ```

   - 추가적으로 ChangeNotifier는 flutter:foundaition에 있고 higher-level classes(고수준 클래스 : Widget, etc,,) 에 의존성이 없어서 테스트하기가 쉽다고 합니다. 만약 Widget과 같은 **복잡한** 클래스(Widget 생성, 관리 코드 등등)를 상속하거나 알고있으면 테스트하기가 어렵겠죠,,, 아래는 간단한 단위 테스트입니다.

   ```
   test('adding item increases total cost', () {
     final cart = CartModel();
     final startingPrice = cart.totalPrice;
     cart.addListener(() {
       expect(cart.totalPrice, greaterThan(startingPrice));
     });
     cart.add(Item('Dash'));
   });
   ```

   

2. ChangeNotifierProvider

   - ChangeNotifierProvider는 ChangeNotifier를 하위 항목에 제공하는 위젯입니다. 아까전에 ChangeNotifier를 구독하고 있는 **Listener**에게 변경사항이 전달된다고 하였습니다. ChangeNotifierProvider는 하위 항목들에게 ChangeNotifier를 제공하여 구독할 수 있도록 해줍니다

   ```
   void main() {
     runApp(
       ChangeNotifierProvider( // 여기에 집중
         create: (context) => CartModel(),
         child: MyApp(),
       ),
     );
   }
   ```

   - ChangeNotifierProvider는 똑똑해서 CartModel의 Instance를 잘 관리해줍니다. CartModel의 Instance를 굳이 다시 rebuild 할 필요가 없고, dispose() 또한 ChangeNotifierProvider가 적절한 시점에(CartModel이 더 이상 필요없을때)자동으로 호출해줍니다. 한 문장으로 말하자면 ChangeNotifierProvider에서 생성한 ChangeNotifier(CartModel)은 이후에 신경쓸 필요없습니다.

     위의 예제는 단 한개만의 ChangeProvider를 선언하였는데요. 다음과 같이 여러개의 ChangeProvider를 선언할 수 도 있습니다.

   ```
   void main() {
     runApp(
       MultiProvider(
         providers: [
           ChangeNotifierProvider(create:(context) => CartModel()),// 1
           Provider(create: (context) => SomeOtherClass()), // 2
         ],
         child: MyApp(),
       ),
     );
   }
   ```

   

3. Consumer

   - 드디어 ChangeNotifier를 구독하고 있는 Listener 구간까지 도달했습니다. Consumer는 ChangeNotifierProvider에서 하위 항목에서 ChangeNotifier에 접근할 수 있게 하였습니다. 따라서 다음과 같은 코드가 가능합니다.

   ```
   return HumongousWidget(
     child: AnotherMonstrousWidget(
       child: Consumer<CartModel>( // 여기에 집중
         builder: (context, cart, child) {
           return Text('Total price: ${cart.totalPrice}');
         },
       ),
     ),
   );
   ```

   - 우리가 위에서 정의했던 ChangeNotifier의 이름은 CartModel입니다. 따라서 Consumer<**CartModel>** 과 같이 표기합니다. 그 다음 눈에 들어오는 것은 builder 함수입니다. Consumer 위젯의 유일한 필수 인자가 바로 builder 함수입니다. builder함수는 3가지의 인수로 작동합니다
     - context
     - 모든 build함수는 context를 인수를 가집니다.
     - ChangeNotifier
     - 우리가 정의한 ChangeNotifier(CartModel)입니다. ChangeNotifier의 데이터를 통해서 우리가 원하는 Widget을 작성할 수 있습니다.
     - child
     - 이름 그대로 가지고 있었던 서브트리 위젯입니다. 이를 이용해서 다시 서브트리를 작성하지 않고 재활용할 수 있습니다. 즉 최적화를 하는데 유용하게 사용할 수 있습니다. 아래는 해당 코드입니다.

   ```
   Consumer<CartModel>(
     builder: (context, cart, child) => Stack(
           children: [
             child, // 다시 사용함
             Text("Total price: ${cart.totalPrice}"),
           ],
         ),
     child: SomeExpensiveWidget(),
   );
   ```

   - 이렇게 작성된 Consumer 위젯은 ChangeNotifier(CartModel)에서 notifyListener()가 호출되면, 정의한 builder함수를 호출하여 **새로운 위젯**을 반환합니다. 여기까지 도달하셨다면 ChangeNotifier에 대해서 보다 쉽게 이해하실 수 있으실 것 입니다.

4. Provider.of

   - Provider.of 도 Consumer와 같이 ChangeNotifier를 구독하고 있는 Listener입니다. Consumer와 다른 점이라고 한다면 Provider.of는 위젯이 아니라 ChangeNotifier 그 자체를 반환합니다. 아래의 코드를 보면 보다 명확히 이해하실 것 입니다.

   ```
   class _CartList extends StatelessWidget {
     @override
     Widget build(BuildContext context) {
       // 그냥 CartModel을 반환함
       var cart = Provider.of<CartModel>(context); 
       
       return ListView.builder(
         itemCount: cart.items.length, // 사용 지점
         itemBuilder: (context, index) =>
             ListTile(
               leading: Icon(Icons.done),
               title: Text(
                 cart.items[index].name // 사용 지점
               ),
             ),
       );
     }
   ```

   - 만약 ChangeNotifier에서 notifyListener()가 호출되면 해당 StatelessWidget의 build() 다시 호출합니다. 만약 StatefulWidget 이라면 State.didChangeDependencies를 호출합니다. 간단히 말하자면 해당 Widget을 재빌드합니다.

     Provider.of 에는 특별한 사용법이 하나 더 있습니다. 만약 ChangeNotifier(CartModel)을 통해 UI를 구성하는게 아니라, 데이터를 초기화(removeAll() 함수와 같은 작업) 하려고 했다면 Widget을 다시 build()하는 것은 비용적 손해이지 않을까요? 그럴때는 다음과 같이 코드를 작성하면 됩니다.

   ```
   Provider.of<CartModel>(context, listen: false).removeAll();
   ```

   - 이런식으로 Provider.of 에서 lsitener 인자를 false로 설정하게 되면, notifyListener()가 호출되어도 Widget이 다시 build 되지 않습니다.