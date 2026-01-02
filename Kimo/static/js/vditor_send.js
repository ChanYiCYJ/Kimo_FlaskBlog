const vditor = new Vditor('vditor', {
      height: 420,
      placeholder: '在这里输入 Markdown 内容...',
       toolbar: [
      'bold',
      'italic',
      'strike',
      'headings',
      'quote',
      'code',
      'inline-code',
      'list',
      'ordered-list',
      'link',
      'upload',
      'preview',
      'fullscreen'
    ],
      toolbarConfig: { pin: true },
       cache: {
    enable: false
  }
    });

    document.getElementById('sendBtn').addEventListener('click', async () => {
      const title = document.getElementById('titleInput').value.trim();
      const content = vditor.getValue().trim();
      const categoryToggle = document.getElementById('CategoryConditions')
      const category_id =Number(document.getElementById('categoryId').textContent.trim());
      if (!title) {
        showModal('标题不能为空');
        return;
      }

      if (!content) {
        showModal('内容不能为空');
        return;
      }


      const res = await fetch('/post', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ title, content ,category_id})
});

const data = await res.json();

if (res.ok) {
  showModal('发布成功');
  vditor.setValue('');

  setTimeout(() => {
    window.location.href = '/';
  }, 800);
} else {
  showModal(data.message || '发布失败');
}
    });