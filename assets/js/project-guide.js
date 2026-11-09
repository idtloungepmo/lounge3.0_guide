document.getElementById('copy-button').addEventListener('click',async function(){
 const source=document.getElementById('request-text');
 const status=document.getElementById('copy-status');
 try{
  if(!navigator.clipboard||!navigator.clipboard.writeText)throw new Error('clipboard unavailable');
  await navigator.clipboard.writeText(source.textContent);
  status.textContent='요청문을 복사했습니다. 이번 작업의 자료와 범위를 채워서 사용하세요.';
 }catch(error){
  const selection=window.getSelection();const range=document.createRange();
  range.selectNodeContents(source);selection.removeAllRanges();selection.addRange(range);
  status.textContent='요청문을 선택했습니다. Ctrl+C 또는 복사 메뉴로 복사하세요.';
 }
});
