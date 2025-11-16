'use client';

import React, { useState, useContext, useEffect } from 'react';
import { BookContext } from '../../lib/context/BookContext';
import './BookForm.css';

const BookForm = ({ onBookAdded, editingBook, onCancelEdit }) => {
  const { addBook, updateBook } = useContext(BookContext);
  const [formData, setFormData] = useState({
    title: '',
    author: '',
    status: 'Ingin Dibeli',
  });
  const [error, setError] = useState('');

  useEffect(() => {
    if (editingBook) {
      setFormData({
        title: editingBook.title || '',
        author: editingBook.author || '',
        status: editingBook.status || 'Ingin Dibeli',
      });
    }
  }, [editingBook]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
    setError('');
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!formData.title.trim() || !formData.author.trim()) {
      setError('Judul dan Penulis tidak boleh kosong!');
      return;
    }

    if (editingBook) {
      updateBook(editingBook.id, formData);
    } else {
      addBook(formData);
    }

    setFormData({ title: '', author: '', status: 'Ingin Dibeli' });
    onBookAdded();
  };

  const handleCancel = () => {
    setFormData({ title: '', author: '', status: 'Ingin Dibeli' });
    setError('');
    onCancelEdit();
  };

  return (
    <div className="book-form-container">
      <h2>{editingBook ? '✏️ Edit Buku' : '➕ Tambah Buku Baru'}</h2>
      <form onSubmit={handleSubmit} className="book-form">
        {error && <p className="error-message">{error}</p>}
        
        <div className="form-group">
          <label htmlFor="title">Judul Buku</label>
          <input
            type="text"
            id="title"
            name="title"
            value={formData.title}
            onChange={handleChange}
            placeholder="Masukkan judul buku"
            className="form-input"
          />
        </div>

        <div className="form-group">
          <label htmlFor="author">Penulis</label>
          <input
            type="text"
            id="author"
            name="author"
            value={formData.author}
            onChange={handleChange}
            placeholder="Masukkan nama penulis"
            className="form-input"
          />
        </div>

        <div className="form-group">
          <label htmlFor="status">Status</label>
          <select
            id="status"
            name="status"
            value={formData.status}
            onChange={handleChange}
            className="form-select"
          >
            <option value="Milik">Milik</option>
            <option value="Sedang Dibaca">Sedang Dibaca</option>
            <option value="Ingin Dibeli">Ingin Dibeli</option>
          </select>
        </div>

        <div className="form-buttons">
          <button type="submit" className="btn-submit">
            {editingBook ? 'Update Buku' : 'Tambah Buku'}
          </button>
          {editingBook && (
            <button type="button" onClick={handleCancel} className="btn-cancel">
              Batal
            </button>
          )}
        </div>
      </form>
    </div>
  );
};

export default BookForm;
