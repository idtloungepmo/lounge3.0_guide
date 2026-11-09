# 공통 문서 자원

이 문서는 assets/에 있는 공통 스타일·스크립트·이미지의 역할과 사용 방법을 안내합니다. assets/에는 실행·시각 자원만 두고, 안내·관리 문서는 project/, 독립 다이어그램과 구조 원본·갱신 안내는 diagrams/에서 관리합니다.

| 위치 | 역할 | 사용 대상 |
| --- | --- | --- |
| assets/style/presentation-theme.css | 글꼴·제목·표·코드·반응형·인쇄 기본 테마 | 모든 HTML |
| assets/style/part-colors.css | 기획 핑크·디자인 그린·프론트엔드 블루·백엔드 옐로우 변수 | 모든 HTML |
| assets/style/project-guide.css | 전체 시작 페이지의 카드·시작 흐름 등 | 루트 index.html |
| assets/style/document.css | 파트 시작 페이지와 개별 문서의 공통 구성 | 템플릿과 파트 HTML |
| assets/js/common.js | 긴 코드 접기·절 이동 메뉴 등 공통 동작 | 필요한 HTML |
| assets/js/project-guide.js | 루트 AI 요청문 복사 | 루트 index.html |

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

assets/images/에는 관계도 미리보기와 협업 흐름도 SVG를 둡니다. 이미지·아이콘·폰트를 추가하면 용도·출처·사용 조건을 관련 문서에 기록합니다. 기본 테마는 설치된 한글 글꼴과 시스템 글꼴을 순서대로 사용하며 외부 폰트 다운로드에 의존하지 않습니다.

이 색상과 테마는 프로젝트 문서용입니다. 실제 서비스 UI의 디자인 토큰과는 적용 범위를 구분합니다.

[HTML 템플릿](../templates/index.html) · [AI 관리 지침](AGENTS.md#공통-문서-자원-변경) · [전체 시작 페이지](../index.html)

## 파트 docs에서 연결

공통 문서 운영 기준은 [문서 운영](documentation.md)을 따릅니다. lounge3.0_guide 내부의 파트 docs 바로 아래 HTML은 ../../assets/, docs/guides 바로 아래는 ../../../assets/를 연결합니다. 별도 저장소·호스팅은 실제 배포 경로와 공통 자원 갱신 관계를 PL이 정합니다.

## 공통 HTML 브리핑

[공통 기준 브리핑](../presentation.html)은 기존 브리핑의 시각 형식과 동작을 재사용합니다. 발표 내용의 원본은 [presentation.md](../presentation.md)입니다.

| 파일 | 역할 |
| --- | --- |
| assets/style/briefing-presentation.css | 발표용 스타일 연결. 아래 세 CSS를 불러옵니다. |
| assets/style/briefing-presentation.foundation.css | 색상·글꼴·발표 장면·탐색 기본 형식 |
| assets/style/briefing-presentation.components.css | 공통 카드·역할 색상·순서 팔레트·연결선 |
| assets/style/briefing-presentation.sections.css | 공통 배치·반응형·인쇄 형식 |
| assets/js/briefing-presentation.js | 장면 표시·스크롤 진행·키보드 이동 |

일반 문서의 presentation-theme.css와 발표용 스타일은 적용 목적이 다릅니다. 새 HTML 발표에는 [공용 브리핑 스킬](../skills/guides/html-presentation-design-system/SKILL.md)과 한국어 글쓰기 기준을 함께 적용합니다. 공통 자원은 복사본을 늘리지 않고 참조하며, 개별 발표에만 필요한 배치는 해당 발표의 스타일에서 관리합니다.

## 협업 흐름도

[human-ai-workflow.svg](../assets/images/human-ai-workflow.svg)는 브리핑에서 사용하는 사람·AI 협업 흐름도입니다. 사람과 AI의 역할, 판단 분기, 수정·재검증 후 다시 확인하는 경로를 표시합니다. 내용을 변경하면 presentation.md의 설명과 SVG를 함께 갱신합니다.

## AI 하네스 관계도

[애니메이션 관계도](../diagrams/ai-harness.html)는 프로젝트 공통 ↔ 각 파트 공통 ↔ 개인 하네스의 관계를 설명합니다. 기준의 흐름은 위에서 아래로 재생됩니다. [원본과 갱신 방법](../diagrams/README.md)을 따릅니다.

별도 저장소에서는 공통 가이드의 실제 로컬 위치와 파트 작업 위치를 AI에 함께 전달합니다. 공통 문서·스킬을 복사해 별도 기준으로 유지하지 않습니다. HTML에 필요한 CSS·JS를 파트 저장소로 가져오는 경우 담당 PL이 공통 원본·기준 커밋·복사 위치·갱신 방법을 기록합니다. 원격 자원을 직접 연결하는 경우에는 실제로 확인된 정적 게시 주소만 사용합니다. GitHub 파일 보기 주소를 CSS·JS 주소로 사용하거나 저장소가 형제 폴더에 있다고 가정하지 않습니다.
