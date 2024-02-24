let timeout = null;  // Объявите timeout в глобальной области видимости
const area = document.getElementById('area')
const resultArea = document.getElementById('resultTextArea')
const toLang = document.getElementById('to_lan')
const loader = document.getElementById('loading')
const radios = document.getElementsByName('choice_translator')


function getTranslator() {
    for (var i = 0, length = radios.length; i < length; i++) {
        if (radios[i].checked) {
            // радиокнопка выбрана
            return radios[i].value;
        }
    }
}



function translateText(event) {
    clearTimeout(timeout);  // Очистить предыдущий таймер при каждом вводе

    let href = window.location.href

    timeout = setTimeout(function () {
        if (area.value) {
            if (getTranslator() === 'google') {

                loader.style.display = 'block'
                // http://127.0.0.1:8000/api/v1/translate/<str:text>/<str:to_lang>/<str:translator>
                fetch(href +'/api/v1/translate/' + area.value + '/' + toLang.value + '/')  // Замените на URL вашего сервера
                    .then(response => response.json())  // Преобразовать ответ в JSON
                    .then(data => {
                        loader.style.display = 'none'
                        resultArea.value = data.result
                    })  // Вывести полученные данные в консоль
                    .catch(error => console.error('Ошибка:', error));  // Обработать любые ошибки
            }

            else {
                loader.style.display = 'block'
                // http://127.0.0.1:8000/api/v1/translate/<str:text>/<str:to_lang>/<str:translator>
                url = href +'/api/v1/translate/' + area.value + '/' + toLang.value + '/' + getTranslator() + '/'
                console.log(url)
                fetch(url)  // Замените на URL вашего сервера
                    .then(response => response.json())  // Преобразовать ответ в JSON
                    .then(data => {
                        loader.style.display = 'none'
                        if (data.result) {
                            resultArea.value = data.result
                        }
                        else {
                            resultArea.value = 'Выбранный вами переводчик временно не доступен!'
                        }
                    })  // Вывести полученные данные в консоль
                    // .catch(error => console.error('Ошибка:', error));   Обработать любые ошибки
            }
                
        }
        else {
            resultArea.value = ''
        }
    }, 750);  // Задержка в 1 секунду
    
}


radios.forEach(radioButton => {
    radioButton.addEventListener('change', translateText);
});

area.addEventListener('input', translateText)