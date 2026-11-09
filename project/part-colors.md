# 파트별 공통 색상 기준

상태: 사용자 지정 기준 · 2026-11-06
적용 범위: 프로젝트 문서·가이드에서 기획·디자인·프론트엔드·백엔드를 구분하는 색상.

앞으로 각 파트의 대표 색상은 기획=핑크, 디자인=그린, 프론트엔드=블루, 백엔드=옐로우로 일관되게 사용합니다. 시작 페이지의 카드·파트 이름·표식과 이후 파트별 안내에도 같은 구분을 적용합니다. 파트 이름을 함께 표시해 색상과 의미를 바로 연결합니다.

## 색상 원본

공통 CSS 변수 원본은 [part-colors.css](../assets/style/part-colors.css)입니다. 다른 문서에서도 이 파일을 연결해 재사용합니다. 색 값을 페이지마다 직접 쓰거나 별도 팔레트로 다시 정의하지 않습니다.

| 파트 | 대표 색상 | main | bg: 아주 연한 배경 | border: 테두리 | text: 글자 |
| --- | --- | --- | --- | --- | --- |
| 기획 · planning | 핑크 | #db2777 | #ffedf5 | #efc5d8 | #9d2057 |
| 디자인 · design | 그린 | #16a34a | #eaf7ef | #bfe1cb | #216b3b |
| 프론트엔드 · frontend | 블루 | #2563eb | #eaf2ff | #c3d6f4 | #2452a1 |
| 백엔드 · backend | 옐로우 | #eab308 | #fff7d9 | #e9d996 | #80620b |

색상 계열은 사용자 지정이고 구체적인 값은 초기 적용값입니다. 값을 조정할 때도 파트와 색상 계열의 대응은 유지하고 공통 CSS 원본에서 수정합니다.

## 변수와 사용법

파트별 변수는 `--part-planning-main`, `--part-planning-bg`, `--part-planning-border`, `--part-planning-text` 형식입니다. planning을 design·frontend·backend로 바꿔 해당 파트 변수를 사용할 수 있습니다.

요소나 페이지에 `data-part="planning"`처럼 파트를 지정하면 그 범위에서 `--part-main`, `--part-bg`, `--part-border`, `--part-text`로 사용할 수 있습니다. 공통 컴포넌트는 이 범위 변수를 사용합니다.

```html
<link rel="stylesheet" href="assets/style/part-colors.css">
<article class="part-panel" data-part="planning">기획</article>
```

```css
.part-panel {
  background: var(--part-bg);
  border: 1px solid var(--part-border);
  color: var(--part-text);
}
```

- 대표색 main은 파트 표식·포인트에 사용합니다.
- 넓은 카드·안내 영역은 아주 연한 bg를 사용합니다.
- 글자·링크에는 읽기 쉬운 text를 사용합니다. 특히 옐로우 대표색을 본문 글자색으로 사용하지 않습니다.
- 프로젝트 공통·파트 간 협업에는 네 파트 중 하나의 색을 임의 배정하지 않습니다.
- 실제 서비스 UI의 디자인 토큰은 해당 원본에서 관리합니다. 이 파일은 문서·가이드의 파트 구분 색상 원본입니다.

[사람용 시작점](../index.html#areas) · [정보 관리 기준](maintenance.md)
