### 시맨틱 태그 

-  HTML5에서 의미론적 요소를 담은 태그의 등장 (Non semantic 요소: `div`, `span`) (`h1` ,`table` 태그는 포함 가능)
  - `hearder` : 문서 전체나 섹션의 헤더(머릿말 부분)
  - `nav`: 내비게이션
  - `aside`: 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  - `section`: 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - `article`: 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - `footer`: 문서 전체나 섹션의 푸터(마지막 부분)




### HTML Global Attribute

- 모든 요소가 공통으로 사용할 수 있는 속성(몇몇 요소에는 아무 효과 없을 수 있음)
  -  `id` ,`class`
  - `hidden` 
  - `lang`
  - `style`
  - `tabindex`
  - `title`



### `display: block` vs `display: inline`

- `block` : 줄바꿈 O, 화면 전체 가로 폭 차지, 블록 안에 인라인 들어갈 수 있음
  - `div` / `ul`, `ol`, `li` / `p` / `hr` / `form`
  - `margin-right:auto;` `margin-left:auto;` `margin-right:auto; margin-left:auto;`

- `inline`: 줄바꿈 X, content 너비만큼 가로 폭 차지, width/height/margin-top(bottom) 지정 불가, 상하 여백은 line-height로 지정
  - `span` / `a` / `img` / `input`, `label` / `b`, `em`, `i`, `strong` 등
  - `text-align: left;` `text-align: right;` `text-align: center;`
- `lnline-block`: blcok과 inline 요소의  특징 모두 보유, 한줄에 표시 가능, width/height/margin 모두 지정 가능
- `display: none`:  해당 요소를 화면에 표시 X(공간조차 사라짐)  vs  `visibilty: hidden` 은 화면 표시X이지만 공간은 차지 (출제유력)



- 주의 : `class: 속성`이 다수일 경우, 순서가 바뀌어도 출력에는 영향 없고,  style 소스 내부에서 제일 마지막으로 선언된 속성을 따름

### CSS 상속

- 상속되는 것 예시 : Text 관련 요소(font, color, text-align), opacity, visibility 등

- 상속되지 않는 것 예시 : Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left, z-index) 등



### 5. box model shorthand



### box-sizing

- border까지의 너비를 보기 위해 기본값 `content-box`을 `border-box`로 설정할 필요 있음

  

### 마진 상쇄



### `absolute` vs `relative` vs `fixed`

- 좌표 프로퍼티(top, bottom, left, right) 사용하여 이동 가능(음수도 가능)



HTML : 웹 페이지가 어떻게 구조화되어 있는지 알 수 있도록 하는 마크업 언어

CSS : 사용자에게 문서(HTML)를 표시하는 방법을 지정하는 언어



### float

-  text나 인라인 요소만 감쌀 수 있음. 블록 요소는 float 요소 밑으로 들어가는 현상 발생

  

  ```css
  .left { 
      float: left;
  }
  
  /* 가상요소는 float 요소 위에 부모 요소를 만들어서 클래스로 사용 */
  .clearfix::after {
  content: "";
  display: block;  /* float 가상요소의 기본값은 inline */
  clear:both;     /* 보통 both로 사용 */
  }
  ```

  

### flexbox

```css
flex-direction: row;
flex-direction: row-reverse;
flex-direction: column;
flex-direction: column-reverse;

flex-wrap: nowrap;
flex-wrap: wrap;
flex-wrap: wrap-resverse;

/* flex-direction + flex-wrap의 shorthand */
flex-flow: column wrap;


```



```css
flex-grow /* - 메인축에서 남은 공간을 각 항목에게 분배
        - 각 아이템의 상대적 비율을 정하는 것이 아님
        - 음수는 불가능
        - 기본값 0 
```



### bootstrap

```css
m-1 : 0.25rem 4px

m-2 : 0.5rem 8px

m-3 : 1rem 16px

m-4 : 1.5rem 24px

m-5 : 3rem 48px
```



### grid system

`container` ->  `row` -> `column` 

12개의 column   /    6개의 gird breakpoints

- offset
- nesting
- gutter



### Media Query

```css
@media screen, print { ... }
@media (max-width: 12450px) { ... }
@media (min-width: 30em) and (orientation: landscape) { ... }
@media (orientation: landscape) {
    p.orientation::after { content: '가로입니다.' }
}
```



### Favicon(favorite icon)



### Source files  ->  compiled CSS

##### SCSS(SASS) : Syntactically Awesome Style Sheets

- css 근본
- sass 급진
- scss 중도



##### compiled CSS

- `.rtl.css`: right to left로 작성된 언어(아랍어) 대응용

- `.min.css` : 모든 공백(space, enter, tab 등)을 제거하여 경량화(압축)한 CSS 파일

- `.css.map` :  디버깅을 위해 원본소스와 매핑해주는 파일





















