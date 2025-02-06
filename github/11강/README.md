## 문제
오류가 발생한 지점 찾아내기


## 예제 파일에서 진행
https://www.yalco.kr/zips/lectures/git-github-dive/git-bisect.zip

## 수행 순서
1. 이진탐색 시작
```bash
git bisect start
```

2. 문제시점 표시
```bash
git bisect bad
```

3. 의심지점 이동
```bash
git checkout (v3 - suspicious으로 이동)
```

4. 문제시점을 good 또는 bad로 표시

5. error 지점 찾을 때까지 bisect 진행

6. 이진 탐색 종료
```bash
git bisect reset
```

## 제출
이진 탐색 종료 후 결과 캡쳐하여 `이름.png`로 이미지 제출
