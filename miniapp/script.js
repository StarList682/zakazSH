const tabs = {
    draws: {
      title: 'Розыгрыши',
      html: `<p>— «Участвую» и «Все розыгрыши» (заглушки).</p>`
    },
    create: {
      title: 'Создать розыгрыш',
      html: `<p>— Шаги добавления подарков, каналов и запуска.</p>`
    },
    history: {
      title: 'История',
      html: `<p>— «Участвовал» / «Создал»</p>`
    },
  };
  
  document.querySelectorAll('nav button').forEach(btn => {
    btn.addEventListener('click', () => {
      // переключаем активную кнопку
      document.querySelector('nav button.active').classList.remove('active');
      btn.classList.add('active');
  
      // меняем контент
      const key = btn.id.replace('tab-', '');
      const section = document.getElementById('content');
      section.innerHTML = `<h2>${tabs[key].title}</h2>${tabs[key].html}`;
    });
  });
  