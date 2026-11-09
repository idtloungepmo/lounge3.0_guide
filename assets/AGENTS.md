# 공통 문서 자원 관리 지침

이 폴더는 HTML 문서에서 함께 사용하는 스타일·동작·시각 자원을 관리합니다.

- 파일별 역할과 사용 방법은 [문서 자원 안내](README.md)를 확인합니다.
- style/에는 CSS, js/에는 공통 동작을 둡니다. 이미지·아이콘·폰트는 실제 자료가 생길 때 필요한 폴더만 추가합니다.
- presentation-theme.css와 common.js는 공통 스타일과 동작을 관리합니다. 변경 전 사용하는 문서에 미치는 영향을 확인합니다.
- project-guide.css는 전체 시작 페이지에 사용합니다. document.css는 파트 시작 페이지와 개별 문서에 사용합니다.
- project-guide.js는 전체 시작 페이지의 요청문 복사 기능을 담당합니다. 개별 문서에 불필요하게 추가하지 않습니다.
- 공통 CSS·JS는 같은 원본을 사용합니다. 파트 전용 자원은 담당 PL이 관리하고 여러 파트에서 필요해지면 공통 사용을 협의합니다.
- 파트 색상은 [공통 색상 기준](../project/part-colors.md)을 따릅니다. data-part와 CSS 변수·파일명은 유지합니다.
- 자원을 변경하면 관련 링크·키보드 조작·데스크톱·모바일·인쇄 결과를 가능한 범위에서 확인합니다. 확인하지 못한 범위는 표시합니다.

- HTML 발표에는 briefing-presentation.css와 briefing-presentation.js를 사용합니다. 발표 자원 변경은 [공용 브리핑 스킬](../skills/guides/html-presentation-design-system/SKILL.md)을 적용하고 장면 이동·반응형·인쇄 영향을 확인합니다.
