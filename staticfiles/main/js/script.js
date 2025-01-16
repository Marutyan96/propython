document.addEventListener("DOMContentLoaded", function() {
    var sidebar = document.getElementById('sidebar');
    var toggleButton = document.getElementById('toggle-header');
    var form = document.querySelectorAll('form'); // Получаем все формы на странице

    // Обработчик для открытия/закрытия боковой панели
    toggleButton.addEventListener('click', function(event) {
        sidebar.classList.toggle('active');
        event.stopPropagation(); // Останавливаем всплытие события
    });

    // Закрываем боковую панель при клике вне ее и вне всех форм
    document.addEventListener('click', function(event) {
        if (!sidebar.contains(event.target) && !Array.from(form).some(f => f.contains(event.target))) {
            sidebar.classList.remove('active');
        }
    });

    // Скрываем боковую панель при изменении размера окна
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            sidebar.classList.remove('active');
        }
    });

// Код для кнопки "Прокрутить вверх"
const scrollToTopButton = document.getElementById('scrollToTop');

window.onscroll = function() {
    scrollToTopButton.style.display = (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) ? "block" : "none";
};

scrollToTopButton.onclick = function() {
    const scrollStep = -window.scrollY / (400 / 35); // Определяем шаг прокрутки
    const scrollInterval = setInterval(function() {
        if (window.scrollY !== 0) {
            window.scrollBy(0, scrollStep); // Прокручиваем на шаг
        } else {
            clearInterval(scrollInterval); // Останавливаем интервал, когда достигли верха
        }
    }, 15); // Интервал обновления (мс)
};


    // Проверяем сохраненную тему и применяем её
    const savedTheme = localStorage.getItem('theme');
    const themeIcon = document.getElementById('theme-icon');
    const themeIconSidebar = document.getElementById('theme-icon-sidebar');
    
    if (savedTheme) {
        const isDarkTheme = savedTheme === 'dark';
        document.body.classList.toggle('dark-theme', isDarkTheme);
        themeIcon.classList.toggle('fa-sun', !isDarkTheme);
        themeIcon.classList.toggle('fa-moon', isDarkTheme);
        const main = document.querySelector('main');
        main.classList.toggle('dark-theme', isDarkTheme);
    }

    // Функция для переключения темы
    function toggleTheme() {
        const isDarkTheme = document.body.classList.toggle('dark-theme');
        const main = document.querySelector('main');
        
        main.classList.toggle('dark-theme', isDarkTheme);
        
        // Меняем иконки
        themeIcon.classList.toggle('fa-sun', !isDarkTheme);
        themeIcon.classList.toggle('fa-moon', isDarkTheme);
        themeIconSidebar.classList.toggle('fa-sun', !isDarkTheme);
        themeIconSidebar.classList.toggle('fa-moon', isDarkTheme);
        
        // Сохраняем выбранную тему в localStorage
        localStorage.setItem('theme', isDarkTheme ? 'dark' : 'light');
    }

    // Обработчики событий для переключения темы
    const themeToggle = document.getElementById('theme-toggle');
    const themeToggleSidebar = document.getElementById('theme-toggle-sidebar');

    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }

    if (themeToggleSidebar) {
        themeToggleSidebar.addEventListener('click', toggleTheme);
    }
});
