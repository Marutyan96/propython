const editor = CodeMirror.fromTextArea(document.getElementById("code"), {
    mode: "python",
    lineNumbers: true,
    theme: "elegant",
    extraKeys: {
        "Ctrl-Space": "autocomplete",
        "Tab": function(cm) {
            const cursor = cm.getCursor();
            const token = cm.getTokenAt(cursor);
            if (token.string) {
                const hints = pythonHint(cm).list; // Получаем подсказки
                const filteredHints = hints.filter(hint => hint.text.startsWith(token.string));
                if (filteredHints.length) {
                    cm.replaceRange(filteredHints[0].text, {line: cursor.line, ch: token.start}, {line: cursor.line, ch: token.end});
                    return;
                }
            }
            cm.execCommand("indentMore");
        }
    }
});

let variableNames = new Set(); // Множество для хранения названий переменных

// Функция для извлечения названий переменных из кода
function extractVariableNames(code) {
    const variableRegex = /\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=/g; // Регулярное выражение для поиска переменных
    let match;
    while ((match = variableRegex.exec(code)) !== null) {
        variableNames.add(match[1]); // Добавляем имя переменной в множество
    }
}

editor.on('change', function (cm, change) {
    // Проверяем, был ли добавлен новый символ
    if (change.origin === "setValue" || change.origin === "paste") return;

    const cursor = cm.getCursor();
    const lastChar = change.text[0]; // Последний введенный символ

    // Определяем соответствующий закрывающий символ
    let closingChar = '';
    switch (lastChar) {
        case '(':
            closingChar = ')';
            break;
        case '{':
            closingChar = '}';
            break;
        case '[':
            closingChar = ']';
            break;
        case '"':
            closingChar = '"';
            // Проверяем, есть ли уже закрывающая кавычка
            if (cm.getLine(cursor.line).charAt(cursor.ch) === '"') return;
            break;
        case "'":
            closingChar = "'";
            // Проверяем, есть ли уже закрывающая кавычка
            if (cm.getLine(cursor.line).charAt(cursor.ch) === "'") return;
            break;
        case '<':
            if (cm.getLine(cursor.line).charAt(cursor.ch) === '<') return; // Проверяем, есть ли уже закрывающая двойная угловая скобка
            closingChar = '>';
            break;
        case '>':
            if (cm.getLine(cursor.line).charAt(cursor.ch) === '>') return; // Проверяем, есть ли уже закрывающая двойная угловая скобка
            closingChar = '<';
            break;
        case '`': // Обработка обратной кавычки
            closingChar = '`';
            // Проверяем, есть ли уже закрывающая обратная кавычка
            if (cm.getLine(cursor.line).charAt(cursor.ch) === '`') return;
            break;
        // Добавьте другие символы по мере необходимости
    }

    // Если есть соответствующий закрывающий символ, добавляем его
    if (closingChar) {
        cm.replaceRange(closingChar, cursor);
        cm.setCursor(cursor.line, cursor.ch); // Устанавливаем курсор после закрывающего символа
    }

    // Извлекаем названия переменных из кода
    const code = cm.getValue();
    extractVariableNames(code);
});



