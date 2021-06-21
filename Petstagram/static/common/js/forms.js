[...document.querySelector('.form').children]
    .filter(a => a.tagName === 'INPUT' || a.tagName === 'TEXTAREA' || a.tagName === 'SELECT')
    .forEach(a => {
        a.classList.add('form-field');
    });