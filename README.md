## Capstone Design: customData

### 🌈 customData 소개
```
customData는 0 ~ 9 범위의 숫자로 이루어진 데이터셋 입니다.   
데이터를 수집한 방법은 다음과 같습니다
```
- iPad를 이용하여 `0 ~ 9` 범위의 숫자를 사람들에게 직접 기록을 부탁하였습니다.
- `25~27살` 남자 5명, `20~24살` 여자 5명에게 데이터를 받았습니다.
- 받은 데이터를 가공하여 저장하고, 거기에 `blur` `color` `synthesis` 를 적용하였습니다.
- 현재 숫자당 약 1,200 여개의 데이터가 존재합니다.

<br/>

### 👨🏻‍💻 OpenCV 를 이용한 customDataset 만들기
1. 배경색 변경하기
    ```python
        def coloring(num, source)
   ```
   
2. 이미지에 noise 추가하기 (blur 처리 등)
    ```python
        def bluring(num, source)
    ```
   
3. 다른 이미지와 합성하기(원고지 등을 합성하여 배경으로 사용)
    ```python
        def synthesis(num, source, background)
   ```
<br/>

### 🙆🏻‍♂️ How to use
- `filename`에 원본 이미지 경로를 기입합니다.
- 배경 합성시엔, `background`에 원본 배경 이미지 경로를 기입합니다.
- `change.py` 파일을 실행합니다.
```python
    python3 change.py # 를 통해 실행합니다
```