function pythonHint(cm) {
    const cursor = cm.getCursor();
    const token = cm.getTokenAt(cursor);
    const word = token.string;

    const hints = [
    // Встроенные функции
    {text: "input", displayText: "input", className: "hint-input"},
    {text: "len", displayText: "len", className: "hint-len"},
    {text: "range", displayText: "range", className: "hint-range"},
    {text: "print", displayText: "print", className: "hint-print"},
    {text: "str", displayText: "str", className: "hint-str"},
    {text: "class", displayText: "class", className: "hint-class"},
    {text: "def", displayText: "def", className: "hint-def"},
    {text: "for", displayText: "for", className: "hint-for"},
    {text: "if", displayText: "if", className: "hint-if"},
    {text: "else", displayText: "else", className: "hint-else"},
    {text: "elif", displayText: "elif", className: "hint-elif"},
    {text: "return", displayText: "return", className: "hint-return"},
    {text: "import", displayText: "import", className: "hint-import"},
    {text: "from", displayText: "from", className: "hint-from"},
    {text: "try", displayText: "try", className: "hint-try"},
    {text: "except", displayText: "except", className: "hint-except"},
    {text: "with", displayText: "with", className: "hint-with"},
    {text: "map", displayText: "map", className: "hint-map"},
    {text: "filter", displayText: "filter", className: "hint-filter"},
    {text: "reduce", displayText: "reduce", className: "hint-reduce"},
    
    // Типы данных
    {text: "list", displayText: "list", className: "hint-list"},
    {text: "dict", displayText: "dict", className: "hint-dict"},
    {text: "set", displayText: "set", className: "hint-set"},
    {text: "tuple", displayText: "tuple", className: "hint-tuple"},
    {text: "zip", displayText: "zip", className: "hint-zip"},
    {text: "enumerate", displayText: "enumerate", className: "hint-enumerate"},
    {text: "sorted", displayText: "sorted", className: "hint-sorted"},
    {text: "sum", displayText: "sum", className: "hint-sum"},
    {text: "any", displayText: "any", className: "hint-any"},
    {text: "all", displayText: "all", className: "hint-all"},
    
    // Работа с файлами
    {text: "open", displayText: "open", className: "hint-open"},
    
    // Методы списков
    {text: "append", displayText: "append", className: "hint-append"},
    {text: "pop", displayText: "pop", className: "hint-pop"},
    {text: "remove", displayText: "remove", className: "hint-remove"},
    {text: "extend", displayText: "extend", className: "hint-extend"},
    {text: "insert", displayText: "insert", className: "hint-insert"},
    {text: "sort", displayText: "sort", className: "hint-sort"},
    
    // Методы строк
    {text: "join", displayText: "join", className: "hint-join"},
    {text: "split", displayText: "split", className: "hint-split"},
    {text: "strip", displayText: "strip", className: "hint-strip"},
    {text: "replace", displayText: "replace", className: "hint-replace"},
    {text: "find", displayText: "find", className: "hint-find"},
    {text: "format", displayText: "format", className: "hint-format"},
    
    // Методы словарей
    {text: "get", displayText: "get", className: "hint-get"},
    {text: "keys", displayText: "keys", className: "hint-keys"},
    {text: "values", displayText: "values", className: "hint-values"},
    {text: "items", displayText: "items", className: "hint-items"},
    
    // Методы множеств
    {text: "add", displayText: "add", className: "hint-add"},
    {text: "remove", displayText: "remove", className: "hint-remove"},
    {text: "union", displayText: "union", className: "hint-union"},
    {text: "intersection", displayText: "intersection", className: "hint-intersection"},
    
    

    ];

    // Добавляем переменные в подсказки
    variableNames.forEach(variable => {
        hints.push({text: variable, displayText: variable, className: "hint-variable"});
    });

    // Фильтрация подсказок
    const filteredHints = hints.filter(hint => hint.text.startsWith(word));

    // Если нет подсказок, возвращаем пустой массив
    if (filteredHints.length === 0) {
        return {list: [], from: cursor, to: cursor};
    }

    return {
        list: filteredHints.map(hint => ({
            text: hint.displayText,
            displayText: hint.displayText,
            className: hint.className
        })),
        from: CodeMirror.Pos(cursor.line, token.start),
        to: CodeMirror.Pos(cursor.line, cursor.ch)
    };
}

// Подписка на событие автозаполнения
editor.on("inputRead", function (cm) {
    const cursor = cm.getCursor();
    const token = cm.getTokenAt(cursor);
    const word = token.string;

    // Запуск автозаполнения при вводе
    if (word.length > 0) {
        cm.showHint({
            hint: pythonHint,
            completeSingle: false
        });
    }
});













document.getElementById("run").onclick = async function() {
    const code = editor.getValue();
    try {
        const response = await fetch('/run/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: new URLSearchParams({ code: code })
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Network response was not ok');
        }
        const data = await response.json();
        document.getElementById("result").textContent = data.output || "No output";
    } catch (error) {
        console.error('Ошибка:', error);
        document.getElementById("result").textContent = "Ошибка: " + error.message;
    }
};





document.getElementById("toggle-theme").onclick = function() {
    const isDark = document.body.classList.toggle("dark-mode");
    editor.setOption("theme", isDark ? "monokai" : "elegant");
};

document.getElementById("reset").onclick = function() {
    editor.setValue("");
    document.getElementById("result").textContent = "";
};







const resizer = document.getElementById('resizer');
const editordiv = document.getElementById('editor');
const output = document.getElementById('output');

let isResizing = false;

resizer.addEventListener('mousedown', (event) => {
    isResizing = true;
    document.body.style.cursor = 'ns-resize'; // Изменяем курсор на указатель изменения размера
});

document.addEventListener('mousemove', (event) => {
    if (isResizing) {
        const newHeight = event.clientY; // Получаем высоту от верхней части окна до курсора

        // Устанавливаем высоту для редактора
        if (newHeight >= 0 && newHeight <= window.innerHeight) {
            editordiv.style.height = `${newHeight}px`;
            output.style.height = `${window.innerHeight - newHeight - resizer.offsetHeight}px`; // Высота области вывода
        }
    }
});

document.addEventListener('mouseup', () => {
    isResizing = false;
    document.body.style.cursor = ''; // Возвращаем курсор к нормальному состоянию
});



// Поддержка клавиатурных сокращений: Добавьте возможность 
// запускать код с помощью клавиши, например, Ctrl + Enter.
document.addEventListener('keydown', function(event) {
    if (event.ctrlKey && event.key === 'Enter') {
        document.getElementById('run').click(); // Запускаем код
    }
});
