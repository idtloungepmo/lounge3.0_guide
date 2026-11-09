# 공통 HTML 템플릿

각 PL이 docs/ 아래의 사람용 문서를 만들 때 복사해서 사용하는 공통 형식입니다. 구조·공통 화면 형식은 맞추고, 내용·상세 목차·업무 절차는 각 PL이 정합니다. [공통 문서 운영 기준](../project/documentation.md)을 따릅니다.

| 파일 | 용도 |
| --- | --- |
| [index.html](index.html) | 선택·사용 안내 |
| [overview.md](overview.md) · [overview.html](overview.html) | 파트 docs 시작 페이지의 Markdown 원본과 표현 예시 |
| [document.md](document.md) · [document.html](document.html) | 상세 가이드 원본과 표현 예시 |
| [AGENTS.md](AGENTS.md) | 템플릿 관리 지침 |

## 사용 순서

1. 목차형은 예를 들어 planning/docs/index.md와 index.html로, 문서형은 planning/docs/guides/주제.md와 주제.html로 복사합니다. 폴더와 문서는 실제 내용이 생길 때 만듭니다.
2. Markdown 원본에 내용을 작성한 뒤 HTML의 제목·설명·절·본문·링크를 맞춥니다. HTML 자동 생성은 전제하지 않습니다. 업무 원본은 복제하지 않고 연결합니다.
3. HTML의 body에 data-part="planning", "design", "frontend", "backend" 중 해당 값을 지정합니다. 공통 문서는 생략합니다.
4. 원본 위치·홈·assets 경로를 복사 위치에 맞춥니다. 템플릿은 templates/ 위치에서 미리보기하도록 ../assets/를 사용합니다. 파트 docs 바로 아래는 ../../assets/, docs/guides 바로 아래는 ../../../assets/를 사용합니다.
5. docs/AGENTS.md, 파트 문서 목록, 사람용 목차를 갱신합니다. 업무 절차는 workflow/에, 상세 기준은 guides/에, 필요한 핵심 요약은 ai/에 둡니다.
6. 링크·번호 있는 h2·공통 자원 경로·원본과 HTML의 내용 일치를 확인합니다. 화면 변경은 가능한 범위에서 넓은 화면과 좁은 화면을 확인합니다.

## 공통 화면 규칙

Header에는 종류·제목·설명, Footer에는 문서명만 둡니다. 수기 가이드에 날짜·버전·Draft 표시를 일괄 추가하지 않습니다. 공통 common.js의 h2 메뉴와 별도 수동 목차를 중복 생성하지 않습니다. 코드 예시는 pre.hljs와 code[data-language]를 사용하며 코드의 문자·공백·줄바꿈을 보존합니다. 개별 미정은 badge-tbd를 사용합니다.

[공통 문서 자원 안내](../project/assets.md) · [협의·결정·인수인계 내용 양식](../collaboration/templates.md). 내용 양식과 HTML 템플릿은 역할이 다릅니다.

## 글쓰기 기준

한국어 문서는 [공용 글쓰기 스킬](../skills/guides/korean-work-writing/SKILL.md)을 적용합니다. 적용 조건과 해야 할 행동을 구체적으로 설명합니다. 코드·인용·요청문 예시와 업무상 조건은 유지합니다.

## 별도 파트 저장소에서 사용

별도 저장소에서는 공통 가이드의 실제 로컬 위치와 파트 작업 위치를 AI에 함께 전달합니다. 공통 문서·스킬을 복사해 별도 기준으로 유지하지 않습니다. HTML에 필요한 CSS·JS를 파트 저장소로 가져오는 경우 담당 PL이 공통 원본·기준 커밋·복사 위치·갱신 방법을 기록합니다. 원격 자원을 직접 연결하는 경우에는 실제로 확인된 정적 게시 주소만 사용합니다. GitHub 파일 보기 주소를 CSS·JS 주소로 사용하거나 저장소가 형제 폴더에 있다고 가정하지 않습니다.

위 상대 경로 예시는 이 공통 저장소 내부의 배치 기준입니다. 별도 저장소로 복사하면 실제 자원 위치에 맞춰 변경하고 브라우저에서 경로를 확인합니다.
