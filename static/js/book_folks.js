async function fetchBooks() {
	try {
		const response = await fetch('/books')
		if (!response.ok) throw new Error('Ошибка загрузки')

		const books = await response.json()
		const list = document.getElementById('book-list')

		if (books.length === 0) {
			list.innerHTML = '<li>Нет доступных книг</li>'
		} else {
			list.innerHTML = books
				.map(book => `<li><strong>${book.title}</strong> - ${book.author}</li>`)
				.join('')
		}
	} catch (error) {
		document.getElementById('book-list').innerText =
			'Не удалось загрузить книги'
	}
}

fetchBooks()

document.getElementById('update-list').addEventListener('click', function () {
	fetchBooks()
})

document.getElementById('delete-all').addEventListener('click', function () {
	fetch('/books', {
		method: 'DELETE',
	})
		.then(response => {
			if (!response.ok) {
				throw new Error(`Ошибка: ${response.status}`)
			}
			return response.json()
		})
		.then(data => console.log('Успешно удалено:', data), fetchBooks())
		.catch(error => console.error('Ошибка запроса:', error))
})
