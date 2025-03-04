const form = document.querySelector('form')
form.addEventListener('submit', e => {
	e.preventDefault() // Останавливаем стандартное поведение формы
	const data = {
		title: form.title.value,
		author: form.author.value,
	}

  var name = form.title.value
	var email = form.author.value

  if (!name || !email) {
		alert('Пожалуйста, заполните все обязательные поля.')
		event.preventDefault() // Отменяем отправку формы
	} else {
    fetch('/books', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		})

		window.location.href = '/book_folks'
  }
})
