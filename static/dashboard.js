// 입력 폼 제출 처리
const inputForm = document.getElementById('inputForm');
inputForm.addEventListener('submit', async function(e) {
  e.preventDefault();
  const input = document.getElementById('userInput').value;
  if (!input) return;
  // 각 에이전트별 설정 불러오기
function getAllAgentSettings() {
  return {
    logos: JSON.parse(localStorage.getItem(getAgentSettingsKey('logos')) || '{}'),
    pathos: JSON.parse(localStorage.getItem(getAgentSettingsKey('pathos')) || '{}'),
    ethos: JSON.parse(localStorage.getItem(getAgentSettingsKey('ethos')) || '{}')
  };
}

const response = await fetch('/api/user_input', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ 
      content: input,
      agent_settings: getAllAgentSettings() 
    })
  });
  const data = await response.json();
  document.getElementById('summary').textContent = data.summary || '';
  document.getElementById('logos').textContent = data.logos || '';
  document.getElementById('pathos').textContent = data.pathos || '';
  document.getElementById('ethos').textContent = data.ethos || '';
  document.getElementById('memory').textContent = data.memory || '';
  document.getElementById('sensation').textContent = data.sensation || '';
  document.getElementById('action_plan').textContent = data.action_plan || '';
  document.getElementById('mcp_result').textContent = data.mcp_result || '';
});

// ===== 에이전트별 설정 모달 =====
const settingsBtns = document.querySelectorAll('.settings-btn');
const modal = document.getElementById('settingsModal');
const closeModal = document.getElementById('closeModal');
const settingsForm = document.getElementById('settingsForm');
const modelSelect = document.getElementById('modelSelect');
const apiKeyInput = document.getElementById('apiKeyInput');
let currentAgent = null;

// agent별 localStorage key
function getAgentSettingsKey(agent) {
  return `soulcube_settings_${agent}`;
}

// 설정 버튼 클릭 시 모달 표시
settingsBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    currentAgent = btn.getAttribute('data-agent');
    document.getElementById('modalTitle').textContent = `${btn.previousSibling.textContent.trim()} 에이전트 설정`;
    // 기존 설정 불러오기
    const saved = localStorage.getItem(getAgentSettingsKey(currentAgent));
    if (saved) {
      const obj = JSON.parse(saved);
      modelSelect.value = obj.model || 'gpt-3.5-turbo';
      apiKeyInput.value = obj.apiKey || '';
    } else {
      modelSelect.value = 'gpt-3.5-turbo';
      apiKeyInput.value = '';
    }
    modal.style.display = 'block';
  });
});

// 모달 닫기
closeModal.onclick = () => { modal.style.display = 'none'; };
window.onclick = (e) => { if (e.target === modal) modal.style.display = 'none'; };

// 설정 저장
settingsForm.onsubmit = function(e) {
  e.preventDefault();
  if (!currentAgent) return;
  const settings = {
    model: modelSelect.value,
    apiKey: apiKeyInput.value
  };
  localStorage.setItem(getAgentSettingsKey(currentAgent), JSON.stringify(settings));
  modal.style.display = 'none';
  alert('설정이 저장되었습니다!');
};
