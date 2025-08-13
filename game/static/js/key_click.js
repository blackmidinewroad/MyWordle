document.querySelectorAll('.key').forEach(key => {
    key.addEventListener('click', () => {
        const value = key.textContent.trim();
        let keyEvent;

        if (value === '←') {
            keyEvent = new KeyboardEvent('keydown', { key: 'Backspace', keyCode: 8, which: 8 });
        } else if (value === 'Enter') {
            keyEvent = new KeyboardEvent('keydown', { key: 'Enter', keyCode: 13, which: 13 });
        } else {
            keyEvent = new KeyboardEvent('keydown', {
                key: value,
                keyCode: value.charCodeAt(0),
                which: value.charCodeAt(0)
            });
        }

        document.body.dispatchEvent(keyEvent);
    });
});