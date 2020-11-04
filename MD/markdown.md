# MarkDown Study

## 1. 문단 구분을 위한 강제 개행
---
> 문단을 구별하려면 한 개 이상의 빈 줄을 문단 사이에 삽입하거나 줄의 마지막에 [Space bar] 를 두 번 이상 눌러 띄어쓰기를 하면 된다.


## 2. 헤더( Header )
---
"# 헤더 크기 (h1)"  
"## 헤더 크기 (h2)"  
"### 헤더 크기 (h3)"  
"#### 헤더 크기 (h4)"  
"##### 헤더 크기 (h5)"  
"###### 헤더 크기 (h6)"  
```Markdown
# # h1
## ## h2
### ### h3
#### #### h4
##### ##### h5
###### ###### h6  
```
    
## 3. 목록( Lists )
---
```
Unordered

* Item 1
* Item 2
    * Item 2a
    * Item 2b


Ordered

1. Item 1
1. Item 2
1. Item 3
    1. Item 3a
    1. Item 3b
```
Unordered
* Item 1
* Item 2
    * Item 2a
    * Item 2b

Ordered
1. Item 1
1. Item 2
1. Item 3
    1. Item 3a
    1. Item 3b

## 4. 이미지( Images )
---
```
![Github logo](../data/lena.png)
Format : ![이미지 alt명]( url 링크 )

<a href="#"><img src="../data/lena.png"></a>
Format : img 태그 사용 - 이미지 경로는 상대경로 or 절대경로
```

![Github logo](../data/Lena.png)  
> Format : ![이미지 alt명]( url 링크 )

<a href="#"><img src="../data/Lena.png"></a>  
> Format : img 태그 사용 - 이미지 경로는 상대경로 or 절대경로

  
## 5. 하이퍼 링크( Links )
---
```
[WK-Hanelso_GitHub]( https://github.com/WK-Hanelso )
```
[WK-Hanelso_GitHub]( https://github.com/WK-Hanelso )

## 6. 코드 블록( Code Blocks )
---
> 해당 프로그래밍 언어의 구문 구별 표시를 적용한 코드를 볼 수 있다.
```
 \``` javascript
function test() {
    console.log("Hello MarkDown!");
}
 \```
```
```javascript
function test() {
    console.log("Hello MarkDown!");
}
```

## 7. 인용 상자( BlockQuotes )
---
```
>하하하하
```
>하하하하

## 8. 강조( Emphasis )
---
```
*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

*You **can** combine them*
```
*This text will be italic*  
_This will also be italic_  
  
**This text will be bold**  
__This will also be bold__  

*You **can** combine them*

## 9. 테이블( Tables )
---
```
First Header | Second Header
------------ | --------------
Content cell 1 | Content cell 2
Content column 1 | Content column 2
```
First Header | Second Header
------------ | --------------
Content cell 1 | Content cell 2
Content column 1 | Content column 2

## 10. 체크 박스( Task Lists )
---
```
- [x] this is a complete item
- [ ] this is an incomplete item
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required ( any unordered or ordered list supported )
```
- [x] this is a complete item
- [ ] this is an incomplete item
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required ( any unordered or ordered list supported )
> 이거 안돼는게 같은데......

## 11. 인라인 코드( Inline code )
---
```
문단 중간에 `Code`를 넣을 수 있다.
예를 들어 `printf("Hello MarkDown!");` 이런 식으로 들어간다.
```
문단 중간에 `Code`를 넣을 수 있다.  
예를 들어 `printf("Hello MarkDown!");` 이런 식으로 들어간다.

## 12. 수평선 ( hr )
---
```
---
***
___
```
---
***
___

## 13. 탈출 문자( Backslash Escapes )
---
```
＼*literal asterisks＼* 
*literal asterisks* 
__＼*＼*Text＼*＼*__ 
_＼_Tom＼__
```
\*literal asterisks\*   
*literal asterisks*   
__\*\*Text\*\*__   
_\_Tom\__
