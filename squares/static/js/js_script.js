let phrases = [
    { text: 'CSS - чтобы задать стили объектам сайта',
      image: '/static/images/css_ps.png'},
    { text: 'Django - чтобы сайт заработал',
      image: '/static/images/django_coloroverlay_ps.png'},
    { text: 'HTML - чтобы разместить объекты на страницах сайта',
      image: '/static/images/html5_coloroverlay_ps.png'},
    { text: 'JS - чтобы работали анимации',
      image: '/static/images/js_coloroverlay_ps.png'},
    { text: 'PS - чтобы отредактировать картинки',
      image: '/static/images/ps_coloroverlay_ps.png'},
    { text: 'Python - чтобы работать с Django',
      image: '/static/images/python_coloroverlay_ps.png'},
    { text: 'SQL - чтобы работать с базами данных',
      image: '/static/images/sql_coloroverlay_ps.png'},
];

function getRandomElement(arr) {
    let randIndex = Math.floor(Math.random() * arr.length);
    return arr[randIndex];
}

let button = document.querySelector('.button');
let text = document.querySelector('.text');
let tech = document.querySelector('.tech');
let image = document.querySelector('.image');

button.addEventListener('click', function() {
    let randomElement = getRandomElement(phrases);
    text.textContent = randomElement.text;
    image.src = randomElement.image;
});
