# 공통 문서 자원

전체 시작 페이지와 각 파트 HTML이 같은 모양과 동작을 사용하도록 공통 자원을 모으는 폴더입니다. 문서 본문이나 실제 서비스 구현 코드를 보관하는 곳은 아닙니다.

| 위치 | 역할 | 사용 대상 |
| --- | --- | --- |
| style/presentation-theme.css | 글꼴·제목·표·코드·반응형·인쇄 기본 테마 | 모든 HTML |
| style/part-colors.css | 기획 핑크·디자인 그린·프론트엔드 블루·백엔드 옐로우 변수 | 모든 HTML |
| style/project-guide.css | 전체 시작 페이지의 카드·시작 흐름 등 | 루트 index.html |
| style/document.css | 파트 시작 페이지와 개별 문서의 공통 구성 | 템플릿과 파트 HTML |
| js/common.js | 긴 코드 접기·절 이동 메뉴 등 공통 동작 | 필요한 HTML |
| js/project-guide.js | 루트 AI 요청문 복사 | 루트 index.html |

## 연결 순서

기본 테마 → 파트 색상 → 해당 화면 CSS 순서로 연결합니다. 파트 폴더 바로 아래 HTML의 예:

```html
<link rel="stylesheet" href="../assets/style/presentation-theme.css">
<link rel="stylesheet" href="../assets/style/part-colors.css">
<link rel="stylesheet" href="../assets/style/document.css">
<script src="../assets/js/common.js" defer></script>
```

더 깊은 폴더에서는 상대 경로를 조정합니다. 파일 전체를 복사하는 대신 같은 assets 원본을 연결합니다.

## 이미지·아이콘·폰트

현재 이미지·아이콘·폰트 파일은 포함하지 않습니다. 필요할 때 images/·icons/·fonts/를 만들고 용도·출처·사용 조건을 함께 기록합니다. 기본 테마는 설치된 한글 글꼴과 시스템 글꼴을 순서대로 사용하며 외부 폰트 다운로드에 의존하지 않습니다.

이 색상과 테마는 프로젝트 문서용입니다. 실제 서비스 UI의 디자인 토큰과는 적용 범위를 구분합니다.

[HTML 템플릿](../templates/index.html) · [AI 관리 지침](AGENTS.md) · [전체 시작 페이지](../index.html)

## 파트 docs에서 연결

공통 문서 운영 기준은 [문서 운영](../project/documentation.md)을 따릅니다. project_guide 내부의 파트 docs 바로 아래 HTML은 ../../assets/, docs/guides 바로 아래는 ../../../assets/를 연결합니다. 별도 저장소·호스팅은 실제 배포 경로와 공통 자원 갱신 관계를 PL이 정합니다.

## 공통 HTML 브리핑

[공통 기준 브리핑](../presentation.html)은 기존 브리핑의 시각 형식과 동작을 재사용합니다. 발표 내용의 원본은 [presentation.md](../presentation.md)입니다.

| 파일 | 역할 |
| --- | --- |
| style/briefing-presentation.css | 발표용 스타일 연결. 아래 세 CSS를 불러옵니다. |
| style/briefing-presentation.foundation.css | 색상·글꼴·발표 장면·탐색 기본 형식 |
| style/briefing-presentation.components.css | 공통 카드·역할 색상·순서 팔레트·연결선 |
| style/briefing-presentation.sections.css | 공통 배치·반응형·인쇄 형식 |
| js/briefing-presentation.js | 장면 표시·스크롤 진행·키보드 이동 |

일반 문서의 presentation-theme.css와 발표용 스타일은 적용 목적이 다릅니다. 새 HTML 발표에는 [공용 브리핑 스킬](../skills/guides/html-presentation-design-system/SKILL.md)과 한국어 글쓰기 기준을 함께 적용합니다. 공통 자원은 복사본을 늘리지 않고 참조하며, 개별 발표에만 필요한 배치는 해당 발표의 스타일에서 관리합니다.

## 협업 흐름도

[human-ai-workflow.svg](diagrams/human-ai-workflow.svg)는 브리핑에서 사용하는 사람·AI 협업 흐름도입니다. 사람과 AI의 역할, 판단 분기, 수정·재검증 후 다시 확인하는 경로를 표시합니다. 내용을 변경하면 presentation.md의 설명과 SVG를 함께 갱신합니다.
