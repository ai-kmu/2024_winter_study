# 문제 설명:
강의의 예제파일을 이용하여 새로운 브랜치를 생성하고, HEAD를 활용하여 다양한 커밋 간 이동을 실습하세요.

## 지시 사항:
1. `new-feature`라는 이름의 새로운 브랜치를 생성하세요.
    ```bash
    git branch new-feature
    ```

2. `new-feature` 브랜치로 전환하세요.
    ```bash
    git switch new-feature
    ```

3. 현재 브랜치에서 HEAD를 이용하여 이전 커밋으로 한 단계 이동하세요.
    ```bash
    git checkout HEAD^
    ```

4. 다시 최신 커밋으로 돌아오세요.
    ```bash
    git checkout main
    ```

5. HEAD의 상태를 확인하고, 이전 커밋으로 3단계 이동해보세요.
    ```bash
    git checkout HEAD~3
    ```

6. 특정 커밋 해시를 사용하여 해당 커밋으로 이동해보세요.
    ```bash
    git checkout <커밋 해시>
    ```

7. 이동한 상태에서 현재 브랜치의 상태를 확인하고, 다시 원래 브랜치로 복귀하세요.
    ```bash
    git switch new-feature
    ```

8. 이동한 브랜치에서 새로운 커밋을 추가로 생성하세요. (파일 추가 및 커밋)
    ```bash
    echo "New feature" > feature.txt && git add feature.txt && git commit -m "Add feature"
    ```

9. 추가로 생성된 커밋을 확인하고, HEAD를 사용하여 해당 커밋을 reset 하세요.
    ```bash
    git reset HEAD^
    ```

---

## 제출:
결과물 파일을 `.git` 디렉토리를 포함하여 `이름.zip` 파일로 제출
