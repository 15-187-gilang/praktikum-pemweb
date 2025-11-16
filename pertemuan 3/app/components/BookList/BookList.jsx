'use client';

import React from 'react';
import BookItem from '../BookItem/BookItem';
import './BookList.css';

const BookList = ({ books, onDelete, onEdit }) => {
  if (books.length === 0) {
    return (
      <div className="empty-state">
        <p className="empty-icon">📖</p>
        <p>Tidak ada buku yang ditemukan. Mulai tambah buku sekarang!</p>
      </div>
    );
  }

  return (
    <div className="book-list">
      {books.map(book => (
        <BookItem 
          key={book.id} 
          book={book} 
          onDelete={onDelete}
          onEdit={onEdit}
        />
      ))}
    </div>
  );
};

export default BookList;
