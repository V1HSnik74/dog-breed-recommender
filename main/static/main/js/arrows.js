let currentIndex = 0;
        const cards = document.querySelectorAll('.card');
        const totalCards = cards.length;

        function showCard(index) {
            cards.forEach((card, i) => {
                if (i === index) {
                    card.classList.add('active');
                } else {
                    card.classList.remove('active');
                }
            });
        }

        function nextCard() {
            if (totalCards > 0) {
                currentIndex = (currentIndex + 1) % totalCards;
                showCard(currentIndex);
            }
        }

        function prevCard() {
            if (totalCards > 0) {
                currentIndex = (currentIndex - 1 + totalCards) % totalCards;
                showCard(currentIndex);
            }
        }

        if (totalCards > 0) {
            showCard(0);
        }

        document.querySelector('.prev-btn').addEventListener('click', prevCard);
        document.querySelector('.next-btn').addEventListener('click', nextCard);

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') prevCard();
            if (e.key === 'ArrowRight') nextCard();
        });

        let touchStartX = 0;
        document.querySelector('.cards').addEventListener('touchstart', (e) => {
            touchStartX = e.touches[0].clientX;
        });

        document.querySelector('.cards').addEventListener('touchend', (e) => {
            const touchEndX = e.changedTouches[0].clientX;
            if (touchStartX - touchEndX > 50) {
                nextCard();
            } else if (touchEndX - touchStartX > 50) {
                prevCard();
            }
        });