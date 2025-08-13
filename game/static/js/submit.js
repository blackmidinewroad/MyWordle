document.addEventListener("htmx:oobAfterSwap", () => {
    const tiles = Array.from(document.querySelectorAll('.tile[data-final-state]'));
    if (tiles.length !== 5) return;

    tiles.forEach((tile, i) => {
        const finalState = tile.dataset.finalState;
        const letter = tile.innerHTML.trim().toLocaleUpperCase();
        const key = document.querySelector(`[data-key="${letter}"]`);

        setTimeout(() => {
            tile.setAttribute('data-state', finalState);
            if (key.dataset.state !== 'correct') {
                key.setAttribute('data-state', finalState)
            }
            tile.removeAttribute('data-final-state');

            // After last tile flips, check game over and enable keyboard if not
            if (i === 4) {
                const gameState = document.getElementById('game-state');
                if (gameState?.dataset.gameOver === 'True') {
                    const isWin = gameState.dataset.win === 'True';
                    setTimeout(() => {
                        showGameEndModal(isWin);
                    }, 300);
                }

                document.getElementById('keypress-handler').setAttribute('hx-trigger', 'keydown[keyCode>=65 && keyCode<=90] from:body');
                document.getElementById('backspace-handler').setAttribute('hx-trigger', 'keydown[keyCode==8] from:body');
                document.getElementById('submit-handler').setAttribute('hx-trigger', 'keydown[keyCode==13] from:body');

                if (window.htmx) {
                    htmx.process(document.getElementById('keypress-handler'));
                    htmx.process(document.getElementById('backspace-handler'));
                    htmx.process(document.getElementById('submit-handler'));
                }
            }
        }, i * 250);
    });
});


function showGameEndModal(win) {
    const modal = document.getElementById('game-over-modal');
    const msg = document.getElementById('end-message');
    msg.innerText = win ? 'You won!' : 'You lost(';
    modal.classList.add('visible');
    modal.classList.remove('hidden');

    document.getElementById('restart-btn').onclick = () => {
        modal.classList.remove('visible');
        modal.classList.add('hidden');
        window.location.reload();
    };
}