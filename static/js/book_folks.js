async function fetchBooks() {
	try {
		const response = await fetch('http://localhost:8000/books')
		if (!response.ok) throw new Error('Ошибка загрузки')
		const books = await response.json()
		const list = document.getElementById('book-list')
		list.innerHTML = books
			.map(book => `<li><strong>${book.title}</strong> - ${book.author}</li>`)
			.join('')
	} catch (error) {
		document.getElementById('book-list').innerText =
			'Не удалось загрузить книги'
	}
}

fetchBooks()
