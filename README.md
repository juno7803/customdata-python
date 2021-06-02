## Capstone Design - customData

### 👨🏻‍💻 OpenCV 를 이용한 customDataset 만들기
1. 배경색 변경하기 (색 반전 등)
    ```python
        def coloring(source)
   ```
   
2. 이미지에 noise 추가하기 (blur 처리 등)
    ```python
        def bluring(source)
    ```
   
3. 다른 이미지와 합성하기(원고지 등을 합성하여 배경으로 사용)
    ```python
        def synthesis(source, background)
   ```
   
### 🙆🏻‍♂️ How to use
- `filename`에 원본 이미지 경로를 기입합니다.
- 배경 합성시엔, `background`에 원본 배경 이미지 경로를 기입합니다.
- `change.py` 파일을 실행합니다.
```python
    python3 change.py # 를 통해 실행합니다
```
