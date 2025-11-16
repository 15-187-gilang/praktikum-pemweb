'use client';

import React from 'react';
import './BookItem.css';

const BookItem = ({ book, onDelete, onEdit }) => {
  const getStatusColor = (status) => {
    const colors = {
      'Milik': '#10b981',
      'Sedang Dibaca': '#f59e0b',
      'Ingin Dibeli': '#3b82f6',
    };
    return colors[status] || '#667eea';
  };

  const getStatusEmoji = (status) => {
    const emojis = {
      'Milik': '✅',
      'Sedang Dibaca': '📖',
      'Ingin Dibeli': '🛒',
    };
    return emojis[status] || '📚';
  };

  return (
    <div className="book-item">
      <div className="book-header">
        <div className="book-info">
          <h3>{book.title}</h3>
          <p className="book-author">by {book.author}</p>
        </div>
        <span 
          className="book-status"
          style={{ backgroundColor: getStatusColor(book.status) }}
        >
          {getStatusEmoji(book.status)} {book.status}
        </span>
      </div>
      <div className="book-actions">
        <button 
          onClick={() => onEdit(book)} 
          className="btn-edit"
        >
          ✏️ Edit
        </button>
        <button 
          onClick={() => onDelete(book.id)} 
          className="btn-delete"
        >
          🗑️ Hapus
        </button>
      </div>
    </div>
  );
};

export default BookItem;
