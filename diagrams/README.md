# 다이어그램 안내

[애니메이션 관계도](ai-harness.html) · [미리보기](../assets/images/ai-harness-preview.png) · [구조 원본](ai-harness.architecture.json)

프로젝트 공통 ↔ 각 파트 공통 ↔ 개인 하네스의 관계를 설명합니다. 양방향 화살표는 기준 공유와 작업 경험의 교류를 나타내고, 애니메이션은 공통에서 아래 계층으로 흐르는 기준을 표시합니다. 피드백이 곧 공통 기준의 확정을 뜻하지는 않습니다.

## 파일과 갱신 방법

- `ai-harness.architecture.json`: 노드·관계·설명 원본입니다.
- `ai-harness.html`: Archify 3.2.0으로 생성한 독립 HTML입니다. 브라우저에서 직접 열 수 있으며 상단 동적·정적 버튼으로 재생을 제어합니다.
- `ai-harness.runtime.patch`: 이 관계도에서만 자동 재생하고, 피드백 방향은 정적으로 유지하도록 한 뷰어 조정입니다. 공식 Archify 3.2.0 패키지의 `archify/assets/template.html`에 적용합니다. 다른 다이어그램에는 적용되지 않도록 세 노드 ID로 범위를 제한합니다.
- `../assets/images/ai-harness-preview.png`: 생성한 HTML의 정지 화면입니다. README와 시작 페이지에서 사용합니다.

갱신할 때 JSON 원본을 먼저 수정합니다. Archify 패키지에 뷰어 패치를 적용한 뒤, 이 저장소 루트에서 다음 명령으로 다시 생성합니다. `<Archify 경로>`는 실제 설치 위치로 바꿉니다.

```text
node <Archify 경로>/bin/archify.mjs finalize architecture diagrams/ai-harness.architecture.json diagrams/ai-harness.html --quality showcase --json
```

기존 산출물에 검증 기록이 있으면 Archify의 재생성 기준에 따라 새 `--out-dir`를 지정합니다. 결과 HTML의 다이어그램 구조를 직접 수정하지 않습니다. 재생성 후 양방향 관계, 아래 방향 애니메이션, 일시정지, 동작 줄이기 설정과 미리보기를 확인합니다. 검증 영수증과 임시 화면은 저장소에 올리지 않습니다.

관계도는 합의한 운영 방식을 설명하는 자료입니다. 실제 저장소 연동이나 AI 도구의 자동 적용을 구현한 결과를 뜻하지 않습니다.

## 문서와 자원 구분

이 폴더에는 독립 다이어그램 HTML, 구조 원본과 갱신 안내를 둡니다. README·시작 페이지에서 쓰는 정지 미리보기와 브리핑에 삽입하는 SVG는 assets/images/의 이미지 자원입니다. [공통 문서 자원 안내](../project/assets.md)를 함께 참고합니다.

## AI 컨텍스트 운영 문서의 설명도

[AI 작업 가이드 심화](../project/ai-context.html)의 설명도 8개는 [Markdown 원본](../project/ai-context.md)의 Mermaid 블록으로 관리합니다. 공통 테마의 `diagram-frame`과 프론트엔드 문서에서 사용하는 Mermaid 설정을 그대로 사용합니다. 별도 SVG·전용 CSS는 사용하지 않습니다.

문구와 관계는 Markdown의 Mermaid 블록에서 먼저 수정하고, 저장소 루트에서 다음 명령으로 HTML에 반영합니다.

```text
python diagrams/ai-context.generate.py
```

이 명령은 HTML의 Mermaid 블록만 맞춥니다. 본문과 그림 설명을 변경하면 Markdown·HTML을 함께 수정합니다. 보관함과 작업대·처리 흐름·두 관리 계층·자료 선별·문맥 예산·작업 재개·검증 피드백·원본 대조의 관계를 확인합니다.

`assets/js/mermaid.js`는 2026-11-09에 프론트엔드 가이드 `lounge-docs/docs/assets/js/mermaid.js`에서 가져온 설정입니다. Mermaid 11.16.0 CDN 모듈을 읽으므로 최초 표시에는 네트워크 연결이 필요합니다. 원본 설정이 바뀌면 공통 관리자가 비교한 뒤 갱신합니다. 공통 테마의 색상·폰트·곡선 연결선·자동 배치 설정을 사용하며, 그림별로 글자를 확대하지 않습니다.
