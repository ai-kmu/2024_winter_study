**실습파일** - [프로젝트의 마지막 주소 다운 받기](https://www.yalco.kr/@git-github-dive/7-1/)

**맨 처음 파일에서 Ctrl + S 로 모든 파일 저장 후 first commit**
**모든 제출 이미지는 위에서부터 4개의 commit message를 담을 수 있게 캡처 후 제출한다.**


1. first commit 과 그 아래 3개의 commit message 가 나올 수 있도록 캡처한 이미지를 제출

2. git commit --amend 명령어 사용하여, commit message 를 modify로 변경하고, 이미지 제출

```bash
git commit --amend
```
3. git rebase -i 명령어를 이용하여, modify commit 바로 전 commit 메시지를 삭제하고 이미지 제출하기
```bash
git rebase -i {commit hash}
```
**총 제출 이미지는 3장이며, 이미지의 이름은 순서대로 본인이름_{순서} 형태로 제출한다.**
